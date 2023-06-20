---
description: Returns the number of video frames that were encoded.
ms.assetid: ade9fe69-b3dd-44aa-856b-75d4a7e4c680
title: AVEncStatVideoCodedFrames property (Codecapi.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AVEncStatVideoCodedFrames property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Returns the number of video frames that were encoded.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncStatVideoCodedFrames**

## Remarks

This property is available after the encoding is completed.

The value of this property is equal to the [**AVEncStatVideoTotalFrames**](avencstatvideototalframes-property.md) property minus the number of dropped frames. The encoder might drop frames to stay within the specified bit rate constraints. It might also drop frames at the end of the stream (see [**AVEncCommonStreamEndHandling**](avenccommonstreamendhandling-property.md) property).

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

 

 




