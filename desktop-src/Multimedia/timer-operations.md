---
title: Timer Event Operations
description: Timer Event Operations
ms.assetid: a2b75e84-4da8-449f-b02a-4ffc4846eef5
keywords:
- multimedia timers,events
- timers,events
- timeSetEvent function
- timeKillEvent function
- starting timer events
- single timer events
- periodic timer events
- cancelling timer events
ms.topic: article
ms.date: 05/31/2018
---

# Timer Event Operations

After you have established your application's timer resolution, you can start timer events by using the [**timeSetEvent**](/previous-versions//dd757634(v=vs.85)) function. This function returns a timer identifier that can be used to stop or identify timer events. One of the function's parameters is the address of a [**TimeProc**](/previous-versions//dd757631(v=vs.85)) callback function that is called when the timer event takes place.

There are two types of timer events: *single* and *periodic*. A single timer event occurs once, after a specified number of milliseconds. A periodic timer event occurs every time a specified number of milliseconds elapses. The interval between periodic events is called an *event delay*. Periodic timer events with an event delay of 10 milliseconds or less consume a significant portion of CPU resources.

The relationship between the resolution of a timer event and the length of the event delay is important in timer events. For example, if you specify a resolution of 5 and an event delay of 100, the timer services notify the callback function after an interval ranging from 95 to 105 milliseconds.

You can cancel an active timer event at any time by using the [**timeKillEvent**](/previous-versions//dd757630(v=vs.85)) function. Be sure to cancel any outstanding timers before freeing the memory containing the callback function.

> [!Note]  
> The multimedia timer runs in its own thread.

 

 

 