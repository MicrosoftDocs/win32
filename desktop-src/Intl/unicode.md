---
description: Unicode is a worldwide character-encoding standard. The system uses Unicode exclusively for character and string manipulation. For a detailed description of all aspects of Unicode, refer to The Unicode Standard.
ms.assetid: 'ca5bcdee-ea13-4745-a565-5426c462892d'
title: Unicode
ms.topic: article
ms.date: 05/31/2018
---

# Unicode

Unicode is a worldwide character-encoding standard. The system uses Unicode exclusively for character and string manipulation. For a detailed description of all aspects of Unicode, refer to [The Unicode Standard](https://www.unicode.org/standard/standard.html).

Compared to older mechanisms for handling character and string data, Unicode simplifies software localization and improves multilingual text processing. By using Unicode to represent character and string data in your applications, you can enable universal data exchange capabilities for global marketing, using a single binary file for every possible character code. Unicode does the following:

-   Allows any combination of characters, drawn from any combination of scripts and languages, to co-exist in a single document.
-   Defines semantics for each character.
-   Standardizes script behavior.
-   Provides a standard algorithm for bidirectional text.
-   Defines cross-mappings to other standards.
-   Defines multiple encodings of its single character set: UTF-7, UTF-8, UTF-16, and UTF-32. Conversion of data among these encodings is lossless.

Unicode supports numerous scripts used by languages around the world, and also a large number of technical symbols and special characters used in publishing. The supported scripts include, but are not limited to, Latin, Greek, Cyrillic, Hebrew, Arabic, Devanagari, Thai, Han, Hangul, Hiragana, and Katakana. Supported languages include, but are not limited to, German, French, English, Greek, Russian, Hebrew, Arabic, Hindi, Thai, Chinese, Korean, and Japanese. Unicode currently can represent the vast majority of characters in modern computer use around the world, and continues to be updated to make it even more complete.

Unicode-enabled functions are described in [Conventions for Function Prototypes](conventions-for-function-prototypes.md). These functions use UTF-16 (wide character) encoding, which is the most common encoding of Unicode and the one used for native Unicode encoding on Windows operating systems. Each code value is 16 bits wide, in contrast to the older [code page](code-pages.md) approach to character and string data, which uses 8-bit code values. The use of 16 bits allows the direct encoding of 65,536 characters. In fact, the universe of symbols used to transcribe human languages is even larger than that, and UTF-16 code points in the range U+D800 through U+DFFF are used to form surrogate pairs, which constitute 32-bit encodings of supplementary characters. See [Surrogates and Supplementary Characters](surrogates-and-supplementary-characters.md) for further discussion.

The Unicode character set includes numerous combining characters, such as U+0308 ("¨"), a combining dieresis or umlaut. Unicode can often represent the same glyph in either a ''composed'' or a ''decomposed'' form: for example, the composed form of "Ä" is the single Unicode code point "Ä" (U+00C4), while its decomposed form is "A" + "¨" (U+0041 U+0308). Unicode does not define a composed form for every glyph. For example, the Vietnamese lowercase "o" with circumflex and tilde ("ỗ") is represented by U+006f U+0302 U+0303 (o + Circumflex + Tilde). For further discussion of combining characters and related issues, see [Using Unicode Normalization to Represent Strings](using-unicode-normalization-to-represent-strings.md).

For compatibility with 8-bit and 7-bit environments, Unicode can also be encoded as UTF-8 and UTF-7, respectively. While Unicode-enabled functions in Windows use UTF-16, it is also possible to work with data encoded in UTF-8 or UTF-7, which are supported in Windows as multibyte character set [code pages](code-pages.md).

New Windows applications should use UTF-16 as their internal data representation. Windows also provides extensive support for code pages, and mixed use in the same application is possible. Even new Unicode-based applications sometimes have to work with code pages. Reasons for this are discussed in [Code Pages](code-pages.md).

An application can use the [**MultiByteToWideChar**](/windows/win32/api/Stringapiset/nf-stringapiset-multibytetowidechar) and [**WideCharToMultiByte**](/windows/win32/api/Stringapiset/nf-stringapiset-widechartomultibyte) functions to convert between strings based on code pages and Unicode strings. Although their names refer to "MultiByte", these functions work equally well with [single-byte character set](single-byte-character-sets.md) (SBCS), [double-byte character set](double-byte-character-sets.md) (DBCS), and multibyte character set (MBCS) code pages.

Typically, a Windows application should use UTF-16 internally, converting only as part of a "thin layer" over the interface that must use another format. This technique defends against loss and corruption of data. Each code page supports different characters, but none of them supports the full spectrum of characters provided by Unicode. Most of the code pages support different subsets, differently encoded. The code pages for UTF-8 and UTF-7 are an exception, since they support the complete Unicode character set, and conversion between these encodings and UTF-16 is lossless.

Data converted directly from the encoding used by one code page to the encoding used by another is subject to corruption, because the same data value on different code pages can encode a different character. Even when your application is converting as close to the interface as possible, you should think carefully about the range of data to handle.

Data converted from Unicode to a code page is subject to data loss, because a given code page might not be able to represent every character used in that particular Unicode data. Therefore, note that [**WideCharToMultiByte**](/windows/win32/api/Stringapiset/nf-stringapiset-widechartomultibyte) might lose some data if the target code page cannot represent all of the characters in the Unicode string.

When modernizing code page-based legacy applications to use Unicode, you can use generic functions and the [**TEXT**](/windows/win32/api/Winnt/nf-winnt-text) macro to maintain a single set of sources from which to compile two versions of your application. One version supports Unicode and the other one works with Windows code pages. Using this mechanism, you can convert even very large applications from Windows code pages to Unicode while maintaining application sources that can be compiled, built, and tested at all phases of the conversion. For more information, see [Conventions for Function Prototypes](conventions-for-function-prototypes.md).

Unicode characters and strings use data types that are distinct from those for code page-based characters and strings. Along with a series of macros and naming conventions, this distinction minimizes the chance of accidentally mixing the two types of character data. It facilitates compiler type checking to ensure that only Unicode parameter values are used with functions expecting Unicode strings.

## Related topics

<dl> <dt>

[Character Sets](character-sets.md)
</dt> <dt>

[Sorting](sorting.md)
</dt> <dt>

[Surrogates and Supplementary Characters](surrogates-and-supplementary-characters.md)
</dt> <dt>

[Using Unicode Normalization to Represent Strings](using-unicode-normalization-to-represent-strings.md)
</dt> </dl>

 

 



