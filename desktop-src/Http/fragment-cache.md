---
title: Fragment Cache
description: The HTTP Server API provides functionality for users to store data fragments in a cache for use in rapidly forming HTTP responses.
ms.assetid: 0f9a768e-723c-4c7b-a746-6b817441409c
ms.topic: article
ms.date: 05/31/2018
---

# Fragment Cache

The HTTP Server API provides functionality for users to store data fragments in a cache for use in rapidly forming HTTP responses.

Fragments can be added to the cache by calling the [**HttpAddFragmentToCache**](/windows/desktop/api/Http/nf-http-httpaddfragmenttocache) function. A Fragment is identified by a URL contained in the *pUrlPrefix* parameter. A call to this function with the URL of an existing fragment overwrites the existing fragment.

A fragment can be deleted or overwritten by the owner of the request queue that initially added the fragment. The [**HttpFlushResponseCache**](/windows/desktop/api/Http/nf-http-httpflushresponsecache) function called with a UrlPrefix deletes all fragments within that prefix as well as the hierarchical descendants of that UrlPrefix. The [**HttpReadFragmentFromCache**](/windows/desktop/api/Http/nf-http-httpreadfragmentfromcache) function reads in the entire fragment or a specified byte range within the fragment.

> [!Note]  
> Adding a fragment to the cache does not guarantee that it is available for future calls to send a response. Fragment cache entries can become unavailable at any time. A call that uses a fragment that is not available fails. Applications that use the fragment cache must be prepared to handle this failure.

 

## Sending a Response With a Fragment

Fragments can be used to form all or portions of an HTTP responses entity body. You can send a response and entity body in one call to the [**HttpSendHttpResponse**](/windows/desktop/api/Http/nf-http-httpsendhttpresponse) function by specifying an array of [**HTTP\_DATA\_CHUNK**](/windows/desktop/api/Http/ns-http-http_data_chunk) structures in the [**HTTP\_RESPONSE**](http-response.md) structure.

An [**HTTP\_DATA\_CHUNK**](/windows/desktop/api/Http/ns-http-http_data_chunk) can specify a block of memory, a handle to an already opened file or a fragment cache entry. These correspond to the **HTTP\_DATA\_CHUNK** types: **HttpDataChunkFromMemory**, **HttpDataChunkFromFileHandle**, and **HttpDataChunkFromFragmentCache**, respectively. Full responses in the HTTP cache can also be used as fragments in the [**HTTP\_RESPONSE**](http-response.md) structure, although this practice is not recommended.

The [**HTTP\_RESPONSE**](http-response.md) structure contains a pointer to an array of [**HTTP\_DATA\_CHUNK**](/windows/desktop/api/Http/ns-http-http_data_chunk) structures that comprise the entity body of the response. The **HTTP\_RESPONSE** structure also contains a matching count which specifies the dimension of the array of **HTTP\_DATA\_CHUNK** structures. The HttpDataChunkFromFragmentCache value in the **HTTP\_DATA\_CHUNK** structure specifies the fragment cache type of the data chunk. The **HTTP\_DATA\_CHUNK** structure also specifies the fragment name.

A response that contains a cached fragment fails with an ERROR\_PATH\_NOT\_FOUND if any of the fragment cache entries are not available. Since the fragment cache entries are not guaranteed to be available, applications must be prepared to handle this case. One way to handle this case is to attempt to re-add the fragment cache entry and resend the response. If repeated failures occur, the application can use data chunks stored in memory buffers instead of fragment cache entries.

Fragment cache entries can also be specified in the [**HttpSendResponseEntityBody**](/windows/desktop/api/Http/nf-http-httpsendresponseentitybody) function. The fragment is added to the entity body in the [**HTTP\_DATA\_CHUNK**](/windows/desktop/api/Http/ns-http-http_data_chunk) structure as described above. Again, the send can fail if any of the specified fragment cache entries are not available.

 

 




