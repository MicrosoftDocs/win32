---
Description: System time is the current date and time of day.
ms.assetid: 1a1e251e-2375-4134-bbd8-1e4670b9f9d2
title: System Time
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# System Time

*System time* is the current date and time of day. The system keeps time so that your applications have ready access to accurate time. The system bases system time on *coordinated universal time* (UTC). UTC-based time is loosely defined as the current date and time of day in Greenwich, England.

When the system first starts, it sets the system time to a value based on the real-time clock of the computer and then regularly updates the time. To retrieve the system time, use the [**GetSystemTime**](https://msdn.microsoft.com/en-us/library/ms724390(v=VS.85).aspx) function. **GetSystemTime** copies the time to a [**SYSTEMTIME**](https://msdn.microsoft.com/en-us/library/ms724950(v=VS.85).aspx) structure that contains individual members for month, day, year, weekday, hour, minute, second, and milliseconds. It is easy to display this format to a user.

You can also obtain the system time in file time format using the [**GetSystemTimeAsFileTime**](https://msdn.microsoft.com/en-us/library/ms724397(v=VS.85).aspx) function. **GetSystemTimeAsFileTime** copies the time to a [**FILETIME**](https://msdn.microsoft.com/en-us/library/ms724284(v=VS.85).aspx) structure.

To set the system time, use the [**SetSystemTime**](https://msdn.microsoft.com/en-us/library/ms724942(v=VS.85).aspx) function. **SetSystemTime** assumes you have specified a UTC-based time.

The [**GetSystemTimeAdjustment**](https://msdn.microsoft.com/en-us/library/ms724394(v=VS.85).aspx) and [**SetSystemTimeAdjustment**](https://msdn.microsoft.com/en-us/library/ms724943(v=VS.85).aspx) functions synchronize the time-of-day clock with another time source using a periodic time adjustment applied at each clock interrupt.

Note that the system can periodically refresh the time by synchronizing with a time source. Because the system time can be adjusted either forward or backward, do not compare system time readings to determine elapsed time. Instead, use one of the methods described in [Windows Time](windows-time.md).

 

 



