---
title: MMC 2.0 Console Taskpads
description: Console taskpads are introduced in MMC 1.2. The user can use a console taskpad to run tasks such as starting wizards, opening property pages, performing menu commands, running command lines, and opening webpages.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a2fff9da-ee88-43e9-ba44-97dd1d1f65ec
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMC 2.0 console taskpads
- console taskpads MMC 2.0
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMC 2.0 Console Taskpads

Console taskpads are introduced in MMC 1.2. The user can use a console taskpad to run tasks such as starting wizards, opening property pages, performing menu commands, running command lines, and opening webpages.

Generally in MMC 1.2, there is little reason for choosing snap-in taskpads over console taskpads. Console taskpads offer many advantages in terms of ease of creation, performance, display consistency, and ability of the user to customize console taskpads.

Console taskpads are implemented by MMC. That is, MMC takes care of setting up a console taskpad for a particular scope item. To create a console taskpad, the user selects a scope item and then clicks the **New Taskpad View** context menu item. Next MMC asks the user, through the New Taskpad View wizard and the New Task wizard, for the information that it must create the console taskpad. The user can choose as tasks either menu commands, shell commands, or navigation shortcuts.

The menu commands that the user can choose from are the *same* context menu items that are present in the context menu of the selected scope item. MMC gets these menu commands from snap-ins in exactly the same way that it gets context menu items. That is, there is a one-to-one relationship between a menu command and a context menu item.

When the user chooses a menu command as a task and later clicks that task in the console taskpad, MMC forwards the user's action to the snap-in that added the menu item (menu command) associated with the selected task.

For more information about console taskpads, see the MMC HTML Help file that can be invoked from within an MMC console.

## Related topics

<dl> <dt>

[Using Taskpads](using-taskpads.md)
</dt> </dl>

 

 




