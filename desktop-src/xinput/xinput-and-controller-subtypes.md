---
title: XINPUT and Controller Subtypes
description: A table of controller subtypes available in XInput.
ms.assetid: 4674028b-98cf-5346-7b93-f940150f3051
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# XINPUT and Controller Subtypes

A table of controller subtypes available in XInput.



| Subtype                                                                                           | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| XINPUT\_DEVSUBTYPE\_UNKNOWN                                                                       | Unknown.<br/> The controller type is unknown.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| XINPUT\_DEVSUBTYPE\_GAMEPAD                                                                       | Gamepad controller.<br/> Includes Left and Right Sticks, Left and Right Triggers, Directional Pad, and all standard buttons (A, B, X, Y, START, BACK, LB, RB, LSB, RSB).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                |
| XINPUT\_DEVSUBTYPE\_WHEEL                                                                         | Racing wheel controller. <br/> Left Stick X reports the wheel rotation, Right Trigger is the acceleration pedal, and Left Trigger is the brake pedal. Includes Directional Pad and most standard buttons (A, B, X, Y, START, BACK, LB, RB). LSB and RSB are optional.<br/>                                                                                                                                                                                                                                                                                                                                   |
| XINPUT\_DEVSUBTYPE\_ARCADE\_STICK                                                                 | Arcade stick controller. <br/> Includes a Digital Stick that reports as a DPAD (up, down, left, right), and most standard buttons (A, B, X, Y, START, BACK). The Left and Right Triggers are implemented as digital buttons and report either 0 or 0xFF. LB, LSB, RB, and RSB are optional.<br/>                                                                                                                                                                                                                                                                                                             |
| XINPUT\_DEVSUBTYPE\_FLIGHT\_STICK                                                                 | Flight stick controller. <br/> Includes a pitch and roll stick that reports as the Left Stick, a POV Hat which reports as the Right Stick, a rudder (handle twist or rocker) that reports as Left Trigger, and a throttle control as the Right Trigger. Includes support for a primary weapon (A), secondary weapon (B), and other standard buttons (X, Y, START, BACK). LB, LSB, RB, and RSB are optional.<br/>                                                                                                                                                                                             |
| XINPUT\_DEVSUBTYPE\_DANCE\_PAD                                                                    | Dance pad controller. <br/> Includes the Directional Pad and standard buttons (A, B, X, Y) on the pad, plus BACK and START.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| XINPUT\_DEVSUBTYPE\_GUITAR XINPUT\_DEVSUBTYPE\_GUITAR\_ALTERNATE XINPUT\_DEVSUBTYPE\_GUITAR\_BASS | Guitar controller. <br/> The strum bar maps to DPAD (up and down), and the frets are assigned to A (green), B (red), Y (yellow), X (blue), and LB (orange). Right Stick Y is associated with a vertical orientation sensor; Right Stick X is the whammy bar. Includes support for BACK, START, DPAD (left, right). Left Trigger (pickup selector), Right Trigger, RB, LSB (fret modifier), RSB are optional.<br/> Guitar Bass is identical to Guitar, with the distinct subtype to simplify setup.<br/> Guitar Alt supports a larger range of movement for the vertical orientation sensor.<br/> |
| XINPUT\_DEVSUBTYPE\_DRUM\_KIT                                                                     | Drum controller.<br/> The drum pads are assigned to buttons: A for green (Floor Tom), B for red (Snare Drum), X for blue (Low Tom), Y for yellow (High Tom), and LB for the pedal (Bass Drum). Includes Directional-Pad, BACK, and START. RB, LSB, and RSB are optional.<br/>                                                                                                                                                                                                                                                                                                                                |
| XINPUT\_DEVSUBTYPE\_ARCADE\_PAD                                                                   | Arcade pad controller. <br/> Includes Directional Pad and most standard buttons (A, B, X, Y, START, BACK, LB, RB). The Left and Right Triggers are implemented as digital buttons and report either 0 or 0xFF. Left Stick, Right Stick, LSB, and RSB are optional.<br/>                                                                                                                                                                                                                                                                                                                                      |



 

> [!Note]  
> The legacy version of XINPUT on Windows Vista (XInput 9.1.0) will always return a fixed subtype of **XINPUT\_DEVSUBTYPE\_GAMEPAD** regardless of attached device.

 

 

 





