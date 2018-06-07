---
Description: The following functions are used with system time.
ms.assetid: 3733f611-c6a1-4d48-b21e-ada3490c5de1
title: Time Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Time Functions

The following functions are used with system time.



| Function                                                                   | Description                                                                                            |
|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**GetSystemTime**](/windows/desktop/api/Winbase/)                                     | Retrieves the current system date and time in UTC format.                                              |
| [**GetSystemTimeAdjustment**](/windows/desktop/api/Winbase/)                 | Determines whether the system is applying periodic time adjustments to its time-of-day clock.          |
| [**GetTimeFormat**](https://msdn.microsoft.com/library/windows/desktop/dd318130)                                    | Formats a system time as a time string for a specified locale.                                         |
| [**NtQuerySystemTime**](/windows/desktop/api/Winternl/nf-winternl-ntquerysystemtime)                             | Returns the system time.                                                                               |
| [**RtlLocalTimeToSystemTime**](/windows/desktop/api/Winternl/nf-winternl-rtllocaltimetosystemtime)               | Converts the specified local time to system time.                                                      |
| [**RtlTimeToSecondsSince1970**](/windows/desktop/api/Winternl/nf-winternl-rtltimetosecondssince1970)             | Converts the specified system time to the number of seconds since the first second of January 1, 1970. |
| [**SetSystemTime**](/windows/desktop/api/Winbase/)                                     | Sets the current system time and date.                                                                 |
| [**SetSystemTimeAdjustment**](/windows/desktop/api/Winbase/)                 | Enables or disables periodic time adjustments to the system's time-of-day clock.                       |
| [**SystemTimeToFileTime**](/windows/desktop/api/Winbase/)                       | Converts a system time to a file time.                                                                 |
| [**SystemTimeToTzSpecificLocalTime**](/windows/desktop/api/Winbase/) | Converts a UTC time to a specified time zone's corresponding local time.                               |
| [**TzSpecificLocalTimeToSystemTime**](/windows/desktop/api/Winbase/) | Converts a local time to a UTC time.                                                                   |



 

The following functions are used with local time.



| Function                                                                                           | Description                                                                                                                                     |
|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EnumDynamicTimeZoneInformation**](/windows/desktop/api/Winbase/)                           | Enumerates dynamic daylight saving time information entries stored in the registry.                                                             |
| [**FileTimeToLocalFileTime**](/windows/desktop/api/FileAPI/nf-fileapi-filetimetolocalfiletime)                                         | Converts a UTC file time to a local file time.                                                                                                  |
| [**GetDynamicTimeZoneInformation**](/windows/desktop/api/Winbase/)                             | Retrieves the current time zone and dynamic daylight saving time settings.                                                                      |
| [**GetDynamicTimeZoneInformationEffectiveYears**](/windows/desktop/api/Winbase/) | Retrieves a range, expressed in years, for which a [**DYNAMIC\_TIME\_ZONE\_INFORMATION**](/windows/desktop/api/WinBase/) has valid entries. |
| [**GetLocalTime**](/windows/desktop/api/Winbase/)                                                               | Retrieves the current local date and time.                                                                                                      |
| [**GetTimeZoneInformation**](/windows/desktop/api/Winbase/)                                           | Retrieves the current time zone settings.                                                                                                       |
| [**GetTimeZoneInformationForYear**](/windows/desktop/api/Winbase/)                             | Retrieves the time zone settings for the specified year and time zone.                                                                          |
| [**RtlLocalTimeToSystemTime**](/windows/desktop/api/Winternl/nf-winternl-rtllocaltimetosystemtime)                                       | Converts the specified local time to system time.                                                                                               |
| [**SetDynamicTimeZoneInformation**](/windows/desktop/api/Winbase/)                             | Sets the current time zone and dynamic daylight saving time settings.                                                                           |
| [**SetLocalTime**](/windows/desktop/api/Winbase/)                                                               | Sets the current local time and date.                                                                                                           |
| [**SetTimeZoneInformation**](/windows/desktop/api/Winbase/)                                           | Sets the current time zone settings.                                                                                                            |
| [**SystemTimeToTzSpecificLocalTime**](/windows/desktop/api/Winbase/)                         | Converts a UTC time to a specified time zone's corresponding local time.                                                                        |
| [**SystemTimeToTzSpecificLocalTimeEx**](/windows/desktop/api/Winbase/)                     | Converts a UTC time with dynamic daylight saving time settings to a specified time zone's corresponding local time.                             |
| [**TzSpecificLocalTimeToSystemTime**](/windows/desktop/api/Winbase/)                         | Converts a local time to a UTC time.                                                                                                            |
| [**TzSpecificLocalTimeToSystemTimeEx**](/windows/desktop/api/Winbase/)                     | Converts a local time with dynamic daylight saving time settings to UTC time.                                                                   |



 

The following functions are used with file time.



