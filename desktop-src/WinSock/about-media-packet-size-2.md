---
description: Media packet size affects the ability of IPX protocols to transfer data across networks and can prove challenging to deal with in a transport-independent manner.
ms.assetid: cce31a6a-c187-4ec4-976c-5f9984211ccb
title: About Media Packet Size
ms.topic: article
ms.date: 05/31/2018
---

# About Media Packet Size

Media packet size affects the ability of IPX protocols to transfer data across networks and can prove challenging to deal with in a transport-independent manner. IPX does not segment packets, nor does it report when packets are dropped due to size violations. This means that some entity on the end station must maintain knowledge of the maximum packet size to be used on any given internetwork path. Traditionally, IPX datagrams and SPX connection-oriented services have left this burden to the application, while SPXII has used large Internet packet negotiation to handle it transparently.

Winsock attempts to set rational packet size limits for its various IPX protocols as described in the next section. These limits can be viewed and modified by applications through get/set socket options. When determining maximum packet size, the three areas of concern are:

-   \# Media packet size
-   \# Routable packet size
-   \# End-station packet size

*Media packet size* reflects the maximum packet size acceptable on any media the packet traverses to its destination. Packet size varies among differing media such as Ethernet and token ring. The amount of data space within a packet can also vary within a given media, depending on the packet header arrangement. For instance, the effective data size of an Ethernet packet varies depending on whether it is of the type Ethernet II, Ethernet 802.2, or Ethernet SNAP.

*Routable packet size* reflects the maximum packet size an intermediate router is willing to forward. Most IPX routers are built to route any size datagram as long as it remains within the media size of the sending and receiving network. However, older routers may limit maximum packet size to 576 bytes, including protocol headers.

*End-station packet size* reflects the size of the listen buffers that end stations have posted to receive incoming packets. Even when the media and router limits allow a packet through, it may be discarded by the end station if the receiving application has posted a smaller buffer. Many traditional IPX/SPX applications limit receive buffer size such that the data portion must be no larger than 512 or 1024 bytes.

 

 



