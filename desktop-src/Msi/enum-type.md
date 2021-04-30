---
description: The Enum Type of semantic type is one of the Text Format Types.
ms.assetid: fff01044-5749-42a5-b026-5b22671870bd
title: Enum Type
ms.topic: article
ms.date: 05/31/2018
---

# Enum Type

The Enum Type of [semantic type](semantic-types.md) is one of the [Text Format Types](text-format-types.md). This type consists of a text string chosen by the user from a set of choices. The merge tool substitutes the selected string selected into the templates specified in the Value column of the [ModuleSubstitution table](modulesubstitution-table.md).

To specify a configurable item of this type, module authors should enter the name of the text string into the Name column, enter "0" into the Format column, enter "Enum" into the Type column, and enter the list of possible strings in the ContextData column of the [ModuleConfiguration table](moduleconfiguration-table.md). The list of possible strings must be provided as a list of strings deliminated by semicolons. Each choice must be in the form "Name=Value". A literal semicolon can be added to the value by prefixing the semicolon with a backslash character. Null is a valid value unless the msmConfigItemNonNullable has been included in the Attributes field of the ModuleConfiguration table.

 

 



