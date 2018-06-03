---
title: View RefreshScopeNode method
description: The RefreshScopeNode method refreshes the specified node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1b6b2ad5-cb0a-4128-8982-d4114ebb949f
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- RefreshScopeNode method MMC
- RefreshScopeNode method MMC , View object
- View object MMC , RefreshScopeNode method
- RefreshScopeNode method MMC , View interface
- View interface MMC , RefreshScopeNode method
topic_type:
- apiref
api_name:
- View.RefreshScopeNode
- View.RefreshScopeNode
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# View::RefreshScopeNode method

The **RefreshScopeNode** method refreshes the specified node.

## Syntax


```VB
View.RefreshScopeNode( _
  ByVal ScopeNode As Variant _
)
```



## Parameters

<dl> <dt>

*ScopeNode* 
</dt> <dd>

Optional. A value that specifies the node to be refreshed; if this parameter is not specified, the active scope node is used.

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

[**View.RefreshSelection**](view-refreshselection.md)
</dt> </dl>

 

 





