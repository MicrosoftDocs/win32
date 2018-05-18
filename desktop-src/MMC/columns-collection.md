---
title: Columns Collection object
description: The Columns object is a collection of Column objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '14e3acb5-56ee-4203-aa70-0e7ffd5957ce'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["Columns Collection object MMC", "Columns Collection object MMC , described"]
topic_type:
- apiref
api_name:
- Columns Collection
api_location:
- MmcNdMgr.dll
api_type:
- COM
---

# Columns Collection object

The **Columns** object is a collection of [**Column**](column-object.md) objects.

## Members

The **Columns Collection** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Columns Collection** object has these methods.



| Method                       | Description                                                                           |
|:-----------------------------|:--------------------------------------------------------------------------------------|
| [**Item**](columns-item.md) | Retrieves the [**Column**](column-object.md) object at a specified index.<br/> |



 

### Properties

The **Columns Collection** object has these properties.



| Property                                  | Description                                                                     |
|:------------------------------------------|:--------------------------------------------------------------------------------|
| [**Count**](columns-count.md)<br/> | Number of [**Column**](column-object.md) objects in the collection.<br/> |



 

## Examples

The **Columns** collection supports the "For Each" enumeration syntax, as shown in the following example.


```VB
Dim objCol As MMC20.Column
' objCols is a Columns collection.
For Each objCol In objCols
    ' Use the Column object.
    MsgBox (objCol.Name)
Next
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl> |
| IID<br/>                      | IID\_Columns is defined as 383D4D97-FC44-478B-B139-6323DC48611C<br/>              |



## See also

<dl> <dt>

[**View.Columns Property**](view-columns.md)
</dt> </dl>

 

 





