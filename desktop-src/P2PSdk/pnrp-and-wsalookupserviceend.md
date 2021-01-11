---
description: PNRP uses the WSALookupServiceEnd function to do the following.
ms.assetid: 0732929e-ca03-438f-80d9-48a3da0095f7
title: PNRP and WSALookupServiceEnd
ms.topic: article
ms.date: 05/31/2018
---

# PNRP and WSALookupServiceEnd

PNRP uses the [**WSALookupServiceEnd**](winsock-nsp-reference-links.md) function to do the following:

-   Terminate a query initiated in a previous call to [**WSALookupServiceBegin**](winsock-nsp-reference-links.md)
-   Unblock a call to [**WSALookupServiceNext**](winsock-nsp-reference-links.md) to stop the search

A call to [**WSALookupServiceEnd**](winsock-nsp-reference-links.md) terminates a query and cleans up the context. The handle obtained from a call to **WSALookupServiceBegin** must be passed as a parameter to **WSALookupServiceEnd**.

For more information about PNRP and the [**WSALookupServiceBegin**](winsock-nsp-reference-links.md) function, see [PNRP and WSALookupServiceBegin](pnrp-and-wsalookupservicebegin.md).

## Related topics

<dl> <dt>

[PNRP and WSALookupServiceBegin](pnrp-and-wsalookupservicebegin.md)
</dt> <dt>

[PNRP NSP Error Codes](pnrp-nsp-error-codes.md)
</dt> <dt>

[**WSALookupServiceNext**](winsock-nsp-reference-links.md)
</dt> </dl>

 

 



