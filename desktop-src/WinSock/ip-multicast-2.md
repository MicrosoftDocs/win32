---
description: IP multicast falls into the category of nonrooted data plane and nonrooted control plane.
ms.assetid: 474a1c7f-0ece-4192-a2d9-6e2f3df2ac02
title: IP Multicast
ms.topic: article
ms.date: 05/31/2018
---

# IP Multicast

IP multicast falls into the category of nonrooted data plane and nonrooted control plane. All applications play a leaf role. Currently, most IP multicast implementations use a set of socket options proposed by Steve Deering to the Internet Engineering Task Force (IETF). Five operations are thus made available:

-   IP\_MULTICAST\_TTL—Sets time-to-live, controls scope of a multicast session.
-   IP\_MULTICAST\_IF—Determines interface to be used for multicasting.
-   IP\_ADD\_MEMBERSHI —Joins a specified multicast session.
-   IP\_DROP\_MEMBERSHIP—Drops out of a multicast session.
-   IP\_MULTICAST\_LOOP—Controls loopback of multicast traffic.

Setting the time-to-live for an IP-multicast socket maps directly to using the SIO\_MULTICAST\_SCOPE command code for [**WSAIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl).

The method for determining the IP interface to be used for multicasting is through a TCP/IP-specific socket option as described in the Windows Sockets 2 Protocol-Specific Annex. The remaining three operations are covered well with the Windows Sockets 2 semantics described here.

The application would open sockets with c\_leaf/d\_leaf flags in [**WSASocket**](/windows/desktop/api/Winsock2/nf-winsock2-wsasocketa). It would use [**WSAJoinLeaf**](/windows/desktop/api/Winsock2/nf-winsock2-wsajoinleaf) to add itself to a multicast group on the default interface designated for multicast operations. If the flag in **WSAJoinLeaf** indicates that this socket is only a sender, then the join operation is essentially a no-op and no IGMP messages need to be sent. Otherwise, an IGMP packet is sent out to the router to indicate interests in receiving packets sent to the specified multicast address. Since the application created special c\_leaf/d\_leaf sockets used only for performing multicast, the standard [**closesocket**](/windows/desktop/api/winsock/nf-winsock-closesocket) function would be used to drop out of the multicast session. The SIO\_MULTIPOINT\_LOOPBACK command code for [**WSAIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl) provides a generic control mechanism for determining whether data sent on a d\_leaf socket in a nonrooted multipoint scheme can also be received on the same socket.

> [!Note]  
> The Winsock version of the IP\_MULTICAST\_LOOP option is semantically different than the UNIX version of the IP\_MULTICAST\_LOOP option:

 

-   In Winsock, the IP\_MULTICAST\_LOOP option applies only to the receive path.
-   In the UNIX version, the IP\_MULTICAST\_LOOP option applies to the send path.

For example, applications ON and OFF (which are easier to track than X and Y) join the same group on the same interface; application ON sets the IP\_MULTICAST\_LOOP option on, application OFF sets the IP\_MULTICAST\_LOOP option off. If ON and OFF are Winsock applications, OFF can send to ON, but ON cannot sent to OFF. In contrast, if ON and OFF are UNIX applications, ON can send to OFF, but OFF cannot send to ON.

 

 



