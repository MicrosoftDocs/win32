---
title: Implementing Startup
description: The first time a Resource Monitor creates an instance of a resource type, it calls the Startup entry point function in the appropriate resource DLL.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 022f1e0b-fbd0-480c-9889-879e5d7458a3
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- entry point functions Failover Cluster ,implementing Startup
- Startup Failover Cluster ,implementing
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Implementing Startup

The first time a [Resource Monitor](resource-monitor.md) creates an instance of a [resource type](resource-types.md), it calls the [**Startup**](/windows/previous-versions/ResApi/nc-resapi-pstartup_routine?branch=master) entry point function in the appropriate [resource DLL](resource-dlls.md). The purpose of **Startup** is to allow the resource DLL and the Resource Monitor to exchange two important pieces of information:

-   The Resource Monitor needs the addresses of the entry point functions for the resource type.
-   The resource DLL needs addresses for the [**LogEvent**](/windows/previous-versions/ResApi/nc-resapi-plog_event_routine?branch=master) and [**SetResourceStatus**](/windows/previous-versions/ResApi/nc-resapi-pset_resource_status_routine?branch=master) callback functions.

In addition, [**Startup**](/windows/previous-versions/ResApi/nc-resapi-pstartup_routine?branch=master) indicates the version of the [Resource API](resource-api.md) in use on the local node.

**To implement Startup**

1.  Recommended: Verify that the local version of the [Resource API](resource-api.md) is compatible with your implementation.
2.  Required. Store the addresses of [**LogEvent**](/windows/previous-versions/ResApi/nc-resapi-plog_event_routine?branch=master) and [**SetResourceStatus**](/windows/previous-versions/ResApi/nc-resapi-pset_resource_status_routine?branch=master) callback functions.
3.  Required. Return a function table for the specified resource type.
4.  Recommended. Take no more than 300 milliseconds to return a value.

Once a Resource Monitor has a function table for a resource type, it does not call [**Startup**](/windows/previous-versions/ResApi/nc-resapi-pstartup_routine?branch=master) to create additional instances. A Resource Monitor will retain the function table for a resource type until all instances of the type assigned to the Resource Monitor have been deleted.

Resource DLLs that support multiple resource types typically define a single [**Startup**](/windows/previous-versions/ResApi/nc-resapi-pstartup_routine?branch=master) entry point function for the entire DLL and take appropriate action based on the name of the resource type passed in by the Resource Monitor. However, you could instead create &lt;Name&gt;Startup functions for each &lt;Name&gt; resource type supported by your DLL, as described in [Implementing DllMain](implementing-dllmain.md).

## Example

The following example illustrates a [**Startup**](/windows/previous-versions/ResApi/nc-resapi-pstartup_routine?branch=master) routine in a resource DLL that supports two types, MyTypeAlpha and MyTypeBeta. For additional examples see [Resource DLL Examples](https://msdn.microsoft.com/library/aa370474).


```C++
////////////////////////////////////////////////////////////////

DWORD WINAPI Startup( IN LPCWSTR                       pszResourceType,
                      IN DWORD                         nMinVersionSupported,
                      IN DWORD                         nMaxVersionSupported,
                      IN PSET_RESOURCE_STATUS_ROUTINE  pfnSetResourceStatus,
                      IN PLOG_EVENT_ROUTINE            pfnLogEvent,
                      OUT PCLRES_FUNCTION_TABLE       *pFunctionTable )
{
    DWORD nStatus;

    if (   (nMinVersionSupported > CLRES_VERSION_V1_00)
        || (nMaxVersionSupported < CLRES_VERSION_V1_00) )
    {
        nStatus = ERROR_REVISION_MISMATCH;
    }
    else if( lstrcmpiW( pszResourceType, TYPE_NAME_ALPHA ) == 0 )
    {
        *pFunctionTable              = &amp;g_FTable_Alpha;
        nStatus                      = ERROR_SUCCESS;
    }
    else if( lstrcmpiW( pszResourceType, TYPE_NAME_BETA ) == 0 )
    {
        *pFunctionTable              = &amp;g_FTable_Beta;
        nStatus                      = ERROR_SUCCESS;
    }
    else
    {
        nStatus = ERROR_CLUSTER_RESNAME_NOT_FOUND;
    }

    if( nStatus == ERROR_SUCCESS )
    {
        g_pfnSetResourceStatus = pfnSetResourceStatus;
        g_pfnLogEvent          = pfnLogEvent;
    }

    return nStatus;

}
```



 

 




