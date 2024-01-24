---
description: In the following, a multipoint socket is frequently described by defining its role in one of the two planes (control or data).
ms.assetid: 34f639e2-9363-4f3f-a8de-b7c5d12618c9
title: Semantics for Joining Multipoint Leaves
ms.topic: article
ms.date: 05/31/2018
---

# Semantics for Joining Multipoint Leaves

In the following, a multipoint socket is frequently described by defining its role in one of the two planes (control or data). It should be understood that this same socket has a role in the other plane, but this is not mentioned in order to keep the references short. For example when a reference is made to a "c\_root socket", this could be either a c\_root/d\_root or a c\_root/d\_leaf socket.

In rooted control plane schemes, new leaf nodes are added to a multipoint session in one or both of two different ways. In the first method, the root uses [**WSAJoinLeaf**](/windows/desktop/api/Winsock2/nf-winsock2-wsajoinleaf) to initiate a connection with a leaf node and to invite it to become a participant. On the leaf node, the peer application must have created a c\_leaf socket and used [**listen**](/windows/desktop/api/Winsock2/nf-winsock2-listen) to set it into listen mode. The leaf node receives an FD\_ACCEPT indication when invited to join the session, and signals its willingness to join by calling [**WSAAccept**](/windows/desktop/api/Winsock2/nf-winsock2-wsaaccept). The root application then receives an FD\_CONNECT indication when the **join** operation has been completed.

In the second method, the roles are essentially reversed. The root application creates a c\_root socket and sets it into listen mode. A leaf node wishing to join the session creates a c\_leaf socket and uses [**WSAJoinLeaf**](/windows/desktop/api/Winsock2/nf-winsock2-wsajoinleaf) to initiate the connection and request admittance. The root application receives FD\_ACCEPT when an incoming admittance request arrives, and admits the leaf node by calling [**WSAAccept**](/windows/desktop/api/Winsock2/nf-winsock2-wsaaccept). The leaf node receives FD\_CONNECT when it has been admitted.

In a nonrooted control plane, where all nodes are c\_leaf's, the [**WSAJoinLeaf**](/windows/desktop/api/Winsock2/nf-winsock2-wsajoinleaf) is used to initiate the inclusion of a node into an existing multipoint session. An FD\_CONNECT indication is provided when the join has been completed and the returned socket descriptor is usable in the multipoint session. In the case of IP multicast, this would correspond to the IP\_ADD\_MEMBERSHIP socket option.

(Readers familiar with IP multicast's use of the connectionless UDP protocol may be concerned by the connection-oriented semantics presented here. In particular the notion of using [**WSAJoinLeaf**](/windows/desktop/api/Winsock2/nf-winsock2-wsajoinleaf) on a UDP socket and waiting for an FD\_CONNECT indication may be troubling. There is, however, ample precedent for applying connection-oriented semantics to connectionless protocols. It is allowed and sometimes useful, for example, to invoke the standard [**connect**](/windows/desktop/api/Winsock2/nf-winsock2-connect) function on a UDP socket. The general result of applying connection-oriented semantics to connectionless sockets is a restriction in how such sockets may be used, and this is the case here, as well. A UDP socket used in **WSAJoinLeaf** will have certain restrictions, and waiting for an FD\_CONNECT indication (which in this case simply indicates that the corresponding IGMP message has been sent) is one such limitation.)

There are therefore, three instances where an application would use [**WSAJoinLeaf**](/windows/desktop/api/Winsock2/nf-winsock2-wsajoinleaf) acting as a:

-   Multipoint root and inviting a new leaf to join the session
-   Leaf making an admittance request to a rooted multipoint session
-   Leaf seeking admittance to a nonrooted multipoint session (for example, IP multicast)

 

 



