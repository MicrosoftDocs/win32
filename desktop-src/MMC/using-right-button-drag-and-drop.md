---
title: Using Right-Button Drag-and-Drop Operations
description: MMC 2.0 offers right-button drag-and-drop functionality consistent with Microsoft Windows user interface guidelines.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5c0ff574-2bc4-4fbb-ac73-b1d0ca3791d1
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Right-Button Drag-and-Drop Operations

MMC 2.0 offers right-button drag-and-drop functionality consistent with Microsoft Windows user interface guidelines. Prior to MMC 2.0, right-button drag-and-drop processing was identical to left-button drag-and-drop processing. In MMC 2.0, a context menu for the drag source is displayed if the drag-and-drop operation was invoked while the right mouse button was pressed (the context menu appears when the drop takes place).

The drag source snap-in controls which choices are available in the context menu; only allowable operations (based on the drag source's Cut and Copy enabled state) will appear in the context menu for the right-button drag-and-drop operation. At most, these choices will consist of Copy, Move, and Cancel. The default operation will appear bold in the context menu. The selected operation occurs based on the user's choice. Provided your snap-in supports drag-and-drop operations, no extra action is required to recognize a right-button drag-and-drop operation.

Be aware that pressing the CONTROL or SHIFT key has no effect in MMC while performing a right-button drag-and-drop operation.

 

 




