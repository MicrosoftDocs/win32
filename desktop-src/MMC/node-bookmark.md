---
title: Node Bookmark property
description: The Bookmark property returns a bookmark for the node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2bd01b21-8cc7-44ff-a72f-9023aa9edaea'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["Bookmark property MMC", "Bookmark property MMC , Node object", "Node object MMC , Bookmark property", "Bookmark property MMC , Node interface", "Node interface MMC , Bookmark property"]
topic_type:
- apiref
api_name:
- Node.Bookmark
- Node.Bookmark
api_location:
- Mmc.exe
api_type:
- COM
---

# Node::Bookmark property

The **Bookmark** property returns a bookmark for the node. The bookmark serves as a name of the node, and the bookmark does not change from session to session. The bookmark can be safely persisted and used to navigate to the node at a later time. This property applies to scope nodes only. This property is read-only.

## Syntax


```VB
Property Bookmark As String
```



## Property value

A persistable bookmark for the node.

## Examples


```VB
' Retrieve the Node's Bookmark property.
Dim strBookMark As String
strBookMark = objNode.Bookmark
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_Node is defined as F81ED800-7839-4447-945D-8E15DA59CA55<br/>               |



## See also

<dl> <dt>

[**Node.IsScopeNode**](node-isscopenode.md)
</dt> <dt>

[**View.Memento**](view-memento.md)
</dt> <dt>

[**View.ViewMemento**](view-viewmemento.md)
</dt> </dl>

 

 





