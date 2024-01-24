---
description: The Icon Type of semantic type is one of the Key Format Types. This type consists of a key into the Icon table provided by the user.
ms.assetid: 8e155846-cc29-43f4-b1f7-9880320edbec
title: Icon Type
ms.topic: article
ms.date: 05/31/2018
---

# Icon Type

The Icon Type of [semantic type](semantic-types.md) is one of the [Key Format Types](key-format-types.md). This type consists of a key into the [Icon table](icon-table.md) provided by the user.

The merge tool must substitute a valid Windows Installer [Identifier](identifier.md) for items of this type. Mergemod.dll does not enforce this restriction and it is up to the merge tool to ensure that the user provides a valid key into the Icon table.

Null is a valid value for this type unless the msmConfigItemNonNullable has been included in the Attributes field of the [ModuleConfiguration table](moduleconfiguration-table.md).

The Binary type may be used with the following kinds of ContextData.

**ShortcutIcon ContextData**

A configurable merge module may use this type to enable the user to provide a foreign key to a row in the [Icon Table](icon-table.md) that contains an image suitable for use as a shortcut icon. To specify a configurable item of this type, module authors should enter the name of the configurable item into the Name column, enter "1" into the Format column, enter "Icon" into the Type column, and enter "ShorcutIcon" into the ContextData column of the ModuleConfiguration table. This type is not appropriate for use in a user interface table. To modify a key to the Icon table in these tables see Icon ContextData under [Binary Type](binary-type.md).

 

 



