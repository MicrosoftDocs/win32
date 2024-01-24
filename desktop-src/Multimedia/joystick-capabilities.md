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
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Joystick Capabilities

\[The feature associated with this page, [Joysticks](/windows/win32/multimedia/joysticks), is a legacy feature. It has been superseded by [Windows.Gaming.Input Namespace](/uwp/api/windows.gaming.input). **Windows.Gaming.Input Namespace** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Windows.Gaming.Input Namespace** instead of **Joysticks**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Joysticks can support two- or three-axis movement and up to four buttons. Joysticks also support different *ranges of motion* and *polling frequencies*. The range of motion is the distance a joystick handle can move from its resting position to the position farthest from its resting position. The polling frequency is the time interval between joystick queries.

Joystick drivers can support either one or two joysticks. You can determine the number of joysticks supported by a joystick driver by using the [**joyGetNumDevs**](/windows/win32/api/joystickapi/nf-joystickapi-joygetnumdevs) function. This function returns an unsigned integer that contains the number of supported joysticks or zero if there is no joystick support. The return value does not indicate the number of joysticks attached to the system.

You can determine if a joystick is attached to the system by using the [**joyGetPos**](/windows/win32/api/joystickapi/nf-joystickapi-joygetpos) function. This function returns JOYERR\_NOERROR if the specified device is attached. Otherwise , it returns JOYERR\_UNPLUGGED.

Each joystick has several capabilities that are available to your application. You can retrieve the capabilities of a joystick by using the [**joyGetDevCaps**](/windows/win32/api/joystickapi/nf-joystickapi-joygetdevcaps) function. This function fills a [**JOYCAPS**](/windows/win32/api/joystickapi/ns-joystickapi-joycaps) structure with joystick capabilities such as the minimum and maximum values for its coordinate system, the number of buttons on the joystick, and the minimum and maximum polling frequencies.

 

 