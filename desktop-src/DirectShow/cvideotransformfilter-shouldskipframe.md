---
description: The ShouldSkipFrame method determines whether the filter should drop a specified sample.
ms.assetid: 49f86f7d-28b1-443e-a238-692da96d60fb
title: CVideoTransformFilter.ShouldSkipFrame method (Vtrans.h)
ms.topic: reference
ms.date: 05/31/2018
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
---

# CVideoTransformFilter.ShouldSkipFrame method

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

 

 




