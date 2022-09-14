---
description: When you unregister a peer name, a registered name is removed from a Peer Name Resolution Protocol (PNRP) cloud.
ms.assetid: a451988e-7026-4b3c-a7a3-366f9886aa02
title: Unregistering a Peer Name
ms.topic: article
ms.date: 05/31/2018
---

# Unregistering a Peer Name

When you unregister a peer name, a registered name is removed from a Peer Name Resolution Protocol (PNRP) cloud.

## Unregistering a Peer Name

To unregister a peer name, call [**WSASetService**](pnrp-and-wsasetservice.md). The *essOperation* parameter must have a value of **RNRSERVICE\_DELETE**. Use the guidelines in the following sections of this topic to make the required configurations to the **WSASetService** parameters and the [**WSAQUERYSET**](pnrp-and-wsaqueryset.md) structure.

## Configuring WSASetService

When an application calls [**WSASetService**](pnrp-and-wsasetservice.md), the parameters must be configured according to the following specifications:

-   *essOperation* must have a value of **RNRSERVICE\_DELETE**.
-   *dwFlags* must be zero (0).
-   *lpqsRegInfo* must point to a [**WSAQUERYSET**](pnrp-and-wsaqueryset.md) structure, which must be configured by using the guidelines in the following section of this topic.

## Configuring WSAQUERYSET

The [**WSAQUERYSET**](pnrp-and-wsaqueryset.md) structure must be configured according to the following specifications:

-   **dwSize** must specify the size the [**WSAQUERYSET**](pnrp-and-wsaqueryset.md) structure.
-   **lpszServiceInstanceName** must point to the peer name that is being unregistered.
-   **lpBlob** must point to a [**PNRPINFO**](/windows/desktop/api/Pnrpns/ns-pnrpns-pnrpinfo_v1) structure.
-   **lpcsaBuffer** must point to the address list.

> [!Note]  
> The remaining members are described in [**PNRP and WSASetService**](pnrp-and-wsasetservice.md).

 

## An Example of Unregistering a Peer Name

The following code snippet shows you how to unregister a peer name by providing the correct information when calling [**WSASetService**](pnrp-and-wsasetservice.md) using the [**WSAQUERYSET**](pnrp-and-wsaqueryset.md) structure.


```C++
#define UNICODE
#include <initguid.h>
#include <p2p.h>

#pragma comment(lib, "ws2_32.lib")

//-------------------------------------------------------------------------
// Function: PnrpUnregister
//
// Purpose:  Unregister the given name from a PNRP cloud
//
// Arguments:
//   pwzIdentity : identity string originally used to register the name
//   pwzName     : name to unregister from PNRP
//   pwzCloud    : name of the cloud to unregister from, NULL = global cloud
//
// Returns:  HRESULT
//
HRESULT PnrpUnregister(PWSTR pwzIdentity, PWSTR pwzName, PWSTR pwzCloud)
{
    HRESULT         hr = S_OK;
    PNRPINFO        pnrpInfo = {0};
    BLOB            blPnrpData = {0};
    WSAQUERYSET     querySet = {0};
    INT             iRet;

    //
    // build the WSAQUERYSET required to unregister
    //
    pnrpInfo.dwSize = sizeof(pnrpInfo);
    pnrpInfo.dwLifetime = 60 * 60 * 8; // 8 hours
    pnrpInfo.lpwszIdentity = pwzIdentity;

    blPnrpData.cbSize = sizeof(pnrpInfo);
    blPnrpData.pBlobData = (BYTE*)&pnrpInfo;

    querySet.dwSize = sizeof(querySet);
    querySet.dwNameSpace = NS_PNRPNAME;
    querySet.lpServiceClassId = (LPGUID)&SVCID_PNRPNAME;
    querySet.lpszServiceInstanceName = pwzName;
    querySet.lpszContext = pwzCloud;
    querySet.lpBlob = &blPnrpData;

    // unregister the name with PNRP
    iRet = WSASetService(&querySet, RNRSERVICE_DELETE, 0);
    if (iRet != 0)
    {
        hr = HRESULT_FROM_WIN32(WSAGetLastError());
    }

    return hr;
}
```



 

 



