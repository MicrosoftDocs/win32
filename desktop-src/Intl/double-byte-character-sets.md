---
description: A double-byte character set (DBCS), also known as an &\#0034;expanded 8-bit character set&\#0034;, is an extended single-byte character set (SBCS), implemented as a code page.
ms.assetid: df049d22-02e2-48b2-8b74-52f71c00c549
title: Double-byte Character Sets
ms.topic: article
ms.date: 05/31/2018
---

# Double-byte Character Sets

A double-byte character set (DBCS), also known as an "expanded 8-bit character set", is an extended [single-byte character set](single-byte-character-sets.md) (SBCS), implemented as a code page. DBCSs were originally developed to extend the SBCS design to handle languages such as Japanese and Chinese. Some characters in a DBCS, including the digits and letters used for writing English, have single-byte code values. Other characters, such as Chinese ideographs or Japanese kanji, have double-byte code values. A DBCS can correspond either to a Windows code page or an OEM code page. A DBCS code page can also include a non-native code page, for example, an EBCDIC code page. For definitions of these code pages, see [Code Pages](code-pages.md).

> [!Note]  
> New Windows applications should use [Unicode](unicode.md) to avoid the inconsistencies of varied code pages and for ease of localization. However, some legacy protocols might require the use of DBCS code pages. Each DBCS code page supports different characters, but no page supports the full breadth of characters provided by Unicode. Each DBCS code page supports a different subset, differently encoded. Data converted from one DBCS code page to another is subject to corruption because the same data value on different code pages can encode a different character. Data converted from Unicode to DBCS is subject to data loss, because a given code page might not be able to represent every character used in that particular Unicode data.

 

To interpret a DBCS string, an application must start at the beginning of the string and scan forward. It keeps track when it encounters a lead byte in the string, and treats the next byte as the trailing part of the same character. If the application simply scans the string one byte at a time and encounters a byte that appears to be the code value representing a backslash ("\\"), that byte might simply be the trail byte of a two-byte character. The application cannot just back up one byte to see if the preceding byte is a lead byte, as that byte value might be eligible to be used as both a lead byte and a trail byte. Thus the application has essentially the same problem with it as with the possible backslash. In other words, substring searches are much more complicated with a DBCS than with either SBCSs or Unicode. Accordingly, applications that support a DBCS must use special functions, such as [\_mbsstr](/cpp/c-runtime-library/reference/strstr-wcsstr-mbsstr-mbsstr-l), instead of the [**StrStr**](https://msdn.microsoft.com/library/z9da80kz(v=VS.71).aspx) function.

Your applications use DBCS Windows code pages with the "A" versions of Windows functions. See [Conventions for Function Prototypes](conventions-for-function-prototypes.md) and [Code Pages](code-pages.md). To help identify a DBCS code page, an application can use the [**GetCPInfo**](/windows/desktop/api/Winnls/nf-winnls-getcpinfo) or [**GetCPInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getcpinfoexa) function. An application can use the [**IsDBCSLeadByte**](/windows/desktop/api/Winnls/nf-winnls-isdbcsleadbyte) function to determine if a given value can be used as the lead byte of a 2-byte character. In addition, an application can use the [**MultiByteToWideChar**](/windows/desktop/api/Stringapiset/nf-stringapiset-multibytetowidechar) and [**WideCharToMultiByte**](/windows/desktop/api/Stringapiset/nf-stringapiset-widechartomultibyte) functions to map between Unicode and DBCS strings.

## Related topics

<dl> <dt>

[Character Sets](character-sets.md)
</dt> <dt>

[Single-byte Character Sets](single-byte-character-sets.md)
</dt> </dl>

 

 
