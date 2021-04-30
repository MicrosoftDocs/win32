---
description: LOCALE\_SSCRIPTS
ms.assetid: d15c501a-b77b-4446-bee6-6dbbd714b4e0
title: LOCALE_SSCRIPTS
ms.topic: article
ms.date: 05/31/2018
---

# LOCALE\_SSCRIPTS

**Windows Vista and later:** A string representing a list of scripts, using the 4-character notation used in [ISO 15924](https://www.unicode.org/iso15924/iso15924-codes.html). Each script name consists of four Latin characters and the list is arranged in alphabetical order with each name, including the last, followed by a semicolon.

[**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa) or [**GetLocaleInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoex) can be called with *LCType* set to LOCALE\_SSCRIPTS as part of a strategy to mitigate security issues related to Internationalized Domain Names (IDNs). Here are some example values:



| Locale                  | Locale/language name | Value                                                                                                  |
|-------------------------|----------------------|--------------------------------------------------------------------------------------------------------|
| English (United States) | en-US                | Latn;                                                                                                  |
| Hindi (India)           | hi-IN                | Deva;                                                                                                  |
| Japanese (Japan)        | ja-JP                | **Windows 7 and later:** Hani;Hira;Jpan;Kana;<br/> **Windows Vista:** Hani;Hira;Kana;<br/> |



 

A compound script value does not include the Latin script unless it is an essential part of the writing system used for the particular locale. Latin characters are often used in the context of locales for which they are not native, for example, for a foreign business name. In the example above for Hindi in India, the only script value is "Deva" (for "Devanagari"), although Latin characters can also appear in Hindi text. The [VerifyScripts](/windows/desktop/api/Winnls/nf-winnls-verifyscripts) function has a special flag to address this case.

 

 




