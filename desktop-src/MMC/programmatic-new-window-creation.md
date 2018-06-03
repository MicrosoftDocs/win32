---
title: Programmatic New Window Creation
description: This feature is introduced in MMC version 1.1.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e1e1e741-3bdb-4826-811b-177bb14bf476
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- programmatic new window creation MMC
- window creation MMC
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Programmatic New Window Creation

This feature is introduced in MMC version 1.1.

The [**NewWindow**](https://www.bing.com/search?q=**NewWindow**) method is available in both the [**IConsole**](/windows/desktop/api/Mmc/nn-mmc-iconsole2) and **IConsole2** interfaces. This method enables a snap-in to open a new MDI window with a specified scope item as the root node. This is the programmatic equivalent of the **New Window From Here** command on the **View** context menu. The method also supports options for that displays the title bar text, the standard toolbars, and the scope pane. It also enables you to specify whether to persist the new window to the .msc file.

 

 




