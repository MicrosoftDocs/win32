---
title: RSVP Reservation Styles
description: RSVP recognizes three reservation styles that define how RSVP-enabled network devices set up reservations along the path between an end-to-end QOS-enabled connection.
ms.assetid: e77060fa-63f5-4b9f-9678-6501315c2a99
keywords:
- Quality of Service QOS , described, RSVP reservation styles
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RSVP Reservation Styles

RSVP recognizes three reservation styles that define how RSVP-enabled network devices set up reservations along the path between an end-to-end QOS-enabled connection. RSVP reservation styles are also sometimes called reservation styles. The three RSVP reservation styles are:

-   Fixed Filter (FF)
-   Wildcard Filter (WF)
-   Shared Explicit (SE)

RSVP reservation styles either establish a distinct reservation for each upstream sender, or make a single reservation that is shared among all senders' packets. The RSVP SP automatically selects an appropriate RSVP-reservation style based on the type of connection (unicast or multicast) as part of its RSVP invocation. Application programmers can override the RSVP SP's selection of reservation style, overriding the setting that the RSVP SP provides, through use of the Style member of the [**RSVP\_RESERVE\_INFO**](/windows/previous-versions/Qossp/ns-qossp-_rsvp_reserve_info?branch=master) object. For more information on overriding this setting, see [Overriding Default RSVP Filter Style Settings](overriding-default-rsvp-filter-style-settings.md).

 

 




