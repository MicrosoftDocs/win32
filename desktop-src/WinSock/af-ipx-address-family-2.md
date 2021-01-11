---
description: The IPX address family defines the addressing structure for protocols that use standard IPX socket addressing. For these transports, an endpoint address consists of a network number, node address, and socket number.
ms.assetid: cf749ae7-ab17-4c60-b00c-b34e092c6431
title: AF_IPX Address Family
ms.topic: article
ms.date: 05/31/2018
---

# AF\_IPX Address Family

The IPX address family defines the addressing structure for protocols that use standard IPX socket addressing. For these transports, an endpoint address consists of a network number, node address, and socket number.

The network number is an administrative domain and typically names a single Ethernet or token ring segment. The node number is a station's physical address. The combination of net and node form a unique station address that is presumed to be unique in the world. Net and node numbers are represented in ASCII text in either block or dashed notation as: '0101a040,00001b498765' or '01-01-a0-40,00-00-1b-49-87-65'. Leading zeros need not be present.

The IPX socket number is a network/transport service number much like a TCP port number and is not to be confused with the Winsock socket descriptor. IPX socket numbers are global to the end station and cannot be bound to specific net/node addresses. For instance, if the end station has two network interface cards, a bound socket can send and receive on both cards. In particular, datagram sockets would receive broadcast datagrams on both cards.

> [!Caution]  
> SOCKADDR\_IPX is 14 bytes long and is shorter than the 16-byte [**sockaddr**](sockaddr-2.md) reference structure. IPX/SPX implementations may accept the 16-byte length as well as the true length. If you use SOCKADDR\_IPX and a hard-coded length of 16 bytes, the implementation may assume that it has access to the 2 bytes following your structure.

 



| Field           | Value                                    |
|-----------------|------------------------------------------|
| **sa\_family**  | Address family AF\_IPX in host order.    |
| **Sa\_netnum**  | IPX network identifier in network order. |
| **Sa\_nodenum** | Station node address, flushed right.     |
| **Sa\_socket**  | IPX socket number in network order.      |



 

 

 



