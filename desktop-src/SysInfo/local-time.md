---
description: While the system uses UTC-based time internally, your applications will generally display the local time, which is the date and time of day for your time zone.
ms.assetid: a6570ec5-ac77-427a-86d9-32cbecc62e37
title: Local Time
ms.topic: article
ms.date: 05/31/2018
---

# Local Time

While the system uses UTC-based time internally, your applications will generally display the **local time**, which is the date and time of day for your time zone. Therefore, to ensure correct results, you must be aware of whether a function expects to receive a UTC-based time or a local time, and whether the function returns a UTC-based time or a local time.

The current time-zone settings control how the system converts between UTC and local time. You can retrieve the current time-zone settings by using the [**GetTimeZoneInformation**](/windows/win32/api/timezoneapi/nf-timezoneapi-gettimezoneinformation) function. The function copies the result to a [**TIME\_ZONE\_INFORMATION**](/windows/win32/api/timezoneapi/ns-timezoneapi-time_zone_information) structure and returns a value indicating whether local time is currently in standard time or daylight saving time (DST). You can set the time-zone settings by using the [**SetTimeZoneInformation**](/windows/win32/api/timezoneapi/nf-timezoneapi-settimezoneinformation) function. To support boundaries for daylight saving time that change from year to year, use the [**GetTimeZoneInformationForYear**](/windows/win32/api/timezoneapi/nf-timezoneapi-gettimezoneinformationforyear), [**GetDynamicTimeZoneInformation**](/windows/win32/api/timezoneapi/nf-timezoneapi-getdynamictimezoneinformation) and [**SetDynamicTimeZoneInformation**](/windows/win32/api/timezoneapi/nf-timezoneapi-setdynamictimezoneinformation) functions.

To retrieve the local time, use the [**GetLocalTime**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getlocaltime) function. **GetLocalTime** converts the system time to a local time based on the current time-zone settings and copies the result to a [**SYSTEMTIME**](/windows/win32/api/minwinbase/ns-minwinbase-systemtime) structure. You can set the system time by using the [**SetLocalTime**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-setlocaltime) function. **SetLocalTime** assumes you have specified a local time and converts to UTC before setting the system time.

When you call [**SetLocalTime**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-setlocaltime), the system uses the current time zone information, including the daylight saving time setting, to perform the conversion. Note that the system uses the daylight saving time setting of the current time, not the new time you are setting. Therefore, to ensure the correct result, call **SetLocalTime** a second time, now that the first call has updated the daylight saving time setting.

To convert a UTC-based time to a local time, use the [**SystemTimeToTzSpecificLocalTime**](/windows/win32/api/timezoneapi/nf-timezoneapi-systemtimetotzspecificlocaltime) function. To convert a local time to a UTC-based time, use the [**TzSpecificLocalTimeToSystemTime**](/windows/win32/api/timezoneapi/nf-timezoneapi-tzspecificlocaltimetosystemtime) function.

 

 
