---
description: There are several socket attributes which can be indicated through the flags parameter in WSPSocket.
ms.assetid: 5fd4321b-a5cc-4921-bec5-bdf625261ea2
title: Socket Attribute Flags and Modes
ms.topic: article
ms.date: 05/31/2018
---

# Socket Attribute Flags and Modes

There are several socket attributes which can be indicated through the *flags* parameter in [**WSPSocket**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspsocket). The WSA\_FLAG\_OVERLAPPED flag indicates that a socket will be used for overlapped I/O operations. Support of this attribute is mandatory for all service providers. See [Overlapped I/O](overlapped-i-o-2.md) for more information. Note that creating a socket with the overlapped attribute has no impact on whether a socket is currently in blocking or nonblocking mode. Sockets created with the overlapped attribute may be used to perform overlapped I/O, and doing so does not change the blocking mode of a socket. Since overlapped I/O operations do not block, the blocking mode of a socket is irrelevant for these operations.

Four additional attribute flags are used when creating sockets that are to be used for multipoint and/or multicast operations, and support for these attributes is optional. Providers that support multipoint attributes indicate this through the XP1\_SUPPPORT\_MULTIPOINT bit in their respective [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structures. See [**WSPSocket**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspsocket) and [Protocol-Independent Multicast and Multipoint in the API](protocol-independent-multicast-and-multipoint-in-the-spi-2.md) for the definition and usage of each of these flags. Only sockets that are created with multipoint-related attributes can be used in the [**WSPJoinLeaf**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspjoinleaf) function for creating multipoint sessions.

A socket is in one of two modes, blocking and nonblocking, at any time. Sockets are created in the blocking mode by default, and can be changed to nonblocking mode by calling [**WSPAsyncSelect**](/previous-versions/windows/desktop/legacy/ms742267(v=vs.85)), [**WSPEventSelect**](/previous-versions/windows/hardware/network/ff566287(v=vs.85)), or [**WSPIoctl**](/previous-versions/windows/hardware/network/ff566296(v=vs.85)). A socket can be switched back to blocking mode by using **WSPIoctl** if no **WSPAsyncSelect** or **WSPEventSelect** is active. The mode for a socket only affects those functions which may block, and does not affect overlapped I/O operations. See [Blocking Operations](blocking-operations-2.md) for more information.

 

 
