---
title: HTTP Server API Version 2.0 Data Types
description: HTTP Server API Version 2.0 Data Types
ms.assetid: 13a0cac9-9e75-4350-a523-5ad9a57caad7
ms.topic: article
ms.date: 05/31/2018
---

# HTTP Server API Version 2.0 Data Types

The HTTP Server API uses various special purpose identifier types declared in the Http.h header as follows:

-   **USHORT** HTTP\_SERVICE\_CONFIG\_TIMEOUT\_PARAM, \*PHTTP\_SERVICE\_CONFIG\_TIMEOUT\_PARAM
-   **ULONGLONG** HTTP\_OPAQUE\_ID, \*PHTTP\_OPAQUE\_ID
-   **HTTP\_OPAQUE\_ID** HTTP\_REQUEST\_ID, \*PHTTP\_REQUEST\_ID
-   **HTTP\_OPAQUE\_ID** HTTP\_CONNECTION\_ID, \*PHTTP\_CONNECTION\_ID
-   **HTTP\_OPAQUE\_ID** HTTP\_RAW\_CONNECTION\_ID, \*PHTTP\_RAW\_CONNECTION\_ID
-   **USHORT** HTTP\_SERVICE\_CONFIG\_TIMEOUT\_PARAM, \*PHTTP\_SERVICE\_CONFIG\_TIMEOUT\_PARAM

An application should not attempt to generate or modify any identifier that belongs to one of these types.

 

 




