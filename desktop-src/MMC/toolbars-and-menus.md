---
title: Toolbars and Menus
description: Describes how toolbar buttons get created from menu items.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '26eae90d-8b00-4490-bed4-595c60c63d9e'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["snap-in UI MMC , toolbars and menus"]
---

# Toolbars and Menus

When the user clicks a node, the primary snap-in adds its menu items to the context menu and its snap-in toolbar to the snap-in toolbar frame. Next, extension snap-ins do the same. When the user clicks a menu item, MMC forwards the user's selection to the primary snap-in. As in the context menus, the primary snap-in can add MMC standard verbs so that MMC automatically creates toolbar buttons for those items.

 

 




