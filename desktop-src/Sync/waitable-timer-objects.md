---
description: A waitable timer object is a synchronization object whose state is set to signaled when the specified due time arrives.
ms.assetid: '5d39ada0-ea31-40d7-b075-aeb657ee508c'
title: Waitable Timer Objects
ms.topic: article
ms.date: 05/31/2018
---

# Waitable Timer Objects

A *waitable timer object* is a synchronization object whose state is set to signaled when the specified due time arrives. There are two types of waitable timers that can be created: manual-reset and synchronization. A timer of either type can also be a periodic timer.



| Object                | Description                                                                                                                                                                                             |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| manual-reset timer    | A timer whose state remains signaled until [**SetWaitableTimer**](/windows/win32/api/synchapi/nf-synchapi-setwaitabletimer) is called to establish a new due time.                                                                          |
| synchronization timer | A timer whose state remains signaled until a thread completes a wait operation on the timer object.                                                                                                     |
| periodic timer        | A timer that is reactivated each time the specified period expires, until the timer is reset or canceled. A periodic timer is either a periodic manual-reset timer or a periodic synchronization timer. |



 

> [!Note]  
> When a timer is signaled, the processor must run to process the associated instructions. High-frequency periodic timers keep the processor continually busy, which prevents the system from remaining in a lower [power state](../power/system-power-states.md) for any meaningful amount of time. This can have a negative impact on portable computer battery life and scenarios that depend on effective power management, such as large datacenters. For greater energy efficiency, consider using event-based notifications instead of time-based notifications in your application. If a timer is necessary, use a timer that is signaled once rather than a periodic timer, or set the interval to a value greater than one second.

 

A thread uses the [**CreateWaitableTimer**](/windows/win32/api/synchapi/nf-synchapi-createwaitabletimerw) or [**CreateWaitableTimerEx**](/windows/win32/api/synchapi/nf-synchapi-createwaitabletimerexw) function to create a timer object. The creating thread specifies whether the timer is a manual-reset timer or a synchronization timer. The creating thread can specify a name for the timer object. Threads in other processes can open a handle to an existing timer by specifying its name in a call to the [**OpenWaitableTimer**](/windows/win32/api/synchapi/nf-synchapi-openwaitabletimerw) function. Any thread with a handle to a timer object can use one of the [wait functions](wait-functions.md) to wait for the timer state to be set to signaled.

-   The thread calls the [**SetWaitableTimer**](/windows/win32/api/synchapi/nf-synchapi-setwaitabletimer) function to activate the timer. Note the use of the following parameters for **SetWaitableTimer**:
-   Use the *lpDueTime* parameter to specify the time at which the timer is to be set to the signaled state. When a manual-reset timer is set to the signaled state, it remains in this state until [**SetWaitableTimer**](/windows/win32/api/synchapi/nf-synchapi-setwaitabletimer) establishes a new due time. When a synchronization timer is set to the signaled state, it remains in this state until a thread completes a wait operation on the timer object.
-   Use the *lPeriod* parameter of the [**SetWaitableTimer**](/windows/win32/api/synchapi/nf-synchapi-setwaitabletimer) function to specify the timer period. If the period is not zero, the timer is a periodic timer; it is reactivated each time the period expires, until the timer is reset or canceled. If the period is zero, the timer is not a periodic timer; it is signaled once and then deactivated.

A thread can use the [**CancelWaitableTimer**](/windows/win32/api/synchapi/nf-synchapi-cancelwaitabletimer) function to set the timer to the inactive state. To reset the timer, call [**SetWaitableTimer**](/windows/win32/api/synchapi/nf-synchapi-setwaitabletimer). When you are finished with the timer object, call [**CloseHandle**](/windows/win32/api/handleapi/nf-handleapi-closehandle) to close the handle to the timer object.

The behavior of a waitable timer can be summarized as follows:

-   When a timer is set, it is canceled if it was already active, the state of the timer is nonsignaled, and the timer is placed in the kernel timer queue.
-   When a timer expires, the timer is set to the signaled state. If the timer has a completion routine, it is queued to the thread that set the timer. The completion routine remains in the [asynchronous procedure call](asynchronous-procedure-calls.md) (APC) queue of the thread until the thread enters an alertable wait state. At that time, the APC is dispatched and the completion routine is called. If the timer is periodic, it is placed back in the kernel timer queue.
-   When a timer is canceled, it is removed from the kernel timer queue if it was pending. If the timer had expired and there is still an APC queued to the thread that set the timer, the APC is removed from the thread's APC queue. The signaled state of the timer is not affected.

## Related topics

<dl> <dt>

[Asynchronous Procedure Calls](asynchronous-procedure-calls.md)
</dt> <dt>

[Using Waitable Timer Objects](using-waitable-timer-objects.md)
</dt> </dl>

 

 
