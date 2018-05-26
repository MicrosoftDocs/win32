---
title: IHeaderCtrl2 and Column Persistence
description: The IHeaderCtrl2 interface contains three methods that can be used to modify the column configuration data of a scope items column set
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: acec421f-edd4-49b6-a244-7099c524fe75
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IHeaderCtrl2 and Column Persistence

The [**IHeaderCtrl2**](iheaderctrl2.md) interface contains three methods that can be used to modify the column configuration data of a scope item's column set:

-   [**IHeaderCtrl2::InsertColumn**](iheaderctrl2-insertcolumn.md)
-   [**IHeaderCtrl2::DeleteColumn**](iheaderctrl2-deletecolumn.md)
-   [**IHeaderCtrl2::SetColumnWidth**](iheaderctrl2-setcolumnwidth.md)

MMC does not persist in memory any changes made to a column set due to the action of [**IHeaderCtrl2::InsertColumn**](iheaderctrl2-insertcolumn.md), [**IHeaderCtrl2::DeleteColumn**](iheaderctrl2-deletecolumn.md), or [**IHeaderCtrl2::SetColumnWidth**](iheaderctrl2-setcolumnwidth.md), so snap-ins must update persisted column configuration data after using these methods.

Consider the following scenarios:

-   **Scenario 1:** Suppose the user selects a scope item and does not customize its list view. The snap-in also makes no changes to the column set. The user selects a different item and then reselects the original item. In this case, the user will see the original list view that was displayed when the item was first selected.
-   **Scenario 2:** Suppose the user selects a scope item for which MMC persists column configuration data. The user does not customize its list view. The snap-in does not make any changes either. The user then selects a different item. The user then reselects the original item. In the meantime, the data source for the original item has changed in some way, and as a result, the snap-in inserts an extra column into the list view of the original item using [**IHeaderCtrl2::InsertColumn**](iheaderctrl2-insertcolumn.md). When [applying the persisted data to the list view](how-column-configuration-data-is-used.md#applying-persisted-data-to-a-list-view), MMC notices that the number of new columns does not match the number of columns persisted in memory. As a result, MMC throws away the persisted data and does not apply it to the column set.

In Scenario 2, the snap-in does not persist the new column configuration data after calling [**IHeaderCtrl2::InsertColumn**](iheaderctrl2-insertcolumn.md), and consequently MMC ignores the outdated data persisted in memory when the list view is displayed.

To avoid this situation, snap-ins should always make sure that the persisted column configuration data for a particular column set is up-to-date. Here are a number of strategies that snap-ins can use to guarantee this:

-   Immediately after making changes to a column set using the [**IHeaderCtrl2**](iheaderctrl2.md) interface, snap-ins can call [**IColumnData::SetColumnConfigData**](icolumndata-setcolumnconfigdata.md) to update the column set's persisted column configuration data.
-   If a snap-in knows that a scope item's column set can change because of differences in the data source version or other data source properties, the snap-in can assign a different column set ID for each server version. This guarantees that column configuration data for each server version is stored separately. Then, when MMC asks for the column set ID for that displays the item's list view, the snap-in can apply the appropriate ID corresponding to the current server version.
-   When handling an [**MMCN\_EXPAND**](mmcn-expand.md) notification, a snap-in can use the methods of [**IColumnData**](icolumndata.md) to examine persisted column configuration data for the selected scope item's list view and modify it if required.
-   See [Using IColumnData](using-icolumndata.md) for more suggestions.

## Related topics

<dl> <dt>

[How Column Configuration Data Is Used](how-column-configuration-data-is-used.md)
</dt> <dt>

[Using IColumnData](using-icolumndata.md)
</dt> <dt>

[Using Column Persistence](using-column-persistence.md)
</dt> </dl>

 

 




