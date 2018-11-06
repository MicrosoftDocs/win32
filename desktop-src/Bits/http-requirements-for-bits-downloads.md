---
title: HTTP Requirements for BITS Downloads
description: BITS supports HTTP and HTTPS downloads and uploads and requires that the server supports the HTTP/1.1 protocol.
ms.assetid: 35af422b-62e4-41fd-8890-579ccf016c83
ms.topic: article
ms.date: 05/31/2018
---

# HTTP Requirements for BITS Downloads

BITS supports HTTP and HTTPS downloads and uploads and requires that the server supports the HTTP/1.1 protocol. For downloads, the HTTP server's **Head** method must return the file size and its **Get** method must support the Content-Range and Content-Length headers. As a result, BITS only transfers static file content and generates an error if you try to transfer dynamic content, unless the ASP, ISAPI, or CGI script supports the Content-Range and Content-Length headers.

BITS can use an HTTP/1.0 server as long as it meets the **Head** and **Get** method requirements.

To support downloading ranges of a file, the server must support the following requirements:

-   Allow MIME headers to include the standard Content-Range and Content-Type headers, plus a maximum of 180 bytes of other headers.
-   Allow a maximum of two CR/LFs between the HTTP headers and the first boundary string.

 

 




