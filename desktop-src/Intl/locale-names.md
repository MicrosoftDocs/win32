---
description: A locale name is based on the language tagging conventions of IETF BCP 47 (Windows Vista and later), and is represented by LOCALE\_SNAME.
ms.assetid: 221aae7b-3a7c-4995-ae78-50d97de436d8
title: Locale Names
ms.topic: article
ms.date: 05/31/2018
---

# Locale Names

A [locale](locales-and-languages.md) name is based on the language tagging conventions of [IETF BCP 47](https://www.rfc-editor.org/info/bcp47) ( Windows Vista and later), and is represented by [LOCALE\_SNAME](locale-sname.md). Generally, the pattern `<language>-<REGION>` is used. Here, language is a lowercase ISO 639 language code. The codes from ISO 639-1 are used when available. Otherwise, codes from ISO 639-2/T are used. REGION specifies an uppercase ISO 3166-1 country/region identifier. For example, the locale name for English (United States) is "en-US" and the locale name for Divehi (Maldives) is "dv-MV".

> [!Note]  
> The constant [LOCALE\_NAME\_MAX\_LENGTH](locale-name-constants.md) gives the maximum length of a locale name. It includes space for a terminating null character.

If the locale is a neutral locale (no region), the [LOCALE\_SNAME](locale-sname.md) value follows the pattern `<language>`. If it is a neutral locale for which the script is significant, the pattern is `<language>-<Script>`.

If a locale must be distinguished from another locale for the same language and region using a different script, the LOCALE\_SNAME value follows the pattern `<language>-<Script>-<REGION>`, where Script is an initial-uppercase [ISO 15924](https://www.unicode.org/iso15924/iso15924-codes.html) script code. For example, the LOCALE\_SNAME value for the specific locale Uzbek (Latin, Uzbekistan) is "uz-Latn-UZ". The script component is not included in cases where a language is commonly written in only one script.

Sort orders for locales are designated using [sort order identifiers](sort-order-identifiers.md), for example, SORT\_DEFAULT. To distinguish two or more sort orders for the same language and region, the locale name follows the pattern `<language>-<REGION>\_<sort order>`. If you must distinguish both script and sort order, the name follows the pattern `<language>-<Script>-<REGION>\_<sort order>`. The default sort order is never explicitly specified, only the alternative sort order. For example, Hungarian (Hungary) with either SORT\_DEFAULT or the numerically equivalent SORT\_HUNGARIAN\_DEFAULT is designated "hu-HU". Hungarian (Hungary) with sort order SORT\_HUNGARIAN\_TECHNICAL is designated "hu-HU\_technl".

For a [replacement locale](custom-locales.md), the locale name must be the same as the name for the locale being replaced. For a supplemental locale, the locale name should follow the pattern of `<language>-<REGION>-x-<custom>` or `<language>-<Script>-<REGION>-x-<custom>`, where `<custom>` is an alphanumeric string specific to the supplemental locale. For example, a supplemental locale specific to a company called Fabricam might be called "en-US-x-fabricam".

An application can retrieve the current locale names by using the [**GetSystemDefaultLocaleName**](/windows/desktop/api/Winnls/nf-winnls-getsystemdefaultlocalename) and [**GetUserDefaultLocaleName**](/windows/desktop/api/Winnls/nf-winnls-getuserdefaultlocalename) functions. While each thread can retrieve and set its own locale identifier with [**GetThreadLocale**](/windows/desktop/api/Winnls/nf-winnls-getthreadlocale) and set it with [**SetThreadLocale**](/windows/desktop/api/Winnls/nf-winnls-setthreadlocale), there are no analogous functions to get and set locale by name.

## Related topics

[Locales and Languages](locales-and-languages.md)

[Custom Locales](custom-locales.md)

[Locale Identifiers](locale-identifiers.md)

[Sort Order Identifiers](sort-order-identifiers.md)
