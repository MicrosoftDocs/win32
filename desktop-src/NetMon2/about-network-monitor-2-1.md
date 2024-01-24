---
description: Network Monitor is a component of Microsoft Systems Management Server (SMS) used to detect and troubleshoot problems on LANs, WANs, and serial links running Microsoft Remote Access Server (RAS).
ms.assetid: bd273439-daa2-4263-8f12-28ec988beea0
title: About Network Monitor 2.1
ms.topic: article
ms.date: 05/31/2018
---

# About Network Monitor 2.1

Network Monitor is a component of Microsoft Systems Management Server (SMS) used to detect and troubleshoot problems on LANs, WANs, and serial links running Microsoft Remote Access Server (RAS). Network Monitor provides post-capture network data analysis.

In post-capture analysis, network traffic is saved in a proprietary capture file, so that the captured data can be analyzed later. In this case, analysis can be in the form of protocol [*parsers*](p.md) picking out specific network frame types and displaying the frame data in the Network Monitor UI; or analysis can be in the form of [*experts*](e.md) examining the network data and displaying a report (experts may also manipulate the network data).

Network Monitor provides the following types of functionality:

-   Captures network data in real-time or delayed mode.
-   Provides filtering capabilities when capturing data.
-   Uses experts and parsers for detailed post-capture analysis.

For more information about Network Monitor features, see:

-   [Expert and Parser Architecture](expert-and-parser-architecture.md)
-   [Experts](experts.md)
-   [Parsers](parsers.md)
-   [Network Packet Providers](network-packet-providers.md)
-   [Network Monitor BLOBs](network-monitor-blobs.md)
-   [Event Reference Page](event-reference-page.md)
-   [Capture Filters](capture-filters.md)

**Windows Vista:** Network Monitor 2.1 and earlier are not supported on this platform.

 

 



