---
description: The Dialog Type of semantic type is one of the Key Format Types. This type consists of a foreign key into the Dialog table provided by the user.
ms.assetid: 3656684a-de95-45e1-9c78-5c1cc8ca879a
title: Dialog Type
ms.topic: article
ms.date: 05/31/2018
---

# Dialog Type

The Dialog Type of [semantic type](semantic-types.md) is one of the [Key Format Types](key-format-types.md). This type consists of a foreign key into the [Dialog table](dialog-table.md) provided by the user.

The merge tool must substitute a valid Windows Installer [Identifier](identifier.md) for items of this type. Mergemod.dll does not enforce this restriction and it is up to the merge tool to ensure that the user provides a valid key into the Dialog table.

Null is a valid value for this type unless the msmConfigItemNonNullable has been included in the Attributes field of the [ModuleConfiguration table](moduleconfiguration-table.md).

The Dialog type may be used with the following kinds of ContextData.

**DialogNext ContextData**

A configurable merge module may use this type to enable the user to provide a foreign key into the Dialog Table. To specify a configurable item of this type, module authors should enter the name of the configurable item into the Name column, enter "1" into the Format column, enter "Dialog" into the Type column, and enter "DialogNext" into the ContextData column of the [ModuleConfiguration table](moduleconfiguration-table.md).

**DialogPrev ContextData**

A configurable merge module may use this type to enable the user to provide a foreign key into the Dialog Table. To specify a configurable item of this type, module authors should enter the name of the configurable item into the Name column, enter "1" into the Format column, enter "Dialog" into the Type column, and enter "DialogPrev" into the ContextData column of the ModuleConfiguration table.

 

 



