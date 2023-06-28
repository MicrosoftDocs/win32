---
description: Specifies the width and height of the encoded video, if the video is cropped.
ms.assetid: d6217250-63ff-4dff-a357-ff4aaa764695
title: AVEncVideoEncodeDimension property (Codecapi.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AVEncVideoEncodeDimension property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Specifies the width and height of the encoded video, if the video is cropped.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncVideoEncodeDimension**

## Property value

The upper 16 bits of the value contain the width in pixels, and the lower 16 bits contain the height in pixels.

## Remarks

Applications can set this property to crop the input video. The specified size must be less than the size of the input video frames. Use the [**AVEncVideoEncodeOffsetOrigin**](avencvideoencodeoffsetorigin-property.md) property to specify the left and top corners of the clipping rectangle.

Encoders can return this property as a capability.

This property is also used with [H.264 UVC 1.5 camera encoders](/windows/desktop/medfound/camera-encoder-h264-uvc-1-5).

For UVC 1.5 camera encoders, [AVEncVideoEncodeOffsetOrigin](avencvideoencodeoffsetorigin-property.md) is not supported.

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

 

