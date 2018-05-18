---
title: Using Column Persistence
description: This feature is introduced in MMC 1.2.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '409b8212-a2fc-4d64-a407-ade2fde9ac4d'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["column persistence MMC", "column persistence MMC"]
---

# Using Column Persistence

This feature is introduced in MMC 1.2.

Starting with version 1.2, MMC persists column customization and sorting parameters as the user moves between scope items in the scope pane. This allows a user to customize a list view, select another scope item in the scope pane, and then return to the original scope item with the customizations preserved. MMC will also save the customizations in the .msc file when the user saves the console and then restore them when the file is loaded.

The following column customization features are available:

-   **Persistence of column widths** MMC automatically persists user changes made to column widths.
-   **Reordering of columns** Users can change the order of columns in a list view.
-   **Column visibility in list view** Users can choose which columns to display in a list view.
-   **Sorted column and sort direction information** Users can select a column and choose to sort it in either ascending or descending order. The default sort is based on string comparison. Be aware that MMC does not support multi-column sorting.

MMC also allows users to export a list view to a text file. Only visible columns are exported, in the order in which they appear in the list view.

MMC automatically persists in memory all user column customizations. This persisted information is known collectively as *column configuration data*.

## Column Set and Column Set ID

A *column set* is a set of columns inserted in the result pane by a snap-in when the user selects a scope item in the snap-in. When the user selects a different scope item in that snap-in, the same or a different column set may be shown by the snap-in.

MMC requires that every scope item specify a column set ID for the column set it inserts. MMC uses the ID of a column set to identify its persisted column configuration within each view. If the snap-in does not explicitly supply one then MMC uses the scope item's node type GUID. This means that if the snap-in has multiple scope items of the same node type in the scope pane, and it does not explicitly set an ID, then the user's customization will be propagated across the different list views. Snap-ins can change the ID by using the [**CCF\_COLUMN\_SET\_ID**](ccf-column-set-id.md) clipboard format.

## Column Persistence and Multiple Views

MMC persists column configuration data per column set per view, per snap-in instance. As a result, the same column set ID can be used in multiple views, and all column sets with the same ID can be operated on independently. MMC will preserve each column set's data separately on a per-view basis.

As an example of this, suppose two views are open in a console. Each view shows the column set of the same scope item. Any user customizations to a column set in one of the views is then limited to that column set in that view, even if both column sets have the same ID.

## Supporting CCF\_COLUMN\_SET\_ID

Snap-ins should support [**CCF\_COLUMN\_SET\_ID**](ccf-column-set-id.md) in the following situations:

-   Some snap-ins might have the same set of columns for more than one node type. If such a snap-in wants MMC to propagate changes to the column set for all of these node types, it must implement the **CCF\_COLUMN\_SET\_ID** clipboard format and return the same column set ID for all the node types. This allows a user to select one scope item, change some column configuration settings, and then see settings preserved in the result panes of different node types in the scope pane.
-   A single scope item might have different column sets in its result pane. For example, a snap-in might elect to display different sets of columns, depending on its state. In this case, the snap-in should implement **CCF\_COLUMN\_SET\_ID** for each column set, taking care to specify a unique column set ID for each column set.
-   Some snap-ins (for example, Event Viewer) might have scope items of the same node type, but with different column sets (for example, System Log, Application Log, and Security Log). To distinguish these column sets from each other and to make sure that changes are not propagated to all scope items of the same node type, the snap-in should implement **CCF\_COLUMN\_SET\_ID** to uniquely identify each column set.

## How Snap-ins Affect Column Persistence

MMC allows the user to hide columns or make columns visible in the list view using the **Modify Columns** dialog. If the user makes any column setting changes while the list view is displayed, MMC sends an [**MMCN\_COLUMNS\_CHANGED**](mmcn-columns-changed.md) notification message to the snap-in. The notification tells the snap-in which columns in the list view are visible. The snap-in can return either **S\_OK** or **S\_FALSE** in its **MMCN\_COLUMNS\_CHANGED** notification handler to accept the user changes. If the snap-in rejects the changes, it should return **E\_UNEXPECTED** instead and display a message box indicating why the user changes were rejected.

MMC also allows snap-ins to access the column configuration data that it persists in memory. This is because situations can arise in which snap-ins need to be aware of and react to user changes made to column configurations. For example, a snap-in may not want to fetch data for columns that are hidden in order to improve performance. Snap-ins may also need to modify persisted column configuration data.

MMC allows snap-ins to access column configuration data using the [**IColumnData**](icolumndata.md) interface. The [**GetColumnConfigData**](icolumndata-getcolumnconfigdata.md) and [**SetColumnConfigData**](icolumndata-setcolumnconfigdata.md) methods allow a snap-in to retrieve and set the current width, order, and hidden status of each column in a column set that is stored in memory by MMC. The [**GetColumnSortData**](icolumndata-getcolumnsortdata.md) method enables a snap-in to retrieve from memory the sorted column and sorting direction for a column set, while the [**SetColumnSortData**](icolumndata-setcolumnsortdata.md) method enables a snap-in to set this same information.

## Note

If the user presses the **Restore Defaults** button in the MMC 2.0 **Add/Remove Columns** dialog, the values for the column settings, which the snap-in originally provided, will be restored.

## Related topics

<dl> <dt>

[Using Column Persistence: Interfaces](using-column-persistence-interfaces.md)
</dt> <dt>

[Using Column Persistence: Implementation Details](using-column-persistence-implementation-details.md)
</dt> <dt>

[Using Column Persistence: Advanced Topics](using-column-persistence-advanced-topics.md)
</dt> </dl>

 

 




