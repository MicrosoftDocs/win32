---
title: View RenameSelectedItem method
description: The RenameSelectedItem method renames the selected item.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '65788a9f-7d56-4114-8cb7-479f3899d418'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["RenameSelectedItem method MMC", "RenameSelectedItem method MMC , View object", "View object MMC , RenameSelectedItem method", "RenameSelectedItem method MMC , View interface", "View interface MMC , RenameSelectedItem method"]
topic_type:
- apiref
api_name:
- View.RenameSelectedItem
- View.RenameSelectedItem
api_location:
- Mmc.exe
api_type:
- COM
---

# View::RenameSelectedItem method

The **RenameSelectedItem** method renames the selected item.

## Syntax


```VB
View.RenameSelectedItem( _
  ByVal NewName As String _
)
```



## Parameters

<dl> <dt>

*NewName* 
</dt> <dd>

The new name for the item.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_View is defined as 6EFC2DA2-B38C-457E-9ABB-ED2D189B8C38<br/>               |



## See also

<dl> <dt>

[**View.RenameScopeNode**](view-renamescopenode.md)
</dt> </dl>

 

 





