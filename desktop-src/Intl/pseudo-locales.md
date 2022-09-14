---
description: 'Windows Vista and later: NLS defines several pseudo-locales for use in addition to the existing Windows locales.'
ms.assetid: 8ec3038e-da18-47fc-a689-dd9162a41faa
title: Pseudo-Locales
ms.topic: article
ms.date: 05/31/2018
---

# Pseudo-Locales

**Windows Vista and later:** NLS defines several pseudo-locales for use in addition to the existing Windows locales. Use these pseudo-locales for testing the localization of your applications. For implementation details, see [Using Pseudo-Locales for Localization Testing](using-pseudo-locales-for-localization-testing.md).

## Supported Pseudo-Locales

The pseudo-locales supported by NLS are:

-   Base pseudo-locale
-   Mirrored (right-to-left) pseudo-locale
-   East Asian-language pseudo-locale

Choose the particular pseudo-locale to use based on its code page assignments and the strings for localization, for example, month names, day names. Data for each pseudo-locale includes not only relevant code pages and day and month strings for localization, but also data for several other test cases for NLS. The test cases examine the following types of data:

-   9-bit [locale identifiers](locale-identifiers.md). Pseudo-locales provide a good opportunity to test the operation of 9-bit locale identifiers.
-   Strings from languages that must use small fonts. Because of limitations in the graphics device interface (GDI), the user interface font for some languages is smaller than optimal. Pseudo-locales include several strings from these languages, combined with strings from languages with more standard font handling. You can use these strings in testing to determine how a GDI-limited font renders.
-   Unusual string lengths. Some locale information constants, for example, [LOCALE\_SLIST](locale-slist.md) and [LOCALE\_ICURRENCY](locale-icurrency.md), have conventional limits on string size. The pseudo-locales support the examination of varied string lengths.
-   Alternate sorts. Pseudo-locales can be used to test alternate sort functionality when the alternate [sort order identifier](sort-order-identifiers.md) differs from the base sort order identifier that is usually associated with the locale.

## Pseudo-locale Names and Identifiers

The pseudo-locales have [locale names](locale-names.md) that are chosen from the private use space to avoid conflict with possible strings introduced into the International Organization for Standardization (ISO) 639 and ISO 3166 standards. Each pseudo-locale also has its own locale identifier. The following table provides the names and identifiers for the defined pseudo-locales.



| Pseudo-locale       | Locale name | Locale identifier |
|---------------------|-------------|-------------------|
| Base                | qps-ploc    | 0501              |
| Mirrored            | qps-plocm   | 09ff              |
| East Asian-language | qps-ploca   | 05fe              |



 

## Example

The following example shows text displayed for a base pseudo-locale:

\[Шěđлеśđαỳ !!!\], 8 ōf \[Μäŕςћ !!\] ōf 2006

## Related topics

<dl> <dt>

[Locales and Languages](locales-and-languages.md)
</dt> <dt>

[Locale Identifiers](locale-identifiers.md)
</dt> <dt>

[Locale Names](locale-names.md)
</dt> <dt>

[Sort Order Identifiers](sort-order-identifiers.md)
</dt> <dt>

[Using Pseudo-Locales for Localization Testing](using-pseudo-locales-for-localization-testing.md)
</dt> </dl>

 

 



