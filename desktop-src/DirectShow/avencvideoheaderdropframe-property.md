---
description: Specifies the value of drop-frame flag in the group of pictures (GOP) header.
ms.assetid: 37f8f5f6-ddcb-44ab-a727-632b78e6f599
title: AVEncVideoHeaderDropFrame property (Codecapi.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AVEncVideoHeaderDropFrame property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Specifies the value of drop-frame flag in the group of pictures (GOP) header.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncVideoHeaderDropFrame**

## Property value

The value of this property can be 0 or 1.

## Remarks

Drop-frame mode is used in NTSC video to correct the discrepancy between the video, which is 29.97 frames per second, and the time code display, which is 30 frames per second. In drop-frame mode, frame numbers 00 and 01 are skipped at the start of each minute, except for minutes that are even multiples of ten (00, 10, 20, and so forth). Only the frame numbers in the time code are dropped; no actual frames are dropped.

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

 

 




