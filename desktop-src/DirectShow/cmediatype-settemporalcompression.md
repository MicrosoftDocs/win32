---
description: The SetTemporalCompression method specifies whether samples are compressed using temporal (interframe) compression.
ms.assetid: cdd181ee-d1e9-48b0-96f6-e76db9f3f933
title: CMediaType.SetTemporalCompression method (Mtype.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaType.SetTemporalCompression
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CMediaType.SetTemporalCompression method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `SetTemporalCompression` method specifies whether samples are compressed using temporal (interframe) compression.

## Syntax


```C++
void SetTemporalCompression(
   BOOL bCompressed
);
```



## Parameters

<dl> <dt>

*bCompressed* 
</dt> <dd>

Boolean value that specifies whether the stream uses temporal compression. If the stream uses temporal compression, set the value to **TRUE**.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method sets the **bTemporalCompression** member.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




