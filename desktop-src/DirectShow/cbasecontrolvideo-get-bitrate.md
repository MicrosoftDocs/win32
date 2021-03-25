---
description: The get\_BitRate method retrieves an approximate bit rate for the video.
ms.assetid: e12e4677-a038-479f-8b64-937ad521c4be
title: CBaseControlVideo.get_BitRate method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.get_BitRate
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlVideo.get\_BitRate method

The `get_BitRate` method retrieves an approximate bit rate for the video.

## Syntax


```C++
HRESULT get_BitRate(
   long *pBitRate
);
```



## Parameters

<dl> <dt>

*pBitRate* 
</dt> <dd>

Pointer to the bit rate, in bits per second.

</dd> </dl>

## Return value

Returns NOERROR if successful or E\_OUTOFMEMORY if not enough memory is available.

## Remarks

This member function implements the [**IBasicVideo::get\_BitRate**](/windows/desktop/api/Control/nf-control-ibasicvideo-get_bitrate) method. It calls the pure virtual [**CBaseControlVideo::GetVideoFormat**](cbasecontrolvideo-getvideoformat.md) to retrieve the [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) structure from the derived class.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




