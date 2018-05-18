---
Description: 'This topic defines the calendar identifiers (data type CALID) that are used to specify different calendars.'
ms.assetid: 'ba2e841e-e24e-476a-851e-a29b3af4f04d'
title: Calendar Identifiers
---

# Calendar Identifiers

This topic defines the calendar identifiers (data type CALID) that are used to specify different calendars. Your applications can use these identifiers when using the following NLS functions and callback functions, which have parameters that take the CALID data type:

-   [**ConvertSystemTimeToCalDateTime**](convertsystemtimetocaldatetime.md)
-   [**EnumCalendarInfo**](enumcalendarinfo.md)
-   [**EnumCalendarInfoEx**](enumcalendarinfoex.md)
-   [**EnumCalendarInfoExEx**](enumcalendarinfoexex.md)
-   [**EnumCalendarInfoProcEx**](intl.enumcalendarinfoprocex)
-   [**EnumDateFormatsProcEx**](intl.enumdateformatsprocex)
-   [**GetCalendarInfo**](getcalendarinfo.md)
-   [**GetCalendarInfoEx**](getcalendarinfoex.md)
-   [**GetCalendarSupportedDateRange**](getcalendarsupporteddaterange.md)
-   [**IsCalendarLeapYear**](iscalendarleapyear.md)
-   [**SetCalendarInfo**](setcalendarinfo.md)

The following values are defined. All other values are reserved. These values cannot be combined with one another.



Calendar identifier

Meaning

1

CAL\_GREGORIAN

Gregorian (localized)

2

CAL\_GREGORIAN\_US

Gregorian (English strings always)

3

CAL\_JAPAN

Japanese Emperor Era

4

CAL\_TAIWAN

Taiwan calendar

5

CAL\_KOREA

Korean Tangun Era

6

CAL\_HIJRI

Hijri (Arabic Lunar)

7

CAL\_THAI

Thai

8

CAL\_HEBREW

Hebrew (Lunar)

9

CAL\_GREGORIAN\_ME\_FRENCH

Gregorian Middle East French

10

CAL\_GREGORIAN\_ARABIC

Gregorian Arabic

11

CAL\_GREGORIAN\_XLIT\_ENGLISH

Gregorian transliterated English

12

CAL\_GREGORIAN\_XLIT\_FRENCH

Gregorian transliterated French

23

CAL\_UMALQURA

**Windows Vista and later:** Um Al Qura (Arabic lunar) calendar



 

> [!Note]  
> The gap in numbering between the identifiers CAL\_GREGORIAN\_XLIT\_FRENCH and CAL\_UMALQURA is intentional. The designator for CAL\_UMALQURA is 23, not 13.

 

In addition, [**EnumCalendarInfo**](enumcalendarinfo.md) and [**EnumCalendarInfoEx**](enumcalendarinfoex.md) allow the use of the value ENUM\_ALL\_CALENDARS to request an enumeration of all applicable calendars.

Value

Meaning

0xffffffff

ENUM\_ALL\_CALENDARS

All applicable calendars for the specified locale



 

 

 



