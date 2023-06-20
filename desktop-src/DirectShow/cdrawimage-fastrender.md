---
description: The FastRender method draws the video image using the BitBlt or StretchBlt functions.
ms.assetid: 8bbc96ce-393f-46fb-bf90-61d3ce0ef0d6
title: CDrawImage.FastRender method (Winutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDrawImage.FastRender
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CDrawImage.FastRender method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `FastRender` method draws the video image using the **BitBlt** or **StretchBlt** functions.

## Syntax


```C++
void FastRender(
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

This method does not return a value.

## Remarks

The [**CDrawImage::DrawImage**](cdrawimage-drawimage.md) method calls this method, but only if the allocator for the connection is a [**CImageAllocator**](cimageallocator.md) object. In that case, the media sample is guaranteed to be a [**CImageSample**](cimagesample.md) object. The **CImageSample** object uses the **CreateDIBSection** function to allocate shared memory for the bitmap, which makes it possible to draw the image using either **BitBlt** or **StretchBlt**.

This method calls **BitBlt** if the source and targer rectangles exactly match, or **StretchBlt** otherwise.

If the filter does not own the allocator, the **DrawImage** method uses [**CDrawImage::SlowRender**](cdrawimage-slowrender.md) to draw the image.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> </dl>

 

 




