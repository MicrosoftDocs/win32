---
description: The CreateDIB method creates a GDI device-independent bitmap (DIB). The DIB is allocated in a shared mempory block, which eliminates a copy operation when the owning filter blits the image.
ms.assetid: 8a9ab1cf-4104-48e9-ba6c-28d0f1a1d226
title: CImageAllocator.CreateDIB method (Winutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImageAllocator.CreateDIB
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CImageAllocator.CreateDIB method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `CreateDIB` method creates a GDI device-independent bitmap (DIB). The DIB is allocated in a shared mempory block, which eliminates a copy operation when the owning filter blits the image.

## Syntax


```C++
HRESULT CreateDIB(
        LONG    InSize,
  [ref] DIBDATA &DibData
);
```



## Parameters

<dl> <dt>

*InSize* 
</dt> <dd>

Size of the bitmap.

</dd> <dt>

*DibData* \[ref\]
</dt> <dd>

Reference to a [**DIBDATA**](dibdata.md) structure. The method fills in this structure with information about the DIB.

</dd> </dl>

## Return value

Returns S\_OK if successful, or an error code otherwise.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImageAllocator Class**](cimageallocator.md)
</dt> <dt>

[**CImageAllocator::Alloc**](cimageallocator-alloc.md)
</dt> </dl>

 

 




