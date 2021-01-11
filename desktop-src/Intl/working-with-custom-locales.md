---
description: This topic provides some instructions for handling custom locales in your applications.
ms.assetid: 2622e2b3-b952-4666-a440-85d73d11c5e0
title: Working with Custom Locales
ms.topic: article
ms.date: 05/31/2018
---

# Working with Custom Locales

This topic provides some instructions for handling [custom locales](custom-locales.md) in your applications. It is best to prepare all your source code with these considerations in mind, as your application does not control whether custom locales are installed on the operating system.

## Handle LOCALE\_STIME Constant Correctly

If you have an older application that uses [**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa) to obtain the obsolete time separator indicated by [LOCALE\_STIME](locale-stime-constants.md), the application can fail to parse the time format. Remember that the character that separates hours from minutes is distinct from the character that separates minutes from seconds.

> [!Note]  
> When programming for custom locales, remember that they are unusual. Virtually every field available to NLS has to cope with unusual behavior. For example, the time format 12H34'12'' is legitimate and generally understandable. Yet many applications make assumptions about the time separators that can break buffer lengths or display fields.

 

## Distinguish Among Supplemental Locales

All supplemental locales use the [LOCALE\_CUSTOM\_UNSPECIFIED](locale-custom-constants.md) constant for the [locale identifier](locale-identifiers.md). As a rule, [**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa) cannot distinguish among supplemental locales, but [**GetLocaleInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoex) can because it uses [locale names](locale-names.md) instead of locale identifiers. Your application can retrieve information about a particular supplemental locale only when that locale is the currently selected user locale. Then, the application can call [**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa) and pass the constant [LOCALE\_USER\_DEFAULT](locale-user-default.md) as the locale identifier.

## Handle Replacement Locales

To preserve the reliability of Windows, remember that a replacement locale supported by your application cannot modify the locale identifier of the replaced locale. Neither can a replacement locale modify the sorting properties of Windows.

Although a replacement locale can change the default calendar, it must retain the original default somewhere in the list of available calendars. For example, the Thai (Thailand) locale uses the Thai Buddhist calendar as the default. An administrator can create a replacement locale that uses the Gregorian localized calendar. However, the list of available calendars continues to contain an entry for the Thai Buddhist calendar.

For replacement locales, your application should generally consult locale-specific information instead of attempting a "shortcut" based on knowledge of a certain locale. For example, when [**GetThreadLocale**](/windows/desktop/api/Winnls/nf-winnls-getthreadlocale) retrieves the current locale as English (United States), it might actually be a replacement locale that should be allowed to take effect.

## Customize Calendars

Your applications can customize day and month names for Gregorian calendars, but not for non-Gregorian calendars. Similarly, NLS does not support creation of user-defined custom calendars. For more information, see [Date and Calendar](date-and-calendar.md).

## Handle Sorting Sequences

A supplemental locale can use any Microsoft-defined sorting sequence. A replacement locale must use the same sorting sequence as the locale it replaces. NLS does not support the creation of user-defined sorting sequences. For more information, see [Handling Sorting in Your Applications](handling-sorting-in-your-applications.md).

## Localize Custom Locale Information

NLS does not provide a mechanism for localizing custom locale information. Thus the constant [LOCALE\_SLANGUAGE](locale-slanguage.md) or [LOCALE\_SLOCALIZEDLANGUAGENAME](locale-slocalized-constants.md) used as a locale identifier for a custom locale always retrieves values associated with [LOCALE\_SNATIVELANGNAME](locale-snative-constants.md) or [LOCALE\_SNATIVELANGUAGENAME](locale-snative-constants.md).

## Related topics

<dl> <dt>

[Using National Language Support](using-national-language-support.md)
</dt> <dt>

[Custom Locales](custom-locales.md)
</dt> <dt>

[Date and Calendar](date-and-calendar.md)
</dt> <dt>

[Handling Sorting in Your Applications](handling-sorting-in-your-applications.md)
</dt> </dl>

 

 



