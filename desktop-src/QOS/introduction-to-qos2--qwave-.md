---
title: Introduction to QoS2 and qWAVE
description: QoS2 is a suite of Quality of Service APIs introduced with Windows Vista and Windows Server 2008. It provides differentiated services for \ 0034;on-link \ 0034; (single IP subnet) and \ 0034;off-link \ 0034; (multiple IP subnet) scenarios on a per-socket basis.
ms.assetid: '5dea8889-2595-4f74-8ad6-db71896eb27c'
---

# Introduction to QoS2 and qWAVE

QoS2 is a suite of Quality of Service APIs introduced with Windows Vista and Windows Server 2008. It provides differentiated services for "on-link" (single IP subnet) and "off-link" (multiple IP subnet) scenarios on a per-socket basis.

Specifically, off-link scenarios allow a QoS2 caller to perform the following actions, without any form of admission control:

-   DSCP marking (packet prioritization)
-   Packet send rate limitation (throttling)

On-link scenarios target home networks which have a single subnet defined for them. The QoS subsystem that enables on-link scenarios is called Quality Windows Audio/Video Experience (qWAVE). qWAVE provides several new technologies focused on streaming multimedia and real-time content over works variable bandwidth home networks (such as Wi-Fi enabled local networks). These technologies include:

-   Auto-discovery of end-to-end discovery of QoS capability
-   End-to-end bandwidth estimation of:
    -   Maximum link capacity (bottleneck bandwidth)
    -   Real-time bandwidth availability metrics
-   Intelligent packet prioritization
-   Congestion and congestion relief notifications
-   Send rate limiting (throttling)
-   Distributed admission control

For the specific QoS2 and qWAVE APIs, please refer to the [qWAVE API Reference](qwave-api-reference.md).

 

 




