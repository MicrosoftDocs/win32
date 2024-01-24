---
title: HTTP_RESPONSE (Http.h)
description: The version of the HTTP\_RESPONSE structure is dependent on the version of the request queue used by HTTP Server API. Version 1.0 uses the HTTP\_RESPONSE\_V1 structure. Version 2.0 uses the HTTP\_RESPONSE\_V2 structure.
ms.assetid: F94646C0-7293-4543-842B-F08D8C7E2247
keywords:
- _HTTP_RESPONSE
- HTTP_RESPONSE
- PHTTP_RESPONSE
ms.topic: reference
ms.date: 05/31/2018
---

# HTTP\_RESPONSE

The version of the **HTTP\_RESPONSE** structure is dependent on the version of the request queue used as follows:

-   HTTP Server API Version 1.0: [**HTTP\_RESPONSE\_V1**](/windows/win32/api/http/ns-http-http_response_v1) structure.
-   HTTP Server API Version 2.0: [**HTTP\_RESPONSE\_V2**](/windows/win32/api/http/ns-http-http_response_v2) structure.

Do not use [**HTTP\_RESPONSE\_V1**](/windows/win32/api/http/ns-http-http_response_v1) and [**HTTP\_RESPONSE\_V2**](/windows/win32/api/http/ns-http-http_response_v2) directly in your code; using **HTTP\_RESPONSE** instead ensures the proper version of the structure is used based on the version of the request queue.


```C++
typedef HTTP_RESPONSE_V1 HTTP_RESPONSE;
typedef HTTP_RESPONSE_V2 HTTP_RESPONSE;
typedef HTTP_RESPONSE* PHTTP_RESPONSE;
```



<dl> <dt>

**HTTP\_RESPONSE_V1**
</dt> <dd>

Request was from a v1 request queue.

</dd> <dt>

**HTTP\_RESPONSE_V2**
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



 

 





