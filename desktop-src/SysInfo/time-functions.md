---
Description: 'The following functions are used with system time.'
ms.assetid: '3733f611-c6a1-4d48-b21e-ada3490c5de1'
title: Time Functions
---

# Time Functions

The following functions are used with system time.



| Function                                                                   | Description                                                                                            |
|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**GetSystemTime**](getsystemtime.md)                                     | Retrieves the current system date and time in UTC format.                                              |
| [**GetSystemTimeAdjustment**](getsystemtimeadjustment.md)                 | Determines whether the system is applying periodic time adjustments to its time-of-day clock.          |
| [**GetTimeFormat**](https://msdn.microsoft.com/library/windows/desktop/dd318130)                                    | Formats a system time as a time string for a specified locale.                                         |
| [**NtQuerySystemTime**](ntquerysystemtime.md)                             | Returns the system time.                                                                               |
| [**RtlLocalTimeToSystemTime**](rtllocaltimetosystemtime.md)               | Converts the specified local time to system time.                                                      |
| [**RtlTimeToSecondsSince1970**](rtltimetosecondssince1970.md)             | Converts the specified system time to the number of seconds since the first second of January 1, 1970. |
| [**SetSystemTime**](setsystemtime.md)                                     | Sets the current system time and date.                                                                 |
| [**SetSystemTimeAdjustment**](setsystemtimeadjustment.md)                 | Enables or disables periodic time adjustments to the system's time-of-day clock.                       |
| [**SystemTimeToFileTime**](systemtimetofiletime.md)                       | Converts a system time to a file time.                                                                 |
| [**SystemTimeToTzSpecificLocalTime**](systemtimetotzspecificlocaltime.md) | Converts a UTC time to a specified time zone's corresponding local time.                               |
| [**TzSpecificLocalTimeToSystemTime**](tzspecificlocaltimetosystemtime.md) | Converts a local time to a UTC time.                                                                   |



 

The following functions are used with local time.



| Function                                                                                           | Description                                                                                                                                     |
|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EnumDynamicTimeZoneInformation**](enumdynamictimezoneinformation.md)                           | Enumerates dynamic daylight saving time information entries stored in the registry.                                                             |
| [**FileTimeToLocalFileTime**](filetimetolocalfiletime.md)                                         | Converts a UTC file time to a local file time.                                                                                                  |
| [**GetDynamicTimeZoneInformation**](getdynamictimezoneinformation.md)                             | Retrieves the current time zone and dynamic daylight saving time settings.                                                                      |
| [**GetDynamicTimeZoneInformationEffectiveYears**](getdynamictimezoneinformationeffectiveyears.md) | Retrieves a range, expressed in years, for which a [**DYNAMIC\_TIME\_ZONE\_INFORMATION**](dynamic-time-zone-information.md) has valid entries. |
| [**GetLocalTime**](getlocaltime.md)                                                               | Retrieves the current local date and time.                                                                                                      |
| [**GetTimeZoneInformation**](gettimezoneinformation.md)                                           | Retrieves the current time zone settings.                                                                                                       |
| [**GetTimeZoneInformationForYear**](gettimezoneinformationforyear.md)                             | Retrieves the time zone settings for the specified year and time zone.                                                                          |
| [**RtlLocalTimeToSystemTime**](rtllocaltimetosystemtime.md)                                       | Converts the specified local time to system time.                                                                                               |
| [**SetDynamicTimeZoneInformation**](setdynamictimezoneinformation.md)                             | Sets the current time zone and dynamic daylight saving time settings.                                                                           |
| [**SetLocalTime**](setlocaltime.md)                                                               | Sets the current local time and date.                                                                                                           |
| [**SetTimeZoneInformation**](settimezoneinformation.md)                                           | Sets the current time zone settings.                                                                                                            |
| [**SystemTimeToTzSpecificLocalTime**](systemtimetotzspecificlocaltime.md)                         | Converts a UTC time to a specified time zone's corresponding local time.                                                                        |
| [**SystemTimeToTzSpecificLocalTimeEx**](systemtimetotzspecificlocaltimeex.md)                     | Converts a UTC time with dynamic daylight saving time settings to a specified time zone's corresponding local time.                             |
| [**TzSpecificLocalTimeToSystemTime**](tzspecificlocaltimetosystemtime.md)                         | Converts a local time to a UTC time.                                                                                                            |
| [**TzSpecificLocalTimeToSystemTimeEx**](tzspecificlocaltimetosystemtimeex.md)                     | Converts a local time with dynamic daylight saving time settings to UTC time.                                                                   |



 

