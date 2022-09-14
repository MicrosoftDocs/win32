---
title: Joystick Notifications
description: Joystick Notifications
ms.assetid: 523dfae3-bbd5-4955-96f3-1710e29d003f
keywords:
- joysticks,notifications
- joysticks,messages
- captured joysticks
- unplugged joysticks
ms.topic: article
ms.date: 05/31/2018
---

# Joystick Notifications

You can capture direct joystick messages to be sent to a function by using the [**joySetCapture**](/windows/win32/api/joystickapi/nf-joystickapi-joysetcapture) function. Only one application at a time can capture messages from a joystick, but you can query the joystick from another application by using the [**joyGetPos**](/windows/win32/api/joystickapi/nf-joystickapi-joygetpos) or [**joyGetPosEx**](/windows/win32/api/joystickapi/nf-joystickapi-joygetposex) function.

> [!Note]  
> A joystick message can fail to reach the application that captured the joystick if a second application uses **joyGetPos** or **joyGetPosEx** to query the joystick at approximately the same time that the message is sent. In this case, the second application could intercept the message.

 

If you want to capture messages from two joysticks attached to the system, use [**joySetCapture**](/windows/win32/api/joystickapi/nf-joystickapi-joysetcapture) twice, once for each joystick. Your window receives separate and distinct messages for each device.

You can release a captured joystick by using the [**joyReleaseCapture**](/windows/win32/api/joystickapi/nf-joystickapi-joyreleasecapture) function. If an application does not release the joystick before ending, the joystick is automatically released shortly after the capture window is destroyed.

You cannot capture an unplugged joystick. The **joySetCapture** function returns JOYERR\_UNPLUGGED if the specified device is unplugged.

 

 