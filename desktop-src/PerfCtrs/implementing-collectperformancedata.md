---
description: After the system successfully calls your your OpenPerformanceData function, it calls your CollectPerformanceData function to collect the counter data.
ms.assetid: 73b022df-0148-4afc-8536-8b1c766b1ee6
title: Implementing CollectPerformanceData
ms.topic: article
ms.date: 05/31/2018
---

# Implementing CollectPerformanceData

After the system successfully calls your your [**OpenPerformanceData**](/previous-versions/windows/desktop/legacy/aa372200(v=vs.85)) function, it calls your [**CollectPerformanceData**](/windows/win32/api/winperf/nc-winperf-pm_collect_proc) function to collect the counter data. If the provider supports the queried objects, it contacts the service, driver, or application with which it is associated and asks it for the counter data.

The following example shows an implementation of the [*CollectPerformanceData*](/windows/win32/api/winperf/nc-winperf-pm_collect_proc) function. The header file that contains the definition of the counters used in this function is shown in [Implementing OpenPerformanceData](implementing-openperformancedata.md). If you use C++ to implement this function, be sure to use extern "C" when you declare your function.


```C++
// Callback that the performance service calls when the consumer wants to sample
// your counter data. Get the counter data and return it to the consumer.
extern "C" DWORD APIENTRY CollectPerfData(LPWSTR pQuery,
    LPVOID* ppData,
    LPDWORD pcbData,
    LPDWORD pObjectsReturned)
{
    BOOL fQuerySupported = FALSE;
    DWORD TotalQuerySize = 0;
    PBYTE pObjects = (PBYTE)*ppData;  // Used to add counter objects to the buffer.
    PEER_INSTANCE inst;

    *pObjectsReturned = 0;

    if (0 == g_OpenCount) // Open did not successfully initialize
    {
        *pcbData = 0;
        *pObjectsReturned = 0;
        return ERROR_SUCCESS;
    }

    // Confirm that we support the requested objects. The query string is passed 
    // to this function as it was passed to RegQueryValueEx. For this example,
    // it should never be the case that we are being asked for objects that
    // we do not support because we included the [objects] section in the .ini file.

    fQuerySupported = IsQuerySupported(pQuery, &g_QueriedObjects);
    if (fQuerySupported == FALSE)
    {
        *pcbData = 0;
        *pObjectsReturned = 0;
        return ERROR_SUCCESS;
    }

    // If multiple instance objects are queried, you need to discover how many
    // instances exist so you can determine the buffer size that the 
    // query requires. This value can potentially change from query to query.
    // The Peer object is a multiple instance object. For this example,
    // set the number of instances to 2 if the Peer object was queried.

    if (QUERIED_PEER_OBJECT == (g_QueriedObjects & QUERIED_PEER_OBJECT))
    {
        g_Peer.Object.NumInstances = 2;
        g_Peer.Object.TotalByteLength = sizeof(PEER) + 
            sizeof(PEER_INSTANCE) * g_Peer.Object.NumInstances;
    }

    // Check pcbData to see if ppData is large enough to hold our counters.
    // If the buffer is not large enough, return ERROR_MORE_DATA. This tells 
    // the calling application to increase the buffer size and query again.

    TotalQuerySize = GetQuerySize(g_QueriedObjects);
    if (TotalQuerySize > *pcbData)
    {
        *pcbData = 0;
        *pObjectsReturned = 0;
        return ERROR_MORE_DATA;
    }
    else
    {
        *pcbData = TotalQuerySize;
    }

    // If the query includes the Transfer object, collect the counter data
    // for the Transfer object and copy it to the ppData buffer.

    if (QUERIED_TRANSFER_OBJECT == (g_QueriedObjects & QUERIED_TRANSFER_OBJECT))
    {
        // Add calls to retrieve counter data from the server/driver/application.
        // This example hard codes the counter data.

        g_Transfer.BytesSentData = 5;
        g_Transfer.AvailableBandwidthData = 20;
        g_Transfer.TotalBandwidthData = 50;

        // Since this is a single instance object, just copy the object
        // to the buffer.

        memcpy((PTRANSFER)pObjects, &g_Transfer, sizeof(TRANSFER));
        pObjects += g_Transfer.Object.TotalByteLength;  
        (*pObjectsReturned)++; 
    }

    // If the query includes the Peer object, collect the counter data
    // for the Peer object and its instances and copy it to the ppData buffer.

    if (QUERIED_PEER_OBJECT == (g_QueriedObjects & QUERIED_PEER_OBJECT))
    {
        // Copy the object and counter definition pieces to the buffer,
        // the instance data follows.

        memcpy((PPEER)pObjects, &g_Peer, sizeof(PEER));
        pObjects += sizeof(PEER);
        
        // Initialize the instance information.

        ZeroMemory(&inst, sizeof(PEER_INSTANCE));
        inst.Instance.ByteLength = sizeof(PERF_INSTANCE_DEFINITION) + sizeof(inst.InstanceName);
        inst.Instance.UniqueID = PERF_NO_UNIQUE_ID;
        inst.Instance.NameOffset = sizeof(PERF_INSTANCE_DEFINITION);
        inst.CounterBlock.ByteLength = EndOfPeerData;

        // Instance-specific data for the first instance. This information is
        // hard coded for this example.

        inst.Instance.NameLength = sizeof(INSTANCE_NAME_1);
        StringCchCopy(inst.InstanceName, MAX_INSTANCE_NAME_LEN+1, INSTANCE_NAME_1);
        inst.BytesServedData = 15;

        // Copy the instance.

        memcpy((PPEER_INSTANCE)pObjects, &inst, sizeof(PEER_INSTANCE));
        pObjects += sizeof(PEER_INSTANCE); 

        // Instance-specific data for the second instance.

        inst.Instance.NameLength = sizeof(INSTANCE_NAME_2);
        StringCchCopy(inst.InstanceName, MAX_INSTANCE_NAME_LEN+1, INSTANCE_NAME_2);
        inst.BytesServedData = 30;

        // Copy the instance.

        memcpy((PPEER_INSTANCE)pObjects, &inst, sizeof(PEER_INSTANCE));
        pObjects += sizeof(PEER_INSTANCE);

        (*pObjectsReturned)++; 
    }

    *ppData = (LPVOID)pObjects;

    return ERROR_SUCCESS;
}


// Scan the query string to see if we support the objects.
BOOL IsQuerySupported(LPWSTR pQuery, DWORD* pQueriedObjects)
{
    BOOL fSupported = FALSE;
    WCHAR IndexString[33+1];
    LPWSTR pCopy = NULL;
    DWORD dwQueryLen = 0;

    *pQueriedObjects = 0;

    // Copy the query string and make it lowercase.

    dwQueryLen = wcslen(pQuery) + 1;
    pCopy = new WCHAR[dwQueryLen];
    wcscpy_s(pCopy, dwQueryLen, pQuery);
    _wcslwr_s(pCopy, dwQueryLen);

    if (wcsstr(pCopy, L"global"))
    {
        fSupported = TRUE;
        *pQueriedObjects |= QUERIED_ALL_OBJECTS;
    }
    else
    {
        // See if the query contains the index value for
        // the Transfer object.

        _ultow_s(g_TransferIndex, IndexString, 33, 10);
        if (wcsstr(pCopy, IndexString))
        {
            fSupported = TRUE;
            *pQueriedObjects |= QUERIED_TRANSFER_OBJECT;
        }

        // See if the query contains the index value for
        // the Peer object.

        _ultow_s(g_PeerIndex, IndexString, 33, 10);
        if (wcsstr(pCopy, IndexString))
        {
            fSupported = TRUE;
            *pQueriedObjects |= QUERIED_PEER_OBJECT;
        }
    }

    if (pCopy)
        delete pCopy;

    return fSupported;
}


// Determine the required buffer size for the query.
DWORD GetQuerySize(DWORD QueriedObjects)
{
    DWORD QuerySize = 0;

    if (QUERIED_TRANSFER_OBJECT == (QueriedObjects & QUERIED_TRANSFER_OBJECT))
        QuerySize = g_Transfer.Object.TotalByteLength;

    if (QUERIED_PEER_OBJECT == (g_QueriedObjects & QUERIED_PEER_OBJECT))
        QuerySize += g_Peer.Object.TotalByteLength;

  return QuerySize;
}
```



 

 
