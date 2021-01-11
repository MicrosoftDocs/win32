---
description: A language identifier is a standard international numeric abbreviation for the language in a country or geographical region.
ms.assetid: 076e2a43-256a-4646-a5c8-1d48ab08ce1a
title: Language Identifiers
ms.topic: article
ms.date: 05/31/2018
---

# Language Identifiers

A language identifier is a standard international numeric abbreviation for the [language](locales-and-languages.md) in a country or geographical region. Each language has a unique language identifier (data type LANGID), a 16-bit value that consists of a primary language identifier and a sublanguage identifier. For details of language identifiers, see [Language Identifier Constants and Strings](language-identifier-constants-and-strings.md).

A language identifier is constructed using the [**MAKELANGID**](/windows/desktop/api/Winnt/nf-winnt-makelangid) macro. The following illustration shows the format of the bits in a language identifier.

``` syntax
+-------------------------+-------------------------+
|     SubLanguage ID      |   Primary Language ID   |
+-------------------------+-------------------------+
15                    10  9                         0   bit
```

The following are predefined language identifiers:

-   LANG\_SYSTEM\_DEFAULT. The operating system default language.
-   LANG\_USER\_DEFAULT. The language of the current user.

Your application can retrieve the current language identifiers by using the [Multilingual User Interface](multilingual-user-interface.md) functions.

## Related topics

<dl> <dt>

[Locales and Languages](locales-and-languages.md)
</dt> <dt>

[Language Identifier Constants and Strings](language-identifier-constants-and-strings.md)
</dt> <dt>

[Multilingual User Interface](multilingual-user-interface.md)
</dt> <dt>

[**MAKELANGID**](/windows/desktop/api/Winnt/nf-winnt-makelangid)
</dt> </dl>

 

 



