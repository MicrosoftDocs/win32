---
title: Working with the Scope Pane
description: This section discusses how the features associated with a snap-in's scope pane are implemented.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e53bcfef-78a0-4abc-85e7-19ee5a392dd9'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["working with the scope pane MMC"]
---

# Working with the Scope Pane

This section discusses how the features associated with a snap-in's scope pane are implemented.

MMC defines several interfaces and other language constructs that a snap-in can use to work with the scope pane.

The [**IConsoleNamespace2**](iconsolenamespace2.md) interface enables snap-ins to manipulate items in the scope pane. [**InsertItem**](iconsolenamespace2-insertitem.md) and [**DeleteItem**](iconsolenamespace2-deleteitem.md) insert or remove single items from the scope pane. You can set or retrieve single items by using the [**SetItem**](iconsolenamespace2-setitem.md) and [**GetItem**](iconsolenamespace2-getitem.md) methods. [**GetChildItem**](iconsolenamespace2-getchilditem.md), [**GetNextItem**](iconsolenamespace2-getnextitem.md), and [**GetParentItem**](iconsolenamespace2-getparentitem.md) walk the tree's items. The [**Expand**](iconsolenamespace2-expand.md) method enables a snap-in to expand an item in the namespace without visibly expanding the item in the scope pane. Finally, [**AddExtension**](iconsolenamespace2-addextension.md) enables a snap-in to add an extension snap-in that dynamically extends the namespace of a selected item.

The [**IConsole2**](iconsole2.md) interface also contains a number of methods that snap-ins can use for working with scope items. The [**Expand**](iconsole2-expand.md) method enables a snap-in to expand or collapse an item in the scope pane. The [**SelectScopeItem**](iconsole2-selectscopeitem.md) method enables a snap-in to force the selection of a specified item, and the [**NewWindow**](iconsole2-newwindow.md) method allows the snap-in to programmatically create a new multiple-document interface (MDI) child window rooted at the specified item.

When the user selects a snap-in's scope item in the scope pane for the first time, the snap-in receives an [**MMCN\_EXPAND**](mmcn-expand.md) notification. If the selected item has any child items, the snap-in responds to the notification by inserting the child items. The [**SCOPEDATAITEM**](scopedataitem.md) structure is used for specifying each item's information, such as the snap-in object that corresponds to the item, whether the item also has child items to insert, and where the item should be inserted relative to its parent item.

After filling the [**SCOPEDATAITEM**](scopedataitem.md) structure for each child item of the selected item, the snap-in inserts the items into the scope pane using the [**IConsoleNamespace2::InsertItem**](iconsolenamespace2-insertitem.md) method. When **InsertItem** returns (with S\_OK), the **ID** member of the **SCOPEDATAITEM** structure contains the HSCOPEITEM of the newly inserted item. MMC uses an item's HSCOPEITEM to uniquely identify the item.

MMC calls the snap-in's [**IComponentData::GetDisplayInfo**](icomponentdata-getdisplayinfo.md) method if it requires information to display a specific item in the scope pane; for example, a snap-in does not explicitly specify the display name of items (when filling the [**SCOPEDATAITEM**](scopedataitem.md) structure) before inserting them in the scope pane. MMC then must rely on the snap-in to provide this information during calls to its **GetDisplayInfo** method.

On certain occasions, MMC may send the snap-in an [**MMCN\_EXPANDSYNC**](mmcn-expandsync.md) notification to inform it that a specific scope item must be expanded synchronously; for example, when a console file is reloaded with an item expanded, the snap-in receives the notification so that it can insert any child items of the expanded item.

Be aware that MMC gives namespace extensions the opportunity to insert their own child items to scope items inserted by a primary snap-in. For more information, see [Extending a Primary Snap-in's Namespace](extending-a-primary-snap-ins-namespace.md).

## Related topics

<dl> <dt>

[Working with the Scope Pane: Interfaces](working-with-the-scope-pane-interfaces.md)
</dt> <dt>

[Working with the Scope Pane: Implementation Details](working-with-the-scope-pane-implementation-details.md)
</dt> <dt>

[Working with the Scope Pane: Additional Topics](working-with-the-scope-pane-additional-topics.md)
</dt> </dl>

 

 




