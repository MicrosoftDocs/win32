---
description: Media packet size issues discussed in the topic, About Media Packet Size, affect the various PF\_IPX protocols differently.
ms.assetid: 7f0643b8-6bb2-4dbb-b306-d9b2e0d0e03c
title: How Packet Size Affects Protocols
ms.topic: article
ms.date: 05/31/2018
---

# How Packet Size Affects Protocols

Media packet size issues discussed in the topic, [About Media Packet Size](about-media-packet-size-2.md), affect the various PF\_IPX protocols differently. A common strategy for handling various router and media size constraints is to use the full media size when the remote station's network number matches the local station, and fall back to the minimum packet size otherwise.

## Parameters

<dl> <dt>

<span id="NSPROTO_IPX"></span><span id="nsproto_ipx"></span>NSPROTO\_IPX
</dt> <dd>

Provides a datagram service; each datagram must reside within the maximum packet size. Winsock sets the maximum datagram packet size to the local media packet size minus the IPX header. Keep in mind, however, that if the packet is routed, it may hit router restrictions en route. Make sure your application can fall back to 546-byte datagrams.

</dd> <dt>

<span id="NSPROTO_SPX"></span><span id="nsproto_spx"></span>NSPROTO\_SPX
</dt> <dd>

Provides stream and sequenced-packet services. Winsock IPX/SPX lets data streams and messages span multiple packets, so packet size does not limit the amount of data handled by [**send**](/windows/desktop/api/Winsock2/nf-winsock2-send) and [**recv**](/windows/desktop/api/winsock/nf-winsock-recv). However, the underlying media size must be set correctly or the first large packet will be undeliverable and the connection will reset. If the target station is on the local network, Winsock sets its packet size to the media packet size. Otherwise, it defaults to 512 bytes. This size can be changed immediately after [**connect**](/windows/desktop/api/Winsock2/nf-winsock2-connect) or [**accept**](/windows/desktop/api/Winsock2/nf-winsock2-accept) through [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt).

</dd> <dt>

<span id="NSPROTO_SPXII"></span><span id="nsproto_spxii"></span>NSPROTO\_SPXII
</dt> <dd>

SPXII features large Internet packet negotiation to maintain a best-fit size for packets and does not require programmer intervention. However, if the remote station does not support SPXII and negotiates down to standard SPX, the NSPROTO\_SPX rules are in effect.



| Protocol     | Media      | Type        | Data packet size |
|--------------|------------|-------------|------------------|
| NSPROTO\_IPX | Ethernet   | Ethernet II |                  |
|              |            | 802.3       |                  |
|              |            | 802.2       | 1466             |
|              |            | SNAP        |                  |
|              | Token Ring | 4 megabit   |                  |
|              |            | 16 megabit  |                  |
| NSPROTO\_SPX | Ethernet   | Ethernet II |                  |
|              |            | 802.3       |                  |
|              |            | 802.2       | 1454             |
|              |            | SNAP        |                  |
|              | Token Ring | 4 megabit   |                  |
|              |            | 16 megabit  |                  |



 

</dd> </dl>

 

 



