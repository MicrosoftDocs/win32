---
description: Socket sharing in Windows Sockets (Winsock).
ms.assetid: dad31820-6f60-4c3b-9cdf-e301a5ffce48
title: Shared Sockets in the SPI
ms.topic: article
ms.date: 05/31/2018
---

# Shared Sockets in the SPI

Socket sharing between processes in Windows Sockets is implemented as follows. A source process calls [**WSPDuplicateSocket**](/previous-versions/windows/hardware/network/ff566282(v=vs.85)) to obtain a special [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure. It uses some interprocess communications (IPC) mechanism to pass the contents of this structure to a target process. The target process then uses the **WSAPROTOCOL\_INFO** structure in a call to [**WSPSocket**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspsocket). The socket descriptor returned by this function will be an additional socket descriptor to an underlying socket which thus becomes shared.

It is the service provider's responsibility to perform whatever operations are needed in the source process context and to create a [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure that will be recognized when it subsequently appears as a parameter to [**WSPSocket**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspsocket) in the target processes' context. The **dwProviderReserved** member of the **WSAPROTOCOL\_INFO** structure is available for the service provider's use, and may be used to store any useful context information, including a duplicated handle.

This mechanism is designed to be appropriate for both single-threaded and preemptive multithreaded versions of Windows. Note however, that sockets may be shared among threads in a given process without using the [**WSPDuplicateSocket**](/previous-versions/windows/hardware/network/ff566282(v=vs.85)) function, since a socket descriptor is valid in all of a process' threads.

As is described in section [Descriptor Allocation](descriptor-allocation-2.md), when new socket descriptors are allocated IFS providers must call [**WPUModifyIFSHandle**](/windows/desktop/api/Ws2spi/nf-ws2spi-wpumodifyifshandle) and non-IFS providers must call [**WPUCreateSocketHandle**](/windows/desktop/api/Ws2spi/nf-ws2spi-wpucreatesockethandle).

One possible scenario for establishing and using a shared socket in a handoff mode is illustrated in the following table.

| Source process                                                                                                                          | IPC    | Destination process                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------------------------------------|
| 1) [**WSPSocket**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspsocket), [**WSPConnect**](/previous-versions/windows/hardware/network/ff566275(v=vs.85))                                                                 |        |                                                                               |
| 2) Requests target process identifier.                                                                                                  | ==> |                                                                               |
|                                                                                                                                         |        | 3) Receives process identifier request and responds.                          |
| 4) Receives process identifier.                                                                                                         | <== |                                                                               |
| 5) Calls [**WSPDuplicateSocket**](/previous-versions/windows/hardware/network/ff566282(v=vs.85)) to get a special [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure. |        |                                                                               |
| 6) Sends **WSAPROTOCOL\_INFO** structure to target.                                                                                     |        |                                                                               |
|                                                                                                                                         | ==> | 7) Receives [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure.        |
|                                                                                                                                         |        | 8) Calls [**WSPSocket**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspsocket) to create shared socket descriptor. |
|                                                                                                                                         |        | 9)Uses shared socket for data exchange.                                       |
| 10) [**WSPClosesocket**](/previous-versions/windows/hardware/network/ff566273(v=vs.85))                                                                                          | <== |                                                                               |



 

 

 
