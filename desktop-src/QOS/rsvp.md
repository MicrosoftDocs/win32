---
title: RSVP
description: Resource Reservation Protocol (RSVP) is an IETF-draft networking protocol dedicated to being the facilitator and carrier of standardized QOS information and parameters.
ms.assetid: 2bff34c7-2db9-4845-9db5-906c3ef3fa7f
keywords:
- Quality of Service QOS , described, RSVP
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RSVP

\[RSVP signaling is not supported except on Windows 2000. See [RSVP Operates Only on Windows 2000](rsvp-operates-only-on-windows-2000.md) for more information.\]

Resource Reservation Protocol (RSVP) is an IETF-draft networking protocol dedicated to being the facilitator and carrier of standardized QOS information and parameters. RSVP carries generic (industry-defined) QOS parameters from end nodes (inclusive) to each QOS-aware network device included in the path between RSVP session members. That is, RSVP is a means by which end nodes and network devices can communicate and negotiate QOS parameters and network usage admission.

RSVP is a multifaceted protocol — it is central to application-driven, network-driven, and policy-driven QOS activities — it is the carrier on which systems send QOS parameters and information to the network. RSVP has its own objects that can be filled or interrogated to specify or determine the requested QOS parameters that are either requested by the application, required of the network device, or applied for by the user.

Because RSVP has its own clearly-defined objects, the implementation of RSVP requires QOS parameters to be mapped into (or on the receiving end of RSVP messages, derived from) RSVP objects.

From an application-driven perspective, RSVP is the means by which an application's requests are transported through the network (a container, though one with specifically defined compartments). Calls to the [QOS API](qos-api.md) provide information to the [RSVP SP](rsvp-service-provider.md), which then maps such information into predefined RSVP objects for transmission across the network.

RSVP provides a mechanism for end systems to convey information to network devices about application data flow. Network devices can then take QOS- or policy-related action based on this information.

From a policy-driven perspective, RSVP provides the necessary user information within industry standard–RSVP objects (much like a set of containers, each of which is defined based on its standard formats), that facilitate the exchange of user identity and admission requests.

Although RSVP can be considered responsible for the bulk of QOS interaction among end nodes, it is possible to achieve QOS without RSVP signaling, such as by using traffic control facilities.

 

 




