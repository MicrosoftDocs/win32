---
title: View CellContents property
description: The CellContents property returns the contents from a specified cell. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f76a4a1b-bff9-4de7-8eaa-11973843a48b
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- CellContents property MMC
- CellContents property MMC , View object
- View object MMC , CellContents property
- CellContents property MMC , View interface
- View interface MMC , CellContents property
topic_type:
- apiref
api_name:
- View.CellContents
- View.CellContents
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# View::CellContents property

The **CellContents** property returns the contents from a specified cell. This property is read-only.

## Syntax


```VB
Property CellContents( _
  ByVal Node As Node, _
  ByVal Column As Long _
) As String
```



## Property value

Contents of the cell at the specified node and column.

## Examples


```VB
' Retrieve the first node in the list view.
Dim objNode As MMC20.Node
Set objNode = objView.ListItems(1)
 
' Retrieve the contents of the Node's second column.
Dim strContents As String
strContents = objView.CellContents(objNode, 2)
 
' This example displays the contents in a message box.
MsgBox (strContents)
 
' Free the Node object when done.
Set objNode = Nothing
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



 

 





