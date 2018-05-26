---
Description: The get\_BitRate method retrieves an approximate bit rate for the video.
ms.assetid: e12e4677-a038-479f-8b64-937ad521c4be
title: CBaseControlVideo.get\_BitRate method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

This member function implements the [**IBasicVideo::get\_BitRate**](/windows/win32/Control/nf-control-ibasicvideo-get_bitrate?branch=master) method. It calls the pure virtual [**CBaseControlVideo::GetVideoFormat**](cbasecontrolvideo-getvideoformat.md) to retrieve the [**VIDEOINFOHEADER**](/windows/win32/amvideo/ns-amvideo-tagvideoinfoheader?branch=master) structure from the derived class.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




