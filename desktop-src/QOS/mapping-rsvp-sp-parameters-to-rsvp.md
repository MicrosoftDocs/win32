---
title: Mapping RSVP SP Parameters to RSVP
description: To provide quality of service parameters from the RSVP SP to RSVP, there must be some mechanism to translate parameters that the application provides in the QOS structure to RSVP.
ms.assetid: 6da60e95-dce9-4592-a280-d2dde756329e
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Mapping RSVP SP Parameters to RSVP

To provide quality of service parameters from the RSVP SP to RSVP, there must be some mechanism to translate parameters that the application provides in the [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure to RSVP. Passing RSVP-requisite service quality parameters, based on information provided by the application to the RSVP SP, is done through mapping.

The information provided to RSVP is derived from the **SendingFlowspec** and **ReceivingFlowspec** members of the [**FLOWSPEC**](/previous-versions/windows/desktop/api/Qos/ns-qos-_flowspec) structure, itself a member of the [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure.

 

 




