---
title: View DeleteScopeNode method
description: The DeleteScopeNode method executes the Delete command for the specified node. If the context menu does not support Delete, then this method will not perform any operation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f7678d3a-4638-4b4d-8255-d9517217cd89
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- DeleteScopeNode method MMC
- DeleteScopeNode method MMC , View object
- View object MMC , DeleteScopeNode method
- DeleteScopeNode method MMC , View interface
- View interface MMC , DeleteScopeNode method
topic_type:
- apiref
api_name:
- View.DeleteScopeNode
- View.DeleteScopeNode
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# View::DeleteScopeNode method

The **DeleteScopeNode** method executes the **Delete** command for the specified node. If the context menu does not support **Delete**, then this method will not perform any operation.

## Syntax


```VB
View.DeleteScopeNode( _
  ByVal ScopeNode As Variant _
)
```



## Parameters

<dl> <dt>

*ScopeNode* 
</dt> <dd>

Optional. A value that specifies the node to be deleted; if this parameter is not specified, the active scope node is used.

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

[**View.DeleteSelection**](view-deleteselection.md)
</dt> </dl>

 

 





