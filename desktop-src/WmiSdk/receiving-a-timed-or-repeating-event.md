---
Description: A timed or repeating event is an event that occurs at one specific time and date, or repeatedly at regular intervals. For example, an event can occur at midnight on only December 2, 2015, or one time each week on Tuesdays at 2:31 PM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 369bf2d7-8350-4089-8e11-28e2b641f792
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Receiving a Timed or Repeating Event
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Receiving a Timed or Repeating Event

A timed or repeating event is an event that occurs at one specific time and date, or repeatedly at regular intervals. For example, an event can occur at midnight on only December 2, 2015, or one time each week on Tuesdays at 2:31 PM.

The following table lists the different classes that are used to create a timed or repeating event.



| Class                                                                                            | Description                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Win32\_LocalTime**](https://msdn.microsoft.com/library/aa394171) or [**Win32\_UTCTime**](https://msdn.microsoft.com/library/aa394510) | Standard Microsoft event model.<br/> For more information, see [Creating a Timer Event with Win32\_LocalTime or Win32\_UTCTime](creating-a-timer-event-with-win32-localtime-or-win32-utctime.md).<br/> |
| [**\_\_TimerInstruction**](--timerinstruction.md)                                               | Legacy technique.<br/> For more information, see [Creating a Timer Event with \_TimerInstruction](creating-a-timer-event-with---timerinstruction.md).<br/>                                             |



 

If you want to schedule a task or job to occur at a specific time or repeatedly, use the [**Win32\_ScheduledJob**](https://msdn.microsoft.com/library/aa394399) class and its methods. This class represents a job created with the AT command in a command window from **Start** and then **Run**, or from the **Scheduled Tasks** in **Control Panel**.

 

 




