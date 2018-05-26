---
title: View ExecuteSelectionMenuItem method
description: The ExecuteSelectionMenuItem method executes a specified menu command for the selected item.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4707c94f-f02d-4aa1-b188-0d4f7d0f3fc3
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- ExecuteSelectionMenuItem method MMC
- ExecuteSelectionMenuItem method MMC , View object
- View object MMC , ExecuteSelectionMenuItem method
- ExecuteSelectionMenuItem method MMC , View interface
- View interface MMC , ExecuteSelectionMenuItem method
topic_type:
- apiref
api_name:
- View.ExecuteSelectionMenuItem
- View.ExecuteSelectionMenuItem
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# View::ExecuteSelectionMenuItem method

The **ExecuteSelectionMenuItem** method executes a specified menu command for the selected item.

## Syntax


```VB
View.ExecuteSelectionMenuItem( _
  ByVal MenuItemPath As String _
)
```



## Parameters

<dl> <dt>

*MenuItemPath* 
</dt> <dd>

The menu command path.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_View is defined as 6EFC2DA2-B38C-457E-9ABB-ED2D189B8C38<br/>               |



## See also

<dl> <dt>

[**View.ExecuteScopeNodeMenuItem**](view-executescopenodemenuitem.md)
</dt> </dl>

 

 





