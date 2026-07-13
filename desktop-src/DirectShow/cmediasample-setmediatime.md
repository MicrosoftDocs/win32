---
description: The SetMediaTime method sets the media times for this sample. This method implements the IMediaSample::SetMediaTime method.
ms.assetid: 768812f8-c044-4499-9149-7c334c51e539
title: CMediaSample.SetMediaTime method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaSample.SetMediaTime
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CMediaSample.SetMediaTime method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `SetMediaTime` method sets the media times for this sample. This method implements the [**IMediaSample::SetMediaTime**](/windows/desktop/api/Strmif/nf-strmif-imediasample-setmediatime) method.

## Syntax


```C++
HRESULT SetMediaTime(
   LONGLONG *pStart,
   LONGLONG *pEnd
);
```



## Parameters

<dl> <dt>

*pStart* 
</dt> <dd>

Pointer to the media start time, or **NULL**.

</dd> <dt>

*pEnd* 
</dt> <dd>

Pointer to the media stop time, or **NULL**.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

The media stop time must be greater than the media start time. Use **NULL** to invalidate the media times.

The *pEnd* parameter specifies an absolute media time, but the [**CMediaSample::m\_MediaEnd**](cmediasample-m-mediaend.md) member variable is calculated as an offset from *pStart*. In other words, **m\_MediaEnd** = \**pTimeEnd*  \**pTimeStart*.

For information about media times, see [Time and Clocks in DirectShow](time-and-clocks-in-directshow.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




