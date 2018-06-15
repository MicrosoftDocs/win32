---
title: Joystick Capabilities
description: Joystick Capabilities
ms.assetid: 910c7f1d-e20a-4a03-b512-9a7f8cb1e559
keywords:
- multimedia input,joysticks
- joysticks,two-axis movement
- joysticks,three-axis movement
- joysticks,buttons
- joysticks,ranges of motion
- joysticks,polling frequencies
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Joystick Capabilities

Joysticks can support two- or three-axis movement and up to four buttons. Joysticks also support different *ranges of motion* and *polling frequencies*. The range of motion is the distance a joystick handle can move from its resting position to the position farthest from its resting position. The polling frequency is the time interval between joystick queries.

Joystick drivers can support either one or two joysticks. You can determine the number of joysticks supported by a joystick driver by using the [**joyGetNumDevs**](https://msdn.microsoft.com/en-us/library/Dd757106(v=VS.85).aspx) function. This function returns an unsigned integer that contains the number of supported joysticks or zero if there is no joystick support. The return value does not indicate the number of joysticks attached to the system.

You can determine if a joystick is attached to the system by using the [**joyGetPos**](https://msdn.microsoft.com/en-us/library/Dd757107(v=VS.85).aspx) function. This function returns JOYERR\_NOERROR if the specified device is attached. Otherwise , it returns JOYERR\_UNPLUGGED.

Each joystick has several capabilities that are available to your application. You can retrieve the capabilities of a joystick by using the [**joyGetDevCaps**](https://msdn.microsoft.com/en-us/library/Dd757105(v=VS.85).aspx) function. This function fills a [**JOYCAPS**](https://msdn.microsoft.com/en-us/library/Dd757103(v=VS.85).aspx) structure with joystick capabilities such as the minimum and maximum values for its coordinate system, the number of buttons on the joystick, and the minimum and maximum polling frequencies.

 

 




