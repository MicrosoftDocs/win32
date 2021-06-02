---
description: The RTF Type of semantic type is one of the Text Format Types.
ms.assetid: 91fc47c1-520a-4002-9dbe-4ee2b56f84b3
title: RTF Type
ms.topic: article
ms.date: 05/31/2018
---

# RTF Type

The RTF Type of [semantic type](semantic-types.md) is one of the [Text Format Types](text-format-types.md). This type consists of an arbitrary text string in the Rich Text Format (RTF) of any length provided by the user. The merge tool substitutes this string into the templates specified in the Value column of the [ModuleSubstitution table](modulesubstitution-table.md).

To specify a configurable item of this type, module authors should enter the name of the text string into the Name column, enter "0" into the Format column, enter "RTF" into the Type column, and leave blank the ContextData column of the [ModuleConfiguration table](moduleconfiguration-table.md).The string may be in any language compatible with the code page of the database. See [Code Page Handling (Windows Installer)](code-page-handling-windows-installer-.md). Null is a valid value for the text string unless the msmConfigItemNonNullable has been included in the Attributes field of the ModuleConfiguration table.

 

 



