---
title: View IsSelected method
description: The IsSelected method returns whether the specified node is selected.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: afce77e6-ed5b-4151-9965-80ed70af5772
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- IsSelected method MMC
- IsSelected method MMC , View object
- View object MMC , IsSelected method
- IsSelected method MMC , View interface
- View interface MMC , IsSelected method
topic_type:
- apiref
api_name:
- View.IsSelected
- View.IsSelected
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# View::IsSelected method

The **IsSelected** method returns whether the specified node is selected.

## Syntax


```VB
View.IsSelected( _
  ByVal Node As Node _
) As Long
```



## Parameters

<dl> <dt>

*Node* 
</dt> <dd>

The [**Node**](node-object.md) object whose selection state is being queried.

</dd> </dl>

## Examples


```VB
' This code determines if the first node is selected.
' Retrieve the first node.
Dim node1 As MMC20.Node
Set node1 = objView.ListItems(1)
 
' Determine if the node is selected.
Dim nSelected As Long
nSelected = objView.IsSelected(node1)
If (nSelected = 1) Then
    MsgBox ("The first node is selected")
Else
    MsgBox ("The first node is not selected")
End If
 
' Free the Node object when done.
Set node1 = Nothing
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

[**View.Select**](view-select.md)
</dt> <dt>

[**View.SelectAll**](view-selectall.md)
</dt> </dl>

 

 





