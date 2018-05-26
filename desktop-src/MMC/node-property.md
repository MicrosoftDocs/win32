---
title: Node Property property
description: The Property property returns the node property value for a given property name. The property name and value are defined by the snap-in that owns the node. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: edb52d1b-e422-4c94-9462-7dca2f15b231
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Property property MMC
- Property property MMC , Node object
- Node object MMC , Property property
- Property property MMC , Node interface
- Node interface MMC , Property property
topic_type:
- apiref
api_name:
- Node.Property
- Node.Property
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Node::Property property

The **Property** property returns the node property value for a given property name. The property name and value are defined by the snap-in that owns the node. This property is read-only.

## Syntax


```VB
Property Property( _
  ByVal PropertyName As String _
) As Property
```



## Property value

The property value corresponding to the property specified by *PropertyName*.

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

[**INodeProperties**](/windows/win32/Mmc/nn-mmc-inodeproperties?branch=master)
</dt> </dl>

 

 





