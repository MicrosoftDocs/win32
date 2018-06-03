---
title: Node IsScopeNode method
description: The IsScopeNode method returns whether the node is a scope node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1c01c520-b4c8-4109-92b4-2e1595259f3c
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- IsScopeNode method MMC
- IsScopeNode method MMC , Node object
- Node object MMC , IsScopeNode method
- IsScopeNode method MMC , Node interface
- Node interface MMC , IsScopeNode method
topic_type:
- apiref
api_name:
- Node.IsScopeNode
- Node.IsScopeNode
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Node::IsScopeNode method

The **IsScopeNode** method returns whether the node is a scope node.

## Syntax


```VB
Node.IsScopeNode() As Long
```



## Parameters

This method has no parameters.

## Remarks

Nodes that appear in the scope tree are scope nodes. Be aware that the child of a scope node may also be a scope node. If the child of a scope node appears in both the scope tree and the result view, then calling the **IsScopeNode** method using the child's [**Node object**](node-object.md) will return 1.

## Examples


```VB
' Determine if the node is a scope node.
Dim lScopeNode As Long
lScopeNode = objNode.IsScopeNode()
If (1 = lScopeNode) Then
    MsgBox ("Node is a ScopeNode")
Else
    MsgBox ("Node is not a ScopeNode")
End If
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_Node is defined as F81ED800-7839-4447-945D-8E15DA59CA55<br/>               |



 

 





