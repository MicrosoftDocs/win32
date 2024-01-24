---
description: The NotifyAllocator method informs the CDrawImage object whether the allocator for the connection is a CImageAllocator object.
ms.assetid: cc1604e7-f755-4a7a-9294-6fd06bb434d4
title: CDrawImage.NotifyAllocator method (Winutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDrawImage.NotifyAllocator
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CDrawImage.NotifyAllocator method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `NotifyAllocator` method informs the **CDrawImage** object whether the allocator for the connection is a [**CImageAllocator**](cimageallocator.md) object.

## Syntax


```C++
void NotifyAllocator(
   BOOL bUsingImageAllocator
);
```



## Parameters

<dl> <dt>

*bUsingImageAllocator* 
</dt> <dd>

Boolean value that indicates what kind of allocator is being used.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The owning filter should call this method after the pins agree to an allocator. If the filter knows the allocator is a **CImageAllocator** object, it should call this method with the value **TRUE**. (Typically, the filter will know this only if it owns the allocator in question.) Otherwise, it should call this method with the value **FALSE**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> <dt>

[**CDrawImage::DrawImage**](cdrawimage-drawimage.md)
</dt> </dl>

 

 




