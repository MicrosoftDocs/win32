---
title: HTTP_RESPONSE (Http.h)
description: The version of the HTTP\_RESPONSE structure is dependent on the version of the request queue used as follows HTTP Server API Version 1.0 request queue This is an HTTP\_REQUEST\_V1 structure.HTTP Server API Version 2.0 request queue This is an HTTP\_REQUEST\_V2 structure.
ms.assetid: F94646C0-7293-4543-842B-F08D8C7E2247
keywords:
- HTTP_RESPONSE
- HTTP_RESPONSE
- PHTTP_RESPONSE
ms.topic: reference
ms.date: 05/31/2018
---

# HTTP\_RESPONSE

The version of the **HTTP\_RESPONSE** structure is dependent on the version of the request queue used as follows:

-   HTTP Server API Version 1.0 request queue: This is an [**HTTP\_REQUEST\_V1**](/windows/desktop/api/Http/ns-http-http_request_v1) structure.
-   HTTP Server API Version 2.0 request queue: This is an [**HTTP\_REQUEST\_V2**](/windows/desktop/api/Http/ns-http-http_request_v2) structure.

Do not use [**HTTP\_REQUEST\_V1**](/windows/desktop/api/Http/ns-http-http_request_v1) and [**HTTP\_REQUEST\_V2**](/windows/desktop/api/Http/ns-http-http_request_v2) directly in your code; using **HTTP\_RESPONSE** instead ensures the proper version of the structure is used based on the version of the request queue.


```C++
typedef HTTP_REQUEST_V1 HTTP_RESPONSE;
typedef HTTP_REQUEST_V2 HTTP_RESPONSE;
typedef HTTP_RESPONSE* PHTTP_RESPONSE;
```



<dl> <dt>

**HTTP\_RESPONSE**
</dt> <dd>

Request was from a v1 request queue.

</dd> <dt>

**HTTP\_RESPONSE**
</dt> <dd>

Request was from a v2 request queue.

</dd> <dt>

**PHTTP\_RESPONSE**
</dt> <dd>

Pointer to an **HTTP\_RESPONSE** structure.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>Http.h</dt> </dl> |



 

 





