---
title: View ActiveScopeNode property
description: The ActiveScopeNode property sets or returns the scope node that owns the view. This property is read/write.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 43bfb482-d9a5-46cb-98a5-05f0ec2294e0
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- ActiveScopeNode property MMC
- ActiveScopeNode property MMC , View object
- View object MMC , ActiveScopeNode property
- ActiveScopeNode property MMC , View interface
- View interface MMC , ActiveScopeNode property
topic_type:
- apiref
api_name:
- View.ActiveScopeNode
- View.ActiveScopeNode
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# View::ActiveScopeNode property

The **ActiveScopeNode** property sets or returns the scope node that owns the view. This property is read/write.

## Syntax


```VB
Property ActiveScopeNode As Node
```



## Property value

The scope node, as a [**Node object**](node-object.md), that owns the view.

## Examples


```VB
' Retrieve the View's ActiveScopeNode.
Dim objScopeNode As MMC20.Node
Set objScopeNode = objView.ActiveScopeNode
 
' Use the scope node.
' ...
 
' Free the object when done.
Set objScopeNode = Nothing
 
' Set the active scope node.
' objNewNode is a previously assigned Node object.
objView.ActiveScopeNode = objNewNode
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

[**Node object**](node-object.md)
</dt> </dl>

 

 





