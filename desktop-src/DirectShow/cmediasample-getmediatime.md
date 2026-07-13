---
description: The GetMediaTime method retrieves the media times for this sample. This method implements the IMediaSample::GetMediaTime method.
ms.assetid: f58a2162-5764-48f2-8984-ee4bba1229ab
title: CMediaSample.GetMediaTime method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaSample.GetMediaTime
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CMediaSample.GetMediaTime method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `GetMediaTime` method retrieves the media times for this sample. This method implements the [**IMediaSample::GetMediaTime**](/windows/desktop/api/Strmif/nf-strmif-imediasample-getmediatime) method.

## Syntax


```C++
HRESULT GetMediaTime(
   LONGLONG *pStart,
   LONGLONG *pEnd
);
```



## Parameters

<dl> <dt>

*pStart* 
</dt> <dd>

Pointer to a variable that receives the media start time.

</dd> <dt>

*pEnd* 
</dt> <dd>

Pointer to a variable that receives the media stop time.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                                                  | Description                                         |
|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                         | Success.<br/>                                 |
| <dl> <dt>**VFW\_E\_MEDIA\_TIME\_NOT\_SET**</dt> </dl> | No media times were set for this sample.<br/> |



 

## Remarks

The [**CMediaSample::m\_MediaEnd**](cmediasample-m-mediaend.md) member variable specifies an offset from [**CMediaSample::m\_MediaStart**](cmediasample-m-mediastart.md), but the value received by the *pEnd* parameter is an absolute media time, calculated as **m\_MediaStart** + **m\_MediaEnd**.

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

 

 




