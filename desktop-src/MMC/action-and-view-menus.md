---
title: Action and View Menus
description: Describes the role of the Action and View menus.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 53eebb49-6eb6-44ad-a89d-f47c3a738d21
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- snap-in UI MMC , action and view menus
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Action and View Menus

The **Action** and **View** menus in the snap-in toolbar frame display the same context menu items that appear in the item's right-click context menu. The snap-in cannot discern between a user gaining access to these items through the **Action** and **View** menus and a user gaining access through the context menu.

The **Action** and **View** menus behave differently, however, depending on whether the nodes are accessed through the console tree or through the Favorites menu. When a node is clicked in the Favorites menu, the ordinary context menu items and the **Action** menu pertain to the Favorites node, not to the console tree node from which the Favorites node was selected. Consequently, you cannot access the context menu for the node through Favorites.

 

 




