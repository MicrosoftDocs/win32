---
Description: The data transport functions exposed by Ws2spi.h.
ms.assetid: 6900faa3-79bb-4ed8-b83e-148eb10425a0
title: Generic Data Transport Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Generic Data Transport Functions

This section lists the data transport functions exposed by Ws2spi.h.



| Function                                                   | Description                                                                                                                                                                                             |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WSPAccept**](/windows/win32/Ws2spi/nc-ws2spi-lpwspaccept?branch=master)                           | An incoming connection is acknowledged and associated with an immediately created socket. The original socket is returned to the listening state. This function also allows for conditional acceptance. |
| [**WSPAsyncSelect**](/windows/win32/Ws2spi/?branch=master)                 | Performs asynchronous version of [**WSPSelect**](/windows/win32/Ws2spi/?branch=master).                                                                                                                                      |
| [**WSPBind**](/windows/win32/Ws2spi/?branch=master)                               | Assigns a local name to an unnamed socket.                                                                                                                                                              |
| [**WSPCancelBlockingCall**](/windows/win32/Ws2spi/?branch=master)   | Cancels an outstanding blocking Windows Sockets call.                                                                                                                                                   |
| [**WSPCleanup**](/windows/win32/Ws2spi/?branch=master)                         | Signs off from the underlying Windows Sockets service provider.                                                                                                                                         |
| [**WSPCloseSocket**](/windows/win32/Ws2spi/?branch=master)                 | Removes a socket from the per-process object reference table. Only blocks if SO\_LINGER is set with a nonzero time-out on a blocking socket.                                                            |
| [**WSPConnect**](/windows/win32/Ws2spi/?branch=master)                         | Initiates a connection on the specified socket. This function also allows for exchange of connect data and QoS specification.                                                                           |
| [**WSPDuplicateSocket**](/windows/win32/Ws2spi/?branch=master)         | Returns a [**WSAPROTOCOL\_INFO**](/windows/win32/Winsock2/?branch=master) structure that can be used to create a new socket descriptor for a shared socket.                                                             |
| [**WSPEnumNetworkEvents**](/windows/win32/Ws2spi/?branch=master)     | Discovers occurrences of network events.                                                                                                                                                                |
| [**WSPEventSelect**](/windows/win32/Ws2spi/?branch=master)                 | Associates network events with an event object.                                                                                                                                                         |
| [**WSPGetOverlappedResult**](/windows/win32/Ws2spi/nc-ws2spi-lpwspgetoverlappedresult?branch=master) | Gets completion status of overlapped operation.                                                                                                                                                         |
| [**WSPGetPeerName**](/windows/win32/Ws2spi/?branch=master)                 | Retrieves the name of the peer connected to the specified socket.                                                                                                                                       |
| [**WSPGetSockName**](/windows/win32/Ws2spi/?branch=master)                 | Retrieves the local address to which the specified socket is bound.                                                                                                                                     |
| [**WSPGetSockOpt**](/windows/win32/Ws2spi/?branch=master)                   | Retrieves options associated with the specified socket.                                                                                                                                                 |
| [**WSPGetQOSByName**](/windows/win32/Ws2spi/nc-ws2spi-lpwspgetqosbyname?branch=master)               | Supplies QoS parameters based on a well-known service name.                                                                                                                                             |
| [**WSPIoctl**](/windows/win32/Ws2spi/?branch=master)                             | Provides control for sockets.                                                                                                                                                                           |
| [**WSPJoinLeaf**](/windows/win32/Ws2spi/nc-ws2spi-lpwspjoinleaf?branch=master)                       | Joins a leaf node into a multipoint session.                                                                                                                                                            |
| [**WSPListen**](/windows/win32/Ws2spi/?branch=master)                           | Listens for incoming connections on a specified socket.                                                                                                                                                 |
| [**WSPRecv**](/windows/win32/Ws2spi/?branch=master)                               | Receives data from a connected or unconnected socket. This function accommodates scatter/gather I/O, overlapped sockets, and provides the flags parameter as IN/OUT.                                    |
| [**WSPRecvDisconnect**](/windows/win32/Ws2spi/?branch=master)           | Terminates reception on a socket, and retrieve the disconnect data if the socket is connection-oriented.                                                                                                |
| [**WSPRecvFrom**](/windows/win32/Ws2spi/?branch=master)                       | Receives data from either a connected or unconnected socket. This function accommodates scatter/gather I/O, overlapped sockets and provides the flags parameter as IN/OUT.                              |
| [**WSPSelect**](/windows/win32/Ws2spi/?branch=master)                           | Performs synchronous I/O multiplexing.                                                                                                                                                                  |
| [**WSPSend**](/windows/win32/Ws2spi/?branch=master)                               | Sends data to a connected socket. This function also accommodates scatter/gather I/O and overlapped sockets.                                                                                            |
| [**WSPSendDisconnect**](/windows/win32/Ws2spi/?branch=master)           | Initiates termination of a socket connection and optionally send disconnect data.                                                                                                                       |
| [**WSPSendTo**](/windows/win32/Ws2spi/?branch=master)                           | Sends data to either a connected or unconnected socket. This function also accommodates scatter/gather I/O and overlapped sockets.                                                                      |
| [**WSPSetSockOpt**](/windows/win32/Ws2spi/?branch=master)                   | Stores options associated with the specified socket.                                                                                                                                                    |
| [**WSPShutdown**](/windows/win32/Ws2spi/?branch=master)                       | Shuts down part of a full-duplex connection.                                                                                                                                                            |
| [**WSPSocket**](/windows/win32/Ws2spi/nc-ws2spi-lpwspsocket?branch=master)                           | A socket creation function which takes a [**WSAPROTOCOL\_INFO**](/windows/win32/Winsock2/?branch=master) structure as input and allows overlapped sockets to be created.                                                |
| [**WSPStartup**](/windows/win32/Ws2spi/nf-ws2spi-wspstartup?branch=master)                         | Initializes the underlying Windows Sockets service provider.                                                                                                                                            |



 

 

 



