---
title: MMC Snap-ins
description: Outlines MMC snap-in implementation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f7a50641-9bb1-4aff-9455-149ade07c300
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMC Snap-ins

Without a snap-in loaded, an MMC console has no management functionality. The snap-in provides the interface to the management task and the access to programs and data required to perform the task.

A snap-in is implemented as a Component Object Model (COM) in-process server. The compiled code is linked to create a DLL. MMC interacts with snap-ins using several MMC-defined programming interfaces. The MMC interfaces allow snap-ins to share a common hosting environment (consoles) and provide cross-application integration.

 

 




