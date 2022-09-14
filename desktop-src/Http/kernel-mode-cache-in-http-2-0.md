---
title: Kernel Mode Cache
description: Kernel Mode Cache
ms.assetid: f9a46ff4-779b-4b3a-b8f5-1ae10a3c0a61
ms.topic: article
ms.date: 05/31/2018
---

# Kernel Mode Cache

The HTTP Server version 2.0 API allows applications to cache responses with static content in kernel mode. Increased performance is achieved when requests are served from the kernel cache without transitioning to user mode.

The HTTP Server API applies the appropriate property configurations to all requests served from the kernel cache, including logging responses. Requests that require authentication, however, will not be served from the cache.

The HTTP Server API limits the kernel mode cache to requests that meet the following conditions:

-   The request verb is GET and the entire request is received.
-   The request must not have an entity body.
-   The HTTP protocol is version 1.0 or later.
-   The "Translate: f " header is not present.
-   Expect headers other than "Expect: 100-Continue" are not present.
-   The authorization header is not present.
-   The Range and If-Range headers are not present.

In addition to the restrictions on the request, the response must also meet the following conditions:

-   Response size is limited to 256 KB, by default. To change the size of the response that is cached, set the **UriMaxUriBytes** registry value to the required number of bytes.

    ```
    HKEY_LOCAL_MACHINE
       System
          CurrentControlSet
             Services
                HTTP
                   Parameters
                      UriMaxUriBytes
    ```

-   The entire response must be provided in a single call to [**HttpSendHttpResponse**](/windows/desktop/api/Http/nf-http-httpsendhttpresponse).
-   The date header on the response must not be suppressed.
-   If the last-modified header is present, the value of the header must have the correct syntax. The time value in this header is used for cache control verification.
-   The kernel mode cache has enough space left to store the response.

By default, kernel mode response cache is enabled. If any of the conditions for the request or response listed above are not met, the response will be sent, but it will not be cached. In HTTP Server version 2.0 API, [**HttpSendHttpResponse**](/windows/desktop/api/Http/nf-http-httpsendhttpresponse) includes an optional *pCachePolicy* parameter to pass the [**HTTP\_CACHE\_POLICY**](/windows/desktop/api/Http/ns-http-http_cache_policy) structure. Applications use the cache policy structure to configure the cache.

 

 




