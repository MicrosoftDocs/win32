---
title: DirectInput and XUSB Devices
description: The driver for the Xbox Common Controller class (XUSB) on Windows implements the kernel-mode interface for the XINPUT DLL.
ms.assetid: 8bf47b07-a1b6-7721-2136-3853e72c71ad
ms.topic: article
ms.date: 05/31/2018
---

# DirectInput and XUSB Devices

The driver for the Xbox Common Controller class (XUSB) on Windows implements the kernel-mode interface for the XINPUT DLL. To provide a good experience for legacy titles that use the [DirectInput](/previous-versions/windows/desktop/ee416842(v=vs.85)) API with the common controller device, the driver also exports a Human Interface Device (HID) class interface, which is picked up by DirectInput. We chose the mapping of XUSB to HID based on typical behavior in a set of gaming applications for the original XINPUT version, and we updated the mapping for newer subtypes. This topic describes the mapping.

## Human Interface Device (HID)

HID standard is a standard from the Universal Serial Bus (USB) committee originally proposed by Microsoft to generalize protocols for input devices. It consists of a byte-code description language and can express gamepads, mice, joysticks, throttle and rudder controls, and multi-axis controllers. Because this standard is so generalized, you might have difficulty writing software that consumes input from arbitrary devices. Therefore, for the game-centric [DirectInput](/previous-versions/windows/desktop/ee416842(v=vs.85)) API, we developed a specific sub-mapping of types to encourage hardware manufactures to support through their drivers.

