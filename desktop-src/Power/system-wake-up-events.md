---
description: Your application can restore a computer that is in a sleep state to the working state by using a scheduled timer or a device event.
ms.assetid: b7326b09-0829-4e76-80d0-e4ecdf7f556e
title: System Wake-up Events
ms.topic: article
ms.date: 05/31/2018
---

# System Wake-up Events

The following information applies to wakes from [sleep (S3) and hibernate (S4)](/windows-hardware/drivers/kernel/system-sleeping-states). For wakes from Modern Standby (S0 Low Power Idle), please refer to [transitions from idle to active](/windows-hardware/design/device-experiences/transition-from-idle-to-active).

Your application can restore a computer that is in a sleep state to the working state by using a scheduled timer or a device event. This is known as a *wake-up event*. Use a [waitable timer object](/windows/desktop/Sync/waitable-timer-objects) to specify the time at which the system should wake. To create the object, use the [**CreateWaitableTimer**](/windows/win32/api/synchapi/nf-synchapi-createwaitabletimerw) function. To set the timer, use the [**SetWaitableTimer**](/windows/desktop/api/synchapi/nf-synchapi-setwaitabletimer) function. The *pDueTime* parameter specifies when the timer will be signaled. To specify that the system should wake when the timer is signaled, set the *fResume* parameter to **TRUE**.

When the system wakes automatically because of an event (other than power switch or user activity), the system automatically sets an unattended idle timer to at least 2 minutes. This timer gives applications sufficient time to call the [**SetThreadExecutionState**](/windows/desktop/api/Winbase/nf-winbase-setthreadexecutionstate) function to indicate that they are busy. This time enables the system to return to the sleep state quickly after the computer is no longer required. The following criteria determine whether the system returns to the sleep state:

-   If the system wakes automatically (that is, no user activity is present), it shuts down as soon as the unattended idle timer expires, assuming that no applications have called [**SetThreadExecutionState**](/windows/desktop/api/Winbase/nf-winbase-setthreadexecutionstate) to indicate that the system is required.
-   Device-based wakes trigger the unattended idle timer by default unless the device driver indicates user presence. If the driver indicates user presence, then the system idle timer is used.
-   If the system wakes automatically, but the user provides new input while the event is handled, the system does not automatically return to sleep based on the unattended idle timer. Instead, the system returns to sleep based on the system idle timer.
-   If the system wakes due to user activity, the system does not automatically return to sleep based on the unattended idle timer. Instead the system returns to sleep based on the system idle timer.

When the system wakes automatically, it broadcasts the [PBT\_APMRESUMEAUTOMATIC](pbt-apmresumeautomatic.md) event to all applications. Because the user is not present, most applications should do nothing. Event-handling applications, such as fax servers, should handle their events. To determine whether the system is in this state, call the [**IsSystemResumeAutomatic**](/windows/desktop/api/Winbase/nf-winbase-issystemresumeautomatic) function. When the system wakes automatically, the display is not automatically turned on.

If the system wakes due to user activity, the system will first broadcast the [PBT\_APMRESUMEAUTOMATIC](pbt-apmresumeautomatic.md) event followed by a [PBT\_APMRESUMESUSPEND](pbt-apmresumesuspend.md) event. In addition, the system will turn on the display. Your application should reopen files that it closed when the system entered sleep and prepare for user input.

## Related topics

<dl> <dt>

[About Power Management](about-power-management.md)
</dt> <dt>

[System Sleep Criteria](system-sleep-criteria.md)
</dt> </dl>

 

 
