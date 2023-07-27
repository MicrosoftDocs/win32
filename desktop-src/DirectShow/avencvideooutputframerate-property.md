---
description: Specifies the frame rate on the encoder's output stream, in frames per second.
ms.assetid: 72e16c7d-977e-4269-9576-afc789e31826
title: AVEncVideoOutputFrameRate property (Codecapi.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AVEncVideoOutputFrameRate property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Specifies the frame rate on the encoder's output stream, in frames per second.

This property is read/write.

## Data type

**UINT64** (**VT\_UI8**)

## Property GUID

**CODECAPI\_AVEncVideoOutputFrameRate**

## Property value

The value of this property is a ratio that defines the frame rate. The upper 32 bits contain the numerator, and the lower 32 bits contain the denominator. The following table shows common frame rates, in frames per second.



| Frame rate | Ratio      |
|------------|------------|
| 23.97      | 24000/1001 |
| 24         | 24/1       |
| 25         | 25/1       |
| 29.97      | 30000/1001 |
| 30         | 30/1       |
| 50         | 50/1       |
| 59.94      | 60000/1001 |
| 60         | 60/1       |



 

## Remarks

Applications can set this property to specify the output frame rate. Encoders can also return this property as a capability. Depending on the encoder, the value might be restricted to the input frame rate. If not, the encoder is able to convert the frame rate internally. See [**AVEncVideoOutputFrameRateConversion Property**](avencvideooutputframerateconversion-property.md).

This property is also used with [H.264 UVC 1.5 camera encoders](/windows/desktop/medfound/camera-encoder-h264-uvc-1-5).

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

 

