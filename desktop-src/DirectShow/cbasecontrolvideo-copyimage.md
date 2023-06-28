---
description: Creates a memory copy of an image.
ms.assetid: 83a980bc-1298-439f-8dfc-49534591977f
title: CBaseControlVideo.CopyImage method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.CopyImage
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseControlVideo.CopyImage method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Creates a memory copy of an image.

## Syntax


```C++
HRESULT CopyImage(
   IMediaSample    *pMediaSample,
   VIDEOINFOHEADER *pVideoInfo,
   LONG            *pBufferSize,
   BYTE            *pVideoImage,
   RECT            *pSourceRect
);
```



## Parameters

<dl> <dt>

*pMediaSample* 
</dt> <dd>

Pointer to the sample containing the video image.

</dd> <dt>

*pVideoInfo* 
</dt> <dd>

Pointer to the format representing the video image.

</dd> <dt>

*pBufferSize* 
</dt> <dd>

Pointer to the size of the output buffer.

</dd> <dt>

*pVideoImage* 
</dt> <dd>

Pointer to the output buffer.

</dd> <dt>

*pSourceRect* 
</dt> <dd>

Pointer to the source video rectangle.

</dd> </dl>

## Return value

If the *pVideoImage* parameter is **NULL**, the *pBufferSize* parameter is filled in with the number of bytes the output buffer requires to store the image. If the buffer passed in is too small or the member function fails to allocate sufficient memory, the member function returns E\_OUTOFMEMORY.

## Remarks

The member function retrieves the image from the sample and copies it into the output buffer. The section of video copied into the output buffer reflects the source rectangle that is set through the [**IBasicVideo**](/windows/desktop/api/Control/nn-control-ibasicvideo) interface (although it does not reflect the destination rectangle).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




