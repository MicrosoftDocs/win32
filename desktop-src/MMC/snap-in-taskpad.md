---
title: Snap-in Taskpad
description: Introduces a snap-in taskpad.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3acdfbc3-8153-4502-9001-253210d62e85
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Snap-in Taskpad

A snap-in taskpad is implemented as a view on the selected scope node, and that view is represented as an HTML page in the result pane. The taskpad HTML page lists actions that can be performed on the selected node. Each action is represented as a task consisting of an image, a label, a description, and a mechanism for commanding the snap-in to perform the associated action.

The following list contains types of snap-in taskpads:

-   Standard

    MMC provides a default taskpad that displays the taskpad title and tasks.

-   Standard list view

    MMC provides a standard list view taskpad (listpad) that displays the taskpad title, a list control that displays items that can be selected, and tasks that can perform actions on the selected items.

-   Custom

    Your snap-in can provide its own HTML page that displays tasks to perform as well as other elements.

If a particular node has a taskpad view, it is the responsibility of the primary snap-in to provide the user with a mechanism for gaining access to the taskpad. One solution is to add a menu item to the node's **View** context submenu. Be aware that you can set a snap-in's default properties to display a taskpad automatically when a node is clicked.

When a taskpad view for a selected node is displayed in the result pane, MMC allows the primary snap-in to set up and add tasks to the taskpad. MMC then allows any extension snap-ins to add their own tasks to the taskpad. Be aware that for listpads, only the primary snap-in is permitted to insert items into its listpad's list view.

When the user clicks one of the tasks on the taskpad, MMC forwards the user's selection to the snap-in that added the task.

 

 




