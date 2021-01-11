---
description: The data transport functions exposed by Ws2spi.h.
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
| [**WSPAsyncSelect**](/previous-versions/windows/desktop/legacy/ms742267(v=vs.85))                 | Performs asynchronous version of [**WSPSelect**](/previous-versions/windows/desktop/legacy/ms742289(v=vs.85)).                                                                                                                                      |
| [**WSPBind**](/previous-versions/windows/hardware/network/ff566268(v=vs.85))                               | Assigns a local name to an unnamed socket.                                                                                                                                                              |
| [**WSPCancelBlockingCall**](/previous-versions/windows/desktop/legacy/ms742269(v=vs.85))   | Cancels an outstanding blocking Windows Sockets call.                                                                                                                                                   |
| [**WSPCleanup**](/previous-versions/windows/hardware/network/ff566270(v=vs.85))                         | Signs off from the underlying Windows Sockets service provider.                                                                                                                                         |
| [**WSPCloseSocket**](/previous-versions/windows/hardware/network/ff566273(v=vs.85))                 | Removes a socket from the per-process object reference table. Only blocks if SO\_LINGER is set with a nonzero time-out on a blocking socket.                                                            |
| [**WSPConnect**](/previous-versions/windows/hardware/network/ff566275(v=vs.85))                         | Initiates a connection on the specified socket. This function also allows for exchange of connect data and QoS specification.                                                                           |
| [**WSPDuplicateSocket**](/previous-versions/windows/hardware/network/ff566282(v=vs.85))         | Returns a [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure that can be used to create a new socket descriptor for a shared socket.                                                             |
| [**WSPEnumNetworkEvents**](/previous-versions/windows/hardware/network/ff566284(v=vs.85))     | Discovers occurrences of network events.                                                                                                                                                                |
| [**WSPEventSelect**](/previous-versions/windows/hardware/network/ff566287(v=vs.85))                 | Associates network events with an event object.                                                                                                                                                         |
| [**WSPGetOverlappedResult**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspgetoverlappedresult) | Gets completion status of overlapped operation.                                                                                                                                                         |
| [**WSPGetPeerName**](/previous-versions/windows/desktop/legacy/ms742278(v=vs.85))                 | Retrieves the name of the peer connected to the specified socket.                                                                                                                                       |
| [**WSPGetSockName**](/previous-versions/windows/desktop/legacy/ms742280(v=vs.85))                 | Retrieves the local address to which the specified socket is bound.                                                                                                                                     |
| [**WSPGetSockOpt**](/previous-versions/windows/hardware/network/ff566292(v=vs.85))                   | Retrieves options associated with the specified socket.                                                                                                                                                 |
| [**WSPGetQOSByName**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspgetqosbyname)               | Supplies QoS parameters based on a well-known service name.                                                                                                                                             |
| [**WSPIoctl**](/previous-versions/windows/hardware/network/ff566296(v=vs.85))                             | Provides control for sockets.                                                                                                                                                                           |
| [**WSPJoinLeaf**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspjoinleaf)                       | Joins a leaf node into a multipoint session.                                                                                                                                                            |
| [**WSPListen**](/previous-versions/windows/hardware/network/ff566297(v=vs.85))                           | Listens for incoming connections on a specified socket.                                                                                                                                                 |
| [**WSPRecv**](/previous-versions/windows/hardware/network/ff566309(v=vs.85))                               | Receives data from a connected or unconnected socket. This function accommodates scatter/gather I/O, overlapped sockets, and provides the flags parameter as IN/OUT.                                    |
| [**WSPRecvDisconnect**](/previous-versions/windows/desktop/legacy/ms742285(v=vs.85))           | Terminates reception on a socket, and retrieve the disconnect data if the socket is connection-oriented.                                                                                                |
| [**WSPRecvFrom**](/previous-versions/windows/desktop/legacy/ms742287(v=vs.85))                       | Receives data from either a connected or unconnected socket. This function accommodates scatter/gather I/O, overlapped sockets and provides the flags parameter as IN/OUT.                              |
| [**WSPSelect**](/previous-versions/windows/desktop/legacy/ms742289(v=vs.85))                           | Performs synchronous I/O multiplexing.                                                                                                                                                                  |
| [**WSPSend**](/previous-versions/windows/hardware/network/ff566316(v=vs.85))                               | Sends data to a connected socket. This function also accommodates scatter/gather I/O and overlapped sockets.                                                                                            |
| [**WSPSendDisconnect**](/previous-versions/windows/desktop/legacy/ms742290(v=vs.85))           | Initiates termination of a socket connection and optionally send disconnect data.                                                                                                                       |
| [**WSPSendTo**](/previous-versions/windows/desktop/legacy/ms742291(v=vs.85))                           | Sends data to either a connected or unconnected socket. This function also accommodates scatter/gather I/O and overlapped sockets.                                                                      |
| [**WSPSetSockOpt**](/previous-versions/windows/hardware/network/ff566318(v=vs.85))                   | Stores options associated with the specified socket.                                                                                                                                                    |
| [**WSPShutdown**](/previous-versions/windows/desktop/legacy/ms742294(v=vs.85))                       | Shuts down part of a full-duplex connection.                                                                                                                                                            |
| [**WSPSocket**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspsocket)                           | A socket creation function which takes a [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure as input and allows overlapped sockets to be created.                                                |
| [**WSPStartup**](/windows/desktop/api/Ws2spi/nf-ws2spi-wspstartup)                         | Initializes the underlying Windows Sockets service provider.                                                                                                                                            |



 

 

 
