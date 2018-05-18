---
title: View SnapinScopeObject method
description: The SnapinScopeObject method returns the automation interface supplied by the snap-in for the specified scope node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '340ab6d0-e674-438a-9c84-87dcb274ae6a'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["SnapinScopeObject method MMC", "SnapinScopeObject method MMC , View object", "View object MMC , SnapinScopeObject method", "SnapinScopeObject method MMC , View interface", "View interface MMC , SnapinScopeObject method"]
topic_type:
- apiref
api_name:
- View.SnapinScopeObject
- View.SnapinScopeObject
api_location:
- Mmc.exe
api_type:
- COM
---

# View::SnapinScopeObject method

The **SnapinScopeObject** method returns the automation interface supplied by the snap-in for the specified scope node.

## Syntax


```VB
View.SnapinScopeObject( _
  ByVal ScopeNode As Variant _
) As Object
```



## Parameters

<dl> <dt>

*ScopeNode* 
</dt> <dd>

Optional. Scope node that contains the object. If this parameter is not specified, then the object will be retrieved from the active scope node.

</dd> </dl>

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

[**View.SnapinSelectionObject**](view-snapinselectionobject.md)
</dt> </dl>

 

 





