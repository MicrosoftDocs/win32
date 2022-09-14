---
description: Windows Sockets 2 supports overlapped I/O and all transport providers support this capability.
ms.assetid: b36ab606-df1a-4254-b048-6d47eb366275
title: Overlapped I/O and Event Objects
ms.topic: article
ms.date: 05/31/2018
---

# Overlapped I/O and Event Objects

Windows Sockets 2 supports overlapped I/O and all transport providers support this capability. Overlapped I/O follows the model established in Windows and can be performed on sockets created with the [**socket**](/windows/desktop/api/Winsock2/nf-winsock2-socket) function or sockets created with the [**WSASocket**](/windows/desktop/api/Winsock2/nf-winsock2-wsasocketa) function with the **WSA\_FLAG\_OVERLAPPED** flag set in the *dwFlags* parameter.

> [!Note]  
> Creating a socket with the overlapped attribute has no impact on whether a socket is currently in blocking or nonblocking mode. Sockets created with the overlapped attribute can be used to perform overlapped I/O—doing so does not change the blocking mode of a socket. Since overlapped I/O operations do not block, the blocking mode of a socket is irrelevant for these operations.

 

For receiving, applications use the [**WSARecv**](/windows/desktop/api/Winsock2/nf-winsock2-wsarecv) or [**WSARecvFrom**](/windows/desktop/api/Winsock2/nf-winsock2-wsarecvfrom) functions to supply buffers into which data is to be received. If one or more buffers are posted prior to the time when data has been received by the network, that data could be placed in the user's buffers immediately as it arrives. Thus, it can avoid the copy operation that would otherwise occur at the time the [**recv**](/windows/desktop/api/winsock/nf-winsock-recv) or [**recvfrom**](/windows/desktop/api/winsock/nf-winsock-recvfrom) function is invoked. If data is already present when receive buffers are posted, it is copied immediately into the user's buffers.

If data arrives when no receive buffers have been posted by the application, the network resorts to the familiar synchronous style of operation. That is, the incoming data is buffered internally until the application issues a receive call and thereby supplies a buffer into which the data can be copied. An exception to this is when the application uses [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt) to set the size of the receive buffer to zero. In this instance, reliable protocols would only allow data to be received when application buffers had been posted and data on unreliable protocols would be lost.

On the sending side, applications use [**WSASend**](/windows/desktop/api/Winsock2/nf-winsock2-wsasend) or [**WSASendTo**](/windows/desktop/api/Winsock2/nf-winsock2-wsasendto) to supply pointers to filled buffers and then agree not to disturb the buffers in any way until the network has consumed the buffer's contents.

Overlapped send and receive calls return immediately. A return value of zero indicates that the I/O operation was completed immediately and that the corresponding completion indication already occurred. That is, the associated event object has been signaled, or a completion routine has been queued and will be executed when the calling thread gets into the alertable wait state.

A return value of SOCKET\_ERROR coupled with an error code of [WSA\_IO\_PENDING](windows-sockets-error-codes-2.md) indicates that the overlapped operation has been successfully initiated and that a subsequent indication will be provided when send buffers have been consumed or when a receive operation has been completed. However, for sockets that are byte-stream style, the completion indication occurs whenever the incoming data is exhausted, regardless of whether the buffers are full. Any other error code indicates that the overlapped operation was not successfully initiated and that no completion indication will be forthcoming.

Both send and receive operations can be overlapped. The receive functions can be invoked several times to post receive buffers in preparation for incoming data, and the send functions can be invoked several times to queue multiple buffers to send. While the application can rely upon a series of overlapped send buffers being sent in the order supplied, the corresponding completion indications might occur in a different order. Likewise, on the receiving side, buffers can be filled in the order they are supplied, but the completion indications might occur in a different order.

In many cases, Winsock overlapped operations using [**AcceptEx**](/windows/win32/api/mswsock/nf-mswsock-acceptex), [**ConnectEx**](/windows/desktop/api/Mswsock/nc-mswsock-lpfn_connectex), [**WSASend**](/windows/desktop/api/Winsock2/nf-winsock2-wsasend), [**WSARecv**](/windows/desktop/api/Winsock2/nf-winsock2-wsarecv), [**TransmitFile**](/windows/win32/api/mswsock/nf-mswsock-transmitfile), and similar functions are cancelable. However, behavior is undefined for the continued use of a socket that has canceled outstanding operations. The [**closesocket**](/windows/desktop/api/winsock/nf-winsock-closesocket) function should be called after canceling an overlapped operation. Therefore, for best results, instead of canceling the I/O directly, the **closesocket** function should be called to close the socket which will eventually discontinue all pending operations.

The deferred completion feature of overlapped I/O is also available for [**WSAIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl), which is an enhanced version of [**ioctlsocket**](/windows/desktop/api/winsock/nf-winsock-ioctlsocket).

 

 
