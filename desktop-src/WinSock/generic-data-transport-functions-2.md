---
Description: The data transport functions exposed by Ws2spi.h.
ms.assetid: 6900faa3-79bb-4ed8-b83e-148eb10425a0
title: Generic Data Transport Functions
ms.topic: article
ms.date: 05/31/2018
---

# Generic Data Transport Functions

This section lists the data transport functions exposed by Ws2spi.h.



| Function                                                   | Description                                                                                                                                                                                             |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WSPAccept**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspaccept)                           | An incoming connection is acknowledged and associated with an immediately created socket. The original socket is returned to the listening state. This function also allows for conditional acceptance. |
| [**WSPAsyncSelect**](https://msdn.microsoft.com/library/ms742267(v=VS.85).aspx)                 | Performs asynchronous version of [**WSPSelect**](https://msdn.microsoft.com/library/ms742289(v=VS.85).aspx).                                                                                                                                      |
| [**WSPBind**](https://msdn.microsoft.com/library/ms742268(v=VS.85).aspx)                               | Assigns a local name to an unnamed socket.                                                                                                                                                              |
| [**WSPCancelBlockingCall**](https://msdn.microsoft.com/library/ms742269(v=VS.85).aspx)   | Cancels an outstanding blocking Windows Sockets call.                                                                                                                                                   |
| [**WSPCleanup**](https://msdn.microsoft.com/library/ms742270(v=VS.85).aspx)                         | Signs off from the underlying Windows Sockets service provider.                                                                                                                                         |
| [**WSPCloseSocket**](https://msdn.microsoft.com/library/ms742271(v=VS.85).aspx)                 | Removes a socket from the per-process object reference table. Only blocks if SO\_LINGER is set with a nonzero time-out on a blocking socket.                                                            |
| [**WSPConnect**](https://msdn.microsoft.com/library/ms742272(v=VS.85).aspx)                         | Initiates a connection on the specified socket. This function also allows for exchange of connect data and QoS specification.                                                                           |
| [**WSPDuplicateSocket**](https://msdn.microsoft.com/library/ms742274(v=VS.85).aspx)         | Returns a [**WSAPROTOCOL\_INFO**](https://msdn.microsoft.com/library/ms741675(v=VS.85).aspx) structure that can be used to create a new socket descriptor for a shared socket.                                                             |
| [**WSPEnumNetworkEvents**](https://msdn.microsoft.com/library/ms742275(v=VS.85).aspx)     | Discovers occurrences of network events.                                                                                                                                                                |
| [**WSPEventSelect**](https://msdn.microsoft.com/library/ms742276(v=VS.85).aspx)                 | Associates network events with an event object.                                                                                                                                                         |
| [**WSPGetOverlappedResult**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspgetoverlappedresult) | Gets completion status of overlapped operation.                                                                                                                                                         |
| [**WSPGetPeerName**](https://msdn.microsoft.com/library/ms742278(v=VS.85).aspx)                 | Retrieves the name of the peer connected to the specified socket.                                                                                                                                       |
| [**WSPGetSockName**](https://msdn.microsoft.com/library/ms742280(v=VS.85).aspx)                 | Retrieves the local address to which the specified socket is bound.                                                                                                                                     |
| [**WSPGetSockOpt**](https://msdn.microsoft.com/library/ms742281(v=VS.85).aspx)                   | Retrieves options associated with the specified socket.                                                                                                                                                 |
| [**WSPGetQOSByName**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspgetqosbyname)               | Supplies QoS parameters based on a well-known service name.                                                                                                                                             |
| [**WSPIoctl**](https://msdn.microsoft.com/library/ms742282(v=VS.85).aspx)                             | Provides control for sockets.                                                                                                                                                                           |
| [**WSPJoinLeaf**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspjoinleaf)                       | Joins a leaf node into a multipoint session.                                                                                                                                                            |
| [**WSPListen**](https://msdn.microsoft.com/library/ms742284(v=VS.85).aspx)                           | Listens for incoming connections on a specified socket.                                                                                                                                                 |
| [**WSPRecv**](https://msdn.microsoft.com/library/ms742288(v=VS.85).aspx)                               | Receives data from a connected or unconnected socket. This function accommodates scatter/gather I/O, overlapped sockets, and provides the flags parameter as IN/OUT.                                    |
| [**WSPRecvDisconnect**](https://msdn.microsoft.com/library/ms742285(v=VS.85).aspx)           | Terminates reception on a socket, and retrieve the disconnect data if the socket is connection-oriented.                                                                                                |
| [**WSPRecvFrom**](https://msdn.microsoft.com/library/ms742287(v=VS.85).aspx)                       | Receives data from either a connected or unconnected socket. This function accommodates scatter/gather I/O, overlapped sockets and provides the flags parameter as IN/OUT.                              |
| [**WSPSelect**](https://msdn.microsoft.com/library/ms742289(v=VS.85).aspx)                           | Performs synchronous I/O multiplexing.                                                                                                                                                                  |
| [**WSPSend**](https://msdn.microsoft.com/library/ms742292(v=VS.85).aspx)                               | Sends data to a connected socket. This function also accommodates scatter/gather I/O and overlapped sockets.                                                                                            |
| [**WSPSendDisconnect**](https://msdn.microsoft.com/library/ms742290(v=VS.85).aspx)           | Initiates termination of a socket connection and optionally send disconnect data.                                                                                                                       |
| [**WSPSendTo**](https://msdn.microsoft.com/library/ms742291(v=VS.85).aspx)                           | Sends data to either a connected or unconnected socket. This function also accommodates scatter/gather I/O and overlapped sockets.                                                                      |
| [**WSPSetSockOpt**](https://msdn.microsoft.com/library/ms742293(v=VS.85).aspx)                   | Stores options associated with the specified socket.                                                                                                                                                    |
| [**WSPShutdown**](https://msdn.microsoft.com/library/ms742294(v=VS.85).aspx)                       | Shuts down part of a full-duplex connection.                                                                                                                                                            |
| [**WSPSocket**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspsocket)                           | A socket creation function which takes a [**WSAPROTOCOL\_INFO**](https://msdn.microsoft.com/library/ms741675(v=VS.85).aspx) structure as input and allows overlapped sockets to be created.                                                |
| [**WSPStartup**](/windows/desktop/api/Ws2spi/nf-ws2spi-wspstartup)                         | Initializes the underlying Windows Sockets service provider.                                                                                                                                            |



 

 

 



