---
title: Time-Based Notifications
description: Time-Based Notifications
ms.assetid: cf7bc0d4-f3bd-4416-b85f-0ff51a0efbbc
keywords:
- joysticks,notifications
- joysticks,messages
- joysticks,time-based notifications
- time-based joystick notifications
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Time-Based Notifications

\[The feature associated with this page, [Joysticks](/windows/win32/multimedia/joysticks), is a legacy feature. It has been superseded by [Windows.Gaming.Input Namespace](/uwp/api/windows.gaming.input). **Windows.Gaming.Input Namespace** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Windows.Gaming.Input Namespace** instead of **Joysticks**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can notify the operating system to send joystick messages to an application at regular time intervals by setting the *fChanged* parameter of [**joySetCapture**](/windows/win32/api/joystickapi/nf-joystickapi-joysetcapture) to **FALSE** and by specifying the interval length between successive messages. To do this, assign the *uPeriod* parameter a value between the minimum and maximum polling frequencies for the joystick. You can determine this range by using the [**joyGetDevCaps**](/windows/win32/api/joystickapi/nf-joystickapi-joygetdevcaps) function, which fills the **wPeriodMin** and **wPeriodMax** members in the [**JOYCAPS**](/windows/win32/api/joystickapi/ns-joystickapi-joycaps) structure. If the *uPeriod* value is outside the range of valid polling frequencies for the joystick, the joystick driver uses the minimum or maximum polling frequency, whichever is closer to the *uPeriod* value.

> [!Note]  
> Windows sets up a timer event with each call to **joySetCapture**.

 

 

 