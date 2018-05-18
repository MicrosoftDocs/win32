---
title: Packet Scheduler
description: Packet scheduling is the means by which data (packet) transmission-governing \ 8212; a key function of quality of service \ 8212; is achieved.
ms.assetid: '8b005aff-fba2-4833-94be-df288978ea77'
---

# Packet Scheduler

Packet scheduling is the means by which data (packet) transmission-governing — a key function of quality of service — is achieved. The packet scheduler is the traffic control module that regulates how much data an application (or flow) is allowed, essentially enforcing QOS parameters that are set for a particular flow. The packet scheduler incorporates three mechanisms in its scheduling of packets:

-   A conformer
-   The packet shaper
-   A sequencer

The conformer and sequencer are discussed in more detail in the traffic control documentation. Since the packet scheduler's role is essential to overall traffic control understanding, it is defined here.

The packet scheduler considers the classification provided by the Generic Packet Classifier (GPC), and provides preferential treatment to higher-priority traffic. Consequently, the packet scheduler is the first step (in a sequential view) to ensuring that the prioritized network transmission of packets begins with data that has been deemed most important.

Part of the packet scheduler's responsibility is shaping the way packets are transmitted from a network device, a capability often referred to as packet shaping. Though often referenced by its own name, the packet shaper is simply a part of overall packet scheduler functionality.

The packet shaper mitigates the burst nature of computer network transmissions by smoothing transmission peaks over a given period of time, thereby smoothing out network usage to affect a more steady use of the network. The significance of the packet shaper becomes apparent: one factor that contributes to network congestion is the burst nature of computer data transmissions, a side-effect of the inherent "send it all out right now" nature of IP transmission. Packet shaping can help alleviate at least some of the effects of such activity by spacing out QOS-enabled packet transmissions.

 

 




