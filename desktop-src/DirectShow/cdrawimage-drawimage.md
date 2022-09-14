---
description: The DrawImage method draws a video frame on the video window.
ms.assetid: 22e7f59c-90f7-4e0c-8993-eea1eaf58fba
title: CDrawImage.DrawImage method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDrawImage.DrawImage
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDrawImage.DrawImage method

The `DrawImage` method draws a video frame on the video window.

## Syntax


```C++
BOOL DrawImage(
   IMediaSample *pMediaSample
);
```



## Parameters

<dl> <dt>

*pMediaSample* 
</dt> <dd>

Pointer to the [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface of the sample that contains the image.

</dd> </dl>

## Return value

Returns **TRUE** if successful or **FALSE** otherwise.

## Remarks

This method delegates to [**CDrawImage::FastRender**](cdrawimage-fastrender.md) or [**CDrawImage::SlowRender**](cdrawimage-slowrender.md), depending on whether the filter owns the allocator that provided the sample. If the filter does own the allocator, the sample is guaranteed to be a [**CImageSample**](cimagesample.md) object. In that case, the sample uses shared memory allocated by GDI, and the image can be drawn using either **BitBlt** or **StretchBlt**. Otherwise, the images must be drawn using the slower **SetDIBitsToDevice** or **StretchDIBits** functions.

In debug builds, this method calls **DisplaySampleTimes** to draw the sample's time stamps over the video image.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> <dt>

[**CDrawImage::UsingImageAllocator**](cdrawimage-usingimageallocator.md)
</dt> </dl>

 

 




