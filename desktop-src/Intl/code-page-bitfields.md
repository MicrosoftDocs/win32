---
description: The code page bitfields are used in the FONTSIGNATURE and LOCALESIGNATURE structures.Note  All locales do not support code pages.
ms.assetid: 830b1a88-cb0c-4719-b857-4cc2cd67dd5d
title: Code Page Bitfields
ms.topic: reference
ms.date: 05/31/2018
---

# Code Page Bitfields

The code page bitfields are used in the [**FONTSIGNATURE**](/windows/win32/api/wingdi/ns-wingdi-fontsignature) and [**LOCALESIGNATURE**](/windows/win32/api/wingdi/ns-wingdi-localesignature) structures.

> [!Note]  
> All locales do not support code pages. The bitfields described in this topic do not apply to Unicode locales. To determine supported scripts for a locale, your application can use the locale identifier constant [LOCALE\_SSCRIPTS](locale-sscripts.md) with [**GetLocaleInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoex).

> [!Note]  
> The presence of a bit in a code page bitfield does not necessarily mean that all strings for a locale can be encoded in that code page without loss. To preserve data without loss, using Unicode UTF-8 or UTF-16 is recommended.

| Bit          | wingdi.h define | Code page | Description                                           |
|--------------|-----------------|-----------|-------------------------------------------------------|
| 0            | *FS_LATIN1*     | 1252      | Latin 1                                               |
| 1            | *FS_LATIN2*     | 1250      | Latin 2: Eastern Europe                               |
| 2            | *FS_CYRILLIC*   | 1251      | Cyrillic                                              |
| 3            | *FS_GREEK*      | 1253      | Greek                                                 |
| 4            | *FS_TURKISH*    | 1254      | Turkish                                               |
| 5            | *FS_HEBREW*     | 1255      | Hebrew                                                |
| 6            | *FS_ARABIC*     | 1256      | Arabic                                                |
| 7            | *FS_BALTIC*     | 1257      | Windows Baltic                                        |
| 8            | *FS_VIETNAMESE* | 1258      | Vietnamese                                            |
| 9 – 15       |                 |           | Reserved for Alternate ANSI                           |
| 16           | *FS_THAI*       | 874       | Thai                                                  |
| 17           | *FS_JISJAPAN*   | 932       | JIS/Japan                                             |
| 18           | *FS_CHINESESIMP*| 936       | Chinese: Simplified chars—PRC and Singapore           |
| 19           | *FS_WANSUNG*    | 949       | Korean Wansung                                        |
| 20           | *FS_CHINESETRAD*| 950       | Chinese: Traditional chars—Taiwan and Hong Kong SAR   |
| 21           | *FS_JOHAB*      | 1361      | Korean Johab                                          |
| 22 – 28      |                 |           | Reserved for Alternate ANSI or OEM                    |
| 29           |                 |           | Macintosh Character Set (US Roman)                    |
| 30           |                 |           | OEM Character Set                                     |
| 31           | *FS_SYMBOL*     |           | Symbol Character Set                                  |
| 32 – 47      |                 |           | Reserved for OEM                                      |
| 48           |                 | 869       | IBM Greek                                             |
| 49           |                 | 866       | MS-DOS Russian                                        |
| 50           |                 | 865       | MS-DOS Nordic                                         |
| 51           |                 | 864       | Arabic                                                |
| 52           |                 | 863       | MS-DOS Canadian French                                |
| 53           |                 | 862       | Hebrew                                                |
| 54           |                 | 861       | MS-DOS Icelandic                                      |
| 55           |                 | 860       | MS-DOS Portuguese                                     |
| 56           |                 | 857       | IBM Turkish                                           |
| 57           |                 | 855       | IBM Cyrillic; primarily Russian                       |
| 58           |                 | 852       | Latin 2                                               |
| 59           |                 | 775       | MS-DOS Baltic                                         |
| 60           |                 | 737       | Greek; former 437 G                                   |
| 61           |                 | 708       | Arabic; ASMO 708                                      |
| 62           |                 | 850       | WE/Latin 1                                            |
| 63           |                 | 437       | US                                                    |
