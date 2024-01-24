---
description: Several of the font and text-output functions have a parameter that specifies the length of the text-output string. A typical example is the cchText parameter of DrawTextEx.
ms.assetid: 695fd0f9-abd4-4666-acad-2c409624ddc6
title: Specifying length of text-output string
ms.topic: article
ms.date: 05/31/2018
---

# Specifying length of text-output string

Several of the font and text-output functions have a parameter that specifies the length of the text-output string. A typical example is the *cchText* parameter of [**DrawTextEx**](/windows/desktop/api/Winuser/nf-winuser-drawtextexa).

Each of these functions has both an "ANSI" version and a Unicode version (for example, [**DrawTextExA**](/windows/desktop/api/Winuser/nf-winuser-drawtextexa) and **DrawTextExW**, respectively). For the "ANSI" version of each function, the length is specified as a BYTE count and for the Unicode function it is specified as a WORD count.

It is traditional to think of this as a "character count". That is generally accurate for many languages, including English, but it is not accurate in general. In "ANSI" strings, characters in [SBCS](../intl/single-byte-character-sets.md) code pages take one byte each, but most characters in [DBCS](../intl/double-byte-character-sets.md) code pages take two bytes. Similarly, most currently defined Unicode characters reside in the Basic Multilingual Plane (BMP) and their UTF-16 representations fit in one WORD, but supplementary characters are represented in Unicode by ''surrogates'', which require two WORDs.

Each of these functions takes a length count. For the "ANSI" version of each function, the length is specified as a BYTE count length of a string not including the **NULL** terminator. For the Unicode function, the length count is the byte count divided by sizeof(WCHAR), which is 2, not including the **NULL** terminator. The character count is the count of the number of characters, which might not equal the length count of the string. In some instances, characters take more than one BYTE for ANSI (for example, [DBCS](../intl/double-byte-character-sets.md) character) and more than one WORD for Unicode (for example, surrogate characters). Further, the number of glyphs might not equal the number of characters because multiple characters might be composited to make one glyph. Length count is the amount of data. Character count is the number of units that are processed as one entity. Glyphs are what gets rendered. For example, in Unicode, you can have a string with length of 3, which is 2 characters and which results in 1 glyph being rendered. However, typically, most Unicode strings length, character count, and number of rendered glyphs are equal.

You can use \_tcslen() to get the string length. For ANSI, \_tcslen() returns the number of bytes. For Unicode, \_tcslen() returns the number of WCHARs (that is, WORDs).

Special processing characters like tabs and soft hyphens that aren't always drawn can affect the drawn output. They get included in the string length and character counts, but might not be directly represented by a rendered glyph.

Some of these functions allow the caller to specify the length as -1 to indicate that the string is null-terminated; in that case the function will compute the character count automatically. Not all of the functions offer this capability. That is specified on a function-by-function basis; see the individual function documentation.

 

 
