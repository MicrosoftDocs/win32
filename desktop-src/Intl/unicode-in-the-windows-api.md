---
description: 'Windows API functions that manipulate characters are generally implemented in one of three formats:'
ms.assetid: e7698f0b-dbcb-4cd0-9cb5-23a26edb966a
title: Unicode in the Windows API
ms.topic: article
ms.date: 05/31/2018
---

# Unicode in the Windows API

Windows API functions that manipulate characters are generally implemented in one of three formats:

-   A generic version that can be compiled for either Windows code pages or Unicode
-   A [Windows code page](code-pages.md) version with the letter "A" used to indicate "ANSI"
-   A [Unicode](unicode.md) version with the letter "W" used to indicate "wide"

Some newer functions support only Unicode versions. For more information, see [Conventions for Function Prototypes](conventions-for-function-prototypes.md).

The following topics discuss Unicode data types and how they are used in functions and messages; the use of resources, file names, and command line arguments; and methods of translating between different types of strings.

-   [Automatic Message Translation](automatic-message-translation.md)
-   [Character Sets Used in File Names](character-sets-used-in-file-names.md)
-   [Command Line Arguments](command-line-arguments.md)
-   [Conventions for Function Prototypes](conventions-for-function-prototypes.md)
-   [Standard C Functions](standard-c-functions.md)
-   [String Function Differences](string-function-differences.md)
-   [Translation Between String Types](translation-between-string-types.md)
-   [Windows Data Types for Strings](windows-data-types-for-strings.md)

## Related topics

<dl> <dt>

[About Unicode and Character Sets](about-unicode-and-character-sets.md)
</dt> </dl>

 

 



