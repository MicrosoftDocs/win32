---
title: Scope Panes
description: Describes the contents of the scope pane.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 66ea9f68-b277-433b-a112-c886594f7768
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- snap-in UI MMC , scope panes
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Scope Panes

The console tree is composed of nodes that represent containers and objects and is understood from a programming point of view to be made up of nodes. The top-level node of every stand-alone snap-in is a *static node,* which is maintained by MMC. When opening a saved console, MMC displays the title and icon of the node even if the snap-in itself has not been loaded.

The static node is a parent node. The nodes below it are *child* nodes. These child nodes can be placed in the tree either by the stand-alone snap-in or by a namespace extension. These nodes are dynamic because MMC does not know about them until they are added. They are generally added only when their parent node is double-clicked or expanded.

Because of the dynamic nature of child nodes, adding a childless node to the console causes the extension snap-in to notify MMC that a plus sign should not be displayed in the tree. If an extension snap-in later inserts a child into that node, then MMC changes the tree automatically to display the plus sign.

 

 




