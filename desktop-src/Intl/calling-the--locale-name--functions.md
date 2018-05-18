---
Description: 'Windows Vista introduces a large number of functions that use locale names instead of locale identifiers.'
ms.assetid: 'e88c31b2-b1da-40ae-b512-67b8ad409b95'
title: 'Calling the "Locale Name" Functions'
---

# Calling the "Locale Name" Functions

Windows Vista introduces a large number of functions that use [locale names](locale-names.md) instead of [locale identifiers](locale-identifiers.md). These new functions provide good support for [supplemental locales](custom-locales.md), and several of them provide additional functionality not available in the older NLS functions. Some of them, such as the new enumeration functions, also represent design improvements.

> [!Note]  
> Applications that are intended to run only on Windows Vista and later should use the "locale name" functions in preference to the NLS functions that use locale identifiers.

 

The following table lists the locale name functions along with the older functions that they can replace.



| Functions using locale names                                     | Functions using locale identifiers                                                             |
|------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [**CompareStringEx**](comparestringex.md)                       | [**CompareString**](comparestring.md)                                                         |
| [**EnumCalendarInfoExEx**](enumcalendarinfoexex.md)             | [**EnumCalendarInfo**](enumcalendarinfo.md), [**EnumCalendarInfoEx**](enumcalendarinfoex.md) |
| [**EnumDateFormatsExEx**](enumdateformatsexex.md)               | [**EnumDateFormats**](enumdateformats.md), [**EnumDateFormatsEx**](enumdateformatsex.md)     |
| [**EnumSystemLocalesEx**](enumsystemlocalesex.md)               | [**EnumSystemLocales**](enumsystemlocales.md)                                                 |
| [**EnumTimeFormatsEx**](enumtimeformatsex.md)                   | [**EnumTimeFormats**](enumtimeformats.md)                                                     |
| [**FindNLSStringEx**](findnlsstringex.md)                       | [**FindNLSString**](findnlsstring.md)                                                         |
| [**GetCalendarInfoEx**](getcalendarinfoex.md)                   | [**GetCalendarInfo**](getcalendarinfo.md)                                                     |
| [**GetCurrencyFormatEx**](getcurrencyformatex.md)               | [**GetCurrencyFormat**](getcurrencyformat.md)                                                 |
| [**GetDateFormatEx**](getdateformatex.md)                       | [**GetDateFormat**](getdateformat.md)                                                         |
| [**GetDurationFormatEx**](getdurationformatex.md)               | [**GetDurationFormat**](getdurationformat.md)                                                 |
| [**GetLocaleInfoEx**](getlocaleinfoex.md)                       | [**GetLocaleInfo**](getlocaleinfo.md)                                                         |
| [**GetNLSVersionEx**](getnlsversionex.md)                       | [**GetNLSVersion**](getnlsversion.md)                                                         |
| [**GetNumberFormatEx**](getnumberformatex.md)                   | [**GetNumberFormat**](getnumberformat.md)                                                     |
| [**GetSystemDefaultLocaleName**](getsystemdefaultlocalename.md) | [**GetSystemDefaultLCID**](getsystemdefaultlcid.md)                                           |
| [**GetTimeFormatEx**](gettimeformatex.md)                       | [**GetTimeFormat**](gettimeformat.md)                                                         |
| [**GetUserDefaultLocaleName**](getuserdefaultlocalename.md)     | [**GetUserDefaultLCID**](getuserdefaultlcid.md)                                               |
| [**IsValidLocaleName**](isvalidlocalename.md)                   | [**IsValidLocale**](isvalidlocale.md)                                                         |
| [**LCMapStringEx**](lcmapstringex.md)                           | [**LCMapString**](lcmapstring.md)                                                             |



 

## Example

An example showing the use of several functions based on locale names can be found in [NLS: Name-based APIs Sample](nls--name-based-apis-sample.md).

## Related topics

<dl> <dt>

[Using National Language Support](using-national-language-support.md)
</dt> </dl>

 

 



