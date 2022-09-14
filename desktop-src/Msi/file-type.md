---
description: The File Type of semantic type is one of the Key Format Types. This type consists of a foreign key into the File table provided by the user.
ms.assetid: cbcaa016-879e-48c2-93c6-b0e91e1eb9ed
title: File Type
ms.topic: article
ms.date: 05/31/2018
---

# File Type

The File Type of [semantic type](semantic-types.md) is one of the [Key Format Types](key-format-types.md). This type consists of a foreign key into the [File table](file-table.md) provided by the user.

The File type may be used with the following kinds of ContextData.

**AssemblyContext ContextData**

This type may be used to enable users to configure foreign keys to Win32 or common language runtime assemblies. The merge tool must substitute a Windows Installer [Identifier](identifier.md) for items of this type into the template in the Value column of the [ModuleSubstitution table](modulesubstitution-table.md). Mergemod.dll does not enforce this and it is up to the merge tool to ensure that the user provides a valid key into the File table.

Null is a valid value for this type unless the msmConfigItemNonNullable has been included in the Attributes field of the [ModuleConfiguration table](moduleconfiguration-table.md).

 

 



