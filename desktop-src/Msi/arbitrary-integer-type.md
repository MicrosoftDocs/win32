---
description: The Arbitrary Integer Type of semantic type is one of the Integer Format Types.
ms.assetid: e35b27ca-be24-4aca-b12f-ca10ab153409
title: Arbitrary Integer Type
ms.topic: article
ms.date: 05/31/2018
---

# Arbitrary Integer Type

The Arbitrary Integer Type of [semantic type](semantic-types.md) is one of the [Integer Format Types](integer-format-types.md). This type of configurable item is an integer provided by the user. The merge tool substitutes this integer into the templates specified in the Value column of the [ModuleSubstitution table](modulesubstitution-table.md).

To specify a configurable item of this type, module authors should enter the name of the text string into the Name column, enter "2" into the Format column, and leave blank the Type and ContextData columns of the [ModuleConfiguration table](moduleconfiguration-table.md). The Type and ContextData columns are reserved and must be null.

 

 



