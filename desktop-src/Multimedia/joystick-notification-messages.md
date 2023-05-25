---
title: Joystick Notification Messages
description: Joystick Notification Messages
ms.assetid: 9e8ccc1b-85a9-44bf-b561-6ad4c10cddd1
keywords:
- joysticks,notifications
- joysticks,messages
- joysticks,position
- joysticks,buttons
- MM_JOY1 messages
- MM_JOY2 messages
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Joystick Notification Messages

\[The feature associated with this page, [Joysticks](/windows/win32/multimedia/joysticks), is a legacy feature. It has been superseded by [Windows.Gaming.Input Namespace](/uwp/api/windows.gaming.input). **Windows.Gaming.Input Namespace** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Windows.Gaming.Input Namespace** instead of **Joysticks**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Joystick messages notify your application that a joystick has changed position or that one of its buttons has changed states. Messages beginning with MM\_JOY1 are sent to the function if your application requests input from the joystick using the identifier JOYSTICKID1, and MM\_JOY2 messages are sent if your application requests input from the joystick using the identifier JOYSTICKID2.

The messages in the following table identify the status of the joystick buttons:



| Message                                         | Description                                                     |
|-------------------------------------------------|-----------------------------------------------------------------|
| [**MM\_JOY1BUTTONDOWN**](mm-joy1buttondown.md) | A button on joystick JOYSTICKID1 has been pressed.              |
| [**MM\_JOY1BUTTONUP**](mm-joy1buttonup.md)     | A button on joystick JOYSTICKID1 has been released.             |
| [**MM\_JOY1MOVE**](mm-joy1move.md)             | Joystick JOYSTICKID1 changed position in the x- or y-direction. |
| [**MM\_JOY1ZMOVE**](mm-joy1zmove.md)           | Joystick JOYSTICKID1 changed position in the z-direction.       |
| [**MM\_JOY2BUTTONDOWN**](mm-joy2buttondown.md) | A button on joystick JOYSTICKID2 has been pressed.              |
| [**MM\_JOY2BUTTONUP**](mm-joy2buttonup.md)     | A button on joystick JOYSTICKID2 has been released.             |
| [**MM\_JOY2MOVE**](mm-joy2move.md)             | Joystick JOYSTICKID2 changed position in the x- or y-direction  |
| [**MM\_JOY2ZMOVE**](mm-joy2zmove.md)           | Joystick JOYSTICKID2 changed position in the z-direction.       |



 

All messages report nonexistent buttons as released.

 

 




