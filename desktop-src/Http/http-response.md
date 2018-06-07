---
title: HTTP\_RESPONSE
description: The version of the HTTP\_RESPONSE structure is dependent on the version of the request queue used as follows HTTP Server API Version 1.0 request queue This is an HTTP\_REQUEST\_V1 structure.HTTP Server API Version 2.0 request queue This is an HTTP\_REQUEST\_V2 structure.
ms.assetid: F94646C0-7293-4543-842B-F08D8C7E2247
keywords:
- HTTP_RESPONSE
- HTTP_RESPONSE
- PHTTP_RESPONSE
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HTTP\_RESPONSE

The version of the **HTTP\_RESPONSE** structure is dependent on the version of the request queue used as follows:

-   HTTP Server API Version 1.0 request queue: This is an [**HTTP\_REQUEST\_V1**](http-request-v1.md) structure.
-   HTTP Server API Version 2.0 request queue: This is an [**HTTP\_REQUEST\_V2**](http-request-v2.md) structure.

Do not use [**HTTP\_REQUEST\_V1**](http-request-v1.md) and [**HTTP\_REQUEST\_V2**](http-request-v2.md) directly in your code; using **HTTP\_RESPONSE** instead ensures the proper version of the structure is used based on the version of the request queue.


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



|                                     |                                                                                   |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                    |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>Http.h</dt> </dl> |



 

 





