---
title: Generic Packet Classifier
description: Packet classification provides a means by which packets internal to a specific network node can be classified, and consequently prioritized, within and by both user and kernel-mode network components.
ms.assetid: 2cc3109d-7637-4713-97a4-6e092f0c2b9f
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Generic Packet Classifier

Packet classification provides a means by which packets internal to a specific network node can be classified, and consequently prioritized, within and by both user and kernel-mode network components. These classification and prioritization uses include activities such as CPU processing attention or transmission onto the network. The Generic Packet Classifier (GPC) is utilized through the Generic Packet Classifier Interface, or GPC Interface, which facilitates an information store that can be used or associated with specified (defined) subsets of packets.

The importance of GPC hinges on its ability to provide lookup tables and classification services within the network stack, and is thus the first step in an overall and ubiquitous prioritization scheme for network traffic.

 

 




