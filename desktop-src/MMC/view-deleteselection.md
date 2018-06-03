---
title: View DeleteSelection method
description: The DeleteSelection method executes the Delete command for the selected items. If the context menu does not support Delete, then this method will not perform any operation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 850516ae-4450-4773-8662-1e1bda805a30
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- DeleteSelection method MMC
- DeleteSelection method MMC , View object
- View object MMC , DeleteSelection method
- DeleteSelection method MMC , View interface
- View interface MMC , DeleteSelection method
topic_type:
- apiref
api_name:
- View.DeleteSelection
- View.DeleteSelection
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# View::DeleteSelection method

The **DeleteSelection** method executes the **Delete** command for the selected items. If the context menu does not support **Delete**, then this method will not perform any operation.

## Syntax


```VB
View.DeleteSelection()
```



## Parameters

This method has no parameters.

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

[**View.DeleteScopeNode**](view-deletescopenode.md)
</dt> </dl>

 

 





