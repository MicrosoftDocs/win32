---
Description: 'The data transport functions exposed by Ws2spi.h.'
ms.assetid: '6900faa3-79bb-4ed8-b83e-148eb10425a0'
title: Generic Data Transport Functions
---

# Generic Data Transport Functions

This section lists the data transport functions exposed by Ws2spi.h.



| Function                                                   | Description                                                                                                                                                                                             |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WSPAccept**](wspaccept-2.md)                           | An incoming connection is acknowledged and associated with an immediately created socket. The original socket is returned to the listening state. This function also allows for conditional acceptance. |
| [**WSPAsyncSelect**](wspasyncselect-2.md)                 | Performs asynchronous version of [**WSPSelect**](wspselect-2.md).                                                                                                                                      |
| [**WSPBind**](wspbind-2.md)                               | Assigns a local name to an unnamed socket.                                                                                                                                                              |
| [**WSPCancelBlockingCall**](wspcancelblockingcall-2.md)   | Cancels an outstanding blocking Windows Sockets call.                                                                                                                                                   |
| [**WSPCleanup**](wspcleanup-2.md)                         | Signs off from the underlying Windows Sockets service provider.                                                                                                                                         |
| [**WSPCloseSocket**](wspclosesocket-2.md)                 | Removes a socket from the per-process object reference table. Only blocks if SO\_LINGER is set with a nonzero time-out on a blocking socket.                                                            |
| [**WSPConnect**](wspconnect-2.md)                         | Initiates a connection on the specified socket. This function also allows for exchange of connect data and QoS specification.                                                                           |
| [**WSPDuplicateSocket**](wspduplicatesocket-2.md)         | Returns a [**WSAPROTOCOL\_INFO**](wsaprotocol-info-2.md) structure that can be used to create a new socket descriptor for a shared socket.                                                             |
| [**WSPEnumNetworkEvents**](wspenumnetworkevents-2.md)     | Discovers occurrences of network events.                                                                                                                                                                |
| [**WSPEventSelect**](wspeventselect-2.md)                 | Associates network events with an event object.                                                                                                                                                         |
| [**WSPGetOverlappedResult**](wspgetoverlappedresult-2.md) | Gets completion status of overlapped operation.                                                                                                                                                         |
| [**WSPGetPeerName**](wspgetpeername-2.md)                 | Retrieves the name of the peer connected to the specified socket.                                                                                                                                       |
| [**WSPGetSockName**](wspgetsockname-2.md)                 | Retrieves the local address to which the specified socket is bound.                                                                                                                                     |
| [**WSPGetSockOpt**](wspgetsockopt-2.md)                   | Retrieves options associated with the specified socket.                                                                                                                                                 |
| [**WSPGetQOSByName**](wspgetqosbyname-2.md)               | Supplies QoS parameters based on a well-known service name.                                                                                                                                             |
| [**WSPIoctl**](wspioctl-2.md)                             | Provides control for sockets.                                                                                                                                                                           |
| [**WSPJoinLeaf**](wspjoinleaf-2.md)                       | Joins a leaf node into a multipoint session.                                                                                                                                                            |
| [**WSPListen**](wsplisten-2.md)                           | Listens for incoming connections on a specified socket.                                                                                                                                                 |
| [**WSPRecv**](wsprecv-2.md)                               | Receives data from a connected or unconnected socket. This function accommodates scatter/gather I/O, overlapped sockets, and provides the flags parameter as IN/OUT.                                    |
| [**WSPRecvDisconnect**](wsprecvdisconnect-2.md)           | Terminates reception on a socket, and retrieve the disconnect data if the socket is connection-oriented.                                                                                                |
| [**WSPRecvFrom**](wsprecvfrom-2.md)                       | Receives data from either a connected or unconnected socket. This function accommodates scatter/gather I/O, overlapped sockets and provides the flags parameter as IN/OUT.                              |
| [**WSPSelect**](wspselect-2.md)                           | Performs synchronous I/O multiplexing.                                                                                                                                                                  |
| [**WSPSend**](wspsend-2.md)                               | Sends data to a connected socket. This function also accommodates scatter/gather I/O and overlapped sockets.                                                                                            |
| [**WSPSendDisconnect**](wspsenddisconnect-2.md)           | Initiates termination of a socket connection and optionally send disconnect data.                                                                                                                       |
| [**WSPSendTo**](wspsendto-2.md)                           | Sends data to either a connected or unconnected socket. This function also accommodates scatter/gather I/O and overlapped sockets.                                                                      |
| [**WSPSetSockOpt**](wspsetsockopt-2.md)                   | Stores options associated with the specified socket.                                                                                                                                                    |
| [**WSPShutdown**](wspshutdown-2.md)                       | Shuts down part of a full-duplex connection.                                                                                                                                                            |
| [**WSPSocket**](wspsocket-2.md)                           | A socket creation function which takes a [**WSAPROTOCOL\_INFO**](wsaprotocol-info-2.md) structure as input and allows overlapped sockets to be created.                                                |
| [**WSPStartup**](wspstartup-2.md)                         | Initializes the underlying Windows Sockets service provider.                                                                                                                                            |



 

 

 



