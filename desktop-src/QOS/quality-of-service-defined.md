---
title: Quality of Service Defined
description: Quality of Service is an industry-wide movement that achieves more efficient use out of network resources by differentiating between subsets of data.
ms.assetid: 4d0c6549-c175-4114-880b-9e90dfbff5ab
keywords:
- Quality of Service QOS , described, defined
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Quality of Service Defined

Quality of Service is an industry-wide movement that achieves more efficient use out of network resources by differentiating between subsets of data. The IETF (Internet Engineering Task Force) has played a central role in ensuring that QOS standards enable all affected network devices to participate in the end-to-end QOS-enabled connection.

Quality of Service provides applications (or network administrators) with a means by which network resources — such as available bandwidth and latency — can be predicted and managed on both local computers and devices throughout the network.

With such an all-network encompassing definition, QOS functionality requires cooperation among end nodes, switches, routers, and wide area network (WAN) links through which data must pass. Without some level of cooperation among those network devices, the quality of data transmission services can break down. In other words, if each such network device is left to make its own decisions about transmitting data, it would likely treat all data equally, and thus provide service on a first come–first served basis. Although this may be satisfactory in network devices or transmission media that are not heavily loaded, when congestion occurs, such service can delay all data. With this information, we can extend the definition of quality of service — it allows preferential treatment for certain subsets of data as they traverse any QOS-enabled part of (or devices in) the network.

Microsoft implements quality of service by including a number of components that can cooperate with (or invoke) one another. These components are found in DLLs, protocols, services, and individual network device functionality.

 

 




