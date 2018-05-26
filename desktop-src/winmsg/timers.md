---
Description: This topic discusses timers. A timer is an internal routine that repeatedly measures a specified interval, in milliseconds.
ms.assetid: 509a6fc4-ddee-4ff4-88a2-25dad4c48c2f
title: Timers
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Timers

A timer is an internal routine that repeatedly measures a specified interval, in milliseconds.

### In This Section



| Name                                   | Description                                                                                                               |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [About Timers](about-timers.md)       | Describes how to create, identify, set, and delete timers.<br/>                                                     |
| [Using Timers](using-timers.md)       | Discusses how to create and destroy timers, and how to use a timer to trap mouse input at specified intervals.<br/> |
| [Timer Reference](timer-reference.md) | Contains the API reference.<br/>                                                                                    |



 

### Timer Functions



| Name                           | Description                                                                                                                                                                                                                                                              |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**KillTimer**](killtimer.md) | Destroys the specified timer. <br/>                                                                                                                                                                                                                                |
| [**SetTimer**](/windows/win32/Winuser/nf-ndis-ndismsettimer?branch=master)   | Creates a timer with the specified time-out value.<br/>                                                                                                                                                                                                            |
| [*TimerProc*](timerproc.md)   | An application-defined callback function that processes [**WM\_TIMER**](wm-timer.md) messages. The **TIMERPROC** type defines a pointer to this callback function. [*TimerProc*](timerproc.md) is a placeholder for the application-defined function name. <br/> |



 

### Timer Notifications



| Name                          | Description                                                                                                                                                                                     |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_TIMER**](wm-timer.md) | Posted to the installing thread's message queue when a timer expires. The message is posted by the [**GetMessage**](/windows/win32/Winuser/nf-engextcpp-extexception-getmessage?branch=master) or [**PeekMessage**](peekmessage.md) function. <br/> |



 

 

 




