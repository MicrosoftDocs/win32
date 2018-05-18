---
title: Column DisplayPosition property
description: The DisplayPosition property sets or returns the order of the column in the set of columns. The order is 1-based (the first column is at position 1). This property is read/write.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bd2821a8-c2bf-4863-b92f-eab96631a348'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["DisplayPosition property MMC", "DisplayPosition property MMC , Column object", "Column object MMC , DisplayPosition property", "DisplayPosition property MMC , Column interface", "Column interface MMC , DisplayPosition property"]
topic_type:
- apiref
api_name:
- Column.DisplayPosition
- Column.DisplayPosition
api_location:
- Mmc.exe
api_type:
- COM
---

# Column::DisplayPosition property

The **DisplayPosition** property sets or returns the order of the column in the set of columns. The order is 1-based (the first column is at position 1). This property is read/write.

## Syntax


```VB
Property DisplayPosition As Long
```



## Property value

An index of the column in its position among the set of columns.

## Remarks

Setting the **DisplayPosition** property is consistent with a user dragging a column header to another position, or moving a column up or down in the **Add/Remove Columns** dialog box. The first column can be moved to any other position, and any other column can be moved to the first position.

## Examples


```VB
' Retrieve the column's display position.
Dim nPos As Long
nPos = objCol.DisplayPosition
 
' Assign this column to the third position.
objCol.DisplayPosition = 3
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_Column is defined as FD1C5F63-2B16-4D06-9AB3-F45350B940AB<br/>             |



## See also

<dl> <dt>

[**Column.Name**](column-name.md)
</dt> <dt>

[**Column.IsSortColumn**](column-issortcolumn.md)
</dt> </dl>

 

 





