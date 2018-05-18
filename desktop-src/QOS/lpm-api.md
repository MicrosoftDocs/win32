---
title: LPM API
description: The local policy module application programming interface (LPM API) is the programmatic interface by which LPMs communicate and interact with the Admission Control Service (ACS).
ms.assetid: 'bc44b96b-a18d-41e1-ad50-8119a6b215ee'
keywords: ["Quality of Service QOS , described, local policy module API"]
---

# LPM API

The local policy module application programming interface (LPM API) is the programmatic interface by which LPMs communicate and interact with the Admission Control Service (ACS). The LPM API also specifies how LPMs are registered and initialized within the constructs of the ACS.

Such interaction is actually regulated by an abstraction module called the Policy Control Module (PCM). Because it is possible to have multiple LPMs, the PCM manages the policy-based decision information that LPM modules return. Note that LPMs may selectively accept or reject flows. For example, an LPM can receive an RSVP-based request from the PCM that has multiple flow requests; the LPM can then selectively accept or reject individual flows within that request, and return the results to the PCM. Note, too, that the PCM can manage information returned from multiple LPMs (if multiple LPMs are installed on the system), perform logical aggregation of their results, and then return aggregated information to the ACS.

The LPM API consists of a handful of functions used to allow its interaction with the ACS. The interaction of an LPM with its corresponding policy store or server is excluded from this interface; such interfacing would be proprietary to the LPM and the policy store or server.

 

 




