---
description: An application uses the WSAEnumProtocols function to determine which transport protocols and protocol chains are present, and to obtain information about each as contained in the associated WSAPROTOCOL\_INFO structure.
ms.assetid: 4f38cb07-d824-4d43-abd8-89d58dc15810
title: Using Multiple Protocols
ms.topic: article
ms.date: 05/31/2018
---

# Using Multiple Protocols

An application uses the [**WSAEnumProtocols**](/windows/desktop/api/Winsock2/nf-winsock2-wsaenumprotocolsa) function to determine which transport protocols and protocol chains are present, and to obtain information about each as contained in the associated [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure.

In most instances, there is a single [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure for each protocol or protocol chain. However, some protocols exhibit multiple behaviors. For example, the SPX protocol is message oriented (that is, the sender's message boundaries are preserved by the network), but the receiving socket can ignore these message boundaries and treat them as a byte stream. Thus, two different **WSAPROTOCOL\_INFO** structure entries could exist for SPX—one for each behavior.

In Windows Sockets 2, several new address family, socket type, and protocol values appear. Windows Sockets 1.1 supported a single address family (AF\_INET) for IPv4 that consisted of a small number of well-known socket types and protocol identifiers. Windows Sockets 2 retains the existing address family, socket type, and protocol identifiers for compatibility reasons, but it also supports new address family values for new transport protocols with new media types.

New, unique identifiers are not necessarily well known, but this should not pose a problem. Applications that need to be protocol-independent are encouraged to select a protocol on the basis of its suitability rather than the values assigned to their *socket\_type* or *protocol* parameters. Protocol suitability is indicated by the communications attributes, such as message-versus-byte stream, and reliable-versus-unreliable, that are contained in the protocol [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure. Selecting protocols on the basis of suitability as opposed to well-known protocol names and socket types lets protocol-independent applications take advantage of new transport protocols and their associated media types, as they become available.

The server half of a client/server application benefits by establishing listening sockets on all suitable transport protocols. Then, the client can establish its connection using any suitable protocol. For example, this would let a client application be unmodified whether it was running on a desktop system connected through LAN or on a laptop using a wireless network.

 

 
