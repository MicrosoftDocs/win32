---
title: CdromCollection Object
description: The CdromCollection object provides a way to organize and access a collection of CD or DVD drives.
ms.assetid: 02429ba7-a053-42bf-9ed5-c05e13c964c0
keywords:
- CdromCollection Object Windows Media Player
topic_type:
- apiref
api_name:
- CdromCollection Object
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# CdromCollection Object

The **CdromCollection** object provides a way to organize and access a collection of CD or DVD drives.

The **CdromCollection** object supports the following property.



| Property                           | Description                                                        |
|------------------------------------|--------------------------------------------------------------------|
| [count](cdromcollection-count.md) | Retrieves the number of available CD and DVD drives on the system. |



 

The **CdromCollection** object supports the following methods.



| Method                                                         | Description                                                                               |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [getByDriveSpecifier](cdromcollection-getbydrivespecifier.md) | Retrieves the [Cdrom](cdrom-object.md) object associated with a particular drive letter. |
| [item](cdromcollection-item.md)                               | Retrieves the [Cdrom](cdrom-object.md) object at the given index.                        |



 

The **CdromCollection** object is accessed through the following property.



| Object                      | Property                                      |
|-----------------------------|-----------------------------------------------|
| [Player](player-object.md) | [cdromCollection](player-cdromcollection.md) |



 

## See also

<dl> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




