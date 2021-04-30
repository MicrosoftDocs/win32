---
description: Specifies the left and top corners of the clipping rectangle, if the video is cropped.
ms.assetid: 8ce8b3b8-dd91-41e1-a4ba-b0c2d9d0edd2
title: AVEncVideoEncodeOffsetOrigin property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncVideoEncodeOffsetOrigin property

Specifies the left and top corners of the clipping rectangle, if the video is cropped.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncVideoEncodeOffsetOrigin**

## Property value

The upper 16 bits of the value contain the offset from the left edge of the input frame, in pixels. The lower 16 bits contain the offset from the top edge of the input frame, in pixels.

## Remarks

Applications can set this property to crop the input video. Use the [**AVEncVideoEncodeDimension**](avencvideoencodedimension-property.md) property to specify the width and height of the clipping rectangle.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Codec API Properties](codec-api-properties.md)
</dt> <dt>

[**ICodecAPI Interface**](/windows/desktop/api/Strmif/nn-strmif-icodecapi)
</dt> </dl>

 

 




