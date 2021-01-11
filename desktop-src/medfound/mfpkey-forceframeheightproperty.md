---
description: Specifies an intermediate frame height for encoded video.
ms.assetid: 7382ec31-6d59-4e8c-94eb-804786074038
title: MFPKEY_FORCEFRAMEHEIGHT Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_FORCEFRAMEHEIGHT Property

Specifies an intermediate frame height for encoded video.

## Constant for IPropertyBag

g\_wszWMVCForceFrameHeight

## Data Type

VT\_I4

## Remarks

You can set this value and the [MFPKEY\_FORCEFRAMEWIDTH](mfpkey-forceframewidthproperty.md) property to force the encoder to encode the video stream with a frame size that is smaller than the input or output frame sizes. When decoded, the video will be resized to its original input resolution.

Valid frame dimensions on either axis are 2 to 8192 pixels. Frame dimensions must be divisible by 2.

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

 

 




