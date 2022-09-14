---
title: HTTP Server API Features
description: This topic supported and unsupported features of the HTTP Server API.
ms.assetid: 448fe5a5-e79f-4c3a-aa76-94cff988f24f
keywords:
- HTTP Server API Features
ms.topic: article
ms.date: 05/31/2018
---

# HTTP Server API Features

The following lists describe supported and unsupported features of the HTTP Server API.

## Features Supported

HTTP supports the following features:

-   HTTP v1.0 and v1.1 server functionality.
-   Secure Sockets Layer 3.0 (SSL) with support for client and server certificates.
-   Caching of data fragments for use in subsequent responses.
-   Support for IPv6 and IPv4 addressing.
-   URL namespace reservations for application security.
-   True handles for all objects.
-   Synchronous and asynchronous I/O models.
-   Support for WOW64 on computers running on 64-bit Windows starting with Windows Server 2003 with Service Pack 1 (SP1).

## Features Not Supported

The HTTP Server API does not support the following functionality:

-   The HTTP Server API does not perform client or server authentication based on the contents of the HTTP request headers. Any required authentication must be implemented by the application.
-   WOW64 on computers running on 64-bit Windows is not supported on Windows Server 2003, and Windows XP with Service Pack 2 (SP2) and earlier.
-   The HTTP Server API does not support logging HTTP requests and responses.
-   The HTTP Server API does not chunk outgoing HTTP responses. The application must implement response chunking if required.

 

 




