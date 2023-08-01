---
description: This topic describes how to create, identify, set, and delete timers.
ms.assetid: 509a6fc4-ddee-4ff4-88a2-25dad4c48c2f
title: About Timers
ms.topic: article
ms.date: 05/31/2018
---

# About Timers

This topic describes how to create, identify, set, and delete timers. An application uses a timer to schedule an event for a window after a specified time has elapsed. Each time the specified interval (or time-out value) for a timer elapses, the system notifies the window associated with the timer. Because a timer's accuracy depends on the system clock rate and how often the application retrieves messages from the message queue, the time-out value is only approximate.

This topic includes the following sections.

-   [Timer Operations](#timer-operations)
-   [High-Resolution Timer](#high-resolution-timer)
-   [Waitable Timer Objects](#waitable-timer-objects)
-   [Related topics](#related-topics)

## Timer Operations

Applications create timers by using the [**SetTimer**](/windows/win32/api/winuser/nf-winuser-settimer) function. A new timer starts timing the interval as soon as it is created. An application can change a timer's time-out value by using **SetTimer** and can destroy a timer by using the [**KillTimer**](/windows/win32/api/winuser/nf-winuser-killtimer) function. To use system resources efficiently, applications should destroy timers that are no longer necessary.

Each timer has a unique identifier. When creating a timer, an application can either specify an identifier or have the system create a unique value. The first parameter of a [**WM\_TIMER**](wm-timer.md) message contains the identifier of the timer that posted the message.

If you specify a window handle in the call to [**SetTimer**](/windows/win32/api/winuser/nf-winuser-settimer), the application associates the timer with that window. Whenever the time-out value for the timer elapses, the system posts a [**WM\_TIMER**](wm-timer.md) message to the window associated with the timer. If no window handle is specified in the call to **SetTimer**, the application that created the timer must monitor its message queue for **WM\_TIMER** messages and dispatch them to the appropriate window. If you specify a [**TimerProc**](/windows/win32/api/winuser/nc-winuser-timerproc) callback function, the [**TimerProc**](/windows/win32/api/winuser/nc-winuser-timerproc) will be called at [**Message Loop**](https://learn.microsoft.com/en-us/windows/win32/winmsg/about-messages-and-message-queues#message-loop), will not dispatch **WM\_TIMER** to WindowProc.

If you need to be notified when a timer elapses, use a waitable timer. For more information, see [Waitable Timer Objects](/windows/desktop/Sync/waitable-timer-objects).

## High-Resolution Timer

A counter is a general term used in programming to refer to an incrementing variable. Some systems include a high-resolution performance counter that provides high-resolution elapsed times.

If a high-resolution performance counter exists on the system, you can use the [**QueryPerformanceFrequency**](/windows/desktop/api/profileapi/nf-profileapi-queryperformancefrequency) function to express the frequency, in counts per second. The value of the count is processor dependent. On some processors, for example, the count might be the cycle rate of the processor clock.

The [**QueryPerformanceCounter**](/windows/desktop/api/profileapi/nf-profileapi-queryperformancecounter) function retrieves the current value of the high-resolution performance counter. By calling this function at the beginning and end of a section of code, an application essentially uses the counter as a high-resolution timer. For example, suppose that [**QueryPerformanceFrequency**](/windows/desktop/api/profileapi/nf-profileapi-queryperformancefrequency) indicates that the frequency of the high-resolution performance counter is 50,000 counts per second. If the application calls **QueryPerformanceCounter** immediately before and immediately after the section of code to be timed, the counter values might be 1500 counts and 3500 counts, respectively. These values would indicate that .04 seconds (2000 counts) elapsed while the code executed.

## Waitable Timer Objects

A waitable timer object is a synchronization object whose state is set to signaled when the specified due time arrives. There are two types of waitable timers that can be created: manual-reset and synchronization. A timer of either type can also be a periodic timer.

A thread uses the [**CreateWaitableTimer**](/windows/win32/api/synchapi/nf-synchapi-createwaitabletimerw) or [**CreateWaitableTimerEx**](/windows/win32/api/synchapi/nf-synchapi-createwaitabletimerexw) function to create a timer object. The creating thread specifies whether the timer is a manual-reset timer or a synchronization timer. The creating thread can specify a name for the timer object. Threads in other processes can open a handle to an existing timer by specifying its name in a call to the [**OpenWaitableTimer**](/windows/win32/api/synchapi/nf-synchapi-openwaitabletimerw) function. Any thread with a handle to a timer object can use one of the wait functions to wait for the timer state to be set to signaled.

For more information about using waitable timer objects for thread synchronization, see [Waitable Timer Objects](/windows/desktop/Sync/waitable-timer-objects).

## Related topics

<dl> <dt>

[Using Timers](using-timers.md)
</dt> </dl>

 

 
