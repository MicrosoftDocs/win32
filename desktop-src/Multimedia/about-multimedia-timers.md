---
title: About Multimedia Timers
description: About Multimedia Timers
ms.assetid: 42101923-3f46-4234-bfcf-a0d06c382fa1
keywords:
- Windows multimedia,timers
- multimedia,timers
- multimedia input,timers
- multimedia timers,about
- timers,about
- multimedia timers,scheduling events
- timers,scheduling events
- scheduling timer events
- high-resolution timing
- SetTimer function
- CreateWaitableTimer function
- WM_TIMER messages
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About Multimedia Timers

\[The feature associated with this page, [Multimedia Timers](/windows/win32/multimedia/multimedia-timers), is a legacy feature. It has been superseded by [Multimedia Class Scheduler Service](/windows/win32/procthread/multimedia-class-scheduler-service). **Multimedia Class Scheduler Service** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Multimedia Class Scheduler Service** instead of **Multimedia Timers**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Multimedia timer services allow applications to schedule timer events with the greatest resolution (or accuracy) possible for the hardware platform. These multimedia timer services allow you to schedule timer events at a higher resolution than other timer services.

These timer services are useful for applications that demand high-resolution timing. For example, a MIDI sequencer requires a high-resolution timer because it must maintain the pace of MIDI events within a resolution of 1 millisecond.

Applications that do not use high-resolution timing should use the [SetTimer](/windows/win32/api/winuser/nf-winuser-settimer) function instead of multimedia timer services. The timer services provided by **SetTimer** post [WM\_TIMER](../winmsg/wm-timer.md) messages to a message queue, while the multimedia timer services call a callback function. Applications that want a waitable timer should use the [CreateWaitableTimer](/windows/win32/api/synchapi/nf-synchapi-createwaitabletimerw) function.

 

 