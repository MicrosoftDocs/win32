---
description: The following material is provided as clarification for the subject of shutting down socket connections closing the sockets. It is important to distinguish the difference between shutting down a socket connection and closing a socket.
ms.assetid: 383747c3-dd3d-4a18-b4e8-2815d5e5c0c7
title: Graceful Shutdown, Linger Options, and Socket Closure
ms.topic: article
ms.date: 05/31/2018
---

# Graceful Shutdown, Linger Options, and Socket Closure

The following material is provided as clarification for the subject of shutting down socket connections closing the sockets. It is important to distinguish the difference between shutting down a socket connection and closing a socket.

Shutting down a socket connection involves an exchange of protocol messages between the two endpoints, hereafter referred to as a shutdown sequence. Two general classes of shutdown sequences are defined: graceful and abortive (also called hard). In a graceful shutdown sequence, any data that has been queued, but not yet transmitted can be sent prior to the connection being closed. In an abortive shutdown, any unsent data is lost. The occurrence of a shutdown sequence (graceful or abortive) can also be used to provide an FD\_CLOSE indication to the associated applications signifying that a shutdown is in progress.

Closing a socket, on the other hand, causes the socket handle to become deallocated so that the application can no longer reference or use the socket in any manner.

In Windows Sockets, both the [**shutdown**](/windows/desktop/api/winsock/nf-winsock-shutdown) function, and the [**WSASendDisconnect**](/windows/desktop/api/Winsock2/nf-winsock2-wsasenddisconnect) function can be used to initiate a shutdown sequence, while the [**closesocket**](/windows/desktop/api/winsock/nf-winsock-closesocket) function is used to deallocate socket handles and free up any associated resources. Some amount of confusion arises, however, from the fact that the **closesocket** function implicitly causes a shutdown sequence to occur if it has not already happened. In fact, it has become a rather common programming practice to rely on this feature and to use **closesocket** to both initiate the shutdown sequence and deallocate the socket handle.

To facilitate this usage, the sockets interface provides for controls by way of the socket option mechanism that allow the programmer to indicate whether the implicit shutdown sequence should be graceful or abortive, and also whether the [**closesocket**](/windows/desktop/api/winsock/nf-winsock-closesocket) function should linger (that is not complete immediately) to allow time for a graceful shutdown sequence to complete. These important distinctions and the ramifications of using **closesocket** in this manner are still not widely understood.

By establishing appropriate values for the socket options SO\_LINGER and SO\_DONTLINGER, the following types of behavior can be obtained with the [**closesocket**](/windows/desktop/api/winsock/nf-winsock-closesocket) function:

-   Abortive shutdown sequence, immediate return from [**closesocket**](/windows/desktop/api/winsock/nf-winsock-closesocket).
-   Graceful shutdown, delaying return until either shutdown sequence completes or a specified time interval elapses. If the time interval expires before the graceful shutdown sequence completes, an abortive shutdown sequence occurs, and [**closesocket**](/windows/desktop/api/winsock/nf-winsock-closesocket) returns.
-   Graceful shutdown, immediate return—allowing the shutdown sequence to complete in the background. Although this is the default behavior, the application has no way of knowing when (or whether) the graceful shutdown sequence actually completes.

The use of the SO\_LINGER and SO\_DONTLINGER socket options and the associated [**linger**](/windows/desktop/api/winsock/ns-winsock-linger) structure is discussed in more detail in the reference sections on [**SOL\_SOCKET Socket Options**](sol-socket-socket-options.md) and the **linger** structure.

One technique that can be used to minimize the chance of problems occurring during connection teardown is to avoid relying on an implicit shutdown being initiated by [**closesocket**](/windows/desktop/api/winsock/nf-winsock-closesocket). Instead, use one of the two explicit shutdown functions, [**shutdown**](/windows/desktop/api/winsock/nf-winsock-shutdown) or [**WSASendDisconnect**](/windows/desktop/api/Winsock2/nf-winsock2-wsasenddisconnect). This in turn causes an FD\_CLOSE indication to be received by the peer application indicating that all pending data has been received. To illustrate this, the following table shows the functions that would be invoked by the client and server components of an application, where the client is responsible for initiating a graceful shutdown.

| Client side                                                                                                                | Server side                                                                                           |
|----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| (1) Invokes [**shutdown**](/windows/desktop/api/winsock/nf-winsock-shutdown)(s, SD\_SEND) to signal end of session and that client has no more data to send. |                                                                                                       |
|                                                                                                                            | (2) Receives FD\_CLOSE, indicating graceful shutdown in progress and that all data has been received. |
|                                                                                                                            | (3) Sends any remaining response data.                                                                |
| (local timing significance only) Gets FD\_READ and calls [**recv**](/windows/desktop/api/winsock/nf-winsock-recv) to get any response data sent by server .  | (4) Invokes [**shutdown**](/windows/desktop/api/winsock/nf-winsock-shutdown)(s, SD\_SEND) to indicate server has no more data to send.  |
| (5) Receives FD\_CLOSE indication.                                                                                         | (local timing significance only) Invokes [**closesocket**](/windows/desktop/api/winsock/nf-winsock-closesocket) .                       |
| (6) Invokes [**closesocket**](/windows/desktop/api/winsock/nf-winsock-closesocket).                                                                          |                                                                                                       |



 

 

 



