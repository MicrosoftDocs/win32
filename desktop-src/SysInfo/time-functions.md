---
Description: The following functions are used with system time.
ms.assetid: 3733f611-c6a1-4d48-b21e-ada3490c5de1
title: Time Functions
ms.topic: article
ms.date: 05/31/2018
---

# Time Functions

The following functions are used with system time.



| Function                                                                   | Description                                                                                            |
|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**GetSystemTime**](https://msdn.microsoft.com/library/ms724390(v=VS.85).aspx)                                     | Retrieves the current system date and time in UTC format.                                              |
| [**GetSystemTimeAdjustment**](https://msdn.microsoft.com/library/ms724394(v=VS.85).aspx)                 | Determines whether the system is applying periodic time adjustments to its time-of-day clock.          |
| [**GetTimeFormat**](https://docs.microsoft.com/windows/desktop/api/datetimeapi/nf-datetimeapi-gettimeformata)                                    | Formats a system time as a time string for a specified locale.                                         |
| [**NtQuerySystemTime**](/windows/desktop/api/Winternl/nf-winternl-ntquerysystemtime)                             | Returns the system time.                                                                               |
| [**RtlLocalTimeToSystemTime**](/windows/desktop/api/Winternl/nf-winternl-rtllocaltimetosystemtime)               | Converts the specified local time to system time.                                                      |
| [**RtlTimeToSecondsSince1970**](/windows/desktop/api/Winternl/nf-winternl-rtltimetosecondssince1970)             | Converts the specified system time to the number of seconds since the first second of January 1, 1970. |
| [**SetSystemTime**](https://msdn.microsoft.com/library/ms724942(v=VS.85).aspx)                                     | Sets the current system time and date.                                                                 |
| [**SetSystemTimeAdjustment**](https://msdn.microsoft.com/library/ms724943(v=VS.85).aspx)                 | Enables or disables periodic time adjustments to the system's time-of-day clock.                       |
| [**SystemTimeToFileTime**](https://msdn.microsoft.com/library/ms724948(v=VS.85).aspx)                       | Converts a system time to a file time.                                                                 |
| [**SystemTimeToTzSpecificLocalTime**](https://msdn.microsoft.com/library/ms724949(v=VS.85).aspx) | Converts a UTC time to a specified time zone's corresponding local time.                               |
| [**TzSpecificLocalTimeToSystemTime**](https://msdn.microsoft.com/library/ms725485(v=VS.85).aspx) | Converts a local time to a UTC time.                                                                   |



 

The following functions are used with local time.



| Function                                                                                           | Description                                                                                                                                     |
|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EnumDynamicTimeZoneInformation**](https://msdn.microsoft.com/library/Hh706893(v=VS.85).aspx)                           | Enumerates dynamic daylight saving time information entries stored in the registry.                                                             |
| [**FileTimeToLocalFileTime**](/windows/desktop/api/FileAPI/nf-fileapi-filetimetolocalfiletime)                                         | Converts a UTC file time to a local file time.                                                                                                  |
| [**GetDynamicTimeZoneInformation**](https://msdn.microsoft.com/library/ms724318(v=VS.85).aspx)                             | Retrieves the current time zone and dynamic daylight saving time settings.                                                                      |
| [**GetDynamicTimeZoneInformationEffectiveYears**](https://msdn.microsoft.com/library/Hh706894(v=VS.85).aspx) | Retrieves a range, expressed in years, for which a [**DYNAMIC\_TIME\_ZONE\_INFORMATION**](https://msdn.microsoft.com/library/ms724253(v=VS.85).aspx) has valid entries. |
| [**GetLocalTime**](https://msdn.microsoft.com/library/ms724338(v=VS.85).aspx)                                                               | Retrieves the current local date and time.                                                                                                      |
| [**GetTimeZoneInformation**](https://msdn.microsoft.com/library/ms724421(v=VS.85).aspx)                                           | Retrieves the current time zone settings.                                                                                                       |
| [**GetTimeZoneInformationForYear**](https://msdn.microsoft.com/library/Bb540851(v=VS.85).aspx)                             | Retrieves the time zone settings for the specified year and time zone.                                                                          |
| [**RtlLocalTimeToSystemTime**](/windows/desktop/api/Winternl/nf-winternl-rtllocaltimetosystemtime)                                       | Converts the specified local time to system time.                                                                                               |
| [**SetDynamicTimeZoneInformation**](https://msdn.microsoft.com/library/ms724932(v=VS.85).aspx)                             | Sets the current time zone and dynamic daylight saving time settings.                                                                           |
| [**SetLocalTime**](https://msdn.microsoft.com/library/ms724936(v=VS.85).aspx)                                                               | Sets the current local time and date.                                                                                                           |
| [**SetTimeZoneInformation**](https://msdn.microsoft.com/library/ms724944(v=VS.85).aspx)                                           | Sets the current time zone settings.                                                                                                            |
| [**SystemTimeToTzSpecificLocalTime**](https://msdn.microsoft.com/library/ms724949(v=VS.85).aspx)                         | Converts a UTC time to a specified time zone's corresponding local time.                                                                        |
| [**SystemTimeToTzSpecificLocalTimeEx**](https://msdn.microsoft.com/library/JJ206642(v=VS.85).aspx)                     | Converts a UTC time with dynamic daylight saving time settings to a specified time zone's corresponding local time.                             |
| [**TzSpecificLocalTimeToSystemTime**](https://msdn.microsoft.com/library/ms725485(v=VS.85).aspx)                         | Converts a local time to a UTC time.                                                                                                            |
| [**TzSpecificLocalTimeToSystemTimeEx**](https://msdn.microsoft.com/library/JJ206643(v=VS.85).aspx)                     | Converts a local time with dynamic daylight saving time settings to UTC time.                                                                   |



 

The following functions are used with file time.



| Function                                                   | Description                                                                                                     |
|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [**CompareFileTime**](/windows/desktop/api/FileAPI/nf-fileapi-comparefiletime)                 | Compares two file times.                                                                                        |
| [**FileTimeToLocalFileTime**](/windows/desktop/api/FileAPI/nf-fileapi-filetimetolocalfiletime) | Converts a UTC file time to a local file time.                                                                  |
| [**FileTimeToSystemTime**](https://msdn.microsoft.com/library/ms724280(v=VS.85).aspx)       | Converts a file time to system time format.                                                                     |
| [**GetFileTime**](/windows/desktop/api/FileAPI/nf-fileapi-getfiletime)                         | Retrieves the date and time that the specified file or directory was created, last accessed, and last modified. |
| [**GetSystemTimeAsFileTime**](https://msdn.microsoft.com/library/ms724397(v=VS.85).aspx) | Retrieves the current system date and time in UTC format.                                                       |
| [**LocalFileTimeToFileTime**](/windows/desktop/api/FileAPI/nf-fileapi-localfiletimetofiletime) | Converts a local file time to a file time based on UTC.                                                         |
| [**SetFileTime**](/windows/desktop/api/FileAPI/nf-fileapi-setfiletime)                         | Sets the date and time that the specified file or directory was created, last accessed, or last modified.       |
| [**SystemTimeToFileTime**](https://msdn.microsoft.com/library/ms724948(v=VS.85).aspx)       | Converts a system time to a file time.                                                                          |



 

The following functions are used with MS-DOS date and time.



| Function                                               | Description                                          |
|--------------------------------------------------------|------------------------------------------------------|
| [**DosDateTimeToFileTime**](/windows/desktop/api/Winbase/nf-winbase-dosdatetimetofiletime) | Converts MS-DOS date and time values to a file time. |
| [**FileTimeToDosDateTime**](/windows/desktop/api/Winbase/nf-winbase-filetimetodosdatetime) | Converts a file time to MS-DOS date and time values. |



 

The following functions are used with Windows time.



| Function                                 | Description                                                                                           |
|------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**GetSystemTimes**](https://msdn.microsoft.com/library/ms724400(v=VS.85).aspx) | Retrieves system timing information.                                                                  |
| [**GetTickCount**](https://msdn.microsoft.com/library/ms724408(v=VS.85).aspx)     | Retrieves the number of milliseconds that have elapsed since the system was started, up to 49.7 days. |
| [**GetTickCount64**](https://msdn.microsoft.com/library/ms724411(v=VS.85).aspx) | Retrieves the number of milliseconds that have elapsed since the system was started.                  |



 

The following functions are used with high-resolution performance counters.



| Function                                                              | Description                                                             |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------|
| [**QueryPerformanceCounter**](https://msdn.microsoft.com/library/ms644904(v=VS.85).aspx)     | Retrieves the current value of the high-resolution performance counter. |
| [**QueryPerformanceFrequency**](https://msdn.microsoft.com/library/ms644905(v=VS.85).aspx) | Retrieves the frequency of the high-resolution performance counter.     |



 

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
| [**QueryUnbiasedInterruptTime**](https://msdn.microsoft.com/library/Ee662307(v=VS.85).aspx)               | Gets the current unbiased interrupt-time count. The unbiased interrupt-time count does not include time the system spends in sleep or hibernation.                                                                                                    |
| [**QueryUnbiasedInterruptTimePrecise**](/windows/desktop/api/realtimeapiset/nf-realtimeapiset-queryunbiasedinterrupttimeprecise) | Gets the current unbiased interrupt-time count, in a more precise form than [**QueryUnbiasedInterruptTime**](https://msdn.microsoft.com/library/Ee662307(v=VS.85).aspx) does. The unbiased interrupt-time count does not include time the system spends in sleep or hibernation. |



 

 

 



