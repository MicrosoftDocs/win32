---
description: PNRP uses the WSAQUERYSET structure in conjunction with various functions to facilitate resolving names and enumerating names and clouds.
ms.assetid: 0ccf20c1-4c95-4caf-a8f3-82a9e0a9907b
title: PNRP and WSAQUERYSET (P2P.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PNRP and WSAQUERYSET

PNRP uses the [**WSAQUERYSET**](winsock-nsp-reference-links.md) structure in conjunction with various functions to facilitate resolving names and enumerating names and clouds.

For complete definitions of [**WSAQUERYSET**](winsock-nsp-reference-links.md) or Windows Sockets functions, see their respective definitions in the Windows Sockets 2 API documentation in the Platform SDK.

## WSAQUERYSET and WSASetService

The [**WSASetService**](winsock-nsp-reference-links.md) function uses the **WSAQUERYSET** structure to register or remove peer names. The [PNRP and WSASetService](pnrp-and-wsasetservice.md) page outlines how to use the **WSAQUERYSET** structure with this function.

## WSAQUERYSET and WSALookupServiceBegin

The [**WSAQUERYSET**](winsock-nsp-reference-links.md) structure is used extensively with the **WSALookupServiceBegin**, **WSALookupServiceNext**, and **WSALookupServiceEnd** functions. Details about how these functions use the **WSAQUERYSET** structure are detailed in the following reference pages:

-   [PNRP and WSALookupServiceBegin](pnrp-and-wsalookupservicebegin.md)
-   [PNRP and WSALookupServiceNext](pnrp-and-wsalookupservicenext.md)
-   [PNRP and WSALookupServiceEnd](pnrp-and-wsalookupserviceend.md)

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                             |
| Version<br/>                  | Windows XP with SP1 with the Advanced Networking Pack for Windows XP<br/>  |
| Header<br/>                   | <dl> <dt>P2P.h</dt> </dl> |



## See also

<dl> <dt>

[PNRP and BLOB](pnrp-and-blob.md)
</dt> <dt>

[PNRP and WSASetService](pnrp-and-wsasetservice.md)
</dt> </dl>

 

 




