---
title: MMC Enumerated Nodes
description: Every static node in each MDI child (view) can have its own subtree of enumerated nodes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d9a2316f-5934-460f-b607-b7df2b053528
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMC enumerated nodes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMC Enumerated Nodes

Every static node in each MDI child (view) can have its own subtree of enumerated nodes. These enumerated nodes are not persisted by MMC to the .msc file; rather, the snap-in rebuilds them in each view as required. The children of enumerated nodes are always other enumerated nodes, never static or built-in nodes.

When the user selects or expands the static node in the scope pane, the snap-in's implementation of [**IComponentData**](icomponentdata.md) is notified and can insert enumerated nodes as children of that static node. Similarly, the same **IComponentData** interface is notified when one of those enumerated children is selected or expanded. That is, the same **IComponentData** interface is associated with the static node and all of its enumerated children belonging to the snap-in that owns the static node, in all views.

If there is more than one MDI child viewing a static node, the node will appear the same in each MDI child.

 

 




