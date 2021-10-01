---
description: This topic describes the calendar type information (CALTYPE data type) used in the EnumCalendarInfo, EnumCalendarInfoEx, EnumCalendarInfoExEx, GetCalendarInfo, and GetCalendarInfoEx functions.
ms.assetid: 33361a97-0f27-477a-a0ee-3d4d3aaeaacf
title: Calendar Type Information
ms.topic: article
ms.date: 05/31/2018
---

# Calendar Type Information

This topic describes the calendar type information (CALTYPE data type) used in the [**EnumCalendarInfo**](/windows/desktop/api/Winnls/nf-winnls-enumcalendarinfoa), [**EnumCalendarInfoEx**](/windows/desktop/api/Winnls/nf-winnls-enumcalendarinfoexa), [**EnumCalendarInfoExEx**](/windows/desktop/api/Winnls/nf-winnls-enumcalendarinfoexex), [**GetCalendarInfo**](/windows/desktop/api/Winnls/nf-winnls-getcalendarinfoa), and [**GetCalendarInfoEx**](/windows/desktop/api/Winnls/nf-winnls-getcalendarinfoex) functions. Some of these values are also used by the [**SetCalendarInfo**](/windows/desktop/api/Winnls/nf-winnls-setcalendarinfoa) function.

The following CALTYPE constants can be used in combination with any other CALTYPE constants.



| Constant                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CAL\_NOUSEROVERRIDE          | **Windows Me/98, Windows 2000:** Use the system default instead of the user's choice.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| CAL\_RETURN\_GENITIVE\_NAMES | **Windows 7 and later:** Retrieve the result from [**GetCalendarInfo**](/windows/desktop/api/Winnls/nf-winnls-getcalendarinfoa) in the form of genitive names of months, which are the names used when the month names are combined with other items. For example, in Ukrainian the equivalent of January is written "Січень" when the month is named alone. However, when the month name is used in combination, for example, in a date such as January 5th, 2003, the genitive form of the name is used. For the Ukrainian example, the genitive month name is displayed as "5 січня 2003". For more information, see [LOCALE\_RETURN\_GENITIVE\_NAMES](locale-return-constants.md). |
| CAL\_RETURN\_NUMBER          | **Windows Me/98, Windows 2000:** Retrieve the result from [**GetCalendarInfo**](/windows/desktop/api/Winnls/nf-winnls-getcalendarinfoa) as a number instead of a string. This is only valid for values beginning with CAL\_I.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| CAL\_USE\_CP\_ACP            | **Windows Me/98, Windows 2000:** Use the system ANSI code page (ACP) instead of the locale code page for string translation. This is only relevant for ANSI versions of functions, for example, **EnumCalendarInfoA**.                                                                                                                                                                                                                                                                                                                                                                                                                               |



 

The following CALTYPE constants are mutually exclusive and cannot be used in combination with each other in a function call.




