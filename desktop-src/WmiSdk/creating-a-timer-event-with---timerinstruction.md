---
description: You create a timer event by creating an instance of classes derived from the \_\_TimerInstruction class in any WMI namespace.
ms.assetid: 3df2a75a-5231-40d7-ae9d-a7a735fbf316
ms.tgt_platform: multiple
title: Creating a Timer Event with __TimerInstruction
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Timer Event with \_\_TimerInstruction

You create a timer event by creating an instance of classes derived from the [**\_\_TimerInstruction**](--timerinstruction.md) class in any WMI namespace. WMI then generates the timer event at the appropriate time. If you miss a timer event due to computer downtime, WMI notifies you about the missed event. WMI supports timer events for backward compatibility and for scenarios where you must know how many events you have missed since the last delivered event. For most timer events, however, you should create an event filter for [**Win32\_LocalTime**](/previous-versions/windows/desktop/wmitimepprov/win32-localtime) or [**Win32\_UTCTime**](/previous-versions/windows/desktop/wmitimepprov/win32-utctime). For more information, see [Creating a Timer Event with Win32\_LocalTime or Win32\_UTCTime](creating-a-timer-event-with-win32-localtime-or-win32-utctime.md).

The following procedure describes how to create and receive a timer event with \_\_TimerInstruction.

**To create and receive a timer event with \_\_TimerInstruction**

1.  Create an instance of the [**\_\_AbsoluteTimerInstruction**](--absolutetimerinstruction.md) or [**\_\_IntervalTimerInstruction**](--intervaltimerinstruction.md) classes.

    The [**\_\_AbsoluteTimerInstruction**](--absolutetimerinstruction.md) and [**\_\_IntervalTimerInstruction**](--intervaltimerinstruction.md) classes are derived from the [**\_\_TimerInstruction**](--timerinstruction.md) class, which contains a unique developer-assigned string that identifies the type of timer event. The **\_\_TimerInstruction** class also contains a value that specifies whether WMI should send a belated notification if the timer event occurs when WMI is unavailable.

    Use [**\_\_AbsoluteTimerInstruction**](--absolutetimerinstruction.md) to send absolute timer events, which occur on a specific date at a specific time. Use [**\_\_IntervalTimerInstruction**](--intervaltimerinstruction.md) to send interval timer events, which occur on a regular basis.

2.  Set your application to receive a [**\_\_TimerEvent**](--timerevent.md) instance.

    To generate an event, WMI creates an instance of the [**\_\_TimerEvent**](--timerevent.md) class and forwards the instance to your consumer. The **\_\_TimerEvent** instance contains the timer instruction identifier from the consumer. The instance also contains a value that specifies how many times WMI should send the timer event notification during any interval when WMI cannot reach the consumer.

 

 
