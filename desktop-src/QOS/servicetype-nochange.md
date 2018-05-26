---
title: SERVICETYPE\_NOCHANGE
description: The SERVICETYPE\_NOCHANGE service type is useful when making changes to QOS parameters for one direction of a given flow.
ms.assetid: 729f3b74-a1b0-4665-8251-87bb113ca0a5
keywords:
- SERVICETYPE_NOCHANGE service type
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SERVICETYPE\_NOCHANGE

The SERVICETYPE\_NOCHANGE service type is useful when making changes to QOS parameters for one direction of a given flow. Specifically, the SERVICETYPE\_NOCHANGE enables application developers to indicate or implement changes in one direction of a flow, without having to respecify unchanged QOS parameters for the SERVICETYPE\_NOCHANGE-specified direction of the flow.

> [!Note]  
> RSVP signaling is not supported on Windows XP or later versions of Windows. In addition, WSAIoctl() under Windows Vista does not respect bit OR'ed flags.

 

 

 




