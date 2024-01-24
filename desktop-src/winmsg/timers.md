---
description: This topic discusses timers. A timer is an internal routine that repeatedly measures a specified interval, in milliseconds.
ms.assetid: 'vs|winui|~\winui\windowsuserinterface\windowing\timers.htm'
title: Timers
ms.topic: article
ms.date: 05/31/2018
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
| [**KillTimer**](/windows/win32/api/winuser/nf-winuser-killtimer) | Destroys the specified timer. <br/>                                                                                                                                                                                                                                |
| [**SetTimer**](/windows/win32/api/winuser/nf-winuser-settimer)   | Creates a timer with the specified time-out value.<br/>                                                                                                                                                                                                            |
| [*TimerProc*](/windows/win32/api/winuser/nc-winuser-timerproc)   | An application-defined callback function that processes [**WM\_TIMER**](wm-timer.md) messages. The **TIMERPROC** type defines a pointer to this callback function. [*TimerProc*](/windows/win32/api/winuser/nc-winuser-timerproc) is a placeholder for the application-defined function name. <br/> |



 

### Timer Notifications



| Name                          | Description                                                                                                                                                                                     |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_TIMER**](wm-timer.md) | Posted to the installing thread's message queue when a timer expires. The message is posted by the [**GetMessage**](/windows/win32/api/winuser/nf-winuser-getmessage) or [**PeekMessage**](/windows/win32/api/winuser/nf-winuser-peekmessagea) function. <br/> |



 

 

 
