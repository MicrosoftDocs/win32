---
Description: Surrogates and Supplementary Characters
ms.assetid: '0dea39e2-a2b4-47fc-b44a-56af8ba1e346'
title: Surrogates and Supplementary Characters
---

# Surrogates and Supplementary Characters

Windows applications normally use UTF-16 to represent [Unicode](unicode.md) character data. The use of 16 bits allows direct representation of 65,536 unique characters, but this Basic Multilingual Plane (BMP) is not nearly enough to cover all the symbols used in human languages. Unicode version 4.1 includes over 97,000 characters, with over 70,000 characters for Chinese alone.

The Unicode standard has established 16 additional "planes" of characters, each the same size as the BMP. Naturally, most code points beyond the BMP do not yet have characters assigned to them, but definition of the planes gives Unicode the potential to define 1,114,112 characters (that is, 2¹⁶ \* 17 characters) within the code point range U+0000 to U+10FFFF. For UTF-16 to represent this larger set of characters, the Unicode Standard defines "supplementary characters".

## About Supplementary Characters

A supplementary character is a character located beyond the BMP, and a "surrogate" is a UTF-16 code value. For UTF-16, a "surrogate pair" is required to represent a single supplementary character. The first (high) surrogate is a 16-bit code value in the range U+D800 to U+DBFF. The second (low) surrogate is a 16-bit code value in the range U+DC00 to U+DFFF. Using the surrogate mechanism, UTF-16 can support all 1,114,112 potential Unicode characters. For more details about supplementary characters, surrogates, and surrogate pairs, refer to [The Unicode Standard](http://go.microsoft.com/fwlink/p/?linkid=161649).

> [!Note]  
> Windows 2000 introduces support for basic input, output, and simple sorting of supplementary characters. However, not all system components are compatible with supplementary characters.

 

The operating system supports supplementary characters in the following ways:

-   Format 12 of the OpenType font cmap table directly supports the 4-byte character code. For more information, see the [OpenType font specification](http://www.microsoft.com/OpenType/OTSpec/cmap.md).
-   Windows supports surrogate-enabled [input method editors (IMEs)](DxTechArts.installing_and_using_input_method_editors).
-   The [Windows GDI](gdi.windows_gdi) API supports format 12 cmap tables in fonts so that surrogates can be displayed correctly.
-   The [Uniscribe](uniscribe.md) API supports supplementary characters.
-   [Windows controls](_win32_Window_Controls_cpp), including [Edit](_win32_Edit_Controls_cpp) and [Rich Edit](_win32_Rich_Edit_Controls_cpp), support supplementary characters.
-   The HTML engine supports HTML pages that include supplementary characters for display, editing (through Outlook Express), and forms submission.
-   The operating system sorting table supports supplementary characters.

## General Guidelines for Software Development Using Supplementary Characters

UTF-16 handles supplementary characters as surrogate pairs. The operating system processes a surrogate pair similarly to the way it processes [nonspacing marks](using-nonspacing-characters-and-diacritics.md). At display time, the surrogate pair displays as one glyph by means of Uniscribe, as prescribed by the Unicode Standard.

Windows Vista introduces three new macros to help identify surrogates and surrogate pairs in UTF-16 strings. These are [**IS\_HIGH\_SURROGATE**](is-high-surrogate.md), [**IS\_LOW\_SURROGATE**](is-low-surrogate.md), and [**IS\_SURROGATE\_PAIR**](is-surrogate-pair.md).

Applications automatically support supplementary characters if they support Unicode and use system controls and standard API functions, such as [**ExtTextOut**](gdi.exttextout) and [**DrawText**](gdi.drawtext). Thus, if your application uses standard system controls or uses general [**ExtTextOut**](gdi.exttextout)-type calls to display, supplementary characters should work without any special coding.

Applications that implement their own editing support by working out glyph positions in a customized way can use Uniscribe for all text processing. Uniscribe has separate functions to deal with complex script processing, such as text display, hit testing, and cursor movement. An application must call the Uniscribe functions specifically to get these advanced features. Note that applications using the Uniscribe functions are fully multilingual, but this imposes a performance penalty. Thus some applications should do their own processing of supplementary characters.

Because the surrogate mechanism to represent supplementary characters is well-defined, your application can include code to handle UTF-16 surrogate text processing. When the application encounters a separated UTF-16 value from either the lower reserved surrogate range (a low surrogate) or the upper reserved surrogate range (a high surrogate), the value must be one half of a surrogate pair. Thus, the application can detect a surrogate pair by doing simple range checking. If it encounters a UTF-16 value in the lower or upper range, it must track backward or forward one 16-bit width to get the rest of the character. When writing your application, keep in mind that [**CharNext**](_win32_charnext_cpp) and [**CharPrev**](_win32_charprev_cpp) move by 16-bit code points, not by surrogate pairs.

> [!Note]  
> Standalone surrogate code points have either a high surrogate without an adjacent low surrogate, or vice versa. These code points are invalid and are not supported. Their behavior is undefined.

 

If you are developing a font or IME provider, note that pre-Windows XP operating systems disable supplementary character support by default. Windows XP and later enable supplementary characters by default. If you provide a font and IME package that requires supplementary characters, your application must set the following registry values:


```C++
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\LanguagePack]
SURROGATE=(REG_DWORD)0x00000002

[HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\International\Scripts\42]
IEFixedFontName=[Surrogate Font Face Name]
IEPropFontName=[Surrogate Font Face Name]
```



## Related topics

<dl> <dt>

[Character Sets](character-sets.md)
</dt> </dl>

 

 



