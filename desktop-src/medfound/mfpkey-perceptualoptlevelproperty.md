---
description: Specifies whether the codec should use conservative perceptual optimization when encoding.
ms.assetid: f44fd932-d8f8-46c7-b17c-27e6141408ab
title: MFPKEY_PERCEPTUALOPTLEVEL Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_PERCEPTUALOPTLEVEL Property

Specifies whether the codec should use conservative perceptual optimization when encoding.

## Constant for IPropertyBag

g\_wszWMVCPerceptualOptLevel

## Data Type

VT\_I4

## Default Value

0

## Remarks

Conservative perceptual optimization is a process by which the codec attempts to identify "important" and "unimportant" regions in the video frame. After identifying these regions of the frame, the codec will give a higher priority to the quality of important regions, at the expense of the quality of unimportant regions.

Perceptual optimization emphasizes making the image appear correct to the human eye instead of insisting on strict mathematical accuracy.

The results of the optimization will vary considerably depending on the type of video being encoded. This feature could be well suited for low bit-rate and low resolution encoding (for example, web streaming), but should probably be avoided when aiming for archival video quality.

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

 

 




