---
description: These values are used with the ImmGetConversionStatus and ImmSetConversionStatus functions.
ms.assetid: 0b0afb4e-f7aa-4ca6-9174-21983b2a422b
title: IME Conversion Mode Values
ms.topic: article
ms.date: 05/31/2018
---

# IME Conversion Mode Values

These values are used with the [**ImmGetConversionStatus**](/windows/desktop/api/Imm/nf-imm-immgetconversionstatus) and [**ImmSetConversionStatus**](/windows/desktop/api/Imm/nf-imm-immsetconversionstatus) functions.



| Bit                      | Meaning                                                                                   |
|--------------------------|-------------------------------------------------------------------------------------------|
| IME\_CMODE\_ALPHANUMERIC | Alphanumeric input mode. This is the default, defined as 0x0000.                          |
| IME\_CMODE\_CHARCODE     | Set to 1 if character code input mode; 0 if not.                                          |
| IME\_CMODE\_EUDC         | Set to 1 if EUDC conversion mode; 0 if not.                                               |
| IME\_CMODE\_FIXED        | **Windows Me/98, Windows 2000, Windows XP:** Set to 1 if fixed conversion mode; 0 if not. |
| IME\_CMODE\_FULLSHAPE    | Set to 1 if full shape mode; 0 if half shape mode.                                        |
| IME\_CMODE\_HANJACONVERT | Set to 1 if HANJA convert mode; 0 if not.                                                 |
| IME\_CMODE\_KATAKANA     | Set to 1 if KATAKANA mode; 0 if HIRAGANA mode.                                            |
| IME\_CMODE\_NATIVE       | Set to 1 if NATIVE mode; 0 if ALPHANUMERIC mode.                                          |
| IME\_CMODE\_NOCONVERSION | Set to 1 to prevent processing of conversions by IME; 0 if not.                           |
| IME\_CMODE\_ROMAN        | Set to 1 if ROMAN input mode; 0 if not.                                                   |
| IME\_CMODE\_SOFTKBD      | Set to 1 if Soft Keyboard mode; 0 if not.                                                 |
| IME\_CMODE\_SYMBOL       | Set to 1 if SYMBOL conversion mode; 0 if not.                                             |



 

All other bits are reserved.

 

 



