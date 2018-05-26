---
title: Programmatic Expansion of Scope Items
description: This feature is introduced in MMC version 1.1.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fc0c9abb-8622-4600-ae6d-500e9505bb3b
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- programmatic expansion of scope items MMC
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Programmatic Expansion of Scope Items

This feature is introduced in MMC version 1.1.

MMC specifies two **Expand** methods that allow you to programmatically expand a scope item.

The [**IConsole2::Expand**](iconsole2-expand.md) method enables the snap-in to expand or collapse an item in the scope pane of a particular view. This method is the programmatic equivalent of the user clicking the plus or minus sign to expand or collapse an item in the scope pane. Be aware that each MDI window within the console represents a different view.

The [**IConsoleNamespace2::Expand**](iconsolenamespace2-expand.md) method enables the snap-in to expand an item in the namespace without visibly expanding it in the scope pane. Use this method to expand a specified item for the purpose of inserting the child items beneath that item. The method does not expand the item in any views.

 

 




