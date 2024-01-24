---
description: Applications write end-user-defined characters (EUDCs) and private use area (PUA) characters to the screen or printer just as they write other characters, by using output functions such as TextOut and ExtTextOut.
ms.assetid: c975c70d-4231-4a69-bec2-d51d6993fdd4
title: Writing, Mapping, and Sorting EUDC and PUA Characters
ms.topic: article
ms.date: 05/31/2018
---

# Writing, Mapping, and Sorting EUDC and PUA Characters

Applications write end-user-defined characters (EUDCs) and private use area (PUA) characters to the screen or printer just as they write other characters, by using output functions such as [TextOut](/windows/win32/api/wingdi/nf-wingdi-textouta) and [ExtTextOut](/windows/win32/api/wingdi/nf-wingdi-exttextouta). These functions automatically retrieve character information from EUDC or PUA character fonts if EUDC is enabled. For more information, see [End-User\_Defined and Private Use Area Characters](end-user-defined-characters.md).

When writing EUDCs or PUA characters, the operation of the text output function depends on the currently selected font. If the selected font is an integrated EUDC or PUA character font, the function retrieves character information from that font. If the selected font is a [double-byte character set](double-byte-character-sets.md) (DBCS) TrueType font that has an associated separate EUDC font, the function retrieves information from the specified EUDC font. Similarly, if the selected font is a [Unicode](unicode.md) TrueType font that has an associated separate PUA character font, the function retrieves information from the PUA character font. If the selected font does not have an associated EUDC or PUA character font, the function retrieves information from the system default EUDC font. If the character is not in the system default EUDC font or there is no system default EUDC font, the function writes the default character defined by the selected font.

Applications can map EUDCs to and from Unicode by using the [**MultiByteToWideChar**](/windows/desktop/api/Stringapiset/nf-stringapiset-multibytetowidechar) and [**WideCharToMultiByte**](/windows/desktop/api/Stringapiset/nf-stringapiset-widechartomultibyte) functions. The **MultiByteToWideChar** function maps most EUDCs to characters in the Unicode PUA. However, to support certain national or regional standards, some EUDCs can be mapped to non-PUA Unicode code points. The **WideCharToMultiByte** function maps a character in the PUA to its EUDC counterpart, if such a mapping exists and if the code point does not have a valid non-PUA mapping in Unicode. Not all code pages have an EUDC range. The code page specified in a call to **WideCharToMultiByte** must contain an EUDC code range for the mapping to the EUDC range to occur. If the code page does not contain an EUDC code range, the function retrieves the default character for any characters in the Unicode PUA.

[**MultiByteToWideChar**](/windows/desktop/api/Stringapiset/nf-stringapiset-multibytetowidechar) and [**WideCharToMultiByte**](/windows/desktop/api/Stringapiset/nf-stringapiset-widechartomultibyte) do not guarantee round-trip mapping. In other words, it is possible to start with a particular multibyte string containing EUDCs, map the string to Unicode with **MultiByteToWideChar** and map it back to the original DBCS with **WideCharToMultiByte**, and end up with a result that is not identical to the original string. Applications relying on mapping EUDCs to Unicode should ensure that all necessary characters can round-trip between the appropriate code page EUDC area and the Unicode PUA.

Applications should not attempt to map EUDCs from one code page to another. If an application starts with an EUDC from one code page, maps it to Unicode with [**MultiByteToWideChar**](/windows/desktop/api/Stringapiset/nf-stringapiset-multibytetowidechar), and maps to a different DBCS with [**WideCharToMultiByte**](/windows/desktop/api/Stringapiset/nf-stringapiset-widechartomultibyte), there are no guarantees about the results. The original character might be mapped to a different EUDC in the destination code page, or it might be mapped as an undefined character. Similarly, mapping a Unicode string to a code page that has an EUDC range can have unintended results. If the Unicode string contains a PUA code point, it is possible that the code point will be mapped to an EUDC that does not represent the same character.

Applications can compare DBCS strings that contain EUDCs by using the ANSI version of the [CompareString](/windows/win32/api/stringapiset/nf-stringapiset-comparestringw) function. The function effectively maps the characters to Unicode before comparing character values. Applications can create a sort key for the string by using the ANSI version of the [**LCMapString**](/windows/desktop/api/Winnls/nf-winnls-lcmapstringa) function and the LCMAP\_SORTKEY value. This function effectively maps characters to Unicode first. All characters in the PUA are sorted after all other Unicode characters. Within the area, characters are sorted in numerical order. If an application attempts to retrieve CTYPE information for an EUDC by using the [GetStringTypeA](/windows/desktop/api/Winnls/nf-winnls-getstringtypea) function, the function retrieves **NULL** for each character.

## Related topics

<dl> <dt>

[Using Unicode and Character Sets](using-unicode-and-character-sets.md)
</dt> </dl>

 

 
