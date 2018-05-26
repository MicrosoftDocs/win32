---
title: Using IColumnData
description: MMC allows snap-ins to access the column configuration data of a column set using the IColumnData interface. This section covers how and when snap-in developers can use the interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4da79fd1-f887-447c-89fd-d5044bd5751c
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using IColumnData

MMC allows snap-ins to access the column configuration data of a column set using the [**IColumnData**](icolumndata.md) interface. This section covers how and when snap-in developers can use the interface.

The [**IColumnData**](icolumndata.md) interface can be used in any of the following situations:

-   When handling an [**MMCN\_EXPAND**](mmcn-expand.md) notification, a snap-in can use the methods of [**IColumnData**](icolumndata.md) to examine persisted column configuration data for the selected scope item's list view and to modify it if required. Also, if the snap-in initiates data fetching in this event, it can optimize by checking which columns will be visible.
-   The snap-in receives an [**MMCN\_COLUMNS\_CHANGED**](mmcn-columns-changed.md) notification when the user changes the visible status of any column in the column set. Be aware that **MMCN\_COLUMNS\_CHANGED** provides information about the columns of the column set that will be visible after the snap-in returns with **S\_OK** or **S\_FALSE**. If the snap-in calls [**IColumnData::GetColumnConfigData**](icolumndata-getcolumnconfigdata.md) before returning from its **MMCN\_COLUMNS\_CHANGED** notification handler (with **S\_OK** or **S\_FALSE**), it will receive the current column settings.

    The *param* parameter of the [**MMCN\_COLUMNS\_CHANGED**](mmcn-columns-changed.md) notification tells the snap-in which columns are going to be visible due to the user changes. The snap-in can reject the changes by returning **E\_UNEXPECTED** in its **MMCN\_COLUMNS\_CHANGED** notification handler. In this case, the snap-in is responsible for informing the user why it is refusing the changes, for example, by means of a message box.

-   MMC [applies persisted data to a list view](how-column-configuration-data-is-used.md#applying-persisted-data-to-a-list-view) during the snap-in's handling of the [**MMCN\_SHOW**](mmcn-show.md) notification message. MMC applies the data during **MMCN\_SHOW** because it is during this event that the snap-in sets up the list view columns in the result pane.

    -   When receiving an [**MMCN\_SHOW**](mmcn-show.md) notification with the *arg* parameter set to **TRUE** (indicating that the snap-in should set up the result pane), the snap-in can view or modify the configuration data before inserting columns. It can, for example, use the [**IColumnData::GetColumnConfigData**](icolumndata-getcolumnconfigdata.md) method to see which columns in the column set are visible. Then, to optimize populating list view columns, the snap-in can choose to fetch data for and display only visible columns in the list view.

        The snap-in can also modify (and persist) configuration data using [**IColumnData::SetColumnConfigData**](icolumndata-setcolumnconfigdata.md) or [**IColumnData::SetColumnSortData**](icolumndata-setcolumnsortdata.md).

        Be aware that MMC applies the persisted column configuration data for the column set immediately after the snap-in has inserted the first item into the list view (using [**IResultData::InsertItem**](iresultdata-insertitem.md)). MMC assumes at this point that the snap-in has completed adding its columns. If the snap-in must either view or modify configuration data that MMC will apply to the column set, it must do so before inserting the first list view item.

    -   Before the snap-in receives an [**MMCN\_SHOW**](mmcn-show.md) notification with the *arg* parameter set to **FALSE** (indicating that the result pane is being torn down and possibly replaced), MMC has already persisted any user customizations made to the list view (such as which columns are visible or hidden).

        When the snap-in receives [**MMCN\_SHOW**](mmcn-show.md) (with *arg*=**FALSE**), it can choose to modify the persisted data. MMC then applies the (newly) persisted data to the column set the next time the user selects its item. The persisted data is also applied to all column sets with the same ID, so if the user selects a different item with the same column set ID, MMC will also apply the persisted data to it.

        Be aware that the snap-in can undo some or all of the user customizations made to the list view.

    -   Currently, when handling an [**MMCN\_SHOW**](mmcn-show.md) notification, if a snap-in inserts result items asynchronously (the columns are inserted by the notification handler, but items are inserted in the list view later) then it cannot sort the items. In this case, the snap-in can use the methods of [**IColumnData**](icolumndata.md) to get the persisted sort data and then perform the sorting at a later time.

-   A snap-in can add or remove columns in a column set using the methods of [**IHeaderCtrl2**](iheaderctrl2.md). See [IHeaderCtrl2 and Column Persistence](iheaderctrl2-and-column-persistence.md) for information on how this relates to column persistence.
-   Only user-initiated changes are persisted in memory automatically by MMC. The snap-in must use [**IColumnData**](icolumndata.md) to persist in memory any changes that it initiates. Examples of snap-in-initiated changes include changing the visibility status of a column during its insertion (with [**IHeaderCtrl2::InsertColumn**](iheaderctrl2-insertcolumn.md)) and modifying the width of a column (with [**IHeaderCtrl2::SetColumnWidth**](iheaderctrl2-setcolumnwidth.md)).
-   Be aware that the [**IColumnData**](icolumndata.md) interface is not designed to be an alternative to the [**IHeaderCtrl2**](iheaderctrl2.md) interface. Snap-ins should use **IHeaderCtrl2** as much as possible, because it allows the user to see any snap-in changes to a list view immediately. **IColumnData** should only be used in situations for which **IHeaderCtrl2** is not designed.

## Related topics

<dl> <dt>

[How Column Configuration Data Is Used](how-column-configuration-data-is-used.md)
</dt> <dt>

[IHeaderCtrl2 and Column Persistence](iheaderctrl2-and-column-persistence.md)
</dt> <dt>

[Using Column Persistence](using-column-persistence.md)
</dt> </dl>

 

 




