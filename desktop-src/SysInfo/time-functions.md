---
Description: The following functions are used with system time.
ms.assetid: 3733f611-c6a1-4d48-b21e-ada3490c5de1
title: Time Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Time Functions

The following functions are used with system time.



| Function                                                                   | Description                                                                                            |
|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**GetSystemTime**](/windows/win32/Winbase/?branch=master)                                     | Retrieves the current system date and time in UTC format.                                              |
| [**GetSystemTimeAdjustment**](/windows/win32/Winbase/?branch=master)                 | Determines whether the system is applying periodic time adjustments to its time-of-day clock.          |
| [**GetTimeFormat**](https://msdn.microsoft.com/library/windows/desktop/dd318130)                                    | Formats a system time as a time string for a specified locale.                                         |
| [**NtQuerySystemTime**](/windows/win32/Winternl/nf-winternl-ntquerysystemtime?branch=master)                             | Returns the system time.                                                                               |
| [**RtlLocalTimeToSystemTime**](/windows/win32/Winternl/nf-winternl-rtllocaltimetosystemtime?branch=master)               | Converts the specified local time to system time.                                                      |
| [**RtlTimeToSecondsSince1970**](/windows/win32/Winternl/nf-winternl-rtltimetosecondssince1970?branch=master)             | Converts the specified system time to the number of seconds since the first second of January 1, 1970. |
| [**SetSystemTime**](/windows/win32/Winbase/?branch=master)                                     | Sets the current system time and date.                                                                 |
| [**SetSystemTimeAdjustment**](/windows/win32/Winbase/?branch=master)                 | Enables or disables periodic time adjustments to the system's time-of-day clock.                       |
| [**SystemTimeToFileTime**](/windows/win32/Winbase/?branch=master)                       | Converts a system time to a file time.                                                                 |
| [**SystemTimeToTzSpecificLocalTime**](/windows/win32/Winbase/?branch=master) | Converts a UTC time to a specified time zone's corresponding local time.                               |
| [**TzSpecificLocalTimeToSystemTime**](/windows/win32/Winbase/?branch=master) | Converts a local time to a UTC time.                                                                   |



 

The following functions are used with local time.



| Function                                                                                           | Description                                                                                                                                     |
|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EnumDynamicTimeZoneInformation**](/windows/win32/Winbase/?branch=master)                           | Enumerates dynamic daylight saving time information entries stored in the registry.                                                             |
| [**FileTimeToLocalFileTime**](/windows/win32/FileAPI/nf-fileapi-filetimetolocalfiletime?branch=master)                                         | Converts a UTC file time to a local file time.                                                                                                  |
| [**GetDynamicTimeZoneInformation**](/windows/win32/Winbase/?branch=master)                             | Retrieves the current time zone and dynamic daylight saving time settings.                                                                      |
| [**GetDynamicTimeZoneInformationEffectiveYears**](/windows/win32/Winbase/?branch=master) | Retrieves a range, expressed in years, for which a [**DYNAMIC\_TIME\_ZONE\_INFORMATION**](/windows/win32/WinBase/?branch=master) has valid entries. |
| [**GetLocalTime**](/windows/win32/Winbase/?branch=master)                                                               | Retrieves the current local date and time.                                                                                                      |
| [**GetTimeZoneInformation**](/windows/win32/Winbase/?branch=master)                                           | Retrieves the current time zone settings.                                                                                                       |
| [**GetTimeZoneInformationForYear**](/windows/win32/Winbase/?branch=master)                             | Retrieves the time zone settings for the specified year and time zone.                                                                          |
| [**RtlLocalTimeToSystemTime**](/windows/win32/Winternl/nf-winternl-rtllocaltimetosystemtime?branch=master)                                       | Converts the specified local time to system time.                                                                                               |
| [**SetDynamicTimeZoneInformation**](/windows/win32/Winbase/?branch=master)                             | Sets the current time zone and dynamic daylight saving time settings.                                                                           |
| [**SetLocalTime**](/windows/win32/Winbase/?branch=master)                                                               | Sets the current local time and date.                                                                                                           |
| [**SetTimeZoneInformation**](/windows/win32/Winbase/?branch=master)                                           | Sets the current time zone settings.                                                                                                            |
| [**SystemTimeToTzSpecificLocalTime**](/windows/win32/Winbase/?branch=master)                         | Converts a UTC time to a specified time zone's corresponding local time.                                                                        |
| [**SystemTimeToTzSpecificLocalTimeEx**](/windows/win32/Winbase/?branch=master)                     | Converts a UTC time with dynamic daylight saving time settings to a specified time zone's corresponding local time.                             |
| [**TzSpecificLocalTimeToSystemTime**](/windows/win32/Winbase/?branch=master)                         | Converts a local time to a UTC time.                                                                                                            |
| [**TzSpecificLocalTimeToSystemTimeEx**](/windows/win32/Winbase/?branch=master)                     | Converts a local time with dynamic daylight saving time settings to UTC time.                                                                   |



 

The following functions are used with file time.



