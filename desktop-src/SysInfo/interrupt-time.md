---
Description: 'Interrupt time is the amount of time since the system was last started, in 100-nanosecond intervals.'
ms.assetid: '56fe322e-53ea-4186-9b5e-352f69b09109'
title: Interrupt Time
---

# Interrupt Time

*Interrupt time* is the amount of time since the system was last started, in 100-nanosecond intervals. The interrupt-time count begins at zero when the system starts and is incremented at each clock interrupt by the length of a clock tick. The exact length of a clock tick depends on underlying hardware and can vary between systems.

Unlike [system time](system-time.md), the interrupt-time count is not subject to adjustments by users or the Windows time service, making it a better choice for measuring short durations. Applications that require greater precision than the interrupt-time count should use a [high-resolution timer](_win32_about_timers_cpp). Use the [**QueryPerformanceFrequency**](_win32_queryperformancefrequency_cpp) function to retrieve the frequency of the high-resolution timer and the [**QueryPerformanceCounter**](_win32_queryperformancecounter_cpp) function to retrieve the counter's value.

The [**QueryInterruptTime**](queryinterrupttime.md), [**QueryInterruptTimePrecise**](queryinterrupttimeprecise.md), [**QueryUnbiasedInterruptTime**](queryunbiasedinterrupttime.md), and [**QueryUnbiasedInterruptTimePrecise**](queryunbiasedinterrupttimeprecise.md) functions can be used to retrieve the interrupt-time count. Unbiased interrupt-time means that only time that the system is in the working state is counted—therefore, the interrupt-time count is not "biased" by time the system spends in sleep or hibernation.

**Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP/2000:** The [**QueryUnbiasedInterruptTime**](queryunbiasedinterrupttime.md) function is available starting with Windows 7 and Windows Server 2008 R2.

The timer resolution set by the [**timeBeginPeriod**](https://msdn.microsoft.com/library/windows/desktop/dd757624) and [**timeEndPeriod**](https://msdn.microsoft.com/library/windows/desktop/dd757626) functions affects the resolution of the [**QueryInterruptTime**](queryinterrupttime.md) and [**QueryUnbiasedInterruptTime**](queryunbiasedinterrupttime.md) functions. However, increasing the timer resolution is not recommended because it can reduce overall system performance and increase power consumption by preventing the processor from entering power-saving states. Instead, applications should use a high-resolution timer.

> [!Note]  
> The [**QueryInterruptTime**](queryinterrupttime.md), [**QueryInterruptTimePrecise**](queryinterrupttimeprecise.md), [**QueryUnbiasedInterruptTime**](queryunbiasedinterrupttime.md), and [**QueryUnbiasedInterruptTimePrecise**](queryunbiasedinterrupttimeprecise.md) functions produces different results on debug ("checked") builds of Windows, because the interrupt-time count and tick count are advanced by approximately 49 days. This helps to identify bugs that might not occur until the system has been running for a long time. The checked build is available to MSDN subscribers through the [Microsoft Developer Network (MSDN)](http://go.microsoft.com/fwlink/p/?linkid=8714) Web site.

 

The following example shows how to retrieve the interrupt-time count by calling the [**QueryInterruptTime**](queryinterrupttime.md), [**QueryInterruptTimePrecise**](queryinterrupttimeprecise.md), [**QueryUnbiasedInterruptTime**](queryunbiasedinterrupttime.md), and [**QueryUnbiasedInterruptTimePrecise**](queryunbiasedinterrupttimeprecise.md) functions. Link to the OneCore.lib library when you build a console application that calls these functions.


```C++
#include "stdafx.h"
#include <windows.h>
#include <realtimeapiset.h>

void InterruptTimeTest()
{
    ULONGLONG InterruptTime;
    ULONGLONG PreciseInterruptTime;
    ULONGLONG UnbiasedInterruptTime;
    ULONGLONG PreciseUnbiasedInterruptTime;

        // The interrupt time that QueryInterruptTime reports is based on the 
        // latest tick of the system clock timer. The system clock timer is 
        // the hardware timer that periodically generates interrupts for the 
        // system clock. The uniform period between system clock timer 
        // interrupts is referred to as a system clock tick, and is typically 
        // in the range of 0.5 milliseconds to 15.625 milliseconds, depending 
        // on the hardware platform. The interrupt time value retrieved by 
        // QueryInterruptTime is accurate within a system clock tick.

    QueryInterruptTime(&amp;InterruptTime);
    printf("Interrupt time: %.7f seconds\n", 
            (double)InterruptTime/(double)10000000);

        // Precise interrupt time is more precise than the interrupt time that
        // QueryInterruptTime reports because the functions that report  
        // precise interrupt time read the timer hardware directly.

    QueryInterruptTimePrecise(&amp;PreciseInterruptTime);
    printf("Precise interrupt time: %.7f seconds\n", 
            (double)PreciseInterruptTime/(double)10000000);

        // Unbiased interrupt time means that only time that the system is in 
        // the working state is counted. Therefore, the interrupt-time count 
        // is not biased by time the system spends in sleep or hibernation.

    QueryUnbiasedInterruptTime(&amp;UnbiasedInterruptTime);
    printf("Unbiased interrupt time: %.7f seconds\n", 
            (double)UnbiasedInterruptTime/(double)10000000);

        // QueryUnbiasedInterruptTimePrecise gets an interrupt-time count
        // that is both unbiased and precise, as defined in the comments
        // included earlier in this example.

    QueryUnbiasedInterruptTimePrecise(&amp;PreciseUnbiasedInterruptTime);
    printf("Precise unbiased interrupt time: %.7f seconds\n", 
            (double)PreciseUnbiasedInterruptTime/(double)10000000);

}

int main(void)
{
    void InterruptTimeTime();

    InterruptTimeTest();
    return(0);
}
```



To retrieve elapsed time that accounts for sleep or hibernation, use the [**GetTickCount**](gettickcount.md) or [**GetTickCount64**](gettickcount64.md) function, or use the System Up Time performance counter. This performance counter can be retrieved from the performance data in the registry key **HKEY\_PERFORMANCE\_DATA**. The value returned is an 8-byte value. For more information, see [Performance Counters](https://msdn.microsoft.com/library/windows/desktop/aa373083).

## Related topics

<dl> <dt>

[**QueryInterruptTime**](queryinterrupttime.md)
</dt> <dt>

[**QueryInterruptTimePrecise**](queryinterrupttimeprecise.md)
</dt> <dt>

[**QueryUnbiasedInterruptTime**](queryunbiasedinterrupttime.md)
</dt> <dt>

[**QueryUnbiasedInterruptTimePrecise**](queryunbiasedinterrupttimeprecise.md)
</dt> <dt>

[**timeBeginPeriod**](https://msdn.microsoft.com/library/windows/desktop/dd757624)
</dt> <dt>

[**timeEndPeriod**](https://msdn.microsoft.com/library/windows/desktop/dd757626)
</dt> </dl>

 

 



