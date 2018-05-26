---
title: View Select method
description: The Select method selects the specified node in the result pane.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 60ac7181-8cb6-4779-b27c-261faa2c2cc5
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Select method MMC
- Select method MMC , View object
- View object MMC , Select method
- Select method MMC , View interface
- View interface MMC , Select method
topic_type:
- apiref
api_name:
- View.Select
- View.Select
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# View::Select method

The **Select** method selects the specified node in the result pane.

## Syntax


```VB
View.Select( _
  ByVal Node As Node _
)
```



## Parameters

<dl> <dt>

*Node* 
</dt> <dd>

The node, as a [**Node**](node-object.md) object, to be selected.

</dd> </dl>

## Return value

This method does not return a value.

## Examples


```VB
' This code selects the first node in the view.
' Retrieve the first node in the view.
Dim objNode1 As MMC20.Node
Set objNode1 = objView.ListItems(1)
 
' Select the node.
objView.Select objNode1
 
' Take action on the selection.
' ...
 
' Free the Node object when done.
Set objNode1 = Nothing
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

[**View.Deselect**](view-deselect.md)
</dt> <dt>

[**View.SelectAll**](view-selectall.md)
</dt> <dt>

[**View.Selection**](view-selection.md)
</dt> </dl>

 

 





