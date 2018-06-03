---
title: Column SetAsSortColumn method
description: The SetAsSortColumn method specifies the sort order for the column.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dbbf6c9c-ba58-4588-b972-7d9b2029ee91
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- SetAsSortColumn method MMC
- SetAsSortColumn method MMC , Column object
- Column object MMC , SetAsSortColumn method
- SetAsSortColumn method MMC , Column interface
- Column interface MMC , SetAsSortColumn method
topic_type:
- apiref
api_name:
- Column.SetAsSortColumn
- Column.SetAsSortColumn
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Column::SetAsSortColumn method

The **SetAsSortColumn** method specifies the sort order for the column.

## Syntax


```VB
Column.SetAsSortColumn( _
  ByVal SortOrder As ColumnSortOrder _
)
```



## Parameters

<dl> <dt>

*SortOrder* 
</dt> <dd>

The new sort order being assigned for the column. This can be one of the following [**ColumnSortOrder**](/windows/desktop/api/MmcObj/ne-mmcobj-columnsortorder) values.

<dt>

<span id="SortOrder_Ascending"></span><span id="sortorder_ascending"></span><span id="SORTORDER_ASCENDING"></span>

<span id="SortOrder_Ascending"></span><span id="sortorder_ascending"></span><span id="SORTORDER_ASCENDING"></span>**SortOrder\_Ascending**


</dt> <dd>

The column is sorted in ascending order.

</dd> <dt>

<span id="SortOrder_Descending"></span><span id="sortorder_descending"></span><span id="SORTORDER_DESCENDING"></span>

<span id="SortOrder_Descending"></span><span id="sortorder_descending"></span><span id="SORTORDER_DESCENDING"></span>**SortOrder\_Descending**


</dt> <dd>

The column is sorted in descending order.

</dd> </dl> </dd> </dl>

## Return value

This method does not return a value.

## Examples


```VB
' Specify the column as the sort column.
' Make the sort descending.
objCol.SetAsSortColumn (SortOrder_Descending)
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_Column is defined as FD1C5F63-2B16-4D06-9AB3-F45350B940AB<br/>             |



## See also

<dl> <dt>

[**ColumnSortOrder**](/windows/desktop/api/MmcObj/ne-mmcobj-columnsortorder)
</dt> </dl>

 

 





