---
title: Changing a Static Node's Attributes during Loading Implementation Details
description: Changing a Static Node's Attributes during Loading Implementation Details
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e6d33170-47e6-4a89-874a-853aa08a9b2a
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- changing a static node's attributes during loading MMC , implementation details
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Changing a Static Node's Attributes during Loading: Implementation Details

## To change a static node attribute when loading a snap-in

1.  Support the [**CCF\_SNAPIN\_PRELOADS**](ccf-snapin-preloads.md) clipboard format. When saving a console file, MMC calls [**IDataObject::GetDataHere**](https://www.bing.com/search?q=**IDataObject::GetDataHere**) on each loaded snap-in using this clipboard format. In the snap-in handler for the clipboard format, return **TRUE**.
2.  Handle the [**MMCN\_PRELOAD**](mmcn-preload.md) notification. MMC calls the [**IComponentData::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponentdata-notify) method of the snap-in with this notification when the snap-in is loaded from a saved console file. The lpDataObject value passed into the method call is a pointer to the static node's data object. The arg value passed into the call is the handle (an HSCOPEITEM) to the static node. The snap-in can use this handle to modify the attributes of the static node.

## Related topics

<dl> <dt>

[Changing a Static Node's Attributes during Loading](changing-a-static-node-s-attributes-during-loading.md)
</dt> <dt>

[Working with the Scope Pane: Interfaces](working-with-the-scope-pane-interfaces.md)
</dt> <dt>

[Working with the Scope Pane: Implementation Details](working-with-the-scope-pane-implementation-details.md)
</dt> </dl>

 

 




