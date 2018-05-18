---
title: Local Policy Module API Reference
description: The Local Policy Module (LPM) API is a set of functions that the Policy Control Module (PCM) uses to interact with one or more LPMs.
ms.assetid: '55a7c8ba-2151-4a44-b77c-b101041fcd12'
keywords: ["Quality of Service QOS , reference, local policy module"]
---

# Local Policy Module API Reference

The Local Policy Module (LPM) API is a set of functions that the Policy Control Module (PCM) uses to interact with one or more LPMs. LPM API functions must be exported by LPMs to allow the PCM to invoke the LPM. This approach enables multiple LPMs to interact with the PCM, and subsequently, allows the PCM to return policy based–admission control decisions from one or more LPMs to the Admission Control Service (ACS). This concept is similar to a three-tiered approach, and enables multiple LPMs to easily coexist on a single system. Note, too, that LPMs may selectively accept or reject individual flows within a given policy based–decision request.

-   [Policy Elements](policy-elements.md)
-   [LPM Functions](lpm-functions.md)
-   [LPM Structures](lpm-structures.md)

 

 




