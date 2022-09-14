---
description: Windows allows for local definition of nonstandard characters in both double-byte character sets (DBCSs) and Unicode.
ms.assetid: 32d0ddab-4b3f-473e-bf92-3230b3746079
title: Character Sets and Fonts
ms.topic: article
ms.date: 05/31/2018
---

# Character Sets and Fonts

Windows allows for local definition of nonstandard characters in both [double-byte character sets](double-byte-character-sets.md) (DBCSs) and [Unicode](unicode.md). For a DBCS, these nonstandard characters are known as end-user-defined characters (EUDC). Unicode provides a similar capability through its private use area (PUA). Applications identify a specified character by using the associated DBCS or Unicode character value.

The DBCS character values that can be assigned depend on the specified character set. Each East Asian Windows [code page](code-pages.md) has at least one range of reserved values for use as EUDCs. The ranges are defined by the [EUDCCodeRange](eudccoderange.md) registry key. Unicode values for this purpose always come from the Unicode PUA, values U+E000 to U+F8FF, U+F0000 to U+FFFFD, and U+100000 to U+10FFFD.

To create an EUDC or PUA character, the user chooses a character value that is within the specified range and adds the [glyph](uniscribe-glossary.md) to the font in the entry that corresponds to that character value. The user creates the glyph using an EUDC editor or using a font package purchased from a font vendor. Any DBCS font can contain EUDCs, and any Unicode font can contain PUA characters. The font is called a "separate" EUDC/PUA font if it contains only EUDCs. The font is an "integrated" EUDC/PUA font if it contains standard characters as well as EUDCs.

The system default EUDC/PUA font is a font that the operating system automatically associates with all DBCS and Unicode fonts, except fonts that have explicitly associated EUDC/PUA fonts. Applications set the system default EUDC/PUA font by setting the value of the SystemDefaultEUDCFont name under the [EUDC](eudc.md) registry key. Similarly, applications can associate separate EUDC/PUA fonts with corresponding fonts by specifying a font name and associated font file under the EUDC key. The operating system always first tries to find the EUDC/PUA in the currently selected font. If the font is not found, the operating system looks for the character in the associated EUDC/PUA font, if one has been defined for the currently selected font. If it still fails to find the character, the operating system looks for it in the system default EUDC/PUA font.

TrueType fonts can be installed either as .ttf files or as .tte files. Since the operating system hides .tte files, applications cannot enumerate or otherwise examine the installed fonts using GDI API functions. On many operating systems, the system default EUDC/PUA font and separate EUDC/PUA fonts are installed as .tte files. Applications such as EUDC editors and the Control Panel must use registry entries to add, modify, and delete such fonts.

Use of EUDC and PUA characters does not reliably preserve meaning across different computers or character sets. See [End-User-Defined and Private Use Area Characters](end-user-defined-characters.md) for further cautions about the use of EUDC and PUA characters.

## Related topics

<dl> <dt>

[End-User-Defined and Private Use Area Characters](end-user-defined-characters.md)
</dt> </dl>

 

 



