---
description: Windows Sockets (Winsock) and protocol-independent multipoint and multicast capabilities of transports.
ms.assetid: 861f457c-fe7e-4128-a3f3-786424a96ea5
title: Protocol-Independent Multicast and Multipoint in the SPI
ms.topic: article
ms.date: 05/31/2018
---

# Protocol-Independent Multicast and Multipoint in the SPI

Just as Windows Sockets 2 allows the basic data transport capabilities of numerous transport protocols to be accessed in a generic manner, it also provides a generic way to use multipoint and multicast capabilities of transports that implement these features. To simplify, the term *multipoint* is used hereafter to refer to both multicast and multipoint communications.

Current multipoint implementations (for example, IP multicast, ST-II, T.120, ATM UNI) vary widely with respect to how nodes join a multipoint session, whether a particular node is designated as a central or root node, and whether data is exchanged between all nodes or only between a root node and various leaf nodes. The Windows Sockets 2 [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure is used to declare the multipoint attributes of a protocol. By examining these attributes the programmer will know what conventions to follow in using the applicable Winsock functions to set up, use, and tear down multipoint sessions.

The features of Windows Sockets 2 that support multicast can be summarized as follows:

-   Three attribute bits in the [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure.
-   Four flags defined for the *dwFlags* parameter of [**WSPSocket**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspsocket)
-   One function, [**WSPJoinLeaf**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspjoinleaf), for adding leaf nodes into a multipoint session.
-   Two [**WSPIoctl**](/previous-versions/windows/hardware/network/ff566296(v=vs.85)) command codes for controlling multipoint loopback and establishing the scope for multicast transmissions. (The latter corresponds to the IP multicast time-to-live or TTL parameter.)

> [!Note]  
> The inclusion of these multipoint features in Windows Sockets 2 does not preclude a service provider from also supporting an existing protocol-dependent interface, such as the Deering socket options for IP multicast.

 

 

 
