---
title: How Column Configuration Data Is Used
description: This topic identifies how snap-ins and MMC use column configuration data.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 049adfc0-ded6-4b84-aaef-4c58fa063037
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- column configuration data MMC
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How Column Configuration Data Is Used

This topic identifies how snap-ins and MMC use column configuration data.

## Customizing a List View

When a user customizes a list view, the following occurs:

1.  A snap-in is added to a console.
2.  One scope item is selected.
3.  The snap-in populates a list view, and uses [**IHeaderCtrl2**](/windows/desktop/api/Mmc/nn-mmc-iheaderctrl2) to add columns to the result pane.
4.  The user can customize the list view by using the **Modify Columns** dialog box to change column order or visible/hidden status. MMC persists the new column configuration data based on the column set ID or the node type GUID, which depends on whether the snap-in supports **CCF\_COLUMN\_SET\_ID**.
5.  If there is a change in the visible/hidden status of a column, MMC sends the snap-in an [**MMCN\_COLUMNS\_CHANGED**](mmcn-columns-changed.md) notification, which indicates the specific columns in the column set that are visible. The snap-in handles the notification by getting data for visible columns. Be aware that a snap-in can choose to update only the data of the visible columns, for example, when there is concern about the performance impact of populating data in hidden columns.

    Also, the snap-in can reject any user customizations by returning **E\_UNEXPECTED** in its [**MMCN\_COLUMNS\_CHANGED**](mmcn-columns-changed.md) notification handler. In this case, the snap-in is responsible for informing the user why it is refusing the changes, for example, by means of a message box.

6.  MMC applies the new column configuration data to the result pane. Assume column A was previously hidden and now is made visible by the user. When that displays visible columns in the result pane, MMC calls the [**IComponent::GetDisplayInfo**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getdisplayinfo) method to get data for column A. Because the snap-in already has fetched data for the column (in the last Step), the snap-in is ready to present the data when the method is called.

## Applying Persisted Data to a List View

After [customizing a list view](#customizing-a-list-view) or [saving and reloading a console file](#saving-and-reloading-a-console-file), persisted column configuration data is applied to the list view of a selected scope item as follows:

1.  MMC calls [**IComponentData::QueryDataObject**](/windows/desktop/api/Mmc/nf-mmc-icomponentdata-querydataobject) to request a data object for the list view of the selected scope item. MMC then calls the data object's [**GetData**](https://www.bing.com/search?q=**GetData**) method to request the column set ID in [**CCF\_COLUMN\_SET\_ID**](ccf-column-set-id.md) format.
2.  If the snap-in does not support **CCF\_COLUMN\_SET\_ID**, MMC calls [**IComponentData::QueryDataObject**](/windows/desktop/api/Mmc/nf-mmc-icomponentdata-querydataobject) to request a data object for the selected scope item and then queries it for the item's node type **GUID**.
3.  MMC maintains a navigational history of the result pane. For each scope item in the history, MMC stores the view type and view options specified by [**IComponent::GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype) when the result pane was originally displayed during the course of the current console session.

    -   MMC notifies the snap-in with [**MMCN\_RESTORE\_VIEW**](mmcn-restore-view.md) with the stored view type and view options (which include the parameters of [**IComponent::GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype)).
    -   If the snap-in accepts the [**MMCN\_RESTORE\_VIEW**](mmcn-restore-view.md) notification (by handling the notification and returning **S\_OK** in the handler), MMC sets the view; otherwise it calls the snap-in's [**IComponent::GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype) method.

4.  If MMC has column configuration data for the column set ID (or node type **GUID**) returned by the snap-in, the following things happen:

    -   MMC sends the [**MMCN\_SHOW**](mmcn-show.md) notification to the snap-in.
    -   The snap-in inserts columns.
    -   As soon as the snap-in has inserted all its columns (and before inserting the list view items) MMC checks to make sure that the number of inserted columns matches the number of columns it has persisted along with the column configuration data.

        If the numbers match, MMC rearranges the columns using the persisted column configuration data (width, order, hidden status, and so on).

        If the numbers do not match, this means that the snap-in has added or deleted columns from the column set without persisting this new data. MMC does not apply the column configuration data, and throws it away. For more information, see [IHeaderCtrl2 and Column Persistence](iheaderctrl2-and-column-persistence.md).

5.  If MMC does not have column configuration data for the column set ID (or node type **GUID**) returned by the snap-in, this means that the list view is still in its original state. That is, its column configuration data has not been changed by either the user or the snap-in since it was first displayed. In this case, MMC still calls [**IComponent::GetResultViewType**](/windows/desktop/api/Mmc/nf-mmc-icomponent-getresultviewtype), which it normally does when the user selects an item in the scope pane.
6.  The snap-in inserts list view items and returns from [**MMCN\_SHOW**](mmcn-show.md).
7.  MMC uses the sort data to sort on the specified columns.

## Saving and Reloading a Console File

During the saving and reloading of a console file, column configuration data is used as follows:

1.  After [customizing a list view](#customizing-a-list-view), the user saves the console. MMC requests a data object for the scope item and calls the data object's [**IDataObject::GetData**](https://www.bing.com/search?q=**IDataObject::GetData**) method with the **CCF\_COLUMN\_SET\_ID** format. The snap-in provides the ID of the column set in the result pane.

    If the snap-in does not support **CCF\_COLUMN\_SET\_ID**, MMC calls [**IComponentData::QueryDataObject**](/windows/desktop/api/Mmc/nf-mmc-icomponentdata-querydataobject) to request a data object for the selected scope item and then queries it for the item's node type **GUID**.

2.  The console is closed. The selection of the scope item is preserved when the console file is saved.
3.  The console file is reloaded.
4.  MMC loads all column configuration data for the snap-in into its own internal data structures.
5.  The tree in the scope pane is expanded down to the scope item that was selected when the console file was saved, and the scope item is selected.
6.  MMC begins [applying the persisted data to the list view](#applying-persisted-data-to-a-list-view) of the selected scope item.

## Related topics

<dl> <dt>

[Using IColumnData](using-icolumndata.md)
</dt> <dt>

[IHeaderCtrl2 and Column Persistence](iheaderctrl2-and-column-persistence.md)
</dt> <dt>

[Using Column Persistence](using-column-persistence.md)
</dt> </dl>

 

 




