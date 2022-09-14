---
description: As long as the system determines that there is user or application activity, it will not enter sleep.
ms.assetid: 83c9394a-1813-405a-802a-0623e5de50d3
title: System Sleep Criteria
ms.topic: article
ms.date: 05/31/2018
---

# System Sleep Criteria

As long as the system determines that there is user or application activity, it will not enter sleep. The system can detect certain activities, such as user input or network communications. However, there are other activities that the system cannot detect. For example, a presentation application requires the screen for display. However, it may appear that the application is idle during the presentation, causing the system to turn off the display.

To notify the system that your application is busy, use the [**SetThreadExecutionState**](/windows/desktop/api/Winbase/nf-winbase-setthreadexecutionstate) function. This function prevents the system from entering sleep or turning off the display while the application is running.

Presentation and multimedia applications must call the [**SetThreadExecutionState**](/windows/desktop/api/Winbase/nf-winbase-setthreadexecutionstate) function with **ES\_DISPLAY\_REQUIRED** so that the system will know that it should not put the display device to sleep. Event-handling applications, such as tools for managing incoming faxes, must call **SetThreadExecutionState** with **ES\_SYSTEM\_REQUIRED**, handle the event, and then clear the flag so the system can return to sleep. Note that most productivity applications do not need to use **SetThreadExecutionState** because the system can usually determine activity by user input.

To maintain the time since the last user input, the system uses a display idle timer and a system idle timer. The system compares the idle timers to the values configured in the power plan. If the display idle timer value is greater than the display time-out value, and no threads have requested the display by calling [**SetThreadExecutionState**](/windows/desktop/api/Winbase/nf-winbase-setthreadexecutionstate) with **ES\_DISPLAY\_REQUIRED**, the system powers off the display. Similarly, if the system idle timer is greater than the system time-out value and no applications have requested the system by calling **SetThreadExecutionState** with **ES\_SYSTEM\_REQUIRED**, the system enters sleep.

The system maintains a count of applications that have called [**SetThreadExecutionState**](/windows/desktop/api/Winbase/nf-winbase-setthreadexecutionstate). The system tracks each thread that calls **SetThreadExecutionState** and adjusts the counter accordingly. If this counter reaches zero and there has not been any user input, the system enters sleep.

If power is low, an application can request user intervention or request that the system suspend itself. You can suspend system operation by using the [**SetSuspendState**](/windows/desktop/api/PowrProf/nf-powrprof-setsuspendstate) function.

If the system wakes automatically ([PBT\_APMRESUMEAUTOMATIC](pbt-apmresumeautomatic.md)), none of the timers are relevant. For more information, see [System Wake-up Events](system-wake-up-events.md).

## Entering Sleep

When the system enters sleep, it will automatically preserve the state of the entire system and all applications. Therefore, most applications do not need to take any special action. Applications that need to perform specific actions before the system transitions can register for power events.

When the system sends a [PBT\_APMSUSPEND](pbt-apmsuspend.md) event, each application has two seconds to perform any necessary actions before the system starts the transition to sleep. Applications must limit what action they take in response to this event to ensure that they complete all operations in the time allotted.

## Related topics

<dl> <dt>

[About Power Management](about-power-management.md)
</dt> <dt>

[System Wake-up Events](system-wake-up-events.md)
</dt> </dl>

 

 