| Function                                                   | Description                                                                                                     |
|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [**CompareFileTime**](/windows/desktop/api/FileAPI/nf-fileapi-comparefiletime)                 | Compares two file times.                                                                                        |
| [**FileTimeToLocalFileTime**](/windows/desktop/api/FileAPI/nf-fileapi-filetimetolocalfiletime) | Converts a UTC file time to a local file time.                                                                  |
| [**FileTimeToSystemTime**](/windows/desktop/api/FileAPI/)       | Converts a file time to system time format.                                                                     |
| [**GetFileTime**](/windows/desktop/api/FileAPI/nf-fileapi-getfiletime)                         | Retrieves the date and time that the specified file or directory was created, last accessed, and last modified. |
| [**GetSystemTimeAsFileTime**](/windows/desktop/api/Winbase/) | Retrieves the current system date and time in UTC format.                                                       |
| [**LocalFileTimeToFileTime**](/windows/desktop/api/FileAPI/nf-fileapi-localfiletimetofiletime) | Converts a local file time to a file time based on UTC.                                                         |
| [**SetFileTime**](/windows/desktop/api/FileAPI/nf-fileapi-setfiletime)                         | Sets the date and time that the specified file or directory was created, last accessed, or last modified.       |
| [**SystemTimeToFileTime**](/windows/desktop/api/Winbase/)       | Converts a system time to a file time.                                                                          |



 

The following functions are used with MS-DOS date and time.



| Function                                               | Description                                          |
|--------------------------------------------------------|------------------------------------------------------|
| [**DosDateTimeToFileTime**](/windows/desktop/api/Winbase/nf-winbase-dosdatetimetofiletime) | Converts MS-DOS date and time values to a file time. |
| [**FileTimeToDosDateTime**](/windows/desktop/api/Winbase/nf-winbase-filetimetodosdatetime) | Converts a file time to MS-DOS date and time values. |



 

The following functions are used with Windows time.



| Function                                 | Description                                                                                           |
|------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**GetSystemTimes**](https://www.bing.com/search?q=**GetSystemTimes**) | Retrieves system timing information.                                                                  |
| [**GetTickCount**](/windows/desktop/api/Winbase/)     | Retrieves the number of milliseconds that have elapsed since the system was started, up to 49.7 days. |
| [**GetTickCount64**](/windows/desktop/api/Winbase/) | Retrieves the number of milliseconds that have elapsed since the system was started.                  |



 

The following functions are used with high-resolution performance counters.



| Function                                                              | Description                                                             |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------|
| [**QueryPerformanceCounter**](https://www.bing.com/search?q=**QueryPerformanceCounter**)     | Retrieves the current value of the high-resolution performance counter. |
| [**QueryPerformanceFrequency**](https://www.bing.com/search?q=**QueryPerformanceFrequency**) | Retrieves the frequency of the high-resolution performance counter.     |



 

The following functions are used with the auxiliary performance counter.



| Function                                                                                           | Description                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**QueryAuxiliaryCounterFrequency**](/windows/desktop/api/realtimeapiset/nf-realtimeapiset-queryauxiliarycounterfrequency)                           | Queries the auxiliary counter frequency.                                                                                                                                                                      |
| [**ConvertAuxiliaryCounterToPerformanceCounter**](/windows/desktop/api/realtimeapiset/nf-realtimeapiset-convertauxiliarycountertoperformancecounter) | Converts the specified auxiliary counter value to the corresponding performance counter value; optionally provides the estimated conversion error in nanoseconds due to latencies and maximum possible drift. |
| [**ConvertPerformanceCounterToAuxiliaryCounter**](/windows/desktop/api/realtimeapiset/nf-realtimeapiset-convertperformancecountertoauxiliarycounter) | Converts the specified performance counter value to the corresponding auxiliary counter value; optionally provides the estimated conversion error in nanoseconds due to latencies and maximum possible drift. |



 

The following function is used with interrupt time.



| Function                                                                       | Description                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**QueryInterruptTime**](/windows/desktop/api/realtimeapiset/nf-realtimeapiset-queryinterrupttime)                               | Gets the current interrupt-time count.                                                                                                                                                                                                                |
| [**QueryInterruptTimePrecise**](/windows/desktop/api/realtimeapiset/nf-realtimeapiset-queryinterrupttimeprecise)                 | Gets the current interrupt-time count, in a more precise form than [**QueryInterruptTime**](/windows/desktop/api/realtimeapiset/nf-realtimeapiset-queryinterrupttime) does.                                                                                                                             |
| [**QueryUnbiasedInterruptTime**](/windows/desktop/api/winbase/nf-wdm-kequeryunbiasedinterrupttimeprecise)               | Gets the current unbiased interrupt-time count. The unbiased interrupt-time count does not include time the system spends in sleep or hibernation.                                                                                                    |
| [**QueryUnbiasedInterruptTimePrecise**](/windows/desktop/api/realtimeapiset/nf-realtimeapiset-queryunbiasedinterrupttimeprecise) | Gets the current unbiased interrupt-time count, in a more precise form than [**QueryUnbiasedInterruptTime**](/windows/desktop/api/winbase/nf-wdm-kequeryunbiasedinterrupttimeprecise) does. The unbiased interrupt-time count does not include time the system spends in sleep or hibernation. |



 

 

 



