---
title: QOS Events
description: QOS makes certain information available to applications that register interest in obtaining event-related QOS information.
ms.assetid: 5e3a8cb1-e841-4050-8083-48838fdc6caf
keywords:
- Quality of Service QOS , described, events
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# QOS Events

QOS makes certain information available to applications that register interest in obtaining event-related QOS information. QOS makes the following event categories available to applications:

-   Policy-based or administratively-based information that impacts QOS provisioning for a given flow.
-   Errors that occur upon setup, or during the life of a QOS-enabled flow
-   Information regarding acceptance or rejection of QOS requests by the RSVP module or by the network. Keep in mind that rejection of a QOS request may indicate a transient failure, which may be subsequently corrected.
-   Significant changes in the service quality provided by the network (when in contrast with previously negotiated QOS parameters), such as from flow preemption in the network.
-   Status regarding the presence of a QOS peer to send or receive a particular flow.

QOS provides this status information through the FD\_QOS event suite. Applications that take advantage of QOS capabilities, whether sending or receiving data, should use FD\_QOS events to maintain and monitor their QOS-enabled application. Registering interest in QOS events is done by listening for FD\_QOS event notifications.

It is important to realize that all FD\_QOS events are edge-triggered. With edge-triggered events, a message is posted exactly once when a QOS change occurs. Further messages are not forthcoming until the provider detects a further change in quality of service, or the application re-negotiates the flow's quality of service.

For more information about event notification, consult the following Knowledge Base article:

[http://support.microsoft.com/kb/196360](http://go.microsoft.com/fwlink/p/?linkid=83999)

 

 




