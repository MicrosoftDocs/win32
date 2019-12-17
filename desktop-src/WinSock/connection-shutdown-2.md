---
Description: The following describes operations incident to shutting down an established socket connection.
ms.assetid: 052e04a4-5290-4dca-af7a-cd590ebfbe15
title: Connection Shutdown
ms.topic: article
ms.date: 05/31/2018
---

# Connection Shutdown

The following describes operations incident to shutting down an established socket connection.

## Initiating Shutdown Sequence

A socket connection can be taken down in one of several ways. [**WSPShutdown**](https://msdn.microsoft.com/library/ms742294(v=VS.85).aspx) (with *how* equal to SD\_SEND or SD\_BOTH), and [**WSPSendDisconnect**](https://msdn.microsoft.com/library/ms742290(v=VS.85).aspx) may be used to initiate a graceful connection shutdown. [**WSPCloseSocket**](https://msdn.microsoft.com/library/ms742271(v=VS.85).aspx) can be used to initiate either a graceful or abortive shutdown, depending on the linger options invoked by the closing a socket. See below for more information about graceful and abortive shutdowns, and linger options.

## Indicating Remote Shutdown

Service providers indicate connection teardown that is initiated by the remote party through the FD\_CLOSE network event. Graceful shutdown is also be indicated through [**WSPRecv**](https://msdn.microsoft.com/library/ms742288(v=VS.85).aspx) when the number of bytes read is 0 for byte-stream protocols, or through a return error code of WSAEDISCON for message-oriented protocols. In any case, a **WSPRecv** return error code of WSAECONNRESET indicates an abortive shutdown.

## Exchanging User Data at Shutdown Time

At connection teardown time, it is also possible (for protocols that support this) to exchange user data between the endpoints. The end that initiates the teardown can call [**WSPSendDisconnect**](https://msdn.microsoft.com/library/ms742290(v=VS.85).aspx) to indicate that no more data is to be sent and cause the connection teardown sequence to be initiated. For certain protocols, part of this teardown sequence is the delivery of disconnect data from the teardown initiator. After receiving notice that the remote end has initiated the teardown sequence (typically through the FD\_CLOSE indication), the [**WSPRecvDisconnect**](https://msdn.microsoft.com/library/ms742285(v=VS.85).aspx) function may be called to receive the disconnect data (if any).

To illustrate how disconnect data might be used, consider the following scenario. The client half of a client/server application is responsible for terminating a socket connection. Coincident with the termination it provides (through disconnect data) the total number of transactions it processed with the server. The server in turn responds with the cumulative grand total of transactions that it has processed with all clients. The sequence of calls and indications might occur as shown in the following table.

| Client side                                                                                                               | Server side                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| (1) Invokes [**WSPSendDisconnect**](https://msdn.microsoft.com/library/ms742290(v=VS.85).aspx) to conclude session and supply transaction total.            |                                                                                                                                         |
|                                                                                                                           | (2) Gets FD\_CLOSE, or [**WSPRecv**](https://msdn.microsoft.com/library/ms742288(v=VS.85).aspx) with a return value of zero or WSAEDISCON indicating graceful shutdown in progress. |
|                                                                                                                           | (3) Invokes [**WSPRecvDisconnect**](https://msdn.microsoft.com/library/ms742285(v=VS.85).aspx) to get client's transaction total.                                         |
|                                                                                                                           | (4) Computes cumulative grand total of all transactions.                                                                                |
|                                                                                                                           | (5) Invokes [**WSPSendDisconnect**](https://msdn.microsoft.com/library/ms742290(v=VS.85).aspx) to transmit grand total.                                                   |
| (6) Receives FD\_CLOSE indication.                                                                                        | (5') Invokes [**WSPClosesocket**](https://msdn.microsoft.com/library/ms742271(v=VS.85).aspx)                                                                                 |
| (7) Invokes [**WSPRecvDisconnect**](https://msdn.microsoft.com/library/ms742285(v=VS.85).aspx) to receive and store cumulative grand total of transactions. |                                                                                                                                         |
|                                                                                                                           | (8) Invokes [**WSPClosesocket**](https://msdn.microsoft.com/library/ms742271(v=VS.85).aspx)                                                                                  |



 

Step (5') must follow step (5), but has no timing relationship with steps (6), (7), or (8).

 

 



