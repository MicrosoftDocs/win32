---
title: MMC Console Taskpad
description: Introduces a console taskpad.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c3f0e241-38fc-4612-b682-f3ba77916b88
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMC Console Taskpad

Console taskpads are introduced in MMC 1.2. The user can use a console taskpad to run tasks such as starting wizards, opening property pages, performing menu commands, running command lines, and opening webpages.

Console taskpads are implemented by MMC. That is, MMC takes care of setting up a console taskpad for a particular node.

To create a console taskpad, the user right-clicks a scope node and then, on the shortcut menu, clicks **New Taskpad View**. The user, through the New Taskpad View Wizard and the New Task Wizard, then enters the requested information that MMC must create the console taskpad. By using the New Task Wizard, the user can choose as tasks either menu commands, shell commands, or navigation shortcuts.

The menu commands that the user can choose from are the *same* context menu items that are present in the context menu of the selected scope node. MMC receives these menu commands from snap-ins in exactly the same way that it receives context menu items. That is, there is a one-to-one relationship between a menu command and a context menu item.

When the user chooses a menu command as a task and later clicks that task in the console taskpad, MMC forwards the user's action to the snap-in that added the menu item (menu command) associated with the selected task.

Snap-in taskpads are discussed further in the SDK, but since they are effectively replaced by console taskpads, snap-in taskpads are not recommended in the design guidelines.

 

 




