---
description: Custom Locales
ms.assetid: 110efeab-c02f-4244-8950-a975cfc91e8a
title: Custom Locales
ms.topic: article
ms.date: 05/31/2018
---

# Custom Locales

**Windows Vista and later:** Custom locales support international properties providing a more culturally appropriate user experience than those furnished with the standard locales shipped by Microsoft with the operating system. Use of custom locales allows administrators to extend the Microsoft-provided set of locales or to replace the data in a locale that ships with Windows, for example, currency symbols or names of the months of the year.

The two types of custom locales are supplemental locales and replacement locales. Supplemental locales are custom locales that allow corporations, universities, governments, and other third parties to create locale data not available in the shipping operating system. Replacement locales are custom locales that ship with the operating system without changing the [locale identifiers](locale-identifiers.md) or [locale names](locale-names.md).

You can use the Locale Builder utility provided by NLS to build custom locales. For more information, see [Microsoft Locale Builder](https://www.microsoft.com/download/details.aspx?id=41158). Instructions for using custom locales in your applications are provided in [Working with Custom Locales](working-with-custom-locales.md).

## Comparison of Custom Locale Types

The following table describes the differences between supplemental and replacement locales.



| Item                                                                                                                           | Supplemental locale                                                                                                                                                                                                                   | Replacement locale                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Calendars                                                                                                                      | Can include any of the calendars provided by Microsoft. At least one of the calendars provided must be the Gregorian Localized calendar.                                                                                              | Can include any of the calendars provided by Microsoft. At least one of the calendars provided must be the Gregorian Localized calendar, and the collection must include the default calendar of the replaced locale. |
| Sorting                                                                                                                        | Can use any of the Microsoft-supplied sorts.                                                                                                                                                                                          | Retains the sorting behavior of the locale being replaced.                                                                                                                                                            |
| Day and month names                                                                                                            | Can be customized only for the standard Gregorian calendar, not for non-Gregorian calendars and not for specialized Gregorian calendars, such as the Gregorian Middle East French calendar.                                           | Same as for supplemental locale.                                                                                                                                                                                      |
| Language name ([LOCALE\_SLANGUAGE](locale-slanguage.md) or [LOCALE\_SLOCALIZEDLANGUAGENAME](locale-slocalized-constants.md)) | Returns [LOCALE\_SNATIVELANGNAME](locale-snative-constants.md) or [LOCALE\_SNATIVELANGUAGENAME](locale-snative-constants.md).                                                                                                       | Keeps the language name of the locale being replaced.                                                                                                                                                                 |
| Locale identifier                                                                                                              | Set to [LOCALE\_CUSTOM\_UNSPECIFIED](locale-custom-constants.md) unless the locale is the user's currently selected Standards and Formats locale, in which case it is set to [LOCALE\_CUSTOM\_DEFAULT](locale-custom-constants.md). | Keeps the locale identifier of the locale being replaced.                                                                                                                                                             |
| Locale name                                                                                                                    | Arbitrary; should fit the pattern discussed in [Locale Names](locale-names.md).                                                                                                                                                      | Keeps the locale name of the locale being replaced.                                                                                                                                                                   |



 

## Supplemental Locale Examples



| Locale name    | Description                                                                                                                                                                                                                                                                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| en-CA-fabricam | Fabricam is a Canadian PC manufacturer with offices worldwide. To provide consistent user interface behavior for all its computers, the company develops a locale to use company-wide.                                                                                                                                                          |
| fr-US          | Woodlawn Bank uses Windows XP Embedded for its automated teller machines (ATMs), which the bank ships all over North America with user interfaces in French, English, and Spanish. To provide a consistent experience, the bank creates a locale for French in the United States that has United States formats but French day and month names. |



 

## Replacement Locale Example



| Locale name | Description                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| en-US       | Fabricam is a Canadian PC manufacturer with offices worldwide. To provide consistent user interface behavior for all its computers, the company develops a locale to use company-wide. It uses a 24-hour clock, but otherwise behaves like the supported English (United States) locale. Because the custom locale is so similar to the supported locale, Fabricam decides to implement it as a replacement locale instead of a supplemental locale. |



 

## Related topics

<dl> <dt>

[Locales and Languages](locales-and-languages.md)
</dt> <dt>

[Working with Custom Locales](working-with-custom-locales.md)
</dt> </dl>

 

 



