---
description: All fonts use a character set. A character set contains punctuation marks, numerals, uppercase and lowercase letters, and all other printable characters. Each element of a character set is identified by a number.
ms.assetid: 7989c59e-2ec6-4d1a-bb86-f4037ca32764
title: Character Sets Used by Fonts
ms.topic: article
ms.date: 05/31/2018
---

# Character Sets Used by Fonts

All fonts use a character set. A character set contains punctuation marks, numerals, uppercase and lowercase letters, and all other printable characters. Each element of a character set is identified by a number.

Most character sets in use are supersets of the U.S. ASCII character set, which defines characters for the 96 numeric values from 32 through 127. There are five major groups of character sets:

-   Windows
-   Unicode
-   OEM (original equipment manufacturer)
-   Symbol
-   Vendor-specific

## Windows Character Set

The Windows character set is the most commonly used character set. It is essentially equivalent to the ANSI character set. The blank character is the first character in the Windows character set. It has a hexadecimal value of 0x20 (decimal 32). The last character in the Windows character set has a hexadecimal value of 0xFF (decimal 255).

Many fonts specify a default character. Whenever a request is made for a character that is not in the font, the system provides this default character. Many fonts using the Windows character set specify the period (.) as the default character. TrueType and OpenType fonts typically use an open box as the default character.

Fonts use a break character called a quad to separate words and justify text. Most fonts using the Windows character set specify that the blank character will serve as the break character.

## Unicode Character Set

The Windows character set uses 8 bits to represent each character; therefore, the maximum number of characters that can be expressed using 8 bits is 256 (2^8). This is usually sufficient for Western languages, including the diacritical marks used in French, German, Spanish, and other languages. However, Eastern languages employ thousands of separate characters, which cannot be encoded by using a single-byte coding scheme. With the proliferation of computer commerce, double-byte coding schemes were developed so that characters could be represented in 8-bit, 16-bit, 24-bit, or 32-bit sequences. This requires complicated passing algorithms; even so, using different code sets could yield entirely different results on two different computers.

To address the problem of multiple coding schemes, the Unicode standard for data representation was developed. A 16-bit character coding scheme, Unicode can represent 65,536 (2^16) characters, which is enough to include all languages in computer commerce today, as well as punctuation marks, mathematical symbols, and room for expansion. Unicode establishes a unique code for every character to ensure that character translation is always accurate.

## OEM Character Set

The OEM character set is typically used in full-screen MS-DOS sessions for screen display. Characters 32 through 127 are usually the same in the OEM, U.S. ASCII, and Windows character sets. The other characters in the OEM character set (0 through 31 and 128 through 255) correspond to the characters that can be displayed in a full-screen MS-DOS session. These characters are generally different from the Windows characters.

## Symbol Character Set

The Symbol character set contains special characters typically used to represent mathematical and scientific formulas.

## Vendor-Specific Character Sets

Many printers and other output devices provide fonts based on character sets that differ from the Windows and OEM setsfor example, the Extended Binary Coded Decimal Interchange Code (EBCDIC) character set. To use one of these character sets, the printer driver translates from the Windows character set to the vendor-specific character set.

 

 



