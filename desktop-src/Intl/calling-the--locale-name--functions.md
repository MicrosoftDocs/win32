---
Description: Windows Vista introduces a large number of functions that use locale names instead of locale identifiers.
ms.assetid: e88c31b2-b1da-40ae-b512-67b8ad409b95
title: Calling the "Locale Name" Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Calling the "Locale Name" Functions

Windows Vista introduces a large number of functions that use [locale names](locale-names.md) instead of [locale identifiers](locale-identifiers.md). These new functions provide good support for [supplemental locales](custom-locales.md), and several of them provide additional functionality not available in the older NLS functions. Some of them, such as the new enumeration functions, also represent design improvements.

> [!Note]  
> Applications that are intended to run only on Windows Vista and later should use the "locale name" functions in preference to the NLS functions that use locale identifiers.

 

The following table lists the locale name functions along with the older functions that they can replace.



| Functions using locale names                                     | Functions using locale identifiers                                                             |
|------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [**CompareStringEx**](/windows/win32/Stringapiset/nf-stringapiset-comparestringex?branch=master)                       | [**CompareString**](/windows/win32/Winnls/nf-stringapiset-comparestringw?branch=master)                                                         |
| [**EnumCalendarInfoExEx**](/windows/win32/Winnls/nf-winnls-enumcalendarinfoexex?branch=master)             | [**EnumCalendarInfo**](/windows/win32/Winnls/nf-winnls-enumcalendarinfoa?branch=master), [**EnumCalendarInfoEx**](/windows/win32/Winnls/nf-winnls-enumcalendarinfoexa?branch=master) |
| [**EnumDateFormatsExEx**](/windows/win32/Winnls/nf-winnls-enumdateformatsexex?branch=master)               | [**EnumDateFormats**](/windows/win32/Winnls/nf-winnls-enumdateformatsa?branch=master), [**EnumDateFormatsEx**](/windows/win32/Winnls/nf-winnls-enumdateformatsexa?branch=master)     |
| [**EnumSystemLocalesEx**](/windows/win32/Winnls/nf-winnls-enumsystemlocalesex?branch=master)               | [**EnumSystemLocales**](/windows/win32/Winnls/nf-winnls-enumsystemlocalesa?branch=master)                                                 |
| [**EnumTimeFormatsEx**](/windows/win32/Winnls/nf-winnls-enumtimeformatsex?branch=master)                   | [**EnumTimeFormats**](/windows/win32/Winnls/nf-winnls-enumtimeformatsa?branch=master)                                                     |
| [**FindNLSStringEx**](/windows/win32/Winnls/nf-winnls-findnlsstringex?branch=master)                       | [**FindNLSString**](/windows/win32/Winnls/nf-winnls-findnlsstring?branch=master)                                                         |
| [**GetCalendarInfoEx**](/windows/win32/Winnls/nf-winnls-getcalendarinfoex?branch=master)                   | [**GetCalendarInfo**](/windows/win32/Winnls/nf-winnls-getcalendarinfoa?branch=master)                                                     |
| [**GetCurrencyFormatEx**](/windows/win32/Winnls/nf-winnls-getcurrencyformatex?branch=master)               | [**GetCurrencyFormat**](/windows/win32/Winnls/nf-winnls-getcurrencyformata?branch=master)                                                 |
| [**GetDateFormatEx**](/windows/win32/datetimeapi/nf-datetimeapi-getdateformatex?branch=master)                       | [**GetDateFormat**](/windows/win32/datetimeapi/nf-datetimeapi-getdateformata?branch=master)                                                         |
| [**GetDurationFormatEx**](/windows/win32/Winnls/nf-winnls-getdurationformatex?branch=master)               | [**GetDurationFormat**](/windows/win32/Winnls/nf-winnls-getdurationformat?branch=master)                                                 |
| [**GetLocaleInfoEx**](/windows/win32/Winnls/nf-winnls-getlocaleinfoex?branch=master)                       | [**GetLocaleInfo**](/windows/win32/Winnls/nf-winnls-getlocaleinfoa?branch=master)                                                         |
| [**GetNLSVersionEx**](/windows/win32/Winnls/nf-winnls-getnlsversionex?branch=master)                       | [**GetNLSVersion**](/windows/win32/Winnls/nf-winnls-getnlsversion?branch=master)                                                         |
| [**GetNumberFormatEx**](/windows/win32/Winnls/nf-winnls-getnumberformatex?branch=master)                   | [**GetNumberFormat**](/windows/win32/Winnls/nf-winnls-getnumberformata?branch=master)                                                     |
| [**GetSystemDefaultLocaleName**](/windows/win32/Winnls/nf-winnls-getsystemdefaultlocalename?branch=master) | [**GetSystemDefaultLCID**](/windows/win32/Winnls/nf-winnls-getsystemdefaultlcid?branch=master)                                           |
| [**GetTimeFormatEx**](/windows/win32/datetimeapi/nf-datetimeapi-gettimeformatex?branch=master)                       | [**GetTimeFormat**](/windows/win32/datetimeapi/nf-datetimeapi-gettimeformata?branch=master)                                                         |
| [**GetUserDefaultLocaleName**](/windows/win32/Winnls/nf-winnls-getuserdefaultlocalename?branch=master)     | [**GetUserDefaultLCID**](/windows/win32/Winnls/nf-winnls-getuserdefaultlcid?branch=master)                                               |
| [**IsValidLocaleName**](/windows/win32/Winnls/nf-winnls-isvalidlocalename?branch=master)                   | [**IsValidLocale**](/windows/win32/Winnls/nf-winnls-isvalidlocale?branch=master)                                                         |
| [**LCMapStringEx**](/windows/win32/Winnls/nf-winnls-lcmapstringex?branch=master)                           | [**LCMapString**](/windows/win32/Winnls/nf-winnls-lcmapstringa?branch=master)                                                             |



 

## Example

An example showing the use of several functions based on locale names can be found in [NLS: Name-based APIs Sample](nls--name-based-apis-sample.md).

## Related topics

<dl> <dt>

[Using National Language Support](using-national-language-support.md)
</dt> </dl>

 

 



