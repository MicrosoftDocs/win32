---
description: The Formatted Type of semantic type is one of the Text Format Types.
ms.assetid: 44af5b5c-bbf9-4043-8076-0881680a36c1
title: Formatted Type
ms.topic: article
ms.date: 05/31/2018
---

# Formatted Type

The Formatted Type of [semantic type](semantic-types.md) is one of the [Text Format Types](text-format-types.md). This type consists of an arbitrary text string of any length provided by the user and in the Windows Installer formatted text format. For details, see [Formatted](formatted.md). The merge tool substitutes this string into the templates specified in the Value column of the [ModuleSubstitution table](modulesubstitution-table.md).

To specify a configurable item of this type, module authors should enter the name of the text string into the Name column, enter "0" into the Format column, enter "Formatted" into the Type column, and leave blank the ContextData column of the [ModuleConfiguration table](moduleconfiguration-table.md).The string may be in any language compatible with the code page of the database. For details, see [Code Page Handling (Windows Installer)](code-page-handling-windows-installer-.md). Null is a valid value for the text string unless the msmConfigItemNonNullable has been included in the Attributes field of the ModuleConfiguration table.

 

 



