---
description: Certain values used with configurable merge modules require special text handling.
ms.assetid: b9d41400-f3b5-4f85-8728-56f9b90a50ca
title: CMSM Special Format
ms.topic: article
ms.date: 05/31/2018
---

# CMSM Special Format

Certain values used with configurable merge modules require special text handling. A text string described as being in "CMSM Special Format" treats the semicolon (;) and equals (=) characters as reserved characters used by the client merge tool or Mergemod.dll.

CMSM Special format is currently used in the following locations:

-   The Row column of the [ModuleSubstitution table](modulesubstitution-table.md).
-   The Value column of the [ModuleSubstitution table](modulesubstitution-table.md).
-   The ContextData column of the [ModuleConfiguration table](moduleconfiguration-table.md) when Bitfield is the value in the Format column.
-   The ContextData column of the [ModuleConfiguration table](moduleconfiguration-table.md) when Text is the value in the Format column and Enum is the value in the Type column.
-   The DefaultValue column of the [ModuleConfiguration table](moduleconfiguration-table.md) when Key is the value in the Format column.
-   Configurable items in the Key format used by the [**ProvideTextData method**](configuremodule-providetextdata.md).

To enter literal semicolons or equal characters into a value in CMSM special format, prefix the character with a backslash character ('\\'). A literal backslash can be represented by two backslashes. A single character prefixed by a single backslash is translated into the single character, even if escaping the character is not required.

If a semicolon or equals character is not prefixed by a backslash yet does not have a defined behavior in the context of the value, the resulting string is undefined. For example, the DefaultValue column of the ModuleConfiguration table is in CMSM special format for all Key items because the semicolon character is the column delimiter. Although the equal character has no special meaning in this string, literal equal characters must still be escaped in this string.

 

 



