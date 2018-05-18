---
title: View ScopeNodeContextMenu property
description: The ScopeNodeContextMenu property returns the context menu for the specified node. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3b511af6-9265-467e-b075-8e584196f78c'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["ScopeNodeContextMenu property MMC", "ScopeNodeContextMenu property MMC , View object", "View object MMC , ScopeNodeContextMenu property", "ScopeNodeContextMenu property MMC , View interface", "View interface MMC , ScopeNodeContextMenu property"]
topic_type:
- apiref
api_name:
- View.ScopeNodeContextMenu
- View.ScopeNodeContextMenu
api_location:
- Mmc.exe
api_type:
- COM
---

# View::ScopeNodeContextMenu property

The **ScopeNodeContextMenu** property returns the context menu for the specified node. This property is read-only.

## Syntax


```VB
Property ScopeNodeContextMenu( _
  [ ByVal ScopeNode As Variant ] _
) As ContextMenu
```



## Property value

The [**ContextMenu**](contextmenu-object.md) object for the view's specified node.

## Examples


```VB
' This code retrieves the context menu for
' the Document's RootNode.
Dim var1 As Variant
Set var1 = objDoc.RootNode
 
Dim objCtxMenu As MMC20.ContextMenu
Set objCtxMenu = objView.ScopeNodeContextMenu(var1)
 
' Use the ContextMenu. This code displays
' the ContextMenu.Count property.
MsgBox ("objCtxMenu.Count = " & objCtxMenu.Count)
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

[**View.SelectionContextMenu**](view-selectioncontextmenu.md)
</dt> <dt>

[**ContextMenu object**](contextmenu-object.md)
</dt> <dt>

[**Document.ScopeNamespace**](document-scopenamespace.md)
</dt> </dl>

 

 





