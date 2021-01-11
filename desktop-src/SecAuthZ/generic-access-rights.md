---
description: Securable objects use an access mask format in which the four high-order bits specify generic access rights.
ms.assetid: e18cede9-9bf7-4866-850b-5d7fa43a5b0f
title: Generic Access Rights
ms.topic: article
ms.date: 05/31/2018
---

# Generic Access Rights

Securable objects use an [access mask format](access-mask-format.md) in which the four high-order bits specify generic access rights. Each type of securable object maps these bits to a set of its standard and object-specific access rights. For example, a Windows file object maps the GENERIC\_READ bit to the READ\_CONTROL and SYNCHRONIZE standard access rights and to the FILE\_READ\_DATA, FILE\_READ\_EA, and FILE\_READ\_ATTRIBUTES object-specific access rights. Other types of objects map the GENERIC\_READ bit to whatever set of access rights is appropriate for that type of object.

You can use generic access rights to specify the type of access you need when you are opening a handle to an object. This is typically simpler than specifying all the corresponding standard and specific rights.

The following table shows the constants defined for the generic access rights.



| Constant         | Generic meaning            |
|------------------|----------------------------|
| GENERIC\_ALL     | All possible access rights |
| GENERIC\_EXECUTE | Execute access             |
| GENERIC\_READ    | Read access                |
| GENERIC\_WRITE   | Write access               |



 

Applications that define private securable objects can also use the generic access rights.

 

 



