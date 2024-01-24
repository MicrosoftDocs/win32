---
description: Most applications written today handle character data primarily as Unicode, using the UTF-16 encoding.
ms.assetid: 866f09f4-629e-4097-a974-fbda9389d077
title: Code Pages
ms.topic: article
ms.date: 05/31/2018
---

# Code Pages

Most applications written today handle character data primarily as [Unicode](unicode.md), using the UTF-16 encoding. However, many legacy applications continue to use character sets based on code pages. Even new applications sometimes have to work with code pages, often for one of the following reasons:

-   To communicate with legacy applications.
-   To communicate with older mail and news servers, which might not always support Unicode.
-   To communicate with the Windows Console for legacy purposes. (The console does support Unicode, but some legacy command-line application tools may not.)

> [!Note]  
> New Windows applications should use [Unicode](unicode.md) to avoid the inconsistencies of varied code pages and for ease of localization.

 

Each code page is represented by a code page identifier, for example, 1252, and is handled by the Unicode and character set API functions. For a list of supported code page identifiers, see [Code Page Identifiers](code-page-identifiers.md). The "Code Pages" reference on the Microsoft [Go Global Developer Center](https://msdn.microsoft.com/goglobal) gives full descriptions of many code pages.

Windows code pages, commonly called "ANSI code pages", are code pages for which non-ASCII values (values greater than 127) represent international characters. These code pages are used natively in Windows Me, and are also available on Windows NT and later.

> [!Note]  
> Originally, Windows code page 1252, the code page commonly used for English and other Western European languages, was based on an American National Standards Institute (ANSI) draft. That draft eventually became ISO 8859-1, but Windows code page 1252 was implemented before the standard became final, and is not exactly the same as ISO 8859-1.

 

Many Windows API functions have "A" (ANSI) and "W" (wide, Unicode) versions. The "A" version handles text based on Windows code pages, while the "W" version handles Unicode text. See [Windows Data Types for Strings](windows-data-types-for-strings.md) and [Conventions for Function Prototypes](conventions-for-function-prototypes.md).

Windows code pages are also sometimes referred to as "active code pages" or "system active code pages". A Windows operating system always has one currently active Windows code page. All [ANSI versions of API functions](conventions-for-function-prototypes.md) use the currently active code page.

Original equipment manufacturer (OEM) code pages are code pages for which non-ASCII values represent line drawing and punctuation characters. These code pages were originally used for MS-DOS and are still used for console applications. They are also used for the non-extended file names in the FAT12, FAT16, and FAT32 file systems, as described in [Character Sets Used in File Names](character-sets-used-in-file-names.md). The usual OEM code page for English is code page 437.

For both Windows code pages and OEM code pages, the code values 0x00 through 0x7F correspond to the 7-bit ASCII character set. Code values 0x00 through 0x19 and 0x7F always represent standardized control characters and 0x20 through 0x7E represent standardized displayable characters. Characters represented by the remaining codes, 0x80 through 0xff, vary among character sets. Each character set includes different special characters, typically customized for a language or group of languages. Windows code page 1252 and OEM code page 437 are generally used in the United States.

In addition to Windows and OEM code pages, your applications can use non-native code pages. Examples are EBCDIC and Macintosh code pages.

Two encodings of Unicode (UTF-7 and UTF-8) are implemented as code pages. Like other code pages, each page is known by a numeric identifier and can be handled with many of the same Unicode and character set API functions.

Code pages can be either [single-byte character set](single-byte-character-sets.md) (SBCS) pages or [double-byte character set](double-byte-character-sets.md) (DBCS) pages. In SBCS pages, each byte directly encodes a single character, so that it is possible to represent exactly 256 distinct characters (including control characters, letters, digits, punctuation, symbols, and the like). DBCS code pages are used for languages such as Japanese and Chinese. In such a code page, some characters have two-byte encodings with certain byte values (always values greater than 127) serving as "lead bytes". Instead of encoding characters in their own right, lead bytes can be mapped to a character only in conjunction with a "trail byte".

Some legacy protocols require the use of SBCS and DBCS code pages. Each SBCS/DBCS code page supports different characters, but no code page supports the full breadth of characters provided by Unicode. Each SBCS/DBCS code page supports a different subset, differently encoded.

> [!Note]  
> Data converted from one SBCS or DBCS code page to another is subject to corruption, because the same data value on different code pages can encode a different character. Data converted from Unicode to SBCS or DBCS is subject to data loss, because a given code page might not be able to represent every character used in that particular Unicode data.

 

In addition to SBCS and DBCS code pages, your applications have available the multibyte character set code pages 52936, 54936, 51949, and 5022x, which use an approach similar to that for a DBCS. A multibyte character set code page goes beyond two-byte encodings of some characters, however. UTF-7 and UTF-8 use a similar approach to encode Unicode based on a 7-bit and 8-bit bytes, respectively. For more information, see [Unicode](unicode.md).

Several Unicode and character set functions allow your applications to handle code pages. An application can use the [**GetCPInfo**](/windows/desktop/api/Winnls/nf-winnls-getcpinfo) and [**GetCPInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getcpinfoexa) functions to obtain information about a code page. This information includes the default character used when a character in a converted string has no corresponding entry in the code page.

An application can use the [**MultiByteToWideChar**](/windows/desktop/api/Stringapiset/nf-stringapiset-multibytetowidechar) and [**WideCharToMultiByte**](/windows/desktop/api/Stringapiset/nf-stringapiset-widechartomultibyte) functions to convert between strings based on Windows code pages and Unicode strings. Although their names refer to "MultiByte", these functions work equally well with SBCS, DBCS, and multibyte character set code pages.

> [!Note]  
> [**WideCharToMultiByte**](/windows/desktop/api/Stringapiset/nf-stringapiset-widechartomultibyte) can lose some data if the supplied code page cannot represent all characters in a Unicode string.

 

Your application can convert between Windows code pages and OEM code pages using the standard C runtime library functions. However, use of these functions presents a risk of data loss because the characters that can be represented by each code page do not match exactly.

Your applications can also call the [**GetACP**](/windows/desktop/api/Winnls/nf-winnls-getacp) function. This function retrieves the identifier of the current Windows (ANSI) code page.

## Related topics

<dl> <dt>

[Character Sets](character-sets.md)
</dt> </dl>

 

 



