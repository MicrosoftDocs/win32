---
description: Windows time is the number of milliseconds elapsed since the system was last started.
ms.assetid: 95c00204-bfdf-4376-9aae-8d8139ba6750
title: Windows Time
ms.topic: article
ms.date: 05/31/2018
---

# Windows Time

*Windows time* is the number of milliseconds elapsed since the system was last started. This format exists primarily for backward compatibility with 16-bit Windows. To ensure that applications designed for 16-bit Windows continue to run successfully, the [**GetTickCount**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-gettickcount) function returns the current Windows time.

You typically use the [**GetTickCount**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-gettickcount) or [**GetTickCount64**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-gettickcount64) function to compare the current Windows time with the time returned by the [**GetMessageTime**](/windows/win32/api/winuser/nf-winuser-getmessagetime) function. **GetMessageTime** returns the Windows time when the specified message was created. **GetTickCount** and **GetTickCount64** are limited to the resolution of the system timer, which is approximately 10 milliseconds to 16 milliseconds. The elapsed time retrieved by **GetTickCount** or **GetTickCount64** includes time the system spends in sleep or hibernation.

If you need a higher resolution timer, use the [**QueryUnbiasedInterruptTime**](/windows/win32/api/realtimeapiset/nf-realtimeapiset-queryunbiasedinterrupttime) function, a [multimedia timer](/windows/desktop/Multimedia/multimedia-timers), or a [high-resolution timer](../winmsg/about-timers.md). The elapsed time retrieved by the **QueryUnbiasedInterruptTime** function includes only time that the system spends in the working state.

**Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP/2000:** The [**QueryUnbiasedInterruptTime**](/windows/win32/api/realtimeapiset/nf-realtimeapiset-queryunbiasedinterrupttime) function is available starting with Windows 7 and Windows Server 2008 R2.

You can use the System Up Time performance counter to obtain the number of seconds elapsed since the computer was started. This performance counter can be retrieved from the performance data in the registry key **HKEY\_PERFORMANCE\_DATA**. The value returned is an 8-byte value. For more information, see [Performance Counters](/windows/desktop/PerfCtrs/performance-counters-portal).

 

 
