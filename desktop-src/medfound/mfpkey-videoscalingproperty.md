---
description: Specifies whether the codec will use video scaling optimization.
ms.assetid: a21d0100-e020-4e74-b8e3-bb7071194828
title: MFPKEY_VIDEOSCALING Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_VIDEOSCALING Property

Specifies whether the codec will use video scaling optimization.

## Constant for IPropertyBag

g\_wszWMVCVideoScaling

## Data Type

VT\_I4

## Default Value

0

## Remarks

Video scaling is a type of perceptual optimization that can improve the visual quality of video encoded at low bit rates. The video scaling optimization reduces pronounced artifacts, but can sacrifice image detail. This optimization affects the luma range of the encoded video as described below but does not affect the physical resolution of the output video.

This property may be set to one of the following values.



| Value | Description                                                                                                           |
|-------|-----------------------------------------------------------------------------------------------------------------------|
| 0     | Video scaling will not be used.                                                                                       |
| 1     | The encoder will use conservative video scaling optimization. The luma range will be scaled from 0...255 to 26...229. |
| 2     | The encoder will use aggressive video scaling optimization. The luma range will be scaled from 0...255 to 31...224.   |



 

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

 

 




