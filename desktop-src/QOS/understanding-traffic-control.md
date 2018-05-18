---
title: Understanding Traffic Control
description: Traffic control, commonly referred to as TC, regulates traffic on local hosts.
ms.assetid: '566a5524-5af7-424a-86ab-aa3a55178c69'
keywords: ["Quality of Service QOS , described, traffic control"]
---

# Understanding Traffic Control

Traffic control, commonly referred to as TC, regulates traffic on local hosts. Traffic control is responsible for controlling the flow of traffic based on a given flow's priority, both from an internal perspective (within the kernel itself), and from a network perspective (prioritization and queuing of packets based on transmission priority).

> [!Note]  
> RSVP signaling is not supported on Windows XP or later versions of Windows.

 

The following sections detail how traffic control is invoked, how traffic control settings can be checked, and how to programmatically modify how traffic control treats a given flow.

> [!Note]  
> Ownership of TC objects, such as flows and settings, are specific to a given application. As such, one application cannot inherit flow or filter objects from another object, nor can an application change any flows or settings it does not own. Accordingly, all TC objects are deleted when an application (process) dies.

 

 

 