| Function                                                   | Description                                                                                                     |
|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [**CompareFileTime**](/windows/win32/FileAPI/nf-fileapi-comparefiletime?branch=master)                 | Compares two file times.                                                                                        |
| [**FileTimeToLocalFileTime**](/windows/win32/FileAPI/nf-fileapi-filetimetolocalfiletime?branch=master) | Converts a UTC file time to a local file time.                                                                  |
| [**FileTimeToSystemTime**](/windows/win32/FileAPI/?branch=master)       | Converts a file time to system time format.                                                                     |
| [**GetFileTime**](/windows/win32/FileAPI/nf-fileapi-getfiletime?branch=master)                         | Retrieves the date and time that the specified file or directory was created, last accessed, and last modified. |
| [**GetSystemTimeAsFileTime**](/windows/win32/Winbase/?branch=master) | Retrieves the current system date and time in UTC format.                                                       |
| [**LocalFileTimeToFileTime**](/windows/win32/FileAPI/nf-fileapi-localfiletimetofiletime?branch=master) | Converts a local file time to a file time based on UTC.                                                         |
| [**SetFileTime**](/windows/win32/FileAPI/nf-fileapi-setfiletime?branch=master)                         | Sets the date and time that the specified file or directory was created, last accessed, or last modified.       |
| [**SystemTimeToFileTime**](/windows/win32/Winbase/?branch=master)       | Converts a system time to a file time.                                                                          |



 

The following functions are used with MS-DOS date and time.



| Function                                               | Description                                          |
|--------------------------------------------------------|------------------------------------------------------|
| [**DosDateTimeToFileTime**](/windows/win32/Winbase/nf-winbase-dosdatetimetofiletime?branch=master) | Converts MS-DOS date and time values to a file time. |
| [**FileTimeToDosDateTime**](/windows/win32/Winbase/nf-winbase-filetimetodosdatetime?branch=master) | Converts a file time to MS-DOS date and time values. |



 

The following functions are used with Windows time.



| Function                                 | Description                                                                                           |
|------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**GetSystemTimes**](getsystemtimes.md) | Retrieves system timing information.                                                                  |
| [**GetTickCount**](/windows/win32/Winbase/?branch=master)     | Retrieves the number of milliseconds that have elapsed since the system was started, up to 49.7 days. |
| [**GetTickCount64**](/windows/win32/Winbase/?branch=master) | Retrieves the number of milliseconds that have elapsed since the system was started.                  |



 

The following functions are used with high-resolution performance counters.



| Function                                                              | Description                                                             |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------|
| [**QueryPerformanceCounter**](_win32_queryperformancecounter_cpp)     | Retrieves the current value of the high-resolution performance counter. |
| [**QueryPerformanceFrequency**](_win32_queryperformancefrequency_cpp) | Retrieves the frequency of the high-resolution performance counter.     |



 

The following functions are used with the auxiliary performance counter.



| Function                                                                                           | Description                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**QueryAuxiliaryCounterFrequency**](/windows/win32/realtimeapiset/nf-realtimeapiset-queryauxiliarycounterfrequency?branch=master)                           | Queries the auxiliary counter frequency.                                                                                                                                                                      |
| [**ConvertAuxiliaryCounterToPerformanceCounter**](/windows/win32/realtimeapiset/nf-realtimeapiset-convertauxiliarycountertoperformancecounter?branch=master) | Converts the specified auxiliary counter value to the corresponding performance counter value; optionally provides the estimated conversion error in nanoseconds due to latencies and maximum possible drift. |
| [**ConvertPerformanceCounterToAuxiliaryCounter**](/windows/win32/realtimeapiset/nf-realtimeapiset-convertperformancecountertoauxiliarycounter?branch=master) | Converts the specified performance counter value to the corresponding auxiliary counter value; optionally provides the estimated conversion error in nanoseconds due to latencies and maximum possible drift. |



 

The following function is used with interrupt time.



| Function                                                                       | Description                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**QueryInterruptTime**](/windows/win32/realtimeapiset/nf-realtimeapiset-queryinterrupttime?branch=master)                               | Gets the current interrupt-time count.                                                                                                                                                                                                                |
| [**QueryInterruptTimePrecise**](/windows/win32/realtimeapiset/nf-realtimeapiset-queryinterrupttimeprecise?branch=master)                 | Gets the current interrupt-time count, in a more precise form than [**QueryInterruptTime**](/windows/win32/realtimeapiset/nf-realtimeapiset-queryinterrupttime?branch=master) does.                                                                                                                             |
| [**QueryUnbiasedInterruptTime**](/windows/win32/winbase/nf-wdm-kequeryunbiasedinterrupttimeprecise?branch=master)               | Gets the current unbiased interrupt-time count. The unbiased interrupt-time count does not include time the system spends in sleep or hibernation.                                                                                                    |
| [**QueryUnbiasedInterruptTimePrecise**](/windows/win32/realtimeapiset/nf-realtimeapiset-queryunbiasedinterrupttimeprecise?branch=master) | Gets the current unbiased interrupt-time count, in a more precise form than [**QueryUnbiasedInterruptTime**](/windows/win32/winbase/nf-wdm-kequeryunbiasedinterrupttimeprecise?branch=master) does. The unbiased interrupt-time count does not include time the system spends in sleep or hibernation. |



 

 

 



