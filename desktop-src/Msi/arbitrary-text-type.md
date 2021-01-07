---
description: The Arbitrary Text Type of semantic type is one of the Text Format Types.
ms.assetid: 503ad2db-0875-4d8b-90f7-3d04318a6b62
title: Arbitrary Text Type
ms.topic: article
ms.date: 05/31/2018
---

# Arbitrary Text Type

The Arbitrary Text Type of [semantic type](semantic-types.md) is one of the [Text Format Types](text-format-types.md). This type consists of an arbitrary text string of any length provided by the user. The merge tool substitutes this arbitrary string into the templates specified in the Value column of the [ModuleSubstitution table](modulesubstitution-table.md).

To specify a configurable item of this type, module authors should enter the name of the text string into the Name column, enter "0" into the Format column, and leave blank the Type and ContextData columns of the [ModuleConfiguration table](moduleconfiguration-table.md).The arbitrary text string may be in any language compatible with the code page of the database. For details, see [Code Page Handling (Windows Installer)](code-page-handling-windows-installer-.md). Null is a valid value for the text string unless the msmConfigItemNonNullable has been included in the Attributes field of the ModuleConfiguration table.

 

 



