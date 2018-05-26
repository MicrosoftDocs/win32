---
title: Context Menus
description: Describes the use and contents of a context menu.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d3ad30f2-820c-4cf9-a7d0-0445011e1c28
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- snap-in UI MMC , context menus
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Context Menus

When the user right-clicks either a scope node or a list view item in the result pane, MMC displays a context menu. MMC builds the context menu by first adding its own menu items, then allowing the primary snap-in to add its own menu items, and finally by allowing any extension snap-ins to add their menu items. When the user clicks a context menu item, MMC forwards the user action to the primary snap-in.

When the user right-clicks a scope node, MMC first allows the primary snap-in to add its items. The primary snap-in can add menu items and submenus to the top of the context menu as well as to the All Tasks, New, and View submenus. MMC then allows each extension snap-in to add its items to the All Tasks and New submenus only. Extension snap-ins cannot add menu items to the top of the context menu or to the View submenu. Next, MMC displays the context menu and forwards the user selection to the primary snap-in.

Instead of adding common MMC menu commands to the context menu directly, the primary snap-in can enable certain standard verbs. MMC standard verbs include, for example, delete, copy, and paste. Using standard verbs properly is important. Because MMC controls the placement, text, and toolbars for these commands, consistency from snap-in to snap-in is ensured.

 

 




