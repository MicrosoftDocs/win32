---
Description: 'This topic discusses timers. A timer is an internal routine that repeatedly measures a specified interval, in milliseconds.'
ms.assetid: '509a6fc4-ddee-4ff4-88a2-25dad4c48c2f'
title: Timers
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
| [**SetTimer**](settimer.md)   | Creates a timer with the specified time-out value.<br/>                                                                                                                                                                                                            |
| [*TimerProc*](timerproc.md)   | An application-defined callback function that processes [**WM\_TIMER**](wm-timer.md) messages. The **TIMERPROC** type defines a pointer to this callback function. [*TimerProc*](timerproc.md) is a placeholder for the application-defined function name. <br/> |



 

### Timer Notifications



| Name                          | Description                                                                                                                                                                                     |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_TIMER**](wm-timer.md) | Posted to the installing thread's message queue when a timer expires. The message is posted by the [**GetMessage**](getmessage.md) or [**PeekMessage**](peekmessage.md) function. <br/> |



 

 

 




