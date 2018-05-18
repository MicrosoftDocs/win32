---
title: View ListItems property
description: The ListItems property returns the list's set of nodes. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b71b7713-a63f-4a78-bfdf-80fae0bbcd7b'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["ListItems property MMC", "ListItems property MMC , View object", "View object MMC , ListItems property", "ListItems property MMC , View interface", "View interface MMC , ListItems property"]
topic_type:
- apiref
api_name:
- View.ListItems
- View.ListItems
api_location:
- Mmc.exe
api_type:
- COM
---

# View::ListItems property

The **ListItems** property returns the list's set of nodes. This property is read-only.

## Syntax


```VB
Property ListItems As Nodes
```



## Property value

The set of nodes in the list.

## Examples


```VB
' Retrieve the ListItems property.
Dim objNodes As MMC20.Nodes
Set objNodes = objView.ListItems
 
' Use the ListItems.
' This code displays the count of items in the list.
MsgBox (objNodes.Count)
' Use objNodes for other processing.
' ...
 
' Free the object when done.
Set objNodes = Nothing
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

 

 





