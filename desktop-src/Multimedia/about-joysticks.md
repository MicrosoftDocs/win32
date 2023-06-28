---
title: About Joysticks
description: About Joysticks
ms.assetid: 0cfff45b-48d4-4e0c-addf-e131d3a31187
keywords:
- Windows multimedia,joysticks
- multimedia,joysticks
- multimedia input,joysticks
- joysticks,about
- joysticks,two-axis movement
- joysticks,three-axis movement
- joysticks,buttons
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About Joysticks

\[The feature associated with this page, [Joysticks](/windows/win32/multimedia/joysticks), is a legacy feature. It has been superseded by [Windows.Gaming.Input Namespace](/uwp/api/windows.gaming.input). **Windows.Gaming.Input Namespace** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Windows.Gaming.Input Namespace** instead of **Joysticks**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The joystick is an ancillary input device for applications that provide alternatives to using the keyboard and mouse. The joystick provides positional information within a coordinate system that has absolute maximum and minimum values in each axis of movement.

Joystick services are loaded when the operating system is started. The joystick services can simultaneously monitor two joysticks, each with two- or three-axis movement. Each joystick can have up to four buttons. You can use the joystick functions to determine the capabilities of the joysticks and joystick driver. Also, you can process a joystick's positional and button information by querying the joystick directly or by capturing the joystick and processing messages from it. The latter method is simpler because your application does not have to manually query the joystick or track the time to generate queries at regular intervals.

 

 




