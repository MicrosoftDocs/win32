---
title: HTTP Server API Version 1.0 Data Types
description: The HTTP Server API uses various special purpose identifier types declared in the Http.h header file as 64-bit unsigned integers.
ms.assetid: bec1d41e-0c80-49bc-84e1-b16c409cd0f3
keywords:
- HTTP_CONNECTION_ID type HTTP
- HTTP_RAW_CONNECTION_ID type HTTP
- HTTP_REQUEST_ID type HTTP
- HTTP_URL_CONTEXT type HTTP
ms.topic: article
ms.date: 05/31/2018
---

# HTTP Server API Version 1.0 Data Types

The HTTP Server API uses various special purpose identifier types declared in the Http.h header file as 64-bit unsigned integers (**ULONGLONGs**):

-   HTTP\_CONNECTION\_ID
-   HTTP\_RAW\_CONNECTION\_ID
-   HTTP\_REQUEST\_ID
-   HTTP\_URL\_CONTEXT

An application should not attempt to generate or modify any identifier that belongs to one of these types.

 

 




