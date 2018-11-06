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
ms.date: 05/31/2018
---

# About Multimedia Timers

Multimedia timer services allow applications to schedule timer events with the greatest resolution (or accuracy) possible for the hardware platform. These multimedia timer services allow you to schedule timer events at a higher resolution than other timer services.

These timer services are useful for applications that demand high-resolution timing. For example, a MIDI sequencer requires a high-resolution timer because it must maintain the pace of MIDI events within a resolution of 1 millisecond.

Applications that do not use high-resolution timing should use the [SetTimer](http://go.microsoft.com/fwlink/p/?linkid=16908) function instead of multimedia timer services. The timer services provided by **SetTimer** post [WM\_TIMER](http://go.microsoft.com/fwlink/p/?linkid=16909) messages to a message queue, while the multimedia timer services call a callback function. Applications that want a waitable timer should use the [CreateWaitableTimer](http://go.microsoft.com/fwlink/p/?linkid=16910) function.

 

 




