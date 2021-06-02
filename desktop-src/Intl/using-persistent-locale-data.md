---
description: Using Persistent Locale Data
ms.assetid: f62402d6-31de-4ff7-9538-7925a007a089
title: Using Persistent Locale Data
ms.topic: article
ms.date: 05/31/2018
---

# Using Persistent Locale Data

A globalized application often persists or transmits data, for example, time and date. When deciding how your application should handle data persistence, remember that data is not guaranteed to be the same from computer to computer or between runs of the application. This is true for both [locales](locales-and-languages.md) that ship with Windows and [custom locales](custom-locales.md).

Design of the application must take into account a variety of locale-related data changes that can occur. For example:

-   Currency symbols can change as countries adopt the Euro.
-   Regional preferences can change. For example, the format d/m/y might change to the format m/d/y for a particular locale.
-   The spelling of day names can change due to spelling reforms. Additionally, casing can change for month or day names.

## Use Locale-Independent Formats for Storage and Data Interchange

An application that persists data should use locale-independent formats for storage and data interchange. Examples are hard-coded or standard formats; the invariant locale [LOCALE\_NAME\_INVARIANT](locale-name-constants.md); and binary storage formats.

If persistent sorting data is required, the application must use the [**CompareStringOrdinal**](/windows/desktop/api/Stringapiset/nf-stringapiset-comparestringordinal) function. Remember that an invariant format does not remain invariant for [sorting](sorting.md), only for locale and calendar data.

## Use the User Default Locale for Data Presentation

To present persistent data, it is best for the application to reformat the data using the user default locale. Use of this locale allows user overrides. For more information, see [LOCALE\_USER\_DEFAULT](locale-user-default.md).

## Related topics

<dl> <dt>

[Using National Language Support](using-national-language-support.md)
</dt> <dt>

[Custom Locales](custom-locales.md)
</dt> <dt>

[Sorting](sorting.md)
</dt> </dl>

 

 



