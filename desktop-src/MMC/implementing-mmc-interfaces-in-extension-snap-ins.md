---
title: Implementing MMC 2.0 Interfaces in Extension Snap-ins
description: An extension snap-in can support any or all of the following extension types
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3a5ed403-3ad1-4a1d-8829-f22862d68136
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- implementing MMC 2.0 interfaces in extension snap-ins
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Implementing MMC 2.0 Interfaces in Extension Snap-ins

An extension snap-in can support any or all of the following extension types:

-   Namespace extension
-   Context menu extension
-   Toolbar extension
-   Menu button extension
-   Property page extension
-   Taskpad extension
-   View extension (requires MMC 2.0)

Namespace extensions add scope items to a primary snap-in's scope pane. Namespace extensions must implement [**IComponentData**](icomponentdata.md). Non-namespace extensions — context menu, toolbar, menu button, property page, and taskpad extensions — do not add scope items to a primary snap-in's scope pane, and consequently they do not need to implement **IComponentData**.

Context menu extensions must implement [**IExtendContextMenu**](iextendcontextmenu.md), toolbar and menu button extensions implement [**IControlbar**](icontrolbar.md), property page extensions implement [**IExtendPropertySheet2**](iextendpropertysheet2.md), and taskpad extensions implement [**IExtendTaskpad**](iextendtaskpad.md).

View extensions must implement the [**IExtendView**](iextendview.md) interface.

Details about writing extensions are provided in the following topics:

-   [Extending a Primary Snap-in's Namespace](extending-a-primary-snap-ins-namespace.md)
-   [Extending a Primary Snap-in's Context Menu](extending-a-primary-snap-ins-context-menu.md)
-   [Extending a Primary Snap-in's Control Bar](extending-a-primary-snap-ins-control-bar.md)
-   [Extending a Primary Snap-in's Property Sheet](extending-a-primary-snap-ins-property-sheet.md)
-   [Extending a Primary Snap-in's Taskpad](extending-a-primary-snap-ins-taskpad.md)
-   [Extending a Primary Snap-in's View](extending-a-primary-snap-ins-view.md)

## Related topics

<dl> <dt>

[Requirements for Extension Snap-ins](requirements-for-extension-snap-ins.md)
</dt> <dt>

[Working with Extension Snap-ins](working-with-extension-snap-ins.md)
</dt> </dl>

 

 




