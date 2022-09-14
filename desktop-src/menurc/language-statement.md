---
title: LANGUAGE statement
description: Defines the language for all resources up to the next LANGUAGE statement or to the end of the file.
ms.assetid: 175e27e2-903a-4aaf-89ef-532166b167e8
keywords:
- LANGUAGE statement Menus and Other Resources
topic_type:
- apiref
api_name:
- LANGUAGE
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# LANGUAGE statement

Defines the language for all resources up to the next **LANGUAGE** statement or to the end of the file.

When the **LANGUAGE** statement appears before the beginning of the body of an [**ACCELERATORS**](accelerators-resource.md), [**DIALOGEX**](dialogex-resource.md), [**MENU**](menu-resource.md), [**RCDATA**](rcdata-resource.md), or [**STRINGTABLE**](stringtable-resource.md) resource definition, the specified language applies only to that resource.

``` syntax
LANGUAGE language, sublanguage
```

<dl> <dt>

<span id="language"></span><span id="LANGUAGE"></span>*language*
</dt> <dd>

Language identifier.

</dd> <dt>

<span id="sublanguage"></span><span id="SUBLANGUAGE"></span>*sublanguage*
</dt> <dd>

Sublanguage identifier.

</dd> </dl>

For more information, see [Language Identifier Constants and Strings](/windows/desktop/Intl/language-identifier-constants-and-strings).

## See also

<dl> <dt>

[**ACCELERATORS**](accelerators-resource.md)
</dt> <dt>

[**CHARACTERISTICS**](characteristics-statement.md)
</dt> <dt>

[**MENU**](menu-resource.md)
</dt> <dt>

[**RCDATA**](rcdata-resource.md)
</dt> <dt>

[**STRINGTABLE**](stringtable-resource.md)
</dt> <dt>

[**VERSION**](version-statement.md)
</dt> </dl>

 

 