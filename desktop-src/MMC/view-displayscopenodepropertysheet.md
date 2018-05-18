---
title: View DisplayScopeNodePropertySheet method
description: The DisplayScopeNodePropertySheet method displays the property sheet for the specified scope node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b0cb43f6-0cc2-4770-a33b-925dc0c0c61e'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["DisplayScopeNodePropertySheet method MMC", "DisplayScopeNodePropertySheet method MMC , View object", "View object MMC , DisplayScopeNodePropertySheet method", "DisplayScopeNodePropertySheet method MMC , View interface", "View interface MMC , DisplayScopeNodePropertySheet method"]
topic_type:
- apiref
api_name:
- View.DisplayScopeNodePropertySheet
- View.DisplayScopeNodePropertySheet
api_location:
- Mmc.exe
api_type:
- COM
---

# View::DisplayScopeNodePropertySheet method

The **DisplayScopeNodePropertySheet** method displays the property sheet for the specified scope node.

## Syntax


```VB
View.DisplayScopeNodePropertySheet( _
  ByVal ScopeNode As Variant _
)
```



## Parameters

<dl> <dt>

*ScopeNode* 
</dt> <dd>

Optional. A value that specifies the node whose property sheet is displayed; if this parameter is not specified, the active scope node is used.

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

[**View.DisplaySelectionPropertySheet**](view-displayselectionpropertysheet.md)
</dt> </dl>

 

 





