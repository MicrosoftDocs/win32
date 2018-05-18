---
title: View Deselect method
description: The Deselect method removes the specified node from the current selection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c15795f3-6c9c-43df-8fd4-534d22c4763a'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["Deselect method MMC", "Deselect method MMC , View object", "View object MMC , Deselect method", "Deselect method MMC , View interface", "View interface MMC , Deselect method"]
topic_type:
- apiref
api_name:
- View.Deselect
- View.Deselect
api_location:
- Mmc.exe
api_type:
- COM
---

# View::Deselect method

The **Deselect** method removes the specified node from the current selection.

## Syntax


```VB
View.Deselect( _
  ByVal Node As Node _
)
```



## Parameters

<dl> <dt>

*Node* 
</dt> <dd>

A value that specifies the node, as a [**Node**](node-object.md) object, to be removed from the current selection.

</dd> </dl>

## Return value

This method does not return a value.

## Examples


```VB
' Deselect the node.
objView.Deselect objNode
```



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

[**View.Select**](view-select.md)
</dt> <dt>

[**View.SelectAll**](view-selectall.md)
</dt> <dt>

[**View.Selection**](view-selection.md)
</dt> </dl>

 

 





