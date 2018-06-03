---
title: Column IsSortColumn method
description: The IsSortColumn method returns whether the column is the sort column.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b2c6bf3f-fa2b-4c4d-8cb3-35937a6777af
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- IsSortColumn method MMC
- IsSortColumn method MMC , Column object
- Column object MMC , IsSortColumn method
- IsSortColumn method MMC , Column interface
- Column interface MMC , IsSortColumn method
topic_type:
- apiref
api_name:
- Column.IsSortColumn
- Column.IsSortColumn
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Column::IsSortColumn method

The **IsSortColumn** method returns whether the column is the sort column.

## Syntax


```VB
Column.IsSortColumn() As Long
```



## Parameters

This method has no parameters.

## Examples


```VB
' Determine if the column is the sort column.
Dim nSort As Long
nSort = objCol.IsSortColumn
If (1 = nSort) Then
    MsgBox ("This is the sort column.")
Else
    MsgBox ("This is not the sort column.")
End If
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

[**Column.SetAsSortColumn**](column-setassortcolumn.md)
</dt> </dl>

 

 





