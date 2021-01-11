---
description: Specifies the method to use for motion matching.
ms.assetid: 75bbc189-3092-4813-9f45-54e8e48b05cd
title: MFPKEY_MOTIONMATCHMETHOD Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_MOTIONMATCHMETHOD Property

Specifies the method to use for motion matching.

## Constant for IPropertyBag

g\_wszWMVCMotionMatchMethod

## Data Type

VT\_I4

## Default Value

0

## Remarks

This property may be set to one of the following values.



| Value | Method used                       |
|-------|-----------------------------------|
| 0     | sum of absolute differences (SAD) |
| 1     | Hadamard                          |
| -1    | Macroblock-adaptive.              |



 

The sum of absolute differences (SAD) is a faster but less accurate method than the Hadamard transform. The Hadamard transform is more accurate but computationally intensive. The macroblock-adaptive mode provides a reasonable compromise between the two methods by dynamically choosing between the two transforms, selecting the Hadamard transform only when appropriate.

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

 

 




