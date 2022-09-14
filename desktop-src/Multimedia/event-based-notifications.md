---
title: Event-Based Notifications
description: Event-Based Notifications
ms.assetid: bd483865-f983-416a-9b72-475fe9679cd1
keywords:
- joysticks,notifications
- joysticks,messages
- joysticks,event-based notifications
- joysticks,movement threshold
- event-based joystick notifications
ms.topic: article
ms.date: 05/31/2018
---

# Event-Based Notifications

You can ask the system to send joystick messages to an application whenever the position of a joystick axis changes by a value greater than the *movement threshold* of the device. The movement threshold is the distance the joystick must be moved before a joystick position change message is sent to a window that has captured the device. For more information, see [**MM\_JOY1MOVE**](mm-joy1move.md), [**MM\_JOY1ZMOVE**](mm-joy1zmove.md), [**MM\_JOY2MOVE**](mm-joy2move.md), or [**MM\_JOY2ZMOVE**](mm-joy2zmove.md).

The threshold is initially zero. You can set the movement threshold by using the [**joySetThreshold**](/windows/win32/api/joystickapi/nf-joystickapi-joysetthreshold) function. You can retrieve the minimum polling frequency of the joystick by using the [**joyGetDevCaps**](/windows/win32/api/joystickapi/nf-joystickapi-joygetdevcaps) function.

 

 