---
description: This topic includes instructions for using the NLS functions in your applications to retrieve time and date information, as well as duration data. If your application must persist data, see Using Persistent Locale Data.
ms.assetid: 1880ff8f-110c-4661-8b1f-afe1d8d2a38d
title: Retrieving Time and Date Information
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Time and Date Information

This topic includes instructions for using the NLS functions in your applications to retrieve [time and date](time-and-date.md) information, as well as duration data. If your application must persist data, see [Using Persistent Locale Data](using-persistent-locale-data.md).

**Windows Vista and later:** The functions discussed in this topic can retrieve data from [custom locales](custom-locales.md). In particular, they can be used to customize time and date formats. For example, it is possible to have a time format such as "hhHmm'ss''", resulting in time strings like "12H34'12''".

## Retrieve Time Information

Your application can get strings for any time in a format that is appropriate for the current locale by using the [**GetTimeFormat**](/windows/desktop/api/datetimeapi/nf-datetimeapi-gettimeformata) and [**GetTimeFormatEx**](/windows/desktop/api/datetimeapi/nf-datetimeapi-gettimeformatex) functions. Either function checks each of the time values in a valid [**SYSTEMTIME**](/windows/win32/api/minwinbase/ns-minwinbase-systemtime) structure to determine that it is within the appropriate range of values, ignoring the date portions of the structure. If any of the time values are outside the correct range, the function fails with the code ERROR\_INVALID\_PARAMETER. The function returns no errors for a bad format string, but simply forms the best possible time string.

> [!Note]  
> The NLS time functions do not include milliseconds as part of a formatted time string.

 

To obtain the time format without performing any actual formatting, the application can use the [**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa) or [**GetLocaleInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoex) function, specifying the [LOCALE\_STIMEFORMAT](locale-stime-constants.md) constant in the call.

**Use Time Markers**

Examples of time markers are "AM" and "PM" for English (United States) and "de." and "du." for Spanish (Mexico). If TIME\_NOTIMEMARKER is specified in the call to [**GetTimeFormat**](/windows/desktop/api/datetimeapi/nf-datetimeapi-gettimeformata) or [**GetTimeFormatEx**](/windows/desktop/api/datetimeapi/nf-datetimeapi-gettimeformatex), the function removes the separator(s) preceding and following the time marker. If a time marker exists and the TIME\_NOTIMEMARKER flag is not set in the call, the function localizes the time marker based on the specified locale identifier.

**Remove Separators Preceding Minutes and Seconds**

Your application can call [**GetTimeFormat**](/windows/desktop/api/datetimeapi/nf-datetimeapi-gettimeformata) or [**GetTimeFormatEx**](/windows/desktop/api/datetimeapi/nf-datetimeapi-gettimeformatex) with TIME\_NOMINUTESORSECONDS or TIME\_NOSECONDS specified to remove the separators following the minutes and/or seconds elements.

**Use 24-Hour Time Format**

If your application is supporting 24-hour time format, it can call [**GetTimeFormat**](/windows/desktop/api/datetimeapi/nf-datetimeapi-gettimeformata) or [**GetTimeFormatEx**](/windows/desktop/api/datetimeapi/nf-datetimeapi-gettimeformatex) with TIME\_FORCE24HOURFORMAT. Unless the TIME\_NOTIMEMARKER flag is set, the function displays any existing time marker.

## Retrieve Date Information

An application can retrieve strings for any date in a format that is appropriate for the current locale by using the [**GetDateFormat**](/windows/desktop/api/datetimeapi/nf-datetimeapi-getdateformata) and [**GetDateFormatEx**](/windows/desktop/api/datetimeapi/nf-datetimeapi-getdateformatex) functions. Either function checks each of the date values year, month, day, and day of week in a valid [**SYSTEMTIME**](/windows/win32/api/minwinbase/ns-minwinbase-systemtime) structure, ignoring the time portions of structure. The day name, abbreviated day name, month name, and abbreviated month name are all localized based on the locale identifier. If the day of the week is incorrect, the function uses the correct value, and returns no error. If any of the other date values are outside the correct range, the function fails with the code ERROR\_INVALID\_PARAMETER. The function returns no errors for a bad format string, but simply forms the best possible date string.

If the application requires the date format for a particular calendar, it should use [**GetCalendarInfo**](/windows/desktop/api/Winnls/nf-winnls-getcalendarinfoa) or [**GetCalendarInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getcalendarinfoex), passing the appropriate [**Calendar Identifier**](calendar-identifiers.md). To return all date formats for a particular calendar, the application can use [**EnumCalendarInfoEx**](/windows/desktop/api/Winnls/nf-winnls-enumcalendarinfoexa), [**EnumCalendarInfoExEx**](/windows/desktop/api/Winnls/nf-winnls-enumcalendarinfoexex), [**EnumDateFormatsEx**](/windows/desktop/api/Winnls/nf-winnls-enumdateformatsexa), or [**EnumDateFormatsExEx**](/windows/desktop/api/Winnls/nf-winnls-enumdateformatsexex).

**Specify an Alternate Calendar**

The application can call [**GetDateFormat**](/windows/desktop/api/datetimeapi/nf-datetimeapi-getdateformata) or [**GetDateFormatEx**](/windows/desktop/api/datetimeapi/nf-datetimeapi-getdateformatex) with the flag DATE\_USE\_ALT\_CALENDAR to use the default format for the specified alternate calendar. If there is no default format for the alternate calendar, the function uses the user overrides.

To get the date format for an alternate calendar, the application can use [**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa) or [**GetLocaleInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoex) with the [LOCALE\_IOPTIONALCALENDAR](locale-ioptionalcalendar.md) constant.

**Specify Date Type**

If the application wants to use short date format, it specifies DATE\_SHORTDATE in the call to [**GetDateFormat**](/windows/desktop/api/datetimeapi/nf-datetimeapi-getdateformata) or [**GetDateFormatEx**](/windows/desktop/api/datetimeapi/nf-datetimeapi-getdateformatex). A long date format can be obtained by specifying DATE\_LONGDATE in the function call. If neither flag is specified, and the *lpFormat* is set to **NULL**, the function uses DATE\_SHORTDATE as the default.

To obtain the short and long date format for the default locale calendar, the application should use the [**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa) or [**GetLocaleInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoex) function with the [LOCALE\_SSHORTDATE](locale-sshortdate.md) or [LOCALE\_SLONGDATE](locale-slongdate.md) constant.

**Specify the Date Format Picture**

The application can specify a date format picture that [**GetDateFormat**](/windows/desktop/api/datetimeapi/nf-datetimeapi-getdateformata) or [**GetDateFormatEx**](/windows/desktop/api/datetimeapi/nf-datetimeapi-getdateformatex) uses to form the date string. If the date format for the specified locale is required, the application can call the function with *lpFormat* set to **NULL**. If the parameter is not set to **NULL**, the function uses the locale only for information not specified in the format picture string, for example, the day and month names for the locale.

The application can enclose any text that should remain in its exact form within single quotation marks. A single quotation mark can also be used as an escape character to allow the mark itself to be displayed in the date string. However, the escape sequence must be enclosed within two single quotation marks. For example, to display the date as "May '93", the format string is: "MMMM ''''yy ".

## Retrieve Duration Information

**Windows Vista and later:** The functions [**GetDurationFormat**](/windows/desktop/api/Winnls/nf-winnls-getdurationformat) and [**GetDurationFormatEx**](/windows/desktop/api/Winnls/nf-winnls-getdurationformatex) are available to obtain duration formats for locales, including custom locales. To obtain the default duration format for a locale, the application should use the [**GetLocaleInfo**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoa) or [**GetLocaleInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getlocaleinfoex) function with the [LOCALE\_SDURATION](locale-sduration.md) constant.

## Related topics

<dl> <dt>

[Using National Language Support](about-national-language-support.md)
</dt> <dt>

[Time and Date](time-and-date.md)
</dt> <dt>

[Using Persistent Locale Data](using-persistent-locale-data.md)
</dt> </dl>

 

 
