---
title: About HTTP Server API
description: The HTTP Server API provides developers with a low-level interface to the server side of the HTTP functionality as defined in RFC 2616.
ms.assetid: 74ad3a1d-cde2-4849-a412-d9d4101eaf12
keywords:
- HTTP Server API, overview
ms.topic: article
ms.date: 05/31/2018
---

# About HTTP Server API

The HTTP Server API provides developers with a low-level interface to the server side of the HTTP functionality as defined in [RFC 2616](https://www.ietf.org/rfc/rfc2616.txt). The API enables an application to receive HTTP requests directed to URLs and send HTTP responses. For sending dynamic responses, the ISAPI or ASP.NET interfaces are recommended.

The HTTP Server API enables multiple applications to coexist on a system, sharing the same TCP port (for example, port 80 for HTTP or port 443 for HTTPS) and serving different parts of the URL namespace.

The HTTP Server API requires knowledge of the C programming language and a familiarity with Windows API programming. Applications that do not require low-level access to HTTP should use the IIS ISAPI or the .NET Framework classes for HTTP-based solutions.

 

 




