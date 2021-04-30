---
description: Each locale has a default calendar type (data type CALTYPE) associated with it. A locale can also have an alternate calendar type. For details of calendar types, see Calendar Type Information.
ms.assetid: 32772cba-eb30-4cd3-adaf-57fb8425a6d5
title: Date and Calendar
ms.topic: article
ms.date: 05/31/2018
---

# Date and Calendar

Each [locale](locales-and-languages.md) has a default calendar type (data type CALTYPE) associated with it. A locale can also have an alternate calendar type. For details of calendar types, see [Calendar Type Information](calendar-type-information.md).

> [!Note]  
> To use an alternate calendar type for a locale, your application must set the [LOCALE\_IOPTIONALCALENDAR](locale-ioptionalcalendar.md) constant to the alternate calendar type for the locale.

 

Most locales use the standard Gregorian calendar and a set number of date formats. These default choices for date formats are available for display by using the [**EnumDateFormatsEx**](/windows/desktop/api/Winnls/nf-winnls-enumdateformatsexa) or [**EnumDateFormatsExEx**](/windows/desktop/api/Winnls/nf-winnls-enumdateformatsexex) function.

Some locales require special considerations when creating a complete list of format choices. Some of these locales require text strings to be inserted in the date format string, while others require a completely different method of computation of the values. An application addresses these special requirements by the addition of certain locale information types and calendar types.

For details about implementing dates and calendars in your applications, see [Retrieving Time and Date Information](retrieving-time-and-date-information.md).

## Related topics

<dl> <dt>

[About National Language Support](about-national-language-support.md)
</dt> <dt>

[Calendar Type Information](calendar-type-information.md)
</dt> <dt>

[Retrieving Time and Date Information](retrieving-time-and-date-information.md)
</dt> <dt>

[**EnumDateFormatsEx**](/windows/desktop/api/Winnls/nf-winnls-enumdateformatsexa)
</dt> <dt>

[**EnumDateFormatsExEx**](/windows/desktop/api/Winnls/nf-winnls-enumdateformatsexex)
</dt> </dl>

 

 