- [USB Device Class Definition for HID v1.11](https://www.usb.org/document-library/device-class-definition-hid-111)

> [!Important]
> You can also access HID input devices via [RawInput API](../inputdev/about-raw-input.md) and process input reports via low level [HID API](/windows-hardware/drivers/hid/introduction-to-hid-concepts) but vibration feedback will not work as with [DirectInput](/previous-versions/windows/desktop/ee416842(v=vs.85)).

## Mappings

The XUSB driver implements both an XUSB class interface and a HID class interface for devices in order to support both XINPUT and [DirectInput](/previous-versions/windows/desktop/ee416842(v=vs.85)) usage. This mapping is based on the XUSB subtype information. The driver implements four distinct groups of mappings.

| XUSB Subtype                                      | Mapping                     |
|---------------------------------------------------|-----------------------------|
| XINPUT\_DEVSUBTYPE\_GAMEPAD (Subtype 1)           | Gamepad                     |
| XINPUT\_DEVSUBTYPE\_WHEEL (Subtype 2)             | Wheel                       |
| XINPUT\_DEVSUBTYPE\_ARCADE\_STICK (Subtype 3)     | Arcade Stick/Arcade Pad     |
| XINPUT\_DEVSUBTYPE\_FLIGHT\_STICK (Subtype 4)     | Flight Stick                |
| XINPUT\_DEVSUBTYPE\_DANCE\_PAD (Subtype 5)        | Default for any new subtype |
| XINPUT\_DEVSUBTYPE\_GUITAR (Subtype 6)            | Guitar                      |
| XINPUT\_DEVSUBTYPE\_GUITAR\_ALTERNATE (Subtype 7) |                             |
| XINPUT\_DEVSUBTYPE\_DRUM\_KIT (Subtype 8)         |                             |
| XINPUT\_DEVSUBTYPE\_GUITAR\_BASS (Subtype 11)     |                             |
| XINPUT\_DEVSUBTYPE\_ARCADE\_PAD (Subtype 19)      |                             |

> [!Note]  
> The following HID mappings are static. This means that even if the device capabilities report indicates that a particular button or axis is not supported, the mapping will still include it but will always report an off state or center value.

## Gamepad

This is the default mapping and is designed around the standard Xbox Common Controller gamepad, and is exposed as a *Gamepad* HID usage type.

| Control                      | HID Usage Name | Usage Page | Usage ID   |
|------------------------------|----------------|------------|------------|
| Left Stick                   | X, Y           | 0x01       | 0x30, 0x31 |
| Right Stick                  | Rx, Ry         | 0x01       | 0x33, 0x34 |
| Left Trigger + Right Trigger | Z\*            | 0x01       | 0x32       |
| D-Pad Up, Down, Left, Right  | Hat Switch     | 0x01       | 0x39       |
| A                            | Button 1       | 0x09       | 0x01       |
| B                            | Button 2       | 0x09       | 0x02       |
| X                            | Button 3       | 0x09       | 0x03       |
| Y                            | Button 4       | 0x09       | 0x04       |
| LB (left bumper)             | Button 5       | 0x09       | 0x05       |
| RB (right bumper)            | Button 6       | 0x09       | 0x06       |
| BACK                         | Button 7       | 0x09       | 0x07       |
| START                        | Button 8       | 0x09       | 0x08       |
| LSB (left stick button)      | Button 9       | 0x09       | 0x09       |
| RSB (right stick button)     | Button 10      | 0x09       | 0x0A       |

> [!Note]  
> (\*): This is combined so that Z exhibits the centering behavior expected by most titles for rotation; this does mean it is not possible to see all possible trigger combination values through [DirectInput](/previous-versions/windows/desktop/ee416842(v=vs.85)) and HID.

## Arcade Stick/Arcade Pad

This is the mapping designed around the Arcade Stick controller, and is exposed as a *Gamepad* HID usage type. The Arcade Pad is very much like an Arcade Stick, but in a smaller form-factor. These designs replace the analog Left Trigger and Right Trigger with digital buttons that report the minimum and maximum axis value.

| Control                     | HID Usage Name | Usage Page | Usage ID |
|-----------------------------|----------------|------------|----------|
| D-Pad Up, Down, Left, Right | Hat Switch     | 0x01       | 0x39     |
| A                           | Button 1       | 0x09       | 0x01     |
| B                           | Button 2       | 0x09       | 0x02     |
| X                           | Button 3       | 0x09       | 0x03     |
| Y                           | Button 4       | 0x09       | 0x04     |
| LB (left bumper)            | Button 5       | 0x09       | 0x05     |
| RB (right bumper)           | Button 6       | 0x09       | 0x06     |
| BACK                        | Button 7       | 0x09       | 0x07     |
| START                       | Button 8       | 0x09       | 0x08     |
| Left Trigger                | Button 9       | 0x09       | 0x09     |
| Right Trigger               | Button 10      | 0x09       | 0x0A     |

These devices may or may not support additional controls, but these are not exposed by the HID mapping: Left Stick, Right Stick, LSB (left stick button), and RSB (right stick button).

## Wheel

This mapping is designed around the Xbox Racing Wheel, and is exposed as a *Gamepad* HID usage type.

| Control                                                        | HID Usage Name | Usage Page | Usage ID |
|----------------------------------------------------------------|----------------|------------|----------|
| Wheel (Left Stick X)                                           | X              | 0x01       | 0x30     |
| Accelerator Pedal (Right Trigger) + Brake Pedal (Left Trigger) | Z\*            | 0x01       | 0x32     |
| D-Pad Up, Down, Left, Right                                    | Hat Switch     | 0x01       | 0x39     |
| A                                                              | Button 1       | 0x09       | 0x01     |
| B                                                              | Button 2       | 0x09       | 0x02     |
| X                                                              | Button 3       | 0x09       | 0x03     |
| Y                                                              | Button 4       | 0x09       | 0x04     |
| LB (left bumper)                                               | Button 5       | 0x09       | 0x05     |
| RB (right bumper)                                              | Button 6       | 0x09       | 0x06     |
| LSB (left stick button)                                        | Button 7       | 0x09       | 0x07     |
| RSB (right stick button)                                       | Button 8       | 0x09       | 0x08     |
| BACK                                                           | Button 9       | 0x09       | 0x09     |
| START                                                          | Button 10      | 0x09       | 0x0A     |

> [!Note]  
> (\*): This is combined so that Z exhibits the centering behavior expected by most titles for the brake and accelerator controls; this does mean it is not possible to see all possible pedal combination values through [DirectInput](/previous-versions/windows/desktop/ee416842(v=vs.85)).

## Flight Stick

This mapping is designed around the Xbox Flight Stick, and is exposed as a *Joystick* HID usage type.

| Control                     | Usage Name | Usage Page | Usage ID   |
|-----------------------------|------------|------------|------------|
| Flight Stick (Left Stick)   | X, Y       | 0x01       | 0x30, 0x31 |
| POV Hat (Right Stick)       | Rx, Ry     | 0x01       | 0x33, 0x34 |
| Throttle (Right Trigger)    | Z          | 0x01       | 0x32       |
| Rudder (Left Trigger)       | Rz         | 0x01       | 0x35       |
| D-Pad Up, Down, Left, Right | Hat Switch | 0x01       | 0x39       |
| Primary Weapon (A)          | Button 1   | 0x09       | 0x01       |
| Secondary Weapon (B)        | Button 2   | 0x09       | 0x02       |
| X                           | Button 3   | 0x09       | 0x03       |
| Y                           | Button 4   | 0x09       | 0x04       |
| LB (left bumper)            | Button 5   | 0x09       | 0x05       |
| RB (right bumper)           | Button 6   | 0x09       | 0x06       |
| BACK                        | Button 7   | 0x09       | 0x07       |
| START                       | Button 8   | 0x09       | 0x08       |
| LSB (left stick button)     | Button 9   | 0x09       | 0x09       |
| RSB (right stick button)    | Button 10  | 0x09       | 0x0A       |

> [!Note]  
> This is based on the final Flight Stick design. Because this differs from early Flight Stick definitions, many devices have a mode switch that supports the old versus new model. This mapping assumes the new model.