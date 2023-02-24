---
title: Concurrency in WinHTTP
description: Microsoft Windows HTTP Services (WinHTTP) supports multithreaded applications. This topic explains what concurrency requirements must be followed by applications that use WinHTTP.
ms.assetid: d8493979-24d7-4fe9-a6fa-29c30535de24
ms.topic: article
ms.date: 02/09/2023
---

# Concurrency in WinHTTP

Microsoft Windows HTTP Services (WinHTTP) supports multithreaded applications. This topic explains what concurrency requirements must be followed by applications that use WinHTTP.

## Stateless functions

Some WinHTTP functions, such as [**WinHttpCrackUrl**](/windows/win32/api/Winhttp/nf-winhttp-winhttpcrackurl) and [**WinHttpTimeToSystemTime**](/windows/win32/api/winhttp/nf-winhttp-winhttptimetosystemtime), don't take any handle as input and are stateless. These functions may be called by multiple threads at the same time.

## Independent handles

Many WinHTTP functions, such as [**WinHttpSendRequest**](/windows/win32/api/Winhttp/nf-winhttp-winhttpsendrequest), [**WinHttpWriteData**](/windows/win32/api/Winhttp/nf-winhttp-winhttpwritedata), [**WinHttpReadData**](/windows/win32/api/winhttp/nf-winhttp-winhttpreaddata), and [**WinHttpCloseHandle**](/windows/win32/api/Winhttp/nf-winhttp-winhttpclosehandle) accept a handle as input and operate on it. These functions may be called by multiple threads at the same time if each thread uses a different handle.

## Handle creation functions

[**WinHttpOpen**](/windows/win32/api/Winhttp/nf-winhttp-winhttpopen) creates a session handle. Multiple sessions can exist in a process. This function may be called by multiple threads at the same time to create separate sessions.

[**WinHttpConnect**](/windows/win32/api/Winhttp/nf-winhttp-winhttpconnect) creates a connection handle. Multiple connection handles can exist per session. This function may be called by multiple threads at the same time to create separate connection handles, including connection handles tied to the same session.

[**WinHttpOpenRequest**](/windows/win32/api/Winhttp/nf-winhttp-winhttpopenrequest) creates a request handle. Multiple requests can exist per connection handle. This function may be called by multiple threads at the same time to create separate requests, including requests tied to the same connection handle.

[**WinHttpWebSocketCompleteUpgrade**](/windows/win32/api/Winhttp/nf-winhttp-winhttpwebsocketcompleteupgrade) creates a web socket handle. At most one web socket can exist per request, so only one thread may call this function at the same time using the same request.

## Handle close function

[**WinHttpCloseHandle**](/windows/win32/api/Winhttp/nf-winhttp-winhttpclosehandle) closes the session, connection, request, or web socket handle provided to it. Only one thread may call this function at the same time using the same handle.

For a request operating synchronously, the handle may only be closed if no thread is currently calling a WinHTTP function using that handle and waiting for it to return, or if the application is inside an informational callback for that handle.

For a request operating asynchronously, the handle may only be closed if no thread is currently calling a WinHTTP function using that handle and waiting for it to return, or if the application is inside an informational or completion callback for that handle.

Once any thread has called **WinHttpCloseHandle**, your application must ensure that it doesn't use that handle again in any WinHTTP function, including **WinHttpCloseHandle** itself. Internally, WinHTTP may reuse the value for a handle; and if an application were to use a handle after closing it, then a race condition could occur. However, an application may use the handle passed into a callback during that callback, even if that handle has been closed; such calls may fail but they are not inherently unsafe from a concurrency standpoint.

If an asynchronous operation is pending (that is, the completion callback for that operation has not yet been called), an application may request cancellation of that operation by closing the relevant handle. Note that, even if the handle is closed, the operation may complete successfully rather than being cancelled. Note also that closing a parent handle (for example, a session) is not sufficient to request cancellation of an asynchronous operation on a child handle (for example, a request).

## Asynchronous callbacks

When an asynchronous operation completes, and an application's completion callback executes, an application may then begin another operation using that handle or close the handle (as long as the application hasn't previously closed that handle).

## Request operations

Once an application begins an operation on a request, it may not begin another operation on that request until the first operation completes. For a synchronous operation, the application must wait until the function returns before any thread begins another operation on the same request handle. For an asynchronous operation, the application must wait until the function returns, and the completion callback is called before any thread begins another operation on the same request handle. For asynchronous operations, the application may request cancellation of a pending operation by closing the relevant handle as explained above.

In some versions of Windows, the send and receive sides of a request are separate and may be used concurrently; an application may do a send-only operation on one thread at the same time that another thread is performing a receive-only operation.

## Web socket send and receive operations

The send and receive sides of a web socket are separate and may be used concurrently; an application may do a send-only operation on one thread at the same time that another thread is performing a receive-only operation.

The [**WinHttpWebSocketReceive**](/windows/win32/api/winhttp/nf-winhttp-winhttpwebsocketreceive) functions operates only on the receive side, and it may be called at the same time that another thread is performing a send operation.

The [**WinHttpWebSocketSend**](/windows/win32/api/winhttp/nf-winhttp-winhttpwebsocketsend) and [**WinHttpWebSocketShutdown**](/windows/win32/api/winhttp/nf-winhttp-winhttpwebsocketshutdown) functions operate only on the send side, and one of these functions may be called at the same time that another thread is performing a receive operation.

The [**WinHttpWebSocketClose**](/windows/win32/api/winhttp/nf-winhttp-winhttpwebsocketclose) function operates on both the send and receive sides, and it may not be called at the same time that another thread is performing either a send or a receive operation on that web socket.
