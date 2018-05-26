---
title: Nodes Count property
description: The Count property returns the number of Node objects that are in the Nodes collection. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4f6a4276-4ba1-4a0d-8c26-d53231d77837
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Count property MMC
- Count property MMC , Nodes object
- Nodes object MMC , Count property
- Count property MMC , Nodes interface
- Nodes interface MMC , Count property
topic_type:
- apiref
api_name:
- Nodes.Count
- Nodes.Count
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Nodes::Count property

The **Count** property returns the number of [**Node**](node-object.md) objects that are in the [**Nodes**](nodes-collection.md) collection. This property is read-only.

## Syntax


```VB
Property Count As Long
```



## Property value

The number of [**Node**](node-object.md) objects contained in this collection.

## Examples


```VB
' Display the count of Node objects.
Dim nCount As Long
nCount = objNodes.Count
MsgBox ("Number of Node objects: " & nCount)
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

[**Nodes.Item**](nodes-item.md)
</dt> </dl>

 

 





