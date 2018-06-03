---
title: Node Name property
description: The Name property returns the display name of the node. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3e93c163-01bd-4cd7-90f5-45a77b510ff4
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Name property MMC
- Name property MMC , Node object
- Node object MMC , Name property
- Name property MMC , Node interface
- Node interface MMC , Name property
topic_type:
- apiref
api_name:
- Node.Name
- Node.Name
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Node::Name property

The **Name** property returns the display name of the node. This property is read-only.

## Syntax


```VB
Property Name As String
```



## Property value

The display name of the node.

## Examples


```VB
' Retrieve the Node name.
Dim strName As String
strName = objNode.Name
MsgBox ("Name: " & strName)
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

[**Node.Nodetype**](node-nodetype.md)
</dt> </dl>

 

 





