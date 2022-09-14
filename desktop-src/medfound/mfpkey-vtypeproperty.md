---
description: Specifies the logic that the codec will use to detect interlaced source video.
ms.assetid: 29c7fc1c-2047-4562-ba14-48f9cfbfe68c
title: MFPKEY_VTYPE Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_VTYPE Property

Specifies the logic that the codec will use to detect interlaced source video.

## Constant for IPropertyBag

g\_wszWMVCVType

## Data Type

VT\_I4

## Default Value

0

## Remarks

This property may be set to one of the following values.



| Value | Description                                                                                                                                 |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------|
| 0     | The codec will use the standard frame-type detection logic.                                                                                 |
| 1     | The codec will treat all source video frames as interlaced frames.                                                                          |
| 2     | The codec will treat all source video frames as fields of interlaced video.                                                                 |
| 3     | The codec will automatically determine whether input video frames are interlaced frames or fields of interlaced video.                      |
| 4     | The codec will automatically determine whether input video frames are progressive frames, interlaced frames, or fields of interlaced video. |



 

This property determines the picture encoding method used for progressive or interlaced video encoding.

If no video type is specified, the codec will use progressive frame encoding for progressive encoding sessions, and field interlaced encoding for interlaced encoding sessions. The type of video encoding session (progressive or interlaced) is set by using the [MFPKEY\_INTERLACEDCODINGENABLED](mfpkey-interlacedcodingenabledproperty.md) property.

> [!Note]  
> The [MFPKEY\_INTERLACEDCODINGENABLED](mfpkey-interlacedcodingenabledproperty.md) property must be set to VARIANT\_TRUE in order to produce interlaced output; otherwise, setting the MPFKEY\_VTYPE property will have no effect.

 

When interlaced video is being encoded, it is possible to specify several picture encoding methods. Typically the most efficient way to encode interlaced video is to use the field interlaced method (2). If the source video contains very little motion, the frame interlaced method (1) or the auto frame/field method (2) might be more suitable.

When encoding mixed content (containing both progressive and interlaced frames), it's best to use the value auto frame/field/progressive method (4).

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

 

 




