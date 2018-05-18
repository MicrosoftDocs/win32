---
title: View ExecuteScopeNodeMenuItem method
description: The ExecuteScopeNodeMenuItem method executes a menu command for the specified node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1b2fe31a-1a04-45a7-afff-18290c697cb9'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["ExecuteScopeNodeMenuItem method MMC", "ExecuteScopeNodeMenuItem method MMC , View object", "View object MMC , ExecuteScopeNodeMenuItem method", "ExecuteScopeNodeMenuItem method MMC , View interface", "View interface MMC , ExecuteScopeNodeMenuItem method"]
topic_type:
- apiref
api_name:
- View.ExecuteScopeNodeMenuItem
- View.ExecuteScopeNodeMenuItem
api_location:
- Mmc.exe
api_type:
- COM
---

# View::ExecuteScopeNodeMenuItem method

The **ExecuteScopeNodeMenuItem** method executes a menu command for the specified node.

## Syntax


```VB
View.ExecuteScopeNodeMenuItem( _
  ByVal MenuItemPath As String, _
  ByVal ScopeNode As Variant _
)
```



## Parameters

<dl> <dt>

*MenuItemPath* 
</dt> <dd>

The menu command path for the command to be executed.

</dd> <dt>

*ScopeNode* 
</dt> <dd>

Optional. A value that specifies the node whose menu command is executed; if this parameter is not specified, the active scope node is used.

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

[**View.ExecuteSelectionMenuItem**](view-executeselectionmenuitem.md)
</dt> </dl>

 

 





