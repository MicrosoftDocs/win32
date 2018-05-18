---
Description: 'Name service query in Windows Sockets (Winsock).'
ms.assetid: '94d77f7b-824a-4686-b270-9c662976bbc0'
title: Service Query
---

# Service Query

-   [**NSPLookupServiceBegin**](nsplookupservicebegin-2.md)
-   [**NSPLookupServiceNext**](nsplookupservicenext-2.md)
-   [**NSPLookupServiceEnd**](nsplookupserviceend-2.md)

A name service query involves a series of calls: [**NSPLookupServiceBegin**](nsplookupservicebegin-2.md), followed by one or more calls to [**NSPLookupServiceNext**](nsplookupservicenext-2.md) and ending with a call to [**NSPLookupServiceEnd**](nsplookupserviceend-2.md). [**NSPLookupServiceBegin**](nsplookupservicebegin-2.md) takes a [**WSAQUERYSET**](wsaqueryset-2.md) structure as input in order to define the query parameters along with a set of flags to provide additional control over the search operation. It returns a query handle which is used in the subsequent calls to **NSPLookupServiceNext** and **NSPLookupServiceEnd**.

The namespace SPI client invokes [**NSPLookupServiceNext**](nsplookupservicenext-2.md) to obtain query results, with results supplied in an client-supplied [**WSAQUERYSET**](wsaqueryset-2.md) buffer. The client continues to call **NSPLookupServiceNext** until the error code WSA\_E\_NO\_MORE is returned indicating that all results have been retrieved. The search is then terminated by a call to [**NSPLookupServiceEnd**](nsplookupserviceend-2.md). The **NSPLookupServiceEnd** function can also be used to cancel a currently pending **NSPLookupServiceNext** when called from another thread.

In Windows Sockets 2, conflicting error codes are defined for WSAENOMORE (10102) and WSA\_E\_NO\_MORE (10110). The error code WSAENOMORE will be removed in a future version and only WSA\_E\_NO\_MORE will remain. Namespace providers should switch to using the WSA\_E\_NO\_MORE error code as soon as possible to maintain compatibility with the widest possible range of applications.

 

 



