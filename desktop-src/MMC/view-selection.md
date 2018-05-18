---
title: View Selection property
description: The Selection property returns the set of selected nodes. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1ec57b07-4b57-4e8a-953a-0810d350f1c6'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["Selection property MMC", "Selection property MMC , View object", "View object MMC , Selection property", "Selection property MMC , View interface", "View interface MMC , Selection property"]
topic_type:
- apiref
api_name:
- View.Selection
- View.Selection
api_location:
- Mmc.exe
api_type:
- COM
---

# View::Selection property

The **Selection** property returns the set of selected nodes. This property is read-only.

## Syntax


```VB
Property Selection As Nodes
```



## Property value

The set of selected items in the form of a [**Nodes collection**](nodes-collection.md).

## Examples


```VB
' Retrieve the Views Selection property.
Dim objSelNodes As MMC20.Nodes
Set objSelNodes = objView.Selection
 
' Use the Selection nodes.
' This code displays the count of items in the Selection.
MsgBox (objSelNodes.Count)
' Use objSelNodes for other processing.
' ...
 
' Free the object when done.
Set objSelNodes = Nothing
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

[**Nodes collection**](nodes-collection.md)
</dt> </dl>

 

 





