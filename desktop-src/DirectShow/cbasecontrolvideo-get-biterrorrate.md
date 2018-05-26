---
Description: The get\_BitErrorRate method retrieves an approximate bit error rate for the video.
ms.assetid: 4078611c-6e09-47c8-8e1c-f33bc6ddca79
title: CBaseControlVideo.get\_BitErrorRate method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseControlVideo.get\_BitErrorRate method

The `get_BitErrorRate` method retrieves an approximate bit error rate for the video.

## Syntax


```C++
HRESULT get_BitErrorRate(
   long *pBitErrorRate
);
```



## Parameters

<dl> <dt>

*pBitErrorRate* 
</dt> <dd>

Pointer to the bit error rate (one error for approximately this many bits).

</dd> </dl>

## Return value

Returns NOERROR if successful or E\_OUTOFMEMORY if there is not enough memory available.

## Remarks

This member function implements the [**IBasicVideo::get\_BitErrorRate**](/windows/win32/Control/nf-control-ibasicvideo-get_biterrorrate?branch=master) method. It calls the pure virtual [**CBaseControlVideo::GetVideoFormat**](cbasecontrolvideo-getvideoformat.md) method to retrieve the [**VIDEOINFOHEADER**](/windows/win32/amvideo/ns-amvideo-tagvideoinfoheader?branch=master) structure from the derived class.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




