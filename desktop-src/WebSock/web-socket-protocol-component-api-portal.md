---
title: WebSocket Protocol Component API
description: WebSocket Protocol Component API
ms.assetid: ae73fd5e-9715-448c-b7ca-898f2705e228
ms.topic: reference
ms.date: 05/31/2018
---

# WebSocket Protocol Component API

## Purpose

> [!IMPORTANT]
> **Choosing a WebSocket API on Windows** — There are multiple WebSocket options. Choose based on your application type:
>
> | API | Best for | Notes |
> |-----|----------|-------|
> | **WinHTTP WebSocket** ([WinHttpWebSocketSend](/windows/desktop/api/winhttp/nf-winhttp-winhttpwebsocketsend), etc.) | Services, server-side code, C/C++ apps needing WebSocket over WinHTTP | Integrates with WinHTTP proxy/auth; requires Windows 8+. Recommended for Win32 service scenarios. |
> | **Windows.Networking.Sockets** ([MessageWebSocket](/uwp/api/Windows.Networking.Sockets.MessageWebSocket), [StreamWebSocket](/uwp/api/Windows.Networking.Sockets.StreamWebSocket)) | UWP apps, modern C++/WinRT desktop apps | Highest-level API; handles framing and TLS. Apps must implement their own reconnection logic. Recommended for new desktop/UWP apps. |
> | **WebSocket Protocol Component** (this API — websocket.dll) | Custom transport implementations that need only protocol framing/parsing | Low-level: does **not** handle I/O, HTTP upgrade, authentication, or proxy. You must provide your own transport (typically raw Winsock + TLS). |
> | **System.Net.WebSockets** (.NET) | .NET applications | Managed, async-first, cross-platform. Use `ClientWebSocket` for clients. |
> | **Third-party libraries** (libwebsockets, Boost.Beast, etc.) | Cross-platform C/C++ | Not Windows-specific; useful when targeting multiple platforms. |
>
> For most applications, **WinHTTP WebSocket** (services/Win32) or **Windows.Networking.Sockets** (modern apps) is the correct choice. Use the low-level WebSocket Protocol Component API only if you need custom framing over a transport you fully control.

The WebSocket Protocol Component API enables asynchronous, bi-directional communication channels over HTTP that work across existing network intermediaries. With the WebSocket Protocol Component API, a client uses HTTP to communicate with a server, and then both sides switch to using the underlying protocol that HTTP was layered on (such as TCP or SSL). The goal is to first use HTTP to traverse over network intermediaries, and then use the established end-to-end underlying TCP/SSL channel for bi-directional application communication. The WebSocket protocol \[[WSPROTO](https://tools.ietf.org/html/rfc6455)\] is defined at the IETF, while an associated Javascript API ([WebSockets](https://websockets.spec.whatwg.org//)) is defined at the WHATWG.

## In this section



| Topic                                                                                                          | Description                                                                 |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [**WebSocket Protocol Component API Data Types**](web-socket-protocol-component-api-data-types.md)<br/> | The WebSocket Protocol Component API defines these data types.<br/>   |
| [WebSocket Protocol Component API Enumerations](web-socket-protocol-component-api-enumerations.md)<br/> | The WebSocket Protocol Component API defines these enumerations.<br/> |
| [WebSocket Protocol Component API Functions](web-socket-protocol-component-api-functions.md)<br/>       | The WebSocket Protocol Component API defines these functions.<br/>    |
| [WebSocket Protocol Component API Structures](web-socket-protocol-component-api-structures.md)<br/>     | The WebSocket Protocol Component API defines these structures.<br/>   |



 

## Developer audience

The WebSocket Protocol Component API is designed for use by use by C/C++ programmers. Familiarity with HTTP and Windows networking is required.

> [!Note]  
> The preferred way to use the WebSocket protocol on Windows is through the [Windows HTTP Services (WinHTTP) API](/windows/desktop/WinHttp/winhttp-start-page) or the [Windows.Networking.Sockets namespace](/uwp/api/Windows.Networking.Sockets).

 

## Run-time requirements

The WebSocket Protocol Component API requires Windows 8 and later versions of the Windows operating system. The APIs can be dynamically linked through websocket.dll.

> [!Note]  
> websocket.dll provides support for client and server handshake related HTTP headers, verifies received handshake data, and parses the WebSocket data stream. It does not handle any HTTP-specific operations (redirection, authentication, proxy support) nor perform any I/O operations (sending or receiving WebSocket stream bytes).

 

## Related topics

<dl> <dt>

[HTTP](/windows/desktop/Http/http-api-start-page)
</dt> <dt>

[Windows HTTP Services (WinHTTP)](/windows/desktop/WinHttp/winhttp-start-page)
</dt> </dl>

 

