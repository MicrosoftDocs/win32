---
description: The get\_AvgTimePerFrame method retrieves the average time per frame.
ms.assetid: bcfdb241-9ec1-49f4-b2b5-0869c27da953
title: CBaseControlVideo.get_AvgTimePerFrame method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.get_AvgTimePerFrame
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseControlVideo.get\_AvgTimePerFrame method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `get_AvgTimePerFrame` method retrieves the average time per frame.

## Syntax


```C++
HRESULT get_AvgTimePerFrame(
   REFTIME *pAvgTimePerFrame
);
```



## Parameters

<dl> <dt>

*pAvgTimePerFrame* 
</dt> <dd>

Pointer to the average time per frame.

</dd> </dl>

## Return value

Returns NOERROR if successful or E\_OUTOFMEMORY if there is not enough memory available.

## Remarks

This member function implements the [**IBasicVideo::get\_AvgTimePerFrame**](/windows/desktop/api/Control/nf-control-ibasicvideo-get_avgtimeperframe) method. It calls the pure virtual [**CBaseControlVideo::GetVideoFormat**](cbasecontrolvideo-getvideoformat.md) member function to retrieve the [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) structure from the derived class.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




