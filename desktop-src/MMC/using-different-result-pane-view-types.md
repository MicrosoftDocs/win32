---
title: Using Different Result Pane View Types
description: Using Different Result Pane View Types
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6c298348-3ce2-46fa-9b0a-b204774806b6
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- result pane view types MMC
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Different Result Pane View Types

MMC supports the following types of result pane views:

-   Standard result list view (usually called list view)
-   Taskpad view
-   Custom OCX view
-   Custom webpage

The data displayed in a result pane is accessed by means of the snap-in's [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) interface. When the user selects a scope item, the corresponding result data is displayed in the result pane. For a particular scope item, the snap-in can display one of the four types of result pane views.

## List Views

The default result pane view type is a list view. A list view displays a collection of items, each consisting of an icon and a label, and provides several ways to display and arrange the items. For example, additional information about each item can be displayed in columns to the right of the icon and label.

A list view can have one of the following view type modes:

-   Large icon
-   Small icon
-   List
-   Detail
-   Filtered

MMC implements list views using a list-view control. The control supports the preceding view type modes, and the user can choose a mode by selecting a scope item and clicking **View** on the context menu. Be aware that snap-ins can programmatically set all view type modes.

For more information about list views, see [Using List Views](using-list-views.md).

## Taskpad Views

A taskpad is a graphical way of presenting actions that can be performed on a selected item in the scope pane.

There are two types of taskpads: snap-in taskpads and console taskpads. Snap-in taskpads were introduced in MMC version 1.1 and are largely replaced by console taskpads in version 1.2. Console taskpads offer many advantages in terms of ease of creation, performance, display consistency, and ability of the user to customize console taskpads. In MMC 1.2, you should generally use console taskpads.

## Snap-in Taskpad

A snap-in taskpad is implemented as a view on the selected scope item in the scope pane, and that view is represented as a dynamic HTML (DHTML) page in the result pane. The taskpad DHTML page lists actions that can be performed on the selected scope item. Each action is represented as a task, which consists of an image, a label, a description, and a mechanism for instructing the snap-in to perform the associated action.

There are three types of snap-in taskpads:

-   Standard

    MMC provides a default taskpad that displays the taskpad title and tasks.

-   Standard list view

    MMC provides a list view taskpad (listpad) that displays the taskpad title; a list control that displays items that can be selected; and tasks that can perform actions on the selected items.

-   Custom

    Your snap-in can provide its own DHTML page that displays tasks to perform as well as other elements.

If a particular scope item has a taskpad view, it is the responsibility of the snap-in that inserted the scope item to provide the user with a mechanism for accessing the taskpad. One solution is to add a menu item to the scope item's **View** context submenu. Be aware that the snap-in can choose to display a taskpad for a scope item by default, so that the user automatically sees a taskpad view when the item is selected.

For more information about implementing snap-in taskpads, see [Using Taskpads](using-taskpads.md).

## Console Taskpad

Console taskpads are introduced in MMC 1.2. The user can use a console taskpad to run tasks such as starting wizards, opening property pages, performing menu commands, running command lines, and opening webpages.

Console taskpads are implemented by MMC. That is, MMC takes care of setting up a console taskpad for a particular scope item.

To create a console taskpad, the user selects a scope item and then clicks the New Taskpad View context menu item. Next MMC asks the user, through the New Taskpad View wizard and the New Task wizard, for the information that it must create the console taskpad. The user can choose as tasks either menu commands, shell commands, or navigation shortcuts.

The menu commands that the user can choose from are the same context menu items that are present in the context menu of the selected scope item. MMC gets these menu commands from snap-ins in exactly the same way that it gets context menu items. That is, there is a one-to-one relationship between a menu command and a context menu item.

When the user chooses a menu command as a task and later clicks that task in the console taskpad, MMC forwards the user's action to the snap-in that added the menu item (menu command) associated with the selected task.

For more information about console taskpads, see the MMC HTML Help file in the MMC console.

## Custom OCX Views

OCX controls, also known as ActiveX controls, are components (or objects) you can insert into a webpage or other application to reuse packaged functionality that someone else programmed.

A snap-in can start an OCX control in the result pane of an MMC console.

For more information about OCX views, see [Using Custom OCX Controls](using-custom-ocx-controls.md).

## Custom Webpages

The result pane of an MMC console can host HTML pages that are located either locally on the computer with MMC, or on an external web server.

For more information about custom webpages, see [Using Custom Webpages](using-custom-web-pages.md).

## Related topics

<dl> <dt>

[Using List Views](using-list-views.md)
</dt> <dt>

[Using Taskpads](using-taskpads.md)
</dt> <dt>

[Using Custom OCX Controls](using-custom-ocx-controls.md)
</dt> <dt>

[Using Custom Webpages](using-custom-web-pages.md)
</dt> </dl>

 

 




