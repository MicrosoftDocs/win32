---
Description: The WSAAccept function lets an application obtain caller information such as caller identifier and Quality of Service before deciding whether to accept an incoming connection request.
ms.assetid: 65883556-6890-4d0a-8c7f-c4ff68642caf
title: Connection Setup and Teardown
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Connection Setup and Teardown

The [**WSAAccept**](/windows/win32/Winsock2/nf-winsock2-wsaaccept?branch=master) function lets an application obtain caller information such as caller identifier and Quality of Service before deciding whether to accept an incoming connection request. This is done with a callback to an application-supplied condition function.

User-to-user data specified by parameters in the [**WSAConnect**](/windows/win32/Winsock2/nf-winsock2-wsaconnect?branch=master) function and the condition function of [**WSAAccept**](/windows/win32/Winsock2/nf-winsock2-wsaaccept?branch=master) can be transferred to the peer during connection establishment, provided this feature is supported by the service provider.

It is also possible (for protocols that support this) to exchange user data between the endpoints at connection teardown time. The end that initiates the teardown can call the [**WSASendDisconnect**](/windows/win32/Winsock2/nf-winsock2-wsasenddisconnect?branch=master) function to indicate that no more data be sent and to initiate the connection teardown sequence. For certain protocols, part of teardown is the delivery of disconnect data from the teardown initiator. After receiving notice that the remote end has initiated teardown (typically by the FD\_CLOSE indication), the [**WSARecvDisconnect**](/windows/win32/Winsock2/nf-winsock2-wsarecvdisconnect?branch=master) function can be called to receive the disconnect data, if any.

To illustrate how disconnect data can be used, consider the following scenario. The client half of a client/server application is responsible for terminating a socket connection. Coincident with the termination, it provides (using disconnect data) the total number of transactions it processed with the server. The server in turn responds with the cumulative total of transactions that it has processed with all clients. The sequence of calls and indications might occur as follows:

| Client side                                                                                                              | Server side                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| (1) Invoke [**WSASendDisconnect**](/windows/win32/Winsock2/nf-winsock2-wsasenddisconnect?branch=master) to conclude session and supply transaction total.            |                                                                                                                                                                                                                               |
|                                                                                                                          | (2) Get FD\_CLOSE, [**recv**](/windows/win32/winsock/nf-winsock-recv?branch=master) with a return value of zero, or [WSAEDISCON](windows-sockets-error-codes-2.md#wsaediscon) error return from [**WSARecv**](/windows/win32/Winsock2/nf-winsock2-wsarecv?branch=master) indicating graceful shutdown in progress. |
|                                                                                                                          | (3) Invoke [**WSARecvDisconnect**](/windows/win32/Winsock2/nf-winsock2-wsarecvdisconnect?branch=master) to get client's transaction total.                                                                                                                                |
|                                                                                                                          | (4) Compute cumulative grand total of all transactions.                                                                                                                                                                       |
|                                                                                                                          | (5) Invoke [**WSASendDisconnect**](/windows/win32/Winsock2/nf-winsock2-wsasenddisconnect?branch=master) to transmit grand total.                                                                                                                                          |
| (6) Receive FD\_CLOSE indication.                                                                                        | (5a) Invoke [**closesocket**](/windows/win32/winsock/nf-winsock-closesocket?branch=master).                                                                                                                                                                             |
| (7) Invoke [**WSARecvDisconnect**](/windows/win32/Winsock2/nf-winsock2-wsarecvdisconnect?branch=master) to receive and store cumulative grand total of transactions. |                                                                                                                                                                                                                               |
| (8) Invoke [**closesocket**](/windows/win32/winsock/nf-winsock-closesocket?branch=master)                                                                          |                                                                                                                                                                                                                               |



 

Note that step (5a) must follow step (5), but has no timing relationship with step (6), (7), or (8).

 

 



