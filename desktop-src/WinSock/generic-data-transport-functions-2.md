---
Description: The data transport functions exposed by Ws2spi.h.
ms.assetid: 6900faa3-79bb-4ed8-b83e-148eb10425a0
title: Generic Data Transport Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Generic Data Transport Functions

This section lists the data transport functions exposed by Ws2spi.h.



| Function                                                   | Description                                                                                                                                                                                             |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WSPAccept**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspaccept)                           | An incoming connection is acknowledged and associated with an immediately created socket. The original socket is returned to the listening state. This function also allows for conditional acceptance. |
| [**WSPAsyncSelect**](/windows/desktop/api/Ws2spi/)                 | Performs asynchronous version of [**WSPSelect**](/windows/desktop/api/Ws2spi/).                                                                                                                                      |
| [**WSPBind**](/windows/desktop/api/Ws2spi/)                               | Assigns a local name to an unnamed socket.                                                                                                                                                              |
| [**WSPCancelBlockingCall**](/windows/desktop/api/Ws2spi/)   | Cancels an outstanding blocking Windows Sockets call.                                                                                                                                                   |
| [**WSPCleanup**](/windows/desktop/api/Ws2spi/)                         | Signs off from the underlying Windows Sockets service provider.                                                                                                                                         |
| [**WSPCloseSocket**](/windows/desktop/api/Ws2spi/)                 | Removes a socket from the per-process object reference table. Only blocks if SO\_LINGER is set with a nonzero time-out on a blocking socket.                                                            |
| [**WSPConnect**](/windows/desktop/api/Ws2spi/)                         | Initiates a connection on the specified socket. This function also allows for exchange of connect data and QoS specification.                                                                           |
| [**WSPDuplicateSocket**](/windows/desktop/api/Ws2spi/)         | Returns a [**WSAPROTOCOL\_INFO**](/windows/desktop/api/Winsock2/) structure that can be used to create a new socket descriptor for a shared socket.                                                             |
| [**WSPEnumNetworkEvents**](/windows/desktop/api/Ws2spi/)     | Discovers occurrences of network events.                                                                                                                                                                |
| [**WSPEventSelect**](/windows/desktop/api/Ws2spi/)                 | Associates network events with an event object.                                                                                                                                                         |
| [**WSPGetOverlappedResult**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspgetoverlappedresult) | Gets completion status of overlapped operation.                                                                                                                                                         |
| [**WSPGetPeerName**](/windows/desktop/api/Ws2spi/)                 | Retrieves the name of the peer connected to the specified socket.                                                                                                                                       |
| [**WSPGetSockName**](/windows/desktop/api/Ws2spi/)                 | Retrieves the local address to which the specified socket is bound.                                                                                                                                     |
| [**WSPGetSockOpt**](/windows/desktop/api/Ws2spi/)                   | Retrieves options associated with the specified socket.                                                                                                                                                 |
| [**WSPGetQOSByName**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspgetqosbyname)               | Supplies QoS parameters based on a well-known service name.                                                                                                                                             |
| [**WSPIoctl**](/windows/desktop/api/Ws2spi/)                             | Provides control for sockets.                                                                                                                                                                           |
| [**WSPJoinLeaf**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspjoinleaf)                       | Joins a leaf node into a multipoint session.                                                                                                                                                            |
| [**WSPListen**](/windows/desktop/api/Ws2spi/)                           | Listens for incoming connections on a specified socket.                                                                                                                                                 |
| [**WSPRecv**](/windows/desktop/api/Ws2spi/)                               | Receives data from a connected or unconnected socket. This function accommodates scatter/gather I/O, overlapped sockets, and provides the flags parameter as IN/OUT.                                    |
| [**WSPRecvDisconnect**](/windows/desktop/api/Ws2spi/)           | Terminates reception on a socket, and retrieve the disconnect data if the socket is connection-oriented.                                                                                                |
| [**WSPRecvFrom**](/windows/desktop/api/Ws2spi/)                       | Receives data from either a connected or unconnected socket. This function accommodates scatter/gather I/O, overlapped sockets and provides the flags parameter as IN/OUT.                              |
| [**WSPSelect**](/windows/desktop/api/Ws2spi/)                           | Performs synchronous I/O multiplexing.                                                                                                                                                                  |
| [**WSPSend**](/windows/desktop/api/Ws2spi/)                               | Sends data to a connected socket. This function also accommodates scatter/gather I/O and overlapped sockets.                                                                                            |
| [**WSPSendDisconnect**](/windows/desktop/api/Ws2spi/)           | Initiates termination of a socket connection and optionally send disconnect data.                                                                                                                       |
| [**WSPSendTo**](/windows/desktop/api/Ws2spi/)                           | Sends data to either a connected or unconnected socket. This function also accommodates scatter/gather I/O and overlapped sockets.                                                                      |
| [**WSPSetSockOpt**](/windows/desktop/api/Ws2spi/)                   | Stores options associated with the specified socket.                                                                                                                                                    |
| [**WSPShutdown**](/windows/desktop/api/Ws2spi/)                       | Shuts down part of a full-duplex connection.                                                                                                                                                            |
| [**WSPSocket**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspsocket)                           | A socket creation function which takes a [**WSAPROTOCOL\_INFO**](/windows/desktop/api/Winsock2/) structure as input and allows overlapped sockets to be created.                                                |
| [**WSPStartup**](/windows/desktop/api/Ws2spi/nf-ws2spi-wspstartup)                         | Initializes the underlying Windows Sockets service provider.                                                                                                                                            |



 

 

 



