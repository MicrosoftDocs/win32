---
description: A value indicating whether a frame was captured using active infrared (IR) illumination.
ms.assetid: D84772C8-902F-4302-8288-0430892A1896
title: MF_CAPTURE_METADATA_FRAME_ILLUMINATION attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_CAPTURE\_METADATA\_FRAME\_ILLUMINATION attribute

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

A value indicating whether a frame was captured using active infrared (IR) illumination.

## Data type

**UINT64**

## Remarks

This attribute is a bitmask. It is a 64 bit value for backward compatibility.

Active illumination is when a device has a light emitter close to the IR camera emitting a beam of light to illuminate the scene, typically emitting IR light so it won’t disturb human eyes. Set value to (value & 0x1) != 0 if frame was captured when active illumination was on and set (value & 0x1) == 0 if active illumination was off.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                      |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



 

 




