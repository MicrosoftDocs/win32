---
Description: While the system uses UTC-based time internally, your applications will generally display the local time, which is the date and time of day for your time zone.
ms.assetid: a6570ec5-ac77-427a-86d9-32cbecc62e37
title: Local Time
ms.topic: article
ms.date: 05/31/2018
---

# Local Time

While the system uses UTC-based time internally, your applications will generally display the **local time**, which is the date and time of day for your time zone. Therefore, to ensure correct results, you must be aware of whether a function expects to receive a UTC-based time or a local time, and whether the function returns a UTC-based time or a local time.

The current time-zone settings control how the system converts between UTC and local time. You can retrieve the current time-zone settings by using the [**GetTimeZoneInformation**](https://msdn.microsoft.com/library/ms724421(v=VS.85).aspx) function. The function copies the result to a [**TIME\_ZONE\_INFORMATION**](https://msdn.microsoft.com/library/ms725481(v=VS.85).aspx) structure and returns a value indicating whether local time is currently in standard time or daylight saving time (DST). You can set the time-zone settings by using the [**SetTimeZoneInformation**](https://msdn.microsoft.com/library/ms724944(v=VS.85).aspx) function. To support boundaries for daylight saving time that change from year to year, use the [**GetTimeZoneInformationForYear**](https://msdn.microsoft.com/library/Bb540851(v=VS.85).aspx), [**GetDynamicTimeZoneInformation**](https://msdn.microsoft.com/library/ms724318(v=VS.85).aspx) and [**SetDynamicTimeZoneInformation**](https://msdn.microsoft.com/library/ms724932(v=VS.85).aspx) functions.

To retrieve the local time, use the [**GetLocalTime**](https://msdn.microsoft.com/library/ms724338(v=VS.85).aspx) function. **GetLocalTime** converts the system time to a local time based on the current time-zone settings and copies the result to a [**SYSTEMTIME**](https://msdn.microsoft.com/library/ms724950(v=VS.85).aspx) structure. You can set the system time by using the [**SetLocalTime**](https://msdn.microsoft.com/library/ms724936(v=VS.85).aspx) function. **SetLocalTime** assumes you have specified a local time and converts to UTC before setting the system time.

When you call [**SetLocalTime**](https://msdn.microsoft.com/library/ms724936(v=VS.85).aspx), the system uses the current time zone information, including the daylight saving time setting, to perform the conversion. Note that the system uses the daylight saving time setting of the current time, not the new time you are setting. Therefore, to ensure the correct result, call **SetLocalTime** a second time, now that the first call has updated the daylight saving time setting.

To convert a UTC-based time to a local time, use the [**SystemTimeToTzSpecificLocalTime**](https://msdn.microsoft.com/library/ms724949(v=VS.85).aspx) function. To convert a local time to a UTC-based time, use the [**TzSpecificLocalTimeToSystemTime**](https://msdn.microsoft.com/library/ms725485(v=VS.85).aspx) function.

 

 



