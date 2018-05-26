---
title: Time-Based Notifications
description: Time-Based Notifications
ms.assetid: cf7bc0d4-f3bd-4416-b85f-0ff51a0efbbc
keywords:
- joysticks,notifications
- joysticks,messages
- joysticks,time-based notifications
- time-based joystick notifications
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Time-Based Notifications

You can notify the operating system to send joystick messages to an application at regular time intervals by setting the *fChanged* parameter of [**joySetCapture**](joysetcapture.md) to **FALSE** and by specifying the interval length between successive messages. To do this, assign the *uPeriod* parameter a value between the minimum and maximum polling frequencies for the joystick. You can determine this range by using the [**joyGetDevCaps**](joygetdevcaps.md) function, which fills the **wPeriodMin** and **wPeriodMax** members in the [**JOYCAPS**](joycaps.md) structure. If the *uPeriod* value is outside the range of valid polling frequencies for the joystick, the joystick driver uses the minimum or maximum polling frequency, whichever is closer to the *uPeriod* value.

> [!Note]  
> Windows sets up a timer event with each call to **joySetCapture**.

 

 

 




