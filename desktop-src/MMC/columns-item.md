---
title: Columns Item method
description: The Item method returns the Column object at a specified index.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d5e69022-dad6-426d-8d98-5b6039088687
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Item method MMC
- Item method MMC , Columns object
- Columns object MMC , Item method
- Item method MMC , Columns interface
- Columns interface MMC , Item method
topic_type:
- apiref
api_name:
- Columns.Item
- Columns.Item
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Columns::Item method

The **Item** method returns the [**Column**](column-object.md) object at a specified index.

## Syntax


```VB
Columns.Item( _
  ByVal Index As Long _
) As Column
```



## Parameters

<dl> <dt>

*Index* 
</dt> <dd>

The index of the column being retrieved. The index is 1-based.

</dd> </dl>

## Examples


```VB
' This example code writes Column information to a file.
'
' Obtain a Columns collection.
' objView is the active view of the Document object.
Dim objCols As MMC20.Columns
Set objCols = objView.Columns
 
' Determine the number of columns in the view.
Dim nCols As Long
nCols = objCols.Count
' Open an output file for the column information.
Open "D:\columns.txt" For Output As 1
' Write a header for the column information.
Print #1, "Display Position, Name, Hidden, IsSortColumn, Width"
' Declare variables for iterating the Columns collection.
Dim i As Long
Dim objCol As MMC20.Column
' Iterate the Columns collection.
For i = 1 To nCols
    ' Obtain the Column object by index.
    Set objCol = objCols.Item(i)
    'Write the column information to a file.
    Print #1, objCol.DisplayPosition, _
              objCol.Name, _
              objCol.Hidden, _
              objCol.IsSortColumn, _
              objCol.Width
    ' Free the Column object.
    Set objCol = Nothing
Next i
' Close the output file.
Close 1
 
' Free the Columns collection.
Set objCols = Nothing
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_Columns is defined as 383D4D97-FC44-478B-B139-6323DC48611C<br/>            |



## See also

<dl> <dt>

[**Columns.Count**](columns-count.md)
</dt> </dl>

 

 





