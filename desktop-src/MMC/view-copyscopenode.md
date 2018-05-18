---
title: View CopyScopeNode method
description: The CopyScopeNode method copies the specified item's data object to the clipboard.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '997f48fb-5b8f-43e3-8451-c1c1f80ba3b3'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["CopyScopeNode method MMC", "CopyScopeNode method MMC , View object", "View object MMC , CopyScopeNode method", "CopyScopeNode method MMC , View interface", "View interface MMC , CopyScopeNode method"]
topic_type:
- apiref
api_name:
- View.CopyScopeNode
- View.CopyScopeNode
api_location:
- Mmc.exe
api_type:
- COM
---

# View::CopyScopeNode method

The **CopyScopeNode** method copies the specified item's data object to the clipboard.

## Syntax


```VB
View.CopyScopeNode( _
  ByVal ScopeNode As Variant _
)
```



## Parameters

<dl> <dt>

*ScopeNode* 
</dt> <dd>

Optional. A value that specifies the node to be copied; if this parameter is not specified, the active scope node is used.

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

[**View.CopySelection**](view-copyselection.md)
</dt> </dl>

 

 





