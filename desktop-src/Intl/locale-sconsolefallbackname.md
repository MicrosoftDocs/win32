---
description: LOCALE\_SCONSOLEFALLBACKNAME
ms.assetid: 36465a1c-085f-4f80-ad3d-5be6eaefe943
title: LOCALE_SCONSOLEFALLBACKNAME
ms.topic: article
ms.date: 05/31/2018
---

# LOCALE\_SCONSOLEFALLBACKNAME

**Windows Vista and later:** Preferred locale to use for console display. The maximum number of characters allowed for this string is 85, including a terminating null character.

> [!Note]  
> In general, applications should not make direct use of LOCALE\_SCONSOLEFALLBACKNAME data. To determine what language resources to use in a console window, an application should call either [SetThreadUILanguage](/windows/desktop/api/Winnls/nf-winnls-setthreaduilanguage) or [SetThreadPreferredUILanguages](/windows/desktop/api/Winnls/nf-winnls-setthreadpreferreduilanguages). These functions use the console fallback data as a factor in choosing a language that is legible in the console, but it is not the sole determinant. In particular, the console is limited to displaying characters from a single code page. For example, el-GR for Greek (Greece) is a valid console language, but if the current console code page is Latin-1 (code page 1252) the console displays Greek text mostly as a series of character-not-found symbols.

 

If the language corresponding to this locale is supported in the console, the value is the same as that for [LOCALE\_SNAME](locale-sname.md), that is, the locale itself can be used for console display. However, the console cannot display languages that can be rendered only with [Uniscribe](uniscribe.md). For example, the console cannot display Arabic or the various Indic languages. Therefore, the LOCALE\_SCONSOLEFALLBACKNAME value for locales corresponding to these languages is different from the value for LOCALE\_SNAME.

For predefined locales, if the fallback value is different from the value for the locale itself, the value for the neutral locale is used. A specific locale is associated with both a language and a country/region, while a neutral locale is associated with a language but is not associated with any country/region. For example, ar-SA falls back to "en", not to "en-US". This policy of using neutral locales is implemented consistently for predefined locales and is strongly recommended for custom locales. However, the policy is not enforced. For a custom locale, your application can use a specific locale instead of a neutral locale as a fallback.

> [!Note]  
> None of the functions described in [Calling the "Locale Name" Functions](calling-the--locale-name--functions.md) accept neutral locales as inputs. Thus LOCALE\_SCONSOLEFALLBACKNAME data is of very limited use. In particular, neither [**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa) nor [**GetLocaleInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoex) accepts neutral locales as inputs.

 

 

 



