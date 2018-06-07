---
title: DirectInput and XUSB Devices
description: The driver for the Xbox 360 Common Controller class (XUSB) on Windows implements the kernel-mode interface for the XINPUT DLL.
ms.assetid: 8bf47b07-a1b6-7721-2136-3853e72c71ad
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DirectInput and XUSB Devices

The driver for the Xbox 360 Common Controller class (XUSB) on Windows implements the kernel-mode interface for the XINPUT DLL. To provide a good experience for legacy titles that use the [DirectInput](https://msdn.microsoft.com/windows/desktop/c5d0c734-9f01-30f5-651c-82ac9c21310e) API with the common controller device, the driver also exports a Human Interface Device (HID) class interface, which is picked up by DirectInput. We chose the mapping of XUSB to HID based on typical behavior in a set of gaming applications for the original XINPUT version, and we updated the mapping for newer subtypes. This topic describes the mapping.

## Human Interface Device (HID)

HID standard is a standard from the Universal Serial Bus (USB) committee originally proposed by Microsoft to generalize protocols for input devices. It consists of a byte-code description language and can express gamepads, mice, joysticks, throttle and rudder controls, and multi-axis controllers. Because this standard is so generalized, you might have difficulty writing software that consumes input from arbitrary devices. Therefore, for the game-centric [DirectInput](https://msdn.microsoft.com/windows/desktop/c5d0c734-9f01-30f5-651c-82ac9c21310e) API, we developed a specific sub-mapping of types to encourage hardware manufactures to support through their drivers.

-   [USB Device Class Definition for HID v1.11](http://go.microsoft.com/fwlink/p/?LinkID=155094)
-   [HID Game Controllers and DirectInput](http://www.microsoft.com/whdc/archive/hidgame.mspx)

## Mappings

The XUSB driver implements both an XUSB class interface and a HID class interface for devices in order to support both XINPUT and [DirectInput](https://msdn.microsoft.com/windows/desktop/c5d0c734-9f01-30f5-651c-82ac9c21310e) usage. This mapping is based on the XUSB subtype information. The driver implements four distinct groups of mappings. 

| XUSB Subtype                                      | Mapping                     |
|---------------------------------------------------|-----------------------------|
| XINPUT\_DEVSUBTYPE\_GAMEPAD (Subtype 1)           | Gamepad                     |
| XINPUT\_DEVSUBTYPE\_DANCE\_PAD (Subtype 5)        | Default for any new subtype |
| XINPUT\_DEVSUBTYPE\_GUITAR (Subtype 6)            |                             |
| XINPUT\_DEVSUBTYPE\_GUITAR\_ALTERNATE (Subtype 7) |                             |
| XINPUT\_DEVSUBTYPE\_DRUM\_KIT (Subtype 8)         |                             |
| XINPUT\_DEVSUBTYPE\_GUITAR\_BASS (Subtype 11)     |                             |
| XINPUT\_DEVSUBTYPE\_ARCADE\_STICK (Subtype 3)     | Arcade Stick/Arcade Pad     |
| XINPUT\_DEVSUBTYPE\_ARCADE\_PAD (Subtype 19)      |                             |
| XINPUT\_DEVSUBTYPE\_WHEEL (Subtype 2)             | Wheel                       |
| XINPUT\_DEVSUBTYPE\_FLIGHT\_STICK (Subtype 4)     | Flight Stick                |



 

> [!Note]  
> The following HID mappings are static. This means that even if the device capabilities report indicates that a particular button or axis is not supported, the mapping will still include it but will always report an off state or center value.

 

## Gamepad

This is the default mapping and is designed around the standard Xbox 360 Common Controller gamepad, and is exposed as a Gamepad usage type. 

| Control                      | DirectInput HID Mapping |
|------------------------------|-------------------------|
| Left Stick                   | X, Y                    |
| Right Stick                  | Rx, Ry                  |
| Left Trigger + Right Trigger | Z\*                     |
| D-Pad Up, Down, Left, Right  | Hat Switch              |
| A                            | Button1                 |
| B                            | Button 2                |
| X                            | Button 3                |
| Y                            | Button 4                |
| LB (left bumper)             | Button 5                |
| RB (right bumper)            | Button 6                |
| BACK                         | Button 7                |
| START                        | Button 8                |
| LSB (left stick button)      | Button 9                |
| RSB (right stick button)     | Button 10               |



 

> [!Note]  
> (\*): This is combined so that Z exhibits the centering behavior expected by most titles for rotation; this does mean it is not possible to see all possible trigger combination values through [DirectInput](https://msdn.microsoft.com/windows/desktop/c5d0c734-9f01-30f5-651c-82ac9c21310e).

 

## Arcade Stick/Arcade Pad

This is the mapping designed around the Arcade Stick controller, and is exposed as a Gamepad usage type. The Arcade Pad is very much like an Arcade Stick, but in a smaller form-factor. These designs replace the analog Left Trigger and Right Trigger with digital buttons that report the minimum and maximum axis value. 

| Control                     | DirectInput HID Mapping |
|-----------------------------|-------------------------|
| D-Pad Up, Down, Left, Right | Hat Switch              |
| A                           | Button1                 |
| B                           | Button 2                |
| X                           | Button 3                |
| Y                           | Button 4                |
| LB (left bumper)            | Button 5                |
| RB (right bumper)           | Button 6                |
| BACK                        | Button 7                |
| START                       | Button 8                |
| Left Trigger                | Button 9                |
| Right Trigger               | Button 10               |



 

These devices may or may not support additional controls, but these are not exposed by the HID mapping: Left Stick, Right Stick, LSB (left stick button), and RSB (right stick button).

## Wheel

This mapping is designed around the Xbox 360 Racing Wheel, and is exposed as a Gamepad usage type.

| Control                                                        | DirectInput HID Mapping |
|----------------------------------------------------------------|-------------------------|
| Wheel (Left Stick X)                                           | X                       |
| Accelerator Pedal (Right Trigger) + Brake Pedal (Left Trigger) | Z\*                     |
| D-Pad Up, Down, Left, Right                                    | Hat Switch              |
| A                                                              | Button1                 |
| B                                                              | Button 2                |
| X                                                              | Button 3                |
| Y                                                              | Button 4                |
| LB (left bumper)                                               | Button 5                |
| RB (right bumper)                                              | Button 6                |
| LSB (left stick button)                                        | Button 7                |
| RSB (right stick button)                                       | Button 8                |
| BACK                                                           | Button 9                |
| START                                                          | Button 10               |



 

> [!Note]  
> (\*): This is combined so that Z exhibits the centering behavior expected by most titles for the brake and accelerator controls; this does mean it is not possible to see all possible pedal combination values through [DirectInput](https://msdn.microsoft.com/windows/desktop/c5d0c734-9f01-30f5-651c-82ac9c21310e).

 

## Flight Stick

This mapping is designed around the Xbox 360 Flight Stick, and is exposed as a Joystick usage type.

| Control                     | DirectInput HID Mapping |
|-----------------------------|-------------------------|
| Flight Stick (Left Stick)   | X, Y                    |
| POV Hat (Right Stick)       | Rx, Ry                  |
| Throttle (Right Trigger)    | Z                       |
| Rudder (Left Trigger)       | Rz                      |
| D-Pad Up, Down, Left, Right | Hat Switch              |
| Primary Weapon (A)          | Button1                 |
| Secondary Weapon (B)        | Button 2                |
| X                           | Button 3                |
| Y                           | Button 4                |
| LB (left bumper)            | Button 5                |
| RB (right bumper)           | Button 6                |
| BACK                        | Button 7                |
| START                       | Button 8                |
| LSB (left stick button)     | Button 9                |
| RSB (right stick button)    | Button 10               |



 

> [!Note]  
> This is based on the final Flight Stick design. Because this differs from early Flight Stick definitions, many devices have a mode switch that supports the old versus new model. This mapping assumes the new model.

 

 

 




