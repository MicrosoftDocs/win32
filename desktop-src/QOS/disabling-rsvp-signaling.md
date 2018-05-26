---
title: Disabling RSVP Signaling
description: Both receiving applications and senders may disable RSVP signaling on a per-flow basis (a flow is a unidirectional QOS-enabled connection).
ms.assetid: b00f517f-5379-4d18-9bd5-21e30352edb9
keywords:
- Quality of Service QOS , tasks, disabling RSVP signaling
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Disabling RSVP Signaling

Both receiving applications and senders may disable RSVP signaling on a per-flow basis (a flow is a unidirectional QOS-enabled connection). Disabling RSVP signaling for a given flow is done by using the bitwise OR operator in the SERVICE\_NO\_QOS\_SIGNALING flag with the value in the [ServiceType](service-types.md) field of the **ReceivingFlowspec** member of the [**QOS**](/windows/win32/Winsock2/ns-winsock2-_qualityofservice?branch=master) structure.

**Note**  RSVP signaling is not supported on Windows XP, Windows Server 2003, or later versions of Windows.

 

 




