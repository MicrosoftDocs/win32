---
title: Node Nodetype property
description: The Nodetype property returns the node type's GUID. The node type GUID identifies the type of node. By using the node type GUID, snap-ins and automation object model applications can recognize particular nodes. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8a12e4fe-b640-43e7-bf3f-eb21cb458025
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Nodetype property MMC
- Nodetype property MMC , Node object
- Node object MMC , Nodetype property
- Nodetype property MMC , Node interface
- Node interface MMC , Nodetype property
topic_type:
- apiref
api_name:
- Node.Nodetype
- Node.Nodetype
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Node::Nodetype property

The **Nodetype** property returns the node type's GUID. The node type GUID identifies the type of node. By using the node type GUID, snap-ins and automation object model applications can recognize particular nodes. This property is read-only.

## Syntax


```VB
Property Nodetype As String
```



## Property value

The node's type GUID, as a string.

## Examples


```VB
' Retrieve the Node type.
Dim strNodeType As String
strNodeType = objNode.Nodetype
MsgBox ("NodeType: " & strNodeType)
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



## See also

<dl> <dt>

[**Node.Name**](node-name.md)
</dt> </dl>

 

 





