---
title: Nodes and IComponentData
description: The IComponentData interface is closely associated with the functionality of the nodes displayed in the scope pane.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fa26a602-f27a-4244-811d-c768c9a9f94e
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- nodes and IComponentData MMC
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Nodes and IComponentData

The [**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata) interface is closely associated with the functionality of the nodes displayed in the scope pane. A snap-in's **IComponentData** object adds items to the scope pane when it receives an [**MMCN\_EXPAND**](mmcn-expand.md) notification from the console through its [**Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponentdata-notify) method.

While nodes themselves are maintained by MMC after their creation, [**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata) handles notifications sent to it through its [**Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponentdata-notify) method when the user performs an action on a particular node.

Snap-ins implement [**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata) as COM objects. When the user loads a snap-in in an MMC console, MMC creates an instance of the snap-in by creating its **IComponentData** object. There is only one instance of **IComponentData** per instance of a stand-alone snap-in or namespace extension snap-in.

 

 




