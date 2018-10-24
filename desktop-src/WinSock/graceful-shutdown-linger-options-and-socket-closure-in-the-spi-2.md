---
Description: It is important to distinguish between shutting down a socket connection and closing a socket.
ms.assetid: f076b1ec-6b96-4386-8519-4728e0a2b1ff
title: Graceful Shutdown, Linger Options, and Socket Closure in the SPI
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Graceful Shutdown, Linger Options, and Socket Closure in the SPI

It is important to distinguish between shutting down a socket connection and closing a socket. Shutting down a socket connection involves an exchange of protocol messages between the two endpoints, which is hereafter referred to as a shutdown sequence. Two general classes of shutdown sequences are defined: graceful and abortive. In a graceful shutdown sequence, any data that has been queued but not yet transmitted can be sent prior to the connection being closed. In an abortive shutdown, any unsent data is lost. The occurrence of a shutdown sequence (graceful or abortive) can also be used to provide an FD\_CLOSE indication to the associated applications signifying that a shutdown is in progress. Closing a socket, on the other hand, causes the socket handle to become deallocated so that the application can no longer reference or use the socket in any manner.

In Windows Sockets, both the [**WSPShutdown**](https://msdn.microsoft.com/en-us/library/ms742294(v=VS.85).aspx) function and the [**WSPSendDisconnect**](https://msdn.microsoft.com/en-us/library/ms742290(v=VS.85).aspx) function can be used to initiate a shutdown sequence, while the [**WSPCloseSocket**](https://msdn.microsoft.com/en-us/library/ms742271(v=VS.85).aspx) function is used to deallocate socket handles and free up any associated resources. Some amount of confusion arises, however, from the fact that the **WSPCloseSocket** function will implicitly cause a shutdown sequence to occur if it has not already happened. In fact, it has become a rather common programming practice to rely on this feature and use **WSPCloseSocket** to both initiate the shutdown sequence and deallocate the socket handle.

To facilitate this usage, the sockets interface provides for controls through the socket option mechanism that allows the programmer to indicate whether the implicit shutdown sequence should be graceful or abortive, and also whether the function should linger that is, not complete immediately) to allow time for a graceful shutdown sequence to complete.

By establishing appropriate values for the socket options SO\_LINGER and SO\_DONTLINGER, the following types of behavior can be obtained with the [**WSPCloseSocket**](https://msdn.microsoft.com/en-us/library/ms742271(v=VS.85).aspx) function.

-   Abortive shutdown sequence, immediate return from [**WSPCloseSocket**](https://msdn.microsoft.com/en-us/library/ms742271(v=VS.85).aspx).
-   Graceful shutdown, delay return until either shutdown sequence completes or a specified time interval elapses. If the time interval expires before the graceful shutdown sequence completes, an abortive shutdown sequence occurs and [**WSPCloseSocket**](https://msdn.microsoft.com/en-us/library/ms742271(v=VS.85).aspx) returns.
-   Graceful shutdown, return immediately, and allow the shutdown sequence to complete in the background. This is the default behavior. Note, however, that the application has no way of knowing when (or whether) the graceful shutdown sequence completes.

One technique that can be used to minimize the chance of problems occurring during connection teardown is not to rely on an implicit shutdown being initiated by [**WSPCloseSocket**](https://msdn.microsoft.com/en-us/library/ms742271(v=VS.85).aspx). Instead, one of the two explicit shutdown functions ([**WSPShutdown**](https://msdn.microsoft.com/en-us/library/ms742294(v=VS.85).aspx) or [**WSPSendDisconnect**](https://msdn.microsoft.com/en-us/library/ms742290(v=VS.85).aspx)) are used. This in turn will cause an FD\_CLOSE indication to be received by the peer application indicating that all pending data has been received. To illustrate this, the following table shows the functions that would be invoked by the client and server components of an application, where the client is responsible for initiating a graceful shutdown.

| Client side                                                                                                                         | Server side                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| (1) Invokes [**WSPShutdown**](https://msdn.microsoft.com/en-us/library/ms742294(v=VS.85).aspx) (*s*, SD\_SEND) to signal end of session and that client has no more data to send. |                                                                                                              |
|                                                                                                                                     | (2) Receives FD\_CLOSE, indicating graceful shutdown in progress and that all data has been received.        |
|                                                                                                                                     | (3) Sends any remaining response data.                                                                       |
| (5') Gets FD\_READ and invoke recv to get any response data sent by server.                                                         | (4) Invokes [**WSPShutdown**](https://msdn.microsoft.com/en-us/library/ms742294(v=VS.85).aspx)(*s*, SD\_SEND) to indicate server has no more data to send. |
| (5) Receives FD\_CLOSE indication.                                                                                                  | (4') Invokes [**WSPCloseSocket**](https://msdn.microsoft.com/en-us/library/ms742271(v=VS.85).aspx)                                                      |
| (6) Invokes [**WSPCloseSocket**](https://msdn.microsoft.com/en-us/library/ms742271(v=VS.85).aspx)                                                                              |                                                                                                              |



 

The timing sequence is maintained from step (1) to step (6) between the client and the server, except for steps (4') and (5') which only have local timing significance in the sense that step (5) follows step (5') on the client side while step (4') follows step (4) on the server side, with no timing relationship with the remote party.

 

 



