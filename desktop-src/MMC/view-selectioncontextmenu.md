---
title: View SelectionContextMenu property
description: The SelectionContextMenu property retrieves menu items for the List items in the result pane. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 62390cdb-c9a4-4a65-94b1-178039ba0d69
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- SelectionContextMenu property MMC
- SelectionContextMenu property MMC , View object
- View object MMC , SelectionContextMenu property
- SelectionContextMenu property MMC , View interface
- View interface MMC , SelectionContextMenu property
topic_type:
- apiref
api_name:
- View.SelectionContextMenu
- View.SelectionContextMenu
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# View::SelectionContextMenu property

The **SelectionContextMenu** property retrieves menu items for the List items in the result pane. This property is read-only.

## Syntax


```VB
Property SelectionContextMenu As ContextMenu
```



## Property value

The [**ContextMenu object**](contextmenu-object.md) for the view's selected node.

## Examples


```VB
' Retrieve the SelectionContextMenu.
Dim objSelCtxMenu As MMC20.ContextMenu
Set objSelCtxMenu = objView.SelectionContextMenu
 
' Use the ContextMenu.
' This code displays the count of items in the ContextMenu.
MsgBox (objSelCtxMenu.Count)
' Use objSelCtxMenu for other processing.
' ...
 
' Free the object when done.
Set objSelCtxMenu = Nothing
```



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

[**View.ScopeNodeContextMenu**](view-scopenodecontextmenu.md)
</dt> <dt>

[**ContextMenu object**](contextmenu-object.md)
</dt> </dl>

 

 





