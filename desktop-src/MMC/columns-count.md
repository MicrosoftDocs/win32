---
title: Columns Count property
description: The Count property returns the number of Column objects that are in the Columns collection. Hidden columns are included in the collection's count. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ab0c7902-6dc0-4055-b92e-24b46d83e8f6'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["Count property MMC", "Count property MMC , Columns object", "Columns object MMC , Count property", "Count property MMC , Columns interface", "Columns interface MMC , Count property"]
topic_type:
- apiref
api_name:
- Columns.Count
- Columns.Count
api_location:
- Mmc.exe
api_type:
- COM
---

# Columns::Count property

The **Count** property returns the number of [**Column**](column-object.md) objects that are in the [**Columns**](columns-collection.md) collection. Hidden columns are included in the collection's count. This property is read-only.

## Syntax


```VB
Property Count As Long
```



## Property value

The number of [**Column**](column-object.md) objects contained in this collection.

## Examples


```VB
' Determine the number of columns in the view.
Dim nCols As Long
nCols = objCols.Count
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_Columns is defined as 383D4D97-FC44-478B-B139-6323DC48611C<br/>            |



## See also

<dl> <dt>

[**Columns.Item**](columns-item.md)
</dt> </dl>

 

 





