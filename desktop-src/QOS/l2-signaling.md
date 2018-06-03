---
title: L2 Signaling
description: WAN technology manipulates Layer 1, Layer 2, and to a certain extent Layer 3 information, as it transmits data over the telecommunications network.
ms.assetid: 583e788b-aa21-4082-b668-b27c96e283b3
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# L2 Signaling

WAN technology manipulates Layer 1, Layer 2, and to a certain extent Layer 3 information, as it transmits data over the telecommunications network. Since quality of service is an end-to-end solution for data transferred across the network, there must be a means by which data passing through WAN interfaces can be associated with some sort of preferential or nonpreferential treatment. Such a requirement necessitates the mapping of RSVP or other QOS parameters to WAN technology QOS interfaces.

Layer 2, however, is where QOS technology interacts most with the WAN's underlying signaling, since it is in Layer 2 where existing WAN technologies implement their own native QOS components. L2 signaling, in Windows 2000 QOS terms, takes QOS information, such as parameters that are carried in RSVP messages to or through each network node between end devices, and maps that QOS information to native WAN technology QOS interfaces. For example, the classical IP over ATM (CLIP) module in Windows 2000 specifically maps Windows 2000 QOS settings to an appropriate ATM class of service.

 

 




