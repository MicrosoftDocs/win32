---
title: Nodes Item method
description: The Item method returns the Node object at a specified index.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 72ca0815-2a62-4ec6-b178-3ed4b8ad834e
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Item method MMC
- Item method MMC , Nodes object
- Nodes object MMC , Item method
- Item method MMC , Nodes interface
- Nodes interface MMC , Item method
topic_type:
- apiref
api_name:
- Nodes.Item
- Nodes.Item
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Nodes::Item method

The **Item** method returns the [**Node**](node-object.md) object at a specified index.

## Syntax


```VB
Nodes.Item( _
  ByVal Index As Long _
) As Node
```



## Parameters

<dl> <dt>

*Index* 
</dt> <dd>

The index of the item being retrieved. The index is 1-based.

</dd> </dl>

## Examples


```VB
' Retrieve the third Node in the Nodes collection.
Dim objNode1 As MMC20.Node
Set objNode1 = objNodes.Item(3)
 
' Use the Node object.
' This code will display the Node's Name property.
MsgBox (objNode1.Name)
 
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
| IID<br/>                      | IID\_Nodes is defined as 313B01DF-B22F-4D42-B1B8-483CDCF51D35<br/>              |



## See also

<dl> <dt>

[**Node object**](node-object.md)
</dt> <dt>

[**Nodes.Count**](nodes-count.md)
</dt> </dl>

 

 





