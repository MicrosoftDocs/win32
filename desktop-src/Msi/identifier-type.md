---
description: The Identifier Type of semantic type is one of the Text Format Types.
ms.assetid: 137c3ad8-e47c-4cc5-b5c5-ea130236551a
title: Identifier Type
ms.topic: article
ms.date: 05/31/2018
---

# Identifier Type

The Identifier Type of [semantic type](semantic-types.md) is one of the [Text Format Types](text-format-types.md). This type consists of an text string provided by the user in the format of a Windows Installer [Identifier](identifier.md). The merge tool substitutes this string into the templates specified in the Value column of the [ModuleSubstitution table](modulesubstitution-table.md).

To specify a configurable item of this type, module authors should enter the name of the text string into the Name column, enter "0" into the Format column, enter "Identifier" into the Type column, and leave blank the ContextData column of the [ModuleConfiguration table](moduleconfiguration-table.md).The string may be in any language compatible with the code page of the database. See [Code Page Handling (Windows Installer)](code-page-handling-windows-installer-.md). Null is a valid value for the text string unless the msmConfigItemNonNullable has been included in the Attributes field of the ModuleConfiguration table.

 

 



