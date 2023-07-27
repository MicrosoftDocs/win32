---
description: The ShouldSkipFrame method determines whether the filter should drop a specified sample.
ms.assetid: 49f86f7d-28b1-443e-a238-692da96d60fb
title: CVideoTransformFilter.ShouldSkipFrame method (Vtrans.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CVideoTransformFilter.ShouldSkipFrame
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CVideoTransformFilter.ShouldSkipFrame method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `ShouldSkipFrame` method determines whether the filter should drop a specified sample.

## Syntax


```C++
BOOL ShouldSkipFrame(
   IMediaSample *pIn
);
```



## Parameters

<dl> <dt>

*pIn* 
</dt> <dd>

Pointer to the [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface of the sample.

</dd> </dl>

## Return value

Returns **TRUE** if the filter should drop this sample, or **FALSE** if the filter should process this sample.

## Remarks

This method returns **TRUE** if the following conditions are met:

-   The sample has time stamps.
-   The average decoding time is at least 25% of the frame duration.
-   The renderer is currently at least one frame late, as reported through quality messages.
-   Skipping to the next key frame would not cause the frame to arrive more than one frame early.

For purposes of this calculation, the filter records the following information as it processes data:

-   The average decoding time over the past 20 frames (**m\_itrAvgDecode**)
-   The number of frames since the last key frame (**m\_nFramesSinceKeyFrame**)
-   An estimate of how many frames there are between key frames (**m\_nKeyFramePeriod**)

Once the filter drops a frame, it continues to drop frames until it reaches the next key frame. If this method returns **TRUE**, it also sends an [**EC\_QUALITY\_CHANGE**](ec-quality-change.md) event to the Filter Graph Manager.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Vtrans.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CVideoTransformFilter Class**](cvideotransformfilter.md)
</dt> </dl>

 

 




