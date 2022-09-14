---
title: Caching the Result (Client Side)
description: Client-side caching stores the result set in the client memory, providing performance enhancements for the client side.
ms.assetid: 6e61b2f6-dd58-466e-9cef-5bc6301e983f
ms.tgt_platform: multiple
keywords:
- Caching the Result (Client Side) ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Caching the Result (Client Side)

Client-side caching stores the result set in the client memory, providing performance enhancements for the client side. A client can revisit an object repeatedly without multiple trips to the server. By default, ADSI caches the result set for the clients. This enables ADSI to provide clients with SQL-like cursor support. You may iterate through a given result set several times.

ADSI also enables clients to turn off the cache to reduce memory requirements. If client-side caching is disabled, the client does not maintain the result set in memory. Each row is freed after the application retrieves it. Disabling client-side caching can be useful for decreasing the client-side memory requirements in such cases as when you intend only to make a single pass through the result set. However, when clients elect not to cache the result, they give up cursor support.

For more information about results caching with a specific search interface, see:

-   [Result Caching with IDirectorySearch](result-caching-with-idirectorysearch.md)
-   [Searching with ActiveX Data Objects](searching-with-activex-data-objects-ado.md)
-   [Searching with OLE DB](searching-with-ole-db.md)

 

 




