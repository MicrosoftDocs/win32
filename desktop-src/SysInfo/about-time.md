---
description: Time-related functions return time in one of several formats. You can use the time functions to convert between some time formats for ease of comparison and display. The following table summarizes the time formats.
ms.assetid: 74feb158-ba45-4660-970b-3eb577b1ebf8
title: About Time
ms.topic: article
ms.date: 05/31/2018
---

# About Time

Time-related functions return time in one of several formats. You can use the time functions to convert between some time formats for ease of comparison and display. The following table summarizes the time formats.



| Format          | Type                                                                     | Description                                                                                                                         |
|-----------------|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| System          | [**SYSTEMTIME**](/windows/win32/api/minwinbase/ns-minwinbase-systemtime)                                     | Year, month, day, hour, second, and millisecond, taken from the internal hardware clock.                                            |
| Local           | [**SYSTEMTIME**](/windows/win32/api/minwinbase/ns-minwinbase-systemtime) or [**FILETIME**](/windows/win32/api/minwinbase/ns-minwinbase-filetime) | A system time or file time converted to the system's local time zone.                                                               |
| File            | [**FILETIME**](/windows/win32/api/minwinbase/ns-minwinbase-filetime)                                         | The number of 100-nanosecond intervals since January 1, 1601.                                                                       |
| MS-DOS          | **WORD**                                                                 | A packed word for the date, another for the time.                                                                                   |
| Windows         | **DWORD** or **ULONGLONG**                                               | The number of milliseconds since the system was last started. When retrieved as a DWORD value, Windows time cycles every 49.7 days. |
| Interrupt Count | **ULONGLONG**                                                            | The number of 100-nanosecond intervals since the system was last started.                                                           |



 

For more information, see the following topics:

-   [System Time](system-time.md)
-   [Local Time](local-time.md)
-   [File Times](file-times.md)
-   [MS-DOS Date and Time](ms-dos-date-and-time.md)
-   [Windows Time](windows-time.md)
-   [Interrupt Time](interrupt-time.md)

 

 