The following functions are used with file time.



| Function                                                   | Description                                                                                                     |
|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [**CompareFileTime**](comparefiletime.md)                 | Compares two file times.                                                                                        |
| [**FileTimeToLocalFileTime**](filetimetolocalfiletime.md) | Converts a UTC file time to a local file time.                                                                  |
| [**FileTimeToSystemTime**](filetimetosystemtime.md)       | Converts a file time to system time format.                                                                     |
| [**GetFileTime**](getfiletime.md)                         | Retrieves the date and time that the specified file or directory was created, last accessed, and last modified. |
| [**GetSystemTimeAsFileTime**](getsystemtimeasfiletime.md) | Retrieves the current system date and time in UTC format.                                                       |
| [**LocalFileTimeToFileTime**](localfiletimetofiletime.md) | Converts a local file time to a file time based on UTC.                                                         |
| [**SetFileTime**](setfiletime.md)                         | Sets the date and time that the specified file or directory was created, last accessed, or last modified.       |
| [**SystemTimeToFileTime**](systemtimetofiletime.md)       | Converts a system time to a file time.                                                                          |



 

The following functions are used with MS-DOS date and time.



| Function                                               | Description                                          |
|--------------------------------------------------------|------------------------------------------------------|
| [**DosDateTimeToFileTime**](dosdatetimetofiletime.md) | Converts MS-DOS date and time values to a file time. |
| [**FileTimeToDosDateTime**](filetimetodosdatetime.md) | Converts a file time to MS-DOS date and time values. |



 

The following functions are used with Windows time.



| Function                                 | Description                                                                                           |
|------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**GetSystemTimes**](getsystemtimes.md) | Retrieves system timing information.                                                                  |
| [**GetTickCount**](gettickcount.md)     | Retrieves the number of milliseconds that have elapsed since the system was started, up to 49.7 days. |
| [**GetTickCount64**](gettickcount64.md) | Retrieves the number of milliseconds that have elapsed since the system was started.                  |



 

The following functions are used with high-resolution performance counters.



| Function                                                              | Description                                                             |
|-----------------------------------------------------------------------|-------------------------------------------------------------------------|
| [**QueryPerformanceCounter**](_win32_queryperformancecounter_cpp)     | Retrieves the current value of the high-resolution performance counter. |
| [**QueryPerformanceFrequency**](_win32_queryperformancefrequency_cpp) | Retrieves the frequency of the high-resolution performance counter.     |



 

The following functions are used with the auxiliary performance counter.



| Function                                                                                           | Description                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**QueryAuxiliaryCounterFrequency**](queryauxiliarycounterfrequency.md)                           | Queries the auxiliary counter frequency.                                                                                                                                                                      |
| [**ConvertAuxiliaryCounterToPerformanceCounter**](convertauxiliarycountertoperformancecounter.md) | Converts the specified auxiliary counter value to the corresponding performance counter value; optionally provides the estimated conversion error in nanoseconds due to latencies and maximum possible drift. |
| [**ConvertPerformanceCounterToAuxiliaryCounter**](convertperformancecountertoauxiliarycounter.md) | Converts the specified performance counter value to the corresponding auxiliary counter value; optionally provides the estimated conversion error in nanoseconds due to latencies and maximum possible drift. |



 

The following function is used with interrupt time.



| Function                                                                       | Description                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**QueryInterruptTime**](queryinterrupttime.md)                               | Gets the current interrupt-time count.                                                                                                                                                                                                                |
| [**QueryInterruptTimePrecise**](queryinterrupttimeprecise.md)                 | Gets the current interrupt-time count, in a more precise form than [**QueryInterruptTime**](queryinterrupttime.md) does.                                                                                                                             |
| [**QueryUnbiasedInterruptTime**](queryunbiasedinterrupttime.md)               | Gets the current unbiased interrupt-time count. The unbiased interrupt-time count does not include time the system spends in sleep or hibernation.                                                                                                    |
| [**QueryUnbiasedInterruptTimePrecise**](queryunbiasedinterrupttimeprecise.md) | Gets the current unbiased interrupt-time count, in a more precise form than [**QueryUnbiasedInterruptTime**](queryunbiasedinterrupttime.md) does. The unbiased interrupt-time count does not include time the system spends in sleep or hibernation. |



 

 

 



