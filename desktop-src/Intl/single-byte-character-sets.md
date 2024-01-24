---
description: A single-byte character set (SBCS) is a mapping of 256 individual characters to their identifying code values, implemented as a code page.
ms.assetid: 53f74132-91aa-4257-846a-f6e1f2f9ae0b
title: Single-byte Character Sets
ms.topic: article
ms.date: 05/31/2018
---

# Single-byte Character Sets

A single-byte character set (SBCS) is a mapping of 256 individual characters to their identifying code values, implemented as a code page. An SBCS can correspond either to a Windows code page or an OEM code page. An SBCS code page can also include a non-native code page, for example, an EBCDIC code page. For definitions of these code pages, see [Code Pages](code-pages.md).

> [!Note]  
> New Windows applications should use [Unicode](unicode.md) to avoid the inconsistencies of varied code pages and for ease of localization. However, some legacy protocols require the use of an SBCS. Each SBCS code page supports different characters, but no page supports the full breadth of characters provided by Unicode. Each SBCS code page supports a different subset, differently encoded. Data converted from one SBCS code page to another is subject to corruption, because the same data value on different code pages can encode a different character. Data converted from Unicode to SBCS is subject to data loss because a given code page might not be able to represent every character used in that particular Unicode data.

 

Your applications use SBCS Windows code pages with the "A" versions of Windows functions. See [Conventions for Function Prototypes](conventions-for-function-prototypes.md) and [Code Pages](code-pages.md). To help identify an SBCS code page, an application can use the [**GetCPInfo**](/windows/desktop/api/Winnls/nf-winnls-getcpinfo) or [**GetCPInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getcpinfoexa) function. In addition, an application can use the [**MultiByteToWideChar**](/windows/desktop/api/Stringapiset/nf-stringapiset-multibytetowidechar) and [**WideCharToMultiByte**](/windows/desktop/api/Stringapiset/nf-stringapiset-widechartomultibyte) functions to map between Unicode and SBCS strings.

## Related topics

<dl> <dt>

[Character Sets](character-sets.md)
</dt> <dt>

[Double-byte Character Sets](double-byte-character-sets.md)
</dt> </dl>

 

 



