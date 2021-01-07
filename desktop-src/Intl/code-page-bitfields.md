---
description: The code page bitfields are used in the FONTSIGNATURE and LOCALESIGNATURE structures.Note  All locales do not support code pages.
ms.assetid: 830b1a88-cb0c-4719-b857-4cc2cd67dd5d
title: Code Page Bitfields
ms.topic: article
ms.date: 05/31/2018
---

# Code Page Bitfields

The code page bitfields are used in the [**FONTSIGNATURE**](/windows/win32/api/wingdi/ns-wingdi-fontsignature) and [**LOCALESIGNATURE**](/windows/win32/api/wingdi/ns-wingdi-localesignature) structures.

> [!Note]  
> All locales do not support code pages. The bitfields described in this topic do not apply to Unicode locales. To determine supported scripts for a locale, your application can use the locale identifier constant [LOCALE\_SSCRIPTS](locale-sscripts.md) with [**GetLocaleInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoex).

 

> [!Note]  
> The presence of a bit in a code page bitfield does not necessarily mean that all strings for a locale can be encoded in that code page without loss. To preserve data without loss, using Unicode UTF-8 or UTF-16 is recommended.

 



| Bit          | Code page | Description                                           |
|--------------|-----------|-------------------------------------------------------|
| ANSI         |           |                                                       |
| 0            | 1252      | Latin 1                                               |
| 1            | 1250      | Latin 2: Central Europe                               |
| 2            | 1251      | Cyrillic                                              |
| 3            | 1253      | Greek                                                 |
| 4            | 1254      | Turkish                                               |
| 5            | 1255      | Hebrew                                                |
| 6            | 1256      | Arabic                                                |
| 7            | 1257      | Baltic                                                |
| 8            | 1258      | Vietnamese                                            |
| 9 - 15       |           | Reserved for ANSI                                     |
| ANSI and OEM |           |                                                       |
| 16           | 874       | Thai                                                  |
| 17           | 932       | Japanese, Shift-JIS                                   |
| 18           | 936       | Simplified Chinese (PRC, Singapore)                   |
| 19           | 949       | Korean Unified Hangul Code (Hangul TongHabHyung Code) |
| 20           | 950       | Traditional Chinese (Taiwan; Hong Kong SAR, PRC)      |
| 21           | 1361      | Korean (Johab)                                        |
| 22 - 29      |           | Reserved for alternate ANSI and OEM                   |
| 30 - 31      |           | Reserved by system.                                   |
| OEM          |           |                                                       |
| 32 - 46      |           | Reserved for OEM                                      |
| 47           | 1258      | Vietnamese                                            |
| 48           | 869       | Modern Greek                                          |
| 49           | 866       | Russian                                               |
| 50           | 865       | Nordic                                                |
| 51           | 864       | Arabic                                                |
| 52           | 863       | Canadian French                                       |
| 53           | 862       |                                                       |
| 54           | 861       | Icelandic                                             |
| 55           | 860       | Portuguese                                            |
| 56           | 857       | Turkish                                               |
| 57           | 855       | Cyrillic; primarily Russian                           |
| 58           | 852       | Latin 2                                               |
| 59           | 775       | Baltic                                                |
| 60           | 737       | Greek; formerly 437G                                  |
| 61           | 708; 720  | Arabic; ASMO 708                                      |
| 62           | 850       | Multilingual Latin 1                                  |
| 63           | 437       | US                                                    |



 

 

 



