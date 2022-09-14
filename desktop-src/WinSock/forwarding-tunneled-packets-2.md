---
description: There is a limitation in the code that receives encapsulated (tunneled) packets and demultiplexes them to a specific interface.
ms.assetid: 6148fca7-adf4-460d-afd6-79c43285af6c
title: IPv6 Forwarding Tunneled Packets
ms.topic: article
ms.date: 05/31/2018
---

# IPv6 Forwarding Tunneled Packets

There is a limitation in the code that receives encapsulated (tunneled) packets and demultiplexes them to a specific interface. If you want to forward tunneled packets received through a configured tunnel, then it is necessary to enable forwarding on any 6-over-4 interfaces as well as interface \#2. Just enabling forwarding on interface \#2 will not work. Typically when configuring a router, you would enable forwarding on all interfaces except loopback.

 

 



