---
title: Traffic Control API
description: Quality of Service (QOS) traffic control API (TC API).
ms.assetid: '933abfd1-bbde-422f-8c4a-a7e14e034c51'
keywords: ["Quality of Service QOS , described, traffic control API"]
---

# Traffic Control API

The traffic control application programming interface (TC API) is a programmatic interface to the components that regulate network traffic on local hosts; both from an internal perspective (within the kernel itself), and from a network perspective (prioritization and queuing of packets based on transmission priority).

Traffic control is implicitly invoked through calls made to the QOS API and subsequently serviced by the RSVP service provider (RSVP SP). However, applications that require further or specific control over traffic control can use the TC API. The RSVP Service also uses TC API calls.

Note that the use of functions in the TC API requires administrative privilege.

> [!Note]  
> RSVP signaling is not supported on Windows XP or later versions of Windows.

 

 

 




