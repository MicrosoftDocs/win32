---
description: Securable objects use an access mask format in which the four high-order bits specify generic access rights.
ms.assetid: e18cede9-9bf7-4866-850b-5d7fa43a5b0f
title: Generic Access Rights
ms.topic: concept-article
ms.date: 02/13/2024
---

# Generic Access Rights

Securable objects use an [access mask format](access-mask-format.md) in which the four high-order bits specify generic access rights. Each type of securable object maps these bits to a set of its standard and object-specific access rights. For example, a Windows file object maps the **GENERIC_READ** bit to the **READ_CONTROL** and **SYNCHRONIZE** standard access rights and to the **FILE_READ_DATA**, **FILE_READ_EA**, and **FILE_READ_ATTRIBUTES** object-specific access rights. Other types of objects map the **GENERIC_READ** bit to whatever set of access rights is appropriate for that type of object.

You can use generic access rights to specify the type of access you need when you're opening a handle to an object. This is typically simpler than specifying all the corresponding standard and specific rights.

The following table shows the constants defined for the generic access rights.

| Constant | Generic meaning |
|--------|--------|
| **GENERIC_ALL**<br/>`0x10000000` | All possible access rights |
| **GENERIC_EXECUTE**<br/>`0x20000000` | Execute access |
| **GENERIC_WRITE**<br/>`0x40000000` | Write access |
| **GENERIC_READ**<br/>`0x80000000` | Read access |

Applications that define private securable objects can also use the generic access rights.
