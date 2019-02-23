---
title: About WinINet
description: The Windows Internet (WinINet) application programming interface (API) enables your application to interact with FTP and HTTP protocols to access Internet resources.
ms.assetid: 0a06f2af-957a-4dff-a8cc-187370181b5c
keywords:
- About WinINet WinINet
- WinINet WinINet , about
- WinINet WinINet , start page
- Windows Internet WinINet
- Internet, Windows Internet WinINet
ms.topic: article
ms.date: 05/31/2018
---

# About WinINet

> [!NOTE]
> For app containers since Windows 10, version 1709, HTTP/2 (see [RFC7540](https://tools.ietf.org/html/rfc7540)) is on by default.
> 
> WinINet supports HTTP/2 only in a secure connection (HTTPS); there's no clear-text implementation. The server makes the final choice in the HTTP protocol negotiation, and it may decline to use HTTP/2 for any reason. A client has no way of forcing the use of HTTP/2; the server must be willing.
>
> To control whether HTTP/2 is enabled, set the **INTERNET_OPTION_ENABLE_HTTP_PROTOCOL** [option flag](/windows/desktop/wininet/option-flags), which can be set on the session, connection, or request. **INTERNET_OPTION_ENABLE_HTTP_PROTOCOL** is a DWORD bitmask. If the **HTTP_PROTOCOL_FLAG_HTTP2** (0x2) bit is set, then HTTP/2 is enabled.
> 
> To determine what happened after server negotiation, query the option flag **INTERNET_OPTION_HTTP_PROTOCOL_USED**, which can be queried only on the request (not on the session, nor the connection), and pass a DWORD initialized to 0. If, in the result, the **HTTP_PROTOCOL_FLAG_HTTP2** (0x2) bit is set, then the request was over HTTP/2.
> 
> The **HTTP_PROTOCOL_FLAG_HTTP2** (0x2) bit must be set and tested via a bitwise operation. Don't just compare the entire DWORD bitmask for equality with the flag.

The Windows Internet (WinINet) application programming interface (API) enables your application to interact with FTP and HTTP protocols to access Internet resources. As standards evolve, these functions handle the changes in underlying protocols, enabling them to maintain consistent behavior.

**Windows XP and Windows Server 2003 R2 and earlier:** Also enabled applications to interact with Gopher.

For more information, see:

-   [WinINet vs. WinHTTP](wininet-vs-winhttp.md)
-   [HINTERNET Handles](appendix-a-hinternet-handles.md)
-   [IP Version 6 Support](ip-version-6-support.md)
-   [Content\_Encoding](content-encoding.md)
-   [Caching](caching.md)
-   [Common Functions](common-functions.md)
-   [FTP Sessions](ftp-sessions.md)
-   [HTTP Sessions](http-sessions.md)
-   [HTTP Cookies](http-cookies.md)
-   [Asynchronous Operation](asynchronous-operation.md)
-   [Handling Authentication](handling-authentication.md)
-   [Handling Uniform Resource Locators](handling-uniform-resource-locators.md)
-   [Security\_Guideline](security-guidelines.md)

## Internet Protocols

The two primary Internet protocols are FTP and HTTP. For more information about these protocols, see the Request For Comments (RFC) documents for FTP and HTTP:

-   [RFC 959](https://go.microsoft.com/fwlink/p/?linkid=84546), *File Transfer Protocol (FTP)*.
-   [RFC 1945](https://go.microsoft.com/fwlink/p/?linkid=84520), *Hypertext Transfer Protocol - HTTP/1.0*.
-   [RFC 2616](https://go.microsoft.com/fwlink/p/?linkid=84048), *Hypertext Transfer Protocol - HTTP/1.1*.

> [!NOTE]  
> (These resources may not be available in some languages and countries.)

**Windows XP and Windows Server 2003 R2 and earlier:** The Gopher protocol was also supported. See [RFC 1436](https://go.microsoft.com/fwlink/p/?linkid=84551), *The Internet Gopher Protocol*.
