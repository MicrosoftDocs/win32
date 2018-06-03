---
title: Working with the Scope Pane
description: This section discusses how the features associated with a snap-in's scope pane are implemented.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e53bcfef-78a0-4abc-85e7-19ee5a392dd9
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- working with the scope pane MMC
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Working with the Scope Pane

This section discusses how the features associated with a snap-in's scope pane are implemented.

MMC defines several interfaces and other language constructs that a snap-in can use to work with the scope pane.

The [**IConsoleNamespace2**](/windows/desktop/api/Mmc/nn-mmc-iconsolenamespace2) interface enables snap-ins to manipulate items in the scope pane. [**InsertItem**](https://www.bing.com/search?q=**InsertItem**) and [**DeleteItem**](https://www.bing.com/search?q=**DeleteItem**) insert or remove single items from the scope pane. You can set or retrieve single items by using the [**SetItem**](https://www.bing.com/search?q=**SetItem**) and [**GetItem**](https://www.bing.com/search?q=**GetItem**) methods. [**GetChildItem**](https://www.bing.com/search?q=**GetChildItem**), [**GetNextItem**](https://www.bing.com/search?q=**GetNextItem**), and [**GetParentItem**](https://www.bing.com/search?q=**GetParentItem**) walk the tree's items. The [**Expand**](/windows/desktop/api/Mmc/nf-mmc-iconsolenamespace2-expand) method enables a snap-in to expand an item in the namespace without visibly expanding the item in the scope pane. Finally, [**AddExtension**](/windows/desktop/api/Mmc/nf-mmc-iconsolenamespace2-addextension) enables a snap-in to add an extension snap-in that dynamically extends the namespace of a selected item.

The [**IConsole2**](/windows/desktop/api/Mmc/nn-mmc-iconsole2) interface also contains a number of methods that snap-ins can use for working with scope items. The [**Expand**](/windows/desktop/api/Mmc/nf-mmc-iconsole2-expand) method enables a snap-in to expand or collapse an item in the scope pane. The [**SelectScopeItem**](https://www.bing.com/search?q=**SelectScopeItem**) method enables a snap-in to force the selection of a specified item, and the [**NewWindow**](https://www.bing.com/search?q=**NewWindow**) method allows the snap-in to programmatically create a new multiple-document interface (MDI) child window rooted at the specified item.

When the user selects a snap-in's scope item in the scope pane for the first time, the snap-in receives an [**MMCN\_EXPAND**](mmcn-expand.md) notification. If the selected item has any child items, the snap-in responds to the notification by inserting the child items. The [**SCOPEDATAITEM**](/windows/desktop/api/Mmc/ns-mmc-_scopedataitem) structure is used for specifying each item's information, such as the snap-in object that corresponds to the item, whether the item also has child items to insert, and where the item should be inserted relative to its parent item.

After filling the [**SCOPEDATAITEM**](/windows/desktop/api/Mmc/ns-mmc-_scopedataitem) structure for each child item of the selected item, the snap-in inserts the items into the scope pane using the [**IConsoleNamespace2::InsertItem**](https://www.bing.com/search?q=**IConsoleNamespace2::InsertItem**) method. When **InsertItem** returns (with S\_OK), the **ID** member of the **SCOPEDATAITEM** structure contains the HSCOPEITEM of the newly inserted item. MMC uses an item's HSCOPEITEM to uniquely identify the item.

MMC calls the snap-in's [**IComponentData::GetDisplayInfo**](/windows/desktop/api/Mmc/nf-mmc-icomponentdata-getdisplayinfo) method if it requires information to display a specific item in the scope pane; for example, a snap-in does not explicitly specify the display name of items (when filling the [**SCOPEDATAITEM**](/windows/desktop/api/Mmc/ns-mmc-_scopedataitem) structure) before inserting them in the scope pane. MMC then must rely on the snap-in to provide this information during calls to its **GetDisplayInfo** method.

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

 

 




