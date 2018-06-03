---
title: Status Bar Text
description: This feature is introduced in MMC version 1.1.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7bf56a18-ef8e-46c7-942f-01739a3dcaec
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- status bar text MMC
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Status Bar Text

This feature is introduced in MMC version 1.1.

MMC enables a snap-in to change the text in the status bar of each MDI child window (view).

In MMC 1.1 and later, each view has a status bar. In addition, the Status Bar menu item is added to the **View** menu of each child window and its context menu.

The [**IConsole2::SetStatusText**](/windows/desktop/api/Mmc/nf-mmc-iconsole2-setstatustext) method enables a snap-in to change the text in the status bar.

 

 




