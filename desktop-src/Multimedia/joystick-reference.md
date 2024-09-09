---
title: Joystick Reference
description: Joystick Reference
ms.assetid: c2ad092f-a0c5-4e28-ada7-227dc52c3c83
keywords:
- Windows multimedia,joystick reference
- multimedia,joystick reference
- multimedia input,joystick reference
- joysticks,reference
- reference for joysticks,about
- joystick reference,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Joystick Reference

\[The feature associated with this page, [Joysticks](/windows/win32/multimedia/joysticks), is a legacy feature. It has been superseded by [Windows.Gaming.Input Namespace](/uwp/api/windows.gaming.input). **Windows.Gaming.Input Namespace** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Windows.Gaming.Input Namespace** instead of **Joysticks**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section describes the functions, structures, and messages associated with joysticks. The elements are grouped as follows:

## Device Capabilities

-   [**joyGetDevCaps**](/windows/win32/api/joystickapi/nf-joystickapi-joygetdevcaps)
-   [**joyGetNumDevs**](/windows/win32/api/joystickapi/nf-joystickapi-joygetnumdevs)
-   [**JOYCAPS**](/windows/win32/api/joystickapi/ns-joystickapi-joycaps)

## Querying a Joystick

-   [**joyConfigChanged**](/windows/desktop/api/joystickapi/nf-joystickapi-joyconfigchanged)
-   [**joyGetPos**](/windows/win32/api/joystickapi/nf-joystickapi-joygetpos)
-   [**joyGetPosEx**](/windows/win32/api/joystickapi/nf-joystickapi-joygetposex)
-   [**JOYINFO**](/windows/win32/api/joystickapi/ns-joystickapi-joyinfo)
-   [**JOYINFOEX**](/windows/win32/api/joystickapi/ns-joystickapi-joyinfoex)

## Capturing a Joystick

-   [**joyGetThreshold**](/windows/win32/api/joystickapi/nf-joystickapi-joygetthreshold)
-   [**joyReleaseCapture**](/windows/win32/api/joystickapi/nf-joystickapi-joyreleasecapture)
-   [**joySetCapture**](/windows/win32/api/joystickapi/nf-joystickapi-joysetcapture)
-   [**joySetThreshold**](/windows/win32/api/joystickapi/nf-joystickapi-joysetthreshold)
-   [**MM\_JOY1BUTTONDOWN**](mm-joy1buttondown.md)
-   [**MM\_JOY1BUTTONUP**](mm-joy1buttonup.md)
-   [**MM\_JOY1MOVE**](mm-joy1move.md)
-   [**MM\_JOY1ZMOVE**](mm-joy1zmove.md)
-   [**MM\_JOY2BUTTONDOWN**](mm-joy2buttondown.md)
-   [**MM\_JOY2BUTTONUP**](mm-joy2buttonup.md)
-   [**MM\_JOY2MOVE**](mm-joy2move.md)
-   [**MM\_JOY2ZMOVE**](mm-joy2zmove.md)

## Related topics

<dl> <dt>

[Joysticks](joysticks.md)
</dt> </dl>

 

 