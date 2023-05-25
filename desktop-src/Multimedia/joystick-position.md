---
title: Joystick Position
description: Joystick Position
ms.assetid: db0d1125-e39f-445b-bd65-373633cad578
keywords:
- joysticks,position
- joysticks,buttons
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Joystick Position

\[The feature associated with this page, [Joysticks](/windows/win32/multimedia/joysticks), is a legacy feature. It has been superseded by [Windows.Gaming.Input Namespace](/uwp/api/windows.gaming.input). **Windows.Gaming.Input Namespace** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Windows.Gaming.Input Namespace** instead of **Joysticks**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can query a joystick for position and button information by using the [**joyGetPos**](/windows/win32/api/joystickapi/nf-joystickapi-joygetpos) function. For example, an application can query the joystick for baseline position values. The Joystick Control Panel property sheet uses this technique when calibrating the joystick.

You can also query a joystick or other device that has extended capabilities by using the [**joyGetPosEx**](/windows/win32/api/joystickapi/nf-joystickapi-joygetposex) function.

 

 