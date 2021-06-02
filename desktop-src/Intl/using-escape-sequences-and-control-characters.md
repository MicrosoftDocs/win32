---
description: When an application converts strings from ASCII or from a Windows (ANSI) code page to Unicode, it should translate escape sequences character-by-character into Unicode.
ms.assetid: 4be0fd47-0903-44d3-a323-0adc6e9c0cc9
title: Using Escape Sequences and Control Characters
ms.topic: article
ms.date: 05/31/2018
---

# Using Escape Sequences and Control Characters

When an application converts strings from ASCII or from a [Windows (ANSI) code page](code-pages.md) to Unicode, it should translate escape sequences character-by-character into Unicode. When an ASCII or other 8-bit text file is converted to Unicode, there is a chance that it will subsequently be converted back. Converting escape sequences into Unicode on a character-by-character basis, instead of combining them as a single Unicode character, makes it possible to perform the reverse conversion without needing to recognize and parse the escape sequences as such. For example, ESC+A should become 0x001B (ESC), 0x0041 (A), instead of 0x411B.

The first 32 16-bit code values in Unicode are intended for the 32 control characters. This specification supports the existing use of control characters for formatting purposes. Unicode applications can treat these control characters in exactly the same way as they treat their ASCII equivalents.

## Related topics

<dl> <dt>

[Using Special Characters in Unicode](using-special-characters-in-unicode.md)
</dt> </dl>

 

 



