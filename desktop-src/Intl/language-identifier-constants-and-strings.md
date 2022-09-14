---
description: Each language identifier is composed of a primary language identifier indicating the language and a sublanguage identifier indicating the country/region.
ms.assetid: 8a6373e0-46c2-4b1b-bc67-543f426ef15a
title: Language Identifier Constants and Strings
ms.topic: article
ms.date: 05/31/2018
---

# Language Identifier Constants and Strings

> [!IMPORTANT]
> Language identifier constants are deprecated and their use is discouraged. Use of locale names instead of locale identifiers is always preferable.

See [language identifier](language-identifiers.md) for a description of language identifiers.

A primary or sublanguage identifier can be user-defined or predefined. For the predefined primary language identifiers with their valid sublanguage identifiers, see [[MS-LCID]: Windows Language Code Identifier (LCID) Reference](/openspecs/windows_protocols/ms-lcid/70feba9f-294e-491e-b6eb-56532684c37f).

> [!Note]  
> If there is no sublanguage identifier to use with a primary language identifier, your application should use **SUBLANG\_DEFAULT**. It should use **SUBLANG\_NEUTRAL** for resources that are the same for all sublanguages of a primary language.

A user-defined primary language identifier has a value in the range 0x0200 to 0x03ff. All other values are reserved for operating system use.

A user-defined sublanguage identifier has a value in the range 0x20 to 0x3f. All other values are reserved for operating system use.
