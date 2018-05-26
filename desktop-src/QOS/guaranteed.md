---
title: GUARANTEED
description: When the GUARANTEED service type is specified, the RSVP SP and other QOS components included in the transmission of packets attempt to guarantee the level of service quality defined by the applications provided QOS parameters.
ms.assetid: aecaadb4-24dd-4455-86d3-17263ddcd479
keywords:
- GUARANTEED service type
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GUARANTEED

When the GUARANTEED service type is specified, the RSVP SP and other QOS components included in the transmission of packets attempt to guarantee the level of service quality defined by the application's provided QOS parameters. With the GUARANTEED service type, queuing algorithms isolate an application's data flow (the unidirectional transmission of packets on a QOS-enabled connection) to provide the following service characteristics:

-   The application's flow is isolated from other flows as much as possible.
-   The application's flow is guaranteed the ability to transmit data at the TokenRate for the duration of the connection.
-   If the application does not exceed TokenRate over time, latency is also guaranteed.

The GUARANTEED service type is designed for applications that require precisely known service quality (QOS parameters), but would not benefit from better service. An example of such an application is a real-time control system application. The GUARANTEED service type is also designed to transmit within a specific delay bound.

> [!Note]  
> RSVP signaling is not supported on Windows XP or later versions of Windows.

 

 

 