| Constant | Description | 
|----------|-------------|
| CAL_ICALINTVALUE | An integer value indicating the calendar type of the alternate calendar. | 
| CAL_ITWODIGITYEARMAX | <strong>Windows Me/98, Windows 2000:</strong> An integer value indicating the upper boundary of the two-digit year range. | 
| CAL_IYEAROFFSETRANGE | One or more null-terminated strings that specify the year offsets for each of the era ranges. The last string has an extra terminating null character. This value varies in format depending on the type of optional calendar. | 
| CAL_SABBREVDAYNAME1 | Abbreviated native name of the first day of the week. | 
| CAL_SABBREVDAYNAME2 | Abbreviated native name of the second day of the week. | 
| CAL_SABBREVDAYNAME3 | Abbreviated native name of the third day of the week. | 
| CAL_SABBREVDAYNAME4 | Abbreviated native name of the fourth day of the week. | 
| CAL_SABBREVDAYNAME5 | Abbreviated native name of the fifth day of the week. | 
| CAL_SABBREVDAYNAME6 | Abbreviated native name of the sixth day of the week. | 
| CAL_SABBREVDAYNAME7 | Abbreviated native name of the seventh day of the week. | 
| CAL_SABBREVERASTRING | <strong>Windows 7 and later:</strong> Abbreviated native name of an era. The full era is represented by the CAL_SERASTRING constant. | 
| CAL_SABBREVMONTHNAME1 | Abbreviated native name of the first month of the year. | 
| CAL_SABBREVMONTHNAME2 | Abbreviated native name of the second month of the year. | 
| CAL_SABBREVMONTHNAME3 | Abbreviated native name of the third month of the year. | 
| CAL_SABBREVMONTHNAME4 | Abbreviated native name of the fourth month of the year. | 
| CAL_SABBREVMONTHNAME5 | Abbreviated native name of the fifth month of the year. | 
| CAL_SABBREVMONTHNAME6 | Abbreviated native name of the sixth month of the year. | 
| CAL_SABBREVMONTHNAME7 | Abbreviated native name of the seventh month of the year. | 
| CAL_SABBREVMONTHNAME8 | Abbreviated native name of the eighth month of the year. | 
| CAL_SABBREVMONTHNAME9 | Abbreviated native name of the ninth month of the year. | 
| CAL_SABBREVMONTHNAME10 | Abbreviated native name of the tenth month of the year. | 
| CAL_SABBREVMONTHNAME11 | Abbreviated native name of the eleventh month of the year. | 
| CAL_SABBREVMONTHNAME12 | Abbreviated native name of the twelfth month of the year. | 
| CAL_SABBREVMONTHNAME13 | Abbreviated native name of the thirteenth month of the year, if it exists. | 
| CAL_SCALNAME | Native name of the alternate calendar. | 
| CAL_SDAYNAME1 | Native name of the first day of the week. | 
| CAL_SDAYNAME2 | Native name of the second day of the week. | 
| CAL_SDAYNAME3 | Native name of the third day of the week. | 
| CAL_SDAYNAME4 | Native name of the fourth day of the week. | 
| CAL_SDAYNAME5 | Native name of the fifth day of the week. | 
| CAL_SDAYNAME6 | Native name of the sixth day of the week. | 
| CAL_SDAYNAME7 | Native name of the seventh day of the week. | 
| CAL_SERASTRING | One or more null-terminated strings that specify each of the Unicode code points specifying the era associated with CAL_IYEAROFFSETRANGE. The last string has an extra terminating null character. This value varies in format depending on the type of optional calendar. | 
| CAL_SLONGDATE | Long date formats for the calendar type. | 
| CAL_SMONTHDAY | <strong>Windows 7 and later:</strong> Format of the month and day for the calendar type. The formatting is similar to that for CAL_SLONGDATE. For example, if the Month/Day pattern is the full month name followed by the day number with leading zeros, for example, "September 03", the format is "MMMM dd". Single quotation marks can be used to insert non-format characters, for example, 'de' in Spanish.<blockquote>[!Note]<br />This calendar type supports only one format.</blockquote><br /> | 
| CAL_SMONTHNAME1 | Native name of the first month of the year. | 
| CAL_SMONTHNAME2 | Native name of the second month of the year. | 
| CAL_SMONTHNAME3 | Native name of the third month of the year. | 
| CAL_SMONTHNAME4 | Native name of the fourth month of the year. | 
| CAL_SMONTHNAME5 | Native name of the fifth month of the year. | 
| CAL_SMONTHNAME6 | Native name of the sixth month of the year. | 
| CAL_SMONTHNAME7 | Native name of the seventh month of the year. | 
| CAL_SMONTHNAME8 | Native name of the eighth month of the year. | 
| CAL_SMONTHNAME9 | Native name of the ninth month of the year. | 
| CAL_SMONTHNAME10 | Native name of the tenth month of the year. | 
| CAL_SMONTHNAME11 | Native name of the eleventh month of the year. | 
| CAL_SMONTHNAME12 | Native name of the twelfth month of the year. | 
| CAL_SMONTHNAME13 | Native name of the thirteenth month of the year, if it exists. | 
| CAL_SSHORTDATE | Short date formats for the calendar type. | 
| CAL_SSHORTESTDAYNAME1 | <strong>Windows Vista and later:</strong> Short native name of the first day of the week. | 
| CAL_SSHORTESTDAYNAME2 | <strong>Windows Vista and later:</strong> Short native name of the second day of the week. | 
| CAL_SSHORTESTDAYNAME3 | <strong>Windows Vista and later:</strong> Short native name of the third day of the week. | 
| CAL_SSHORTESTDAYNAME4 | <strong>Windows Vista and later:</strong> Short native name of the fourth day of the week. | 
| CAL_SSHORTESTDAYNAME5 | <strong>Windows Vista and later:</strong> Short native name of the fifth day of the week. | 
| CAL_SSHORTESTDAYNAME6 | <strong>Windows Vista and later:</strong> Short native name of the sixth day of the week. | 
| CAL_SSHORTESTDAYNAME7 | <strong>Windows Vista and later:</strong> Short native name of the seventh day of the week. | 
| CAL_SYEARMONTH | <strong>Windows Me/98, Windows 2000:</strong> The year/month formats for the specified calendars. | 




 

> [!Note]  
> If the native name for the day of the week or for a month is an empty string, that name is identical to the name specified in the corresponding locale information and therefore is not duplicated here.

 

 

 




