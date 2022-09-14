---
description: Microsoft Windows HTTP Services (WinHTTP) provides you with a server-supported, high-level interface to the HTTP/2 and 1.1 Internet protocols.
ms.assetid: 8337f699-3ec0-4397-acc2-6dc813f7542d
title: About WinHTTP
ms.topic: article
ms.date: 05/31/2018
---

# About WinHTTP

> [!NOTE]
> For app containers and system services since Windows 10, version 1709, HTTP/2 (see [RFC7540](https://tools.ietf.org/html/rfc7540)) is on by default.

Microsoft Windows HTTP Services (WinHTTP) provides you with a server-supported, high-level interface to the HTTP/2 and 1.1 Internet protocols. WinHTTP is designed to be used primarily in server-based scenarios by server applications that communicate with HTTP servers.

[WinINet](/windows/desktop/WinInet/portal) was designed as an HTTP client platform for interactive desktop applications. WinINet displays a user interface for some operations such as collecting user credentials. WinHTTP, however, handles these operations programmatically. Server applications that require HTTP client services should use WinHTTP instead of WinINet. For more information, see [Porting WinINet Applications to WinHTTP](porting-wininet-applications-to-winhttp.md).

WinHTTP is also designed for use in system services and HTTP-based client applications. However, single-user applications that require FTP protocol functionality, cookie persistence, caching, automatic credential dialog handling, Internet Explorer compatibility, or downlevel platform support should consider using [WinINet](/windows/desktop/WinInet/portal).

This interface is accessible from C/C++ by using either the WinHTTP application programming interface (API), or by using the [**IWinHttpRequest**](iwinhttprequest-interface.md) and [**IWinHttpRequestEvents**](iwinhttprequestevents-interface.md) interfaces. WinHTTP is also accessible from script and Microsoft Visual Basic through the WinHTTP object. For more information and descriptions of the individual functions, see the WinHTTP functions reference for the specific language.

Starting with Windows 8, WinHTTP provides APIs to enable connections using the [WebSocket Protocol](https://tools.ietf.org/html/rfc6455)l, such as [**WinHttpWebSocketSend**](/windows/desktop/api/winhttp/nf-winhttp-winhttpwebsocketsend) and [**WinHttpWebSocketReceive**](/windows/desktop/api/winhttp/nf-winhttp-winhttpwebsocketreceive).

> [!Caution]  
> WinHTTP is not reentrant except during asynchronous completion callback. That is, while a thread has a call pending to one of the WinHTTP functions such as WinHttpSendRequest, WinHttpReceiveResponse, WinHttpQueryDataAvailable, WinHttpSendData, or WinHttpWriteData, it must never call WinHTTP a second time until the first call has completed. One scenario under which a second call could occur is as follows: If an application queues an Asynchronous Procedure Call (APC) to the thread that calls into WinHTTP, and if WinHTTP performs an alertable wait internally, the APC can run. If the APC routine happens also to call WinHTTP, it reenters the WinHTTP API, and the internal state of WinHTTP can be corrupted.

## WinHTTP 5.1 Features

The following features were added in version 5.1 of WinHTTP:

-   IPv6 support.
-   AutoProxy capabilities.
-   HTTP/1.0 protocol, including support for keep-alive (persistent) connections and session cookies.
-   HTTP/1.1 chunked transfer support for HTTP responses.
-   Keep-alive pooling of anonymous connections across sessions.
-   Secure Sockets Layer (SSL) functionality, including client certificates. Supported SSL protocols include the following: SSL 2.0, SSL 3.0, and Transport Layer Security (TLS) 1.0.
-   Support for server and proxy authentication, including integrated support for Microsoft Passport 1.4 and the Negotiate/ [Kerberos](../com/kerberos-v5-protocol.md) package.
-   Automatic handling of redirects unless suppressed.
-   Scriptable interface in addition to the API.
-   Trace utility to help troubleshoot problems.

A number of [WinINet](/windows/desktop/WinInet/portal) features are not supported in WinHTTP, including URL caching and persistent cookies, autoproxy, autodialing, offline support, and File Transfer Protocol (FTP).

For more information about changes introduced in version 5.1, see [What's New in WinHTTP 5.1](what-s-new-in-winhttp-5-1.md).

## Getting Started with WinHTTP

For more information about WinHTTP, see the following topics.

* [WinINet vs. WinHTTP](/windows/desktop/wininet/wininet-vs-winhttp) compares the two technologies for accessing HTTP.
* [WinHTTP Versions](winhttp-versions.md) describes the version history of WinHTTP.
* [What's New in WinHTTP 5.1](what-s-new-in-winhttp-5-1.md) describes changes and new features in WinHTTP 5.1.
* [Network Terminology](network-terminology.md) describes useful concepts and terminology relating to networking in general and the HTTP protocol in particular.
* [Choosing a WinHTTP Interface](choosing-a-winhttp-interface.md) describes the C/C++ API and the COM interface for WinHTTP.
* [WinHTTP Security Considerations](winhttp-security-considerations.md) describes security issues to be aware of when using WinHTTP.
* [Porting WinINet Applications to WinHTTP](porting-wininet-applications-to-winhttp.md) describes how to modify your existing [WinINet](/windows/desktop/WinInet/portal) applications to use the WinHTTP API.
