---
description: The &\#0034;Bitfield&\#0034; type with no context requests that the user provide an integer whose value is used to set one or more bits in a bitfield. This text may be in any language compatible with the code page of the database.
ms.assetid: 28e1bdb9-a42d-46ce-ad24-71bc22e2d92a
title: Arbitrary Bitfield Type
ms.topic: article
ms.date: 05/31/2018
---

# Arbitrary Bitfield Type

The "Bitfield" type with no context requests that the user provide an integer whose value is used to set one or more bits in a bitfield. This text may be in any language compatible with the code page of the database.

The Arbitrary Bitfield Type of [semantic type](semantic-types.md) is one of the Bitfield Types. This type consists of an integer chosen by the user from a set of choices. The merge tool substitutes the selected integer into the templates specified in the Value column of the [ModuleSubstitution table](modulesubstitution-table.md). To specify a configurable item of this type, module authors should enter the name of the item into the Name column, enter "3" into the Format column, leave the Type column blank, and enter the list of possible integers in the ContextData column of the [ModuleConfiguration table](moduleconfiguration-table.md).

The Type column is reserved and must be null. The entry in the ContextData column for all Bitfield Format types must be in the form "<mask>;<Name>=<value>;<Name>=<value>....", where <mask> is an integer value indicating the bits of interest, <Name> is a localizable display name for the choice, and <value> is a decimal integer value. The context column is in use [CMSM Special Format](cmsm-special-format.md) and for all bitfield types. A literal "=" or ";" character can be entered in the <Name> field by prefixing it with a backslash ('\\') character.

 

 



