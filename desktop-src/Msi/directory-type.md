---
description: The Directory Type of semantic type is one of the Key Format Types, which consists of a foreign key into the Directory table provided by the user.
ms.assetid: b5a0ed38-1dda-4c33-9429-0cbe87e13aef
title: Directory Type
ms.topic: article
ms.date: 05/31/2018
---

# Directory Type

The Directory Type of [semantic type](semantic-types.md) is one of the [Key Format Types](key-format-types.md), which consists of a foreign key into the [Directory table](directory-table.md) provided by the user.

The merge tool must substitute a valid Windows Installer [Identifier](identifier.md) for items of this type. Mergemod.dll does not enforce this restriction and it is up to the merge tool to ensure that the user provides a valid key into the Directory table.

A configurable item of the Directory type should only modify the destination directory of the installation and not modify the source image. A configurable item of this type should therefore only modify foreign keys to the Directory table and not modify the Directory table directly.

Because the Directory\_ column of the [Component table](component-table.md) is non-nullable, null is an invalid value for a configurable item of this type even if the msmConfigItemNonNullable is not set in the Attributes column.

The Directory type may be used with two kinds of ContextData.

**IsolationDirectory ContextData**

A configurable merge module may use this type to enable the user to provide a destination directory for files in the module. The merge tool substitutes the directory's identifier into the templates in the Value column of the [ModuleSubstitution table](modulesubstitution-table.md). To specify a configurable item of this type, module authors should enter the name of the directory into the Name column, enter "1" into the Format column, enter "Directory" into the Type column, and enter "IsolationDirectory" into the ContextData column of the [ModuleConfiguration table](moduleconfiguration-table.md).

**ShortcutLocation ContextData**

A configurable merge module may use this type to enable the user to provide a destination directory for shortcuts in the module. The merge tool substitutes the shortcut's identifier into the templates in the Value column of the [ModuleSubstitution table](modulesubstitution-table.md). To specify a configurable item of this type, module authors should enter the name of the directory into the Name column, enter "1" into the Format column, enter "Directory" into the Type column, and enter "ShortcutLocation" into the ContextData column of the [ModuleConfiguration table](moduleconfiguration-table.md).

 

 



