---
Description: 'One major issue in porting applications from a Berkeley Sockets environment to a Windows environment involves blocking; that is, invoking a function that does not return until the associated operation is completed.'
ms.assetid: '13aedad7-5f3b-4d73-b8e5-be3a095294bc'
title: 'Windows Sockets 1.1 Blocking Routines and EINPROGRESS'
---

# Windows Sockets 1.1 Blocking Routines and EINPROGRESS

One major issue in porting applications from a Berkeley Sockets environment to a Windows environment involves blocking; that is, invoking a function that does not return until the associated operation is completed. A problem arises when the operation takes an arbitrarily long time to complete: an example is a [**recv**](recv-2.md) function, which might block until data has been received from the peer system. The default behavior within the Berkeley Sockets model is for a socket to operate in blocking mode unless the programmer explicitly requests that operations be treated as nonblocking. Windows Sockets 1.1 environments could not assume preemptive scheduling. Therefore, it was strongly recommended that programmers use the nonblocking (asynchronous) operations if at all possible with Windows Sockets 1.1. Because this was not always possible, the pseudo-blocking facilities described in the following were provided.

> [!Note]  
> Windows Sockets 2 only runs on preemptive 32-bit operating systems where deadlocks are not a problem. Programming practices recommended for Windows Sockets 1.1 are not necessary in Windows Sockets 2.

 

Even on a blocking socket, some functions — [**bind**](bind-2.md), [**getsockopt**](getsockopt-2.md), and [**getpeername**](getpeername-2.md) for example — complete immediately. There is no difference between a blocking and a nonblocking operation for those functions. Other operations, such as [**recv**](recv-2.md), can complete immediately or take an arbitrary time to complete, depending on various transport conditions. When applied to a blocking socket, these operations are referred to as blocking operations. The following functions can block:

-   [**recv**](recv-2.md)
-   [**recvfrom**](recvfrom-2.md)
-   [**send**](send-2.md)
-   [**sendto**](sendto-2.md)

With 16-bit Windows Sockets 1.1, a blocking operation that cannot complete immediately is handled by pseudo-blocking as follows.

The service provider initiates the operation, then enters a loop in which it dispatches any Windows messages (yielding the processor to another thread, if necessary), and then checks for the completion of the Windows Sockets function. If the function has completed, or if [**WSACancelBlockingCall**](wsacancelblockingcall-2.md) has been invoked, the blocking function completes with an appropriate result.

A service provider must allow installation of a blocking hook function that does not process messages in order to avoid the possibility of re-entrant messages while a blocking operation is outstanding. The simplest such blocking hook function would return **FALSE**. If a Windows Sockets DLL depends on messages for internal operation, it can execute **PeekMessage**(**hMyWnd**...) before executing the application blocking hook so that it can get its messages without affecting the rest of the system.

In a 16-bit Windows Sockets 1.1 environment, if a Windows message is received for a process for which a blocking operation is in progress, there is a risk that the application will attempt to issue another Windows Sockets call. Because of the difficulty in managing this condition safely, Windows Sockets 1.1 does not support such application behavior. An application is not permitted to make more than one nested Windows Sockets function call. Only one outstanding function call is allowed for a particular task. The only exceptions are two functions that are provided to assist the programmer in this situation: [**WSAIsBlocking**](wsaisblocking-2.md) and [**WSACancelBlockingCall**](wsacancelblockingcall-2.md).

The [**WSAIsBlocking**](wsaisblocking-2.md) function can be called at any time to determine whether or not a blocking Windows Sockets 1.1 call is in progress. Similarly, the [**WSACancelBlockingCall**](wsacancelblockingcall-2.md) function can be called at any time to cancel an in-progress blocking call. Any other nesting of Windows Sockets functions fails with the error WSAEINPROGRESS.

It should be emphasized that this restriction applies to both blocking and nonblocking operations. For Windows Sockets 2 applications that negotiate version 2.0 or higher at the time of calling [**WSAStartup**](wsastartup-2.md), no restriction on the nesting of operations exits. Operations can become nested under rare circumstances, such as during a [**WSAAccept**](wsaaccept-2.md) conditional-acceptance callback, or if a service provider in turn invokes a Windows Sockets 2 function.

Although this mechanism is sufficient for simple applications, it cannot support the complex message-dispatching requirements of more advanced applications (for example, those using the MDI model). For such applications, the Windows Sockets API includes the function [**WSASetBlockingHook**](wsasetblockinghook-2.md), which allows the application to specify a special routine which can be called instead of the default message dispatch routine described in the preceding discussion.

The Windows Sockets provider calls the blocking hook only if all of the following are true:

-   The routine is one that is defined as being able to block.
-   The specified socket is a blocking socket.
-   The request cannot be completed immediately.

A socket is set to blocking by default, but the [**ioctlsocket**](ioctlsocket-2.md) function with the **FIONBIO** IOCTL or the [**WSAAsyncSelect**](wsaasyncselect-2.md) function can set a socket to nonblocking mode.

The blocking hook is never called and the application does not need to be concerned with the re-entrancy issues the blocking hook can introduce, if an application follows these guidelines:

-   It uses only nonblocking sockets.
-   It uses the [**WSAAsyncSelect**](wsaasyncselect-2.md) and/or the **WSAAsyncGetXByY** routines instead of [**select**](select-2.md) and the **getXbyY** routines.

If a Windows Sockets 1.1 application invokes an asynchronous or nonblocking operation that takes a pointer to a memory object (a buffer or a global variable, for example) as an argument, it is the responsibility of the application to ensure that the object is available to Windows Sockets throughout the operation. The application must not invoke any Windows function that might affect the mapping or address viability of the memory involved.

 

 



