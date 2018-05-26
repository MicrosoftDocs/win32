---
title: MMCN\_COLUMNS\_CHANGED message
description: The MMCN\_COLUMNS\_CHANGED notification is introduced in MMC 1.2.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 634f14ba-0b6a-41b6-af97-e957d1337623
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_COLUMNS_CHANGED message MMC
topic_type:
- apiref
api_name:
- MMCN_COLUMNS_CHANGED
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMCN\_COLUMNS\_CHANGED message

The **MMCN\_COLUMNS\_CHANGED** notification is introduced in MMC 1.2.

The **MMCN\_COLUMNS\_CHANGED** notification is sent to the snap-in's [**IComponent::Notify**](icomponent-notify.md) method when the user hides columns or makes columns visible in the list view using the **Modify Columns** dialog box.

The notification tells the snap-in which columns in the list view are visible. The *param* parameter passed to the snap-in in the [**IComponent::Notify**](icomponent-notify.md) method is a pointer to the [**MMC\_VISIBLE\_COLUMNS**](mmc-visible-columns.md) structure that contains the visible columns data.

## Parameters

<dl> <dt>

*lpDataObject* \[in\]
</dt> <dd>

A pointer to the data object of the currently selected scope item.

</dd> <dt>

*arg* 
</dt> <dd>

Zero.

</dd> <dt>

*param* \[in\]
</dt> <dd>

A pointer to an [**MMC\_VISIBLE\_COLUMNS**](mmc-visible-columns.md) structure that contains the list of visible columns.

</dd> </dl>

## Return value

<dl> <dt>

**S\_OK**
</dt> <dd>

The snap-in accepts user changes to the visible/hidden status of columns in the list view, and MMC will apply these changes by updating the column configuration data of the affected column set.

</dd> <dt>

**S\_FALSE**
</dt> <dd>

The snap-in does not handle the notification. MMC then performs a default operation for the notification, which is to apply the changes by updating the column configuration data.

</dd> <dt>

**E\_UNEXPECTED**
</dt> <dd>

The snap-in rejects the user changes, and MMC will not apply these changes. Be aware that the snap-in is responsible for informing the user why it is refusing the user changes, for example, by means of a message box.

</dd> </dl>

## Remarks

MMC only updates and persists new column configuration data after the snap-in returns **S\_OK** in its **MMCN\_COLUMNS\_CHANGED** notification handler. Consequently, if the snap-in queries for persisted column configuration data while handling the notification (before returning **S\_OK**), it will retrieve currently persisted data. This data will not reflect the user changes that resulted in the **MMCN\_COLUMNS\_CHANGED** notification message to the snap-in.

The **MMCN\_COLUMNS\_CHANGED** notification is particularly useful in situations in which there is a concern about the performance impact of populating data in columns that aren't being displayed. A snap-in can choose to update only visible columns and can use information from **MMCN\_COLUMNS\_CHANGED** to do so.

Be aware that the **MMCN\_COLUMNS\_CHANGED** notification is not generated for column width changes or sorted column and sort direction changes made by the user or by the snap-in (using the [**IColumnData::SetColumnConfigData**](icolumndata-setcolumnconfigdata.md) and [**IColumnData::SetColumnSortData**](icolumndata-setcolumnsortdata.md) methods).

Also, the **MMCN\_COLUMNS\_CHANGED** notification is not generated for any changes made by the snap-in using the [**IHeaderCtrl2::SetColumnWidth**](iheaderctrl2-setcolumnwidth.md), [**IHeaderCtrl2::InsertColumn**](iheaderctrl2-insertcolumn.md), and [**IHeaderCtrl2::DeleteColumn**](iheaderctrl2-deletecolumn.md) methods.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**IColumnData**](icolumndata.md)
</dt> <dt>

[Using Column Persistence](using-column-persistence.md)
</dt> <dt>

[IHeaderCtrl2 and Column Persistence](iheaderctrl2-and-column-persistence.md)
</dt> </dl>

 

 





