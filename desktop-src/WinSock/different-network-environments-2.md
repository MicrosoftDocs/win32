---
description: Several network environments affect the networked behavior of an application.
ms.assetid: 4a530a17-5e61-4730-95f5-233261b4ceb0
title: Different Network Environments
ms.topic: article
ms.date: 05/31/2018
---

# Different Network Environments

Several network environments affect the networked behavior of an application. Properties that differentiate network environments include low versus high bandwidth, and low versus high RTT. Network environments affect transactional and streaming applications in different ways. Transactional applications are more sensitive to RTT; streaming applications are more sensitive to bandwidth-delay products.

![Diagram showing how different network environments affect the networked behavior of an application.](images/hperf-1.png)

Dial-up networks and some wireless networks have a variable RTT. Satellite networks generally have an asymmetric bandwidth between upstream and downstream. Wireless LAN and xDSL are good examples of networks with bandwidth-delay products similar to that of Fast Ethernet.

## Related topics

<dl> <dt>

[High-performance Windows Sockets Applications](high-performance-windows-sockets-applications-2.md)
</dt> <dt>

[Performance Dimensions](performance-dimensions-2.md)
</dt> </dl>

 

 



