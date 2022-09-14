---
description: The get\_VideoHeight method retrieves the height of the native video.
ms.assetid: f33ba789-f9c6-47f1-879b-241bfdc72010
title: CBaseControlVideo.get_VideoHeight method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseControlVideo.get_VideoHeight
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseControlVideo.get\_VideoHeight method

The `get_VideoHeight` method retrieves the height of the native video.

## Syntax


```C++
HRESULT get_VideoHeight(
   long *pVideoHeight
);
```



## Parameters

<dl> <dt>

*pVideoHeight* 
</dt> <dd>

Pointer to the height of the native video, in pixels.

</dd> </dl>

## Return value

Returns NOERROR if successful or E\_OUTOFMEMORY if there is not enough memory available.

## Remarks

This member function implements the [**IBasicVideo::get\_VideoHeight**](/windows/desktop/api/Control/nf-control-ibasicvideo-get_videoheight) method. It calls the pure virtual [**CBaseControlVideo::GetVideoFormat**](cbasecontrolvideo-getvideoformat.md) to retrieve the [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) structure from the derived class.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




