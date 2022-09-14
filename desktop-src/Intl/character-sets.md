---
description: A &\#0034;character set&\#0034; is a mapping of characters to their identifying code values.
ms.assetid: '0a055c02-c5ed-4790-83e4-183bc3cc6b51'
title: Character Sets
ms.topic: article
ms.date: 05/31/2018
---

# Character Sets

A "character set" is a mapping of characters to their identifying code values. The character set most commonly used in computers today is [Unicode](unicode.md), a global standard for character encoding. Internally, Windows applications use the UTF-16 implementation of Unicode. In UTF-16, most characters are identified by two-byte codes. The less commonly used supplementary characters are each represented by a surrogate pair, which is a pair of two-byte codes. For more information, see [Surrogates and Supplementary Characters](surrogates-and-supplementary-characters.md).

Some Windows applications must work with the older character sets that are native to Windows Me/98/95. [Windows code pages](code-pages.md) allow your application to work with these character sets. These character sets can be divided into:

-   [Single-byte character sets](single-byte-character-sets.md) (SBCS). In an SBCS, each character is identified by a value one byte wide.
-   Multibyte character sets, in particular the [double-byte character sets](double-byte-character-sets.md) (DBCS). Multibyte character sets provide a means to represent the large number of characters in many Asian languages.

For more information, see the following topics:

-   [Code Pages](code-pages.md)
-   [Double-byte Character Sets](double-byte-character-sets.md)
-   [Single-byte Character Sets](single-byte-character-sets.md)
-   [Surrogates and Supplementary Characters](surrogates-and-supplementary-characters.md)
-   [Unicode](unicode.md)

## Related topics

<dl> <dt>

[About Unicode and Character Sets](about-unicode-and-character-sets.md)
</dt> </dl>

 

 



