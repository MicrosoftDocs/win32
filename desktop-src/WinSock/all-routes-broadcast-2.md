---
description: A general broadcast through the Internet is achieved by setting the sa\_netnum and sa\_nodenum fields to binary ones (1).
ms.assetid: a56f3059-d6e5-42eb-8ba2-16071fffafa5
title: All Routes Broadcast
ms.topic: article
ms.date: 05/31/2018
---

# All Routes Broadcast

A general broadcast through the Internet is achieved by setting the **sa\_netnum** and **sa\_nodenum** fields to binary ones (1). The service provider translates this request to a type-20 packet, which IPX routers recognize and forward. The packet visits all subnets and may be duplicated several times. Receivers must handle several duplicate copies of the datagram.

Use of this broadcast type is unpopular among network administrators, so its use should be extremely limited. Many routers disable this type of broadcast, leaving parts of the subnet invisible to the packet.

 

 



