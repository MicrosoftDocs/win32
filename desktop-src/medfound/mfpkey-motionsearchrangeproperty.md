---
description: Specifies the range used in motion searches.
ms.assetid: b2026f47-ac39-4276-8359-c939b202f00c
title: MFPKEY_MOTIONSEARCHRANGE Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_MOTIONSEARCHRANGE Property

Specifies the range used in motion searches.

## Constant for IPropertyBag

g\_wszWMVCMotionSearchRange

## Data Type

VT\_I4

## Default Value

0

## Remarks

This property may be set to one of the following values. H denotes horizontal range and V denotes vertical range. All ranges are given in pixels.



| Value | Range                                |
|-------|--------------------------------------|
| 0     | +63.75/-64.0 H, +31.75/-32.0 V       |
| 1     | +127.75/-128.0 H, +63.75/-64.0 V     |
| 2     | +511.75/-512.0 H, +127.75/-128.0 V   |
| 3     | +1023.75/-1024.0 H, +255.75/-256.0 V |
| -1    | Macroblock-adaptive (automatic)      |



 

This property controls the size of the frame area that the codec will search for an element that may have exhibited motion between frames. A larger search window will help find faster motion but will require more CPU time. The CPU requirements are approximately doubled at each level.

The automatic mode (-1) will dynamically select the most efficient mode.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




