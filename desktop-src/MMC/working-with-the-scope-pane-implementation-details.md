---
title: Working with the Scope Pane Implementation Details
description: The following procedure applies to primary snap-ins that insert their own items into the scope pane. For more information about how extension snap-ins can add items to the scope pane of a primary snap-in, see Extending a Primary Snap-ins Namespace.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5e3fcd72-9623-43dc-b0a4-0c987599d0a0
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- working with the scope pane MMC , implementation details
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Working with the Scope Pane: Implementation Details

The following procedure applies to primary snap-ins that insert their own items into the scope pane. For more information about how extension snap-ins can add items to the scope pane of a primary snap-in, see [Extending a Primary Snap-in's Namespace](extending-a-primary-snap-ins-namespace.md).

**To insert items in the scope pane**

1.  Determine the tree structure of the snap-in's scope pane; that is, how many child items the snap-in's root node (the static node) inserts, and whether these items have child items. Associate a snap-in object with each item in the scope pane, and determine a method for instantiating these objects.

    Also, determine the node type **GUID** for each item in the scope pane. You can use the uuidgen.exe tool for generating GUIDs.

    For more information about nodes, see [Snap-in Namespace](snap-in-namespace.md).

2.  Handle the [**MMCN\_EXPAND**](mmcn-expand.md) notification message, which MMC sends to the snap-in's [**IComponentData**](/windows/win32/Mmc/nn-mmc-icomponentdata?branch=master) implementation when a scope item is selected for the first time in the scope pane. In response to the notification, the snap-in should do the following:

    -   If the selected item has child items, the snap-in must fill a [**SCOPEDATAITEM**](/windows/win32/Mmc/ns-mmc-_scopedataitem?branch=master) structure for each child item and then insert the item in the scope pane by calling the [**IConsoleNamespace2::InsertItem**](iconsolenamespace2-insertitem.md) method with a pointer to the address of the **SCOPEDATAITEM** structure. When **InsertItem** returns (with **S\_OK**), the **ID** member of the **SCOPEDATAITEM** structure contains the **HSCOPEITEM** of the newly inserted item. Snap-ins should store the **HSCOPEITEM** of each inserted item and use it to later manipulate the item using the methods of the [**IConsole2**](/windows/win32/Mmc/nn-mmc-iconsole2?branch=master) and [**IConsoleNameSpace2**](/windows/win32/Mmc/nn-mmc-iconsolenamespace2?branch=master) interfaces.

        Be aware that when filling a [**SCOPEDATAITEM**](/windows/win32/Mmc/ns-mmc-_scopedataitem?branch=master) structure for a child item, the snap-in can also specify whether that child item has child items of its own. If it does not have any child items, the snap-in should set the **cChildren** member of the structure to 0. This instructs MMC to hide the plus (+) sign when inserting the child item. If conditions change and the inserted child item has child items at a later time, the snap-in can modify the **cChildren** member by using [**IConsoleNameSpace2::SetItem**](iconsolenamespace2-setitem.md).

    -   If the selected item does not have any child items, the snap-in must return **S\_FALSE**.

3.  Implement the [**IComponentData::GetDisplayInfo**](/windows/win32/Mmc/nf-mmc-icomponentdata-getdisplayinfo?branch=master) method. When inserting a scope item or a result item into MMC, the display name must be set to **MMC\_CALLBACK**. After the snap-in returns from the [**MMCN\_EXPAND**](mmcn-expand.md) notification handler, MMC calls **GetDisplayInfo** once for each inserted item in the scope pane (for which **SCOPEDATAITEM.displayname** = **MMC\_CALLBACK**) to request the item's display name.
4.  If necessary, handle the [**MMCN\_EXPANDSYNC**](mmcn-expandsync.md) notification.

## Related topics

<dl> <dt>

[Working with the Scope Pane: Interfaces](working-with-the-scope-pane-interfaces.md)
</dt> <dt>

[Working with the Scope Pane: Additional Topics](working-with-the-scope-pane-additional-topics.md)
</dt> </dl>

 

 




