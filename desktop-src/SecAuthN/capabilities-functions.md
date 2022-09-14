---
description: The Network Provider API specifies a single capabilities function.
ms.assetid: fc74a043-da13-485f-9f54-a43064add927
title: Capabilities Functions
ms.topic: article
ms.date: 05/31/2018
---

# Capabilities Functions

The Network Provider API specifies a single capabilities function. When the operating system requests information about a network provider's capabilities, the [*Multiple Provider Router*](/windows/desktop/SecGloss/m-gly) (MPR) calls the [**NPGetCaps**](/windows/desktop/api/Npapi/nf-npapi-npgetcaps) function of each network provider whose network is active.

The [**NPGetCaps**](/windows/desktop/api/Npapi/nf-npapi-npgetcaps) function returns a bitmask indicating which functions of the Network Provider API the network provider supports. The **NPGetCaps** function is the only function that a network provider must implement. The operating system calls this function to determine which other functions of the Network Provider API the provider supports.

 

 
