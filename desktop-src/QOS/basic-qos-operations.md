---
title: Basic QOS Operations
description: The RSVP Service Provider (RSVP SP) is where developers can enable their applications to take advantage of the QOS capabilities built into Windows 2000.
ms.assetid: 2856971a-7e60-4b24-a729-294b24bd52b0
keywords:
- Quality of Service QOS , tasks
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Basic QOS Operations

The RSVP Service Provider (RSVP SP) is where developers can enable their applications to take advantage of the QOS capabilities built into Windows 2000. The RSVP SP provides a service layer; by sitting between applications that want to take advantage of Quality of Service capabilities and QOS components. The RSVP SP shields developers from complexities involved in directly interfacing with QOS components such as RSVP, traffic control, and local policy modules.

**Note**  RSVP signaling is not supported on Windows XP, Windows Server 2003, or later versions of Windows.

 

The process of QOS-enabling an application includes enabling the application to perform the following:

-   [Receiving QOS-enabled Data](receiving-qos-enabled-data.md)
-   [Sending QOS-enabled Data](sending-qos-enabled-data.md)
-   [Closing the QOS connection](closing-the-qos-connection.md)

Throughout the course of a QOS session, applications also need to be able to manage the QOS connection.

Note that there are other components that may affect the success of QOS-enabled connection requests—such as policies in routers or on switches. For the purpose of explaining the process of QOS-enabling applications, the effect of these other QOS components will be addressed apart from the process of QOS enabling an application with the RSVP SP.

**Note**  RSVP is not supported on Windows XP and later versions.

 

 




