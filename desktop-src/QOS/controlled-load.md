---
title: CONTROLLED LOAD
description: When the CONTROLLED LOAD service type is specified, the RSVP SP is instructed to provide end-to-end service quality that approximates the network behavior achieved from BEST EFFORT service under unloaded conditions.
ms.assetid: '374cfd08-7f6d-449e-83e8-a32fb9f9d381'
keywords: ["CONTROLLED LOAD service type"]
---

# CONTROLLED LOAD

When the CONTROLLED LOAD service type is specified, the RSVP SP is instructed to provide end-to-end service quality that approximates the network behavior achieved from BEST EFFORT service under unloaded conditions.

The result of specifying the CONTROLLED LOAD service type is that network devices and elements in the path between the QOS-enabled connection (the end-to-end path) can be expected to:

-   Deliver a very high percentage of packets (packet loss approximates basic packet error rates for the transmission medium).
-   Transit delay by a very high percentage of transmitted packets will not greatly exceed the minimum transit delay experienced by any successfully delivered packet at the speed of light.

These defining characteristics of the CONTROLLED LOAD service type are based on definitions provided by RFC 2210.

> [!Note]  
> RSVP signaling is not supported on Windows XP or later versions of Windows.

 

 

 




