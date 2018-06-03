---
title: MMC Wizards
description: Describes the use and limitations of wizards.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d2ab259e-633e-4d10-bcbd-f0cc3dae1662
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMC, wizards
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMC Wizards

Any stand-alone or extension snap-in can display a wizard in response to a user action. Generally, wizards are invoked from a context menu command or by a toolbar button. When the user clicks a scope node or a result pane item and then performs an action that invokes a wizard, MMC allows the primary snap-in to add wizard pages to the wizard. Any user action entered in a particular wizard page is forwarded to the snap-in.

Be aware that in contrast to property sheets, MMC does not permit extension snap-ins to add their own pages to a wizard that is displayed by another snap-in.

 

 




