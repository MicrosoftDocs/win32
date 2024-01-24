---
description: In the following, a multipoint socket is frequently characterized by describing its role in one of the two planes (control or data).
ms.assetid: 35e4a8c9-d943-44b8-be61-605b60a6cf5d
title: SPI Semantics for Joining Multipoint Leaves
ms.topic: article
ms.date: 05/31/2018
---

# SPI Semantics for Joining Multipoint Leaves

In the following, a multipoint socket is frequently characterized by describing its role in one of the two planes (control or data). It should be understood that this same socket has a role in the other plane, but this is not mentioned in order to keep the references short. For example a reference to a c\_root socket could refer to either a c\_root/d\_root or a c\_root/d\_leaf socket.

In rooted control plane schemes, new leaf nodes are added to a multipoint session in one or both of two different ways. In the first method, the root uses [**WSPJoinLeaf**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspjoinleaf) to initiate a connection with a leaf node and invite it to become a participant. On the leaf node, the peer application must have created a c\_leaf socket and used [**WSPListen**](/previous-versions/windows/hardware/network/ff566297(v=vs.85)) to set it into listen mode. The leaf node will receive an FD\_ACCEPT indication when invited to join the session, and signals its willingness to join by calling [**WSPAccept**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspaccept). The root application will receive an FD\_CONNECT indication when the join operation has been completed.

In the second method, the roles are essentially reversed. The root client creates a c\_root socket and sets it into listen mode. A leaf node wishing to join the session creates a c\_leaf socket and uses [**WSPJoinLeaf**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspjoinleaf) to initiate the connection and request admittance. The root client receives FD\_ACCEPT when an incoming admittance request arrives, and admits the leaf node by calling [**WSPAccept**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspaccept). The leaf node receives FD\_CONNECT when it has been admitted.

In a nonrooted control plane, where all nodes are c\_leafs, the [**WSPJoinLeaf**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspjoinleaf) function is used to initiate the inclusion of a node into an existing multipoint session. An FD\_CONNECT indication is provided when the join has been completed and the returned socket descriptor is usable in the multipoint session. In the case of IP multicast, this would correspond to the IP\_ADD\_MEMBERSHIP socket option.

There are, therefore, three instances where a client would use [**WSPJoinLeaf**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspjoinleaf):

-   Acting as a multipoint root and inviting a new leaf to join the session.
-   Acting as a leaf making an admittance request to a rooted multipoint session.
-   Acting as a leaf seeking admittance to a nonrooted multipoint session (for example, IP multicast.)

 

 
