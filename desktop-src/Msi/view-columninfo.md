---
description: The ColumnInfo property of the View object returns a Record object containing the requested information about each column in the result set.
ms.assetid: 8cfa504c-a6f1-443e-9b3a-b230c4c39b64
title: View.ColumnInfo property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- View.ColumnInfo
api_type: 
- COM
api_location: 
- Msi.dll
---

# View.ColumnInfo property

The **ColumnInfo** property of the [**View**](view-object.md) object returns a [**Record**](record-object.md) object containing the requested information about each column in the result set. Either the column names or the column definitions may be requested. Constants supplied in the Select list do not have names.

This property is read-only.

## Syntax


```JScript
propVal = View.ColumnInfo
```



## Property value

Required information needed for each column.



| Parameter name                                                                                                                                                                                                                                                          | Meaning                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <span id="msiColumnInfoNames"></span><span id="msicolumninfonames"></span><span id="MSICOLUMNINFONAMES"></span><dl> <dt>**msiColumnInfoNames**</dt> <dt>0</dt> </dl> | Returns the names of all nonconstant columns in result set.<br/> |
| <span id="msiColumnInfoTypes"></span><span id="msicolumninfotypes"></span><span id="MSICOLUMNINFOTYPES"></span><dl> <dt>**msiColumnInfoTypes**</dt> <dt>1</dt> </dl> | Returns the types of all nonconstant columns in result set.<br/> |



 

## Remarks

The column descriptions returned by the **ColumnInfo** property are in the format described in [Column Definition Format](column-definition-format.md). Each column is described by a string in the corresponding record field. The definition string consists of a single letter representing the data type followed by the width of the column (in characters when applicable, or else bytes). A width of zero designates an unbounded width (long text fields and streams). An uppercase letter indicates that Null values are allowed in the column.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_IView is defined as 000C109C-0000-0000-C000-000000000046<br/>                                                                                                                                                                                |



 

 




