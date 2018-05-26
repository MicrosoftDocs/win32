---
title: Result Panes
description: Describes the contents of the result pane.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f87683e9-5f6a-4e69-a132-7485a0292c02
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- snap-in UI MMC , result panes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Result Panes

When a user clicks a node in the scope pane, MMC allows the snap-in that added the node to display a view in the result pane for that node. The snap-in that added the node is the *primary snap-in*. Be aware that the concept of a primary snap-in is different than that of a stand-alone snap-in. Every stand-alone snap-in is also the primary snap-in for at least one node, but a namespace extension snap-in is the primary snap-in for the nodes that it has added. Any node in the scope pane can display several different result pane views:

-   **Standard result list view**

    The default result pane view type is a standard result list view (or simply *list view*). A list view displays a collection of items, each consisting of an icon and a label, and provides several ways to display and arrange the items. Unlike the scope pane, in which a snap-in adds items only once, the primary snap-in is expected to insert its result list items each time the scope node is clicked. This allows the result items to be considerably more dynamic than the scope items. For example, if a scope node is selected in more than one multiple-document interface (MDI) window, the result list need not necessarily be the same.

    A special type of standard list is a *virtual list*. In a virtual list, the snap-in provides only as many items as are currently shown. When the user scrolls up or down, the snap-in is asked for additional items. This type of list is particularly well suited for large numbers of result items. Be aware that only the primary snap-in can add list items; extension snap-ins cannot add list items.

-   **Taskpad view**

    A taskpad is a simplified GUI presentation of actions that can be performed within a snap-in. Taskpads are used for such tasks as starting wizards, opening property pages, performing menu commands, running command lines, and opening webpages.

    For more information about Taskpads, see [Taskpads](taskpads.md).

-   **Custom OCX view**

    A snap-in can start an OCX control in the result pane of an MMC console.

-   **Custom webpage**

    The result pane of an MMC console can host HTML pages that are located either locally in MMC, or on an external web server.

Wherever possible, you should design a snap-in to use a standard result list view rather than a custom OCX view or a webpage. Taskpads can be used to supplement a standard result list view. If the standard list simply does not provide enough user interface flexibility, then you should use an OCX or an HTML page.

 

 




