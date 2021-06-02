---
description: The Binary Type of semantic type is one of the Key Format Types. This type consists of a key into the Binary table provided by the user.
ms.assetid: b6a25100-9f3e-4207-b56f-0c27ee16f188
title: Binary Type
ms.topic: article
ms.date: 05/31/2018
---

# Binary Type

The Binary Type of [semantic type](semantic-types.md) is one of the [Key Format Types](key-format-types.md). This type consists of a key into the [Binary table](binary-table.md) provided by the user.

The merge tool must substitute a valid Windows Installer [Identifier](identifier.md) for items of this type. Mergemod.dll does not enforce this restriction and it is up to the merge tool to ensure that the user provides a valid key into the Binary table.

Null is a valid value for this type unless the msmConfigItemNonNullable has been included in the Attributes field of the [ModuleConfiguration table](moduleconfiguration-table.md).

The Binary type may be used with the following kinds of ContextData.

**Bitmap ContextData**

A configurable merge module may use this type to enable the user to provide a foreign key to a row in the Binary Table that contains a bitmap image. Mergmod.dll does not guarantee any specific size or type of bitmap and the merge tool must ensure that the data is a valid image. To specify a configurable item of this type, module authors should enter the name of the configurable item into the Name column, enter "1" into the Format column, enter "Binary" into the Type column, and enter "Bitmap" into the ContextData column of the ModuleConfiguration table.

**Icon ContextData**

A configurable merge module may use this type to enable the user to provide a foreign key to a row in the Binary Table that contains an icon image. Mergmod.dll does not guarantee any specific size or type of icon and the merge tool must ensure that the data is a valid image. To specify a configurable item of this type, module authors should enter the name of the configurable item into the Name column, enter "1" into the Format column, enter "Binary" into the Type column, and enter "Icon" into the ContextData column of the ModuleConfiguration table. This type is not appropriate for use in an advertisement table.

**EXE ContextData**

A configurable merge module may use this type to enable the user to provide a foreign key to a row in the Binary Table that contains a 32-bit executable image. Mergmod.dll does not validate the data is valid and the merge tool must ensure that the data is a valid PE file. To specify a configurable item of this type, module authors should enter the name of the configurable item into the Name column, enter "1" into the Format column, enter "Binary" into the Type column, and enter "EXE" into the ContextData column of the ModuleConfiguration table.

**EXE64 ContextData**

A configurable merge module may use this type to enable the user to provide a foreign key to a row in the Binary Table that contains either a 32-bit or 64-bit executable image. Mergmod.dll does not validate the data is valid and the merge tool must ensure that the data is a valid PE file. To specify a configurable item of this type, module authors should enter the name of the configurable item into the Name column, enter "1" into the Format column, enter "Binary" into the Type column, and enter "EXE64" into the ContextData column of the ModuleConfiguration table.

 

 



