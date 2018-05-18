---
Description: 'The get\_VideoWidth method retrieves the width of the native video.'
ms.assetid: 'dfd897f0-f580-44c0-9445-ba61ae267187'
title: 'CBaseControlVideo.get\_VideoWidth method'
---

# CBaseControlVideo.get\_VideoWidth method

The `get_VideoWidth` method retrieves the width of the native video.

## Syntax


```C++
HRESULT get_VideoWidth(
   long *pVideoWidth
);
```



## Parameters

<dl> <dt>

*pVideoWidth* 
</dt> <dd>

Pointer to the width of the native video, in pixels.

</dd> </dl>

## Return value

Returns NOERROR if successful or E\_OUTOFMEMORY if there is not enough memory available.

## Remarks

This member function implements the [**IBasicVideo::get\_VideoWidth**](ibasicvideo-get-videowidth.md) method. It calls the pure virtual [**CBaseControlVideo::GetVideoFormat**](cbasecontrolvideo-getvideoformat.md) to retrieve the [**VIDEOINFOHEADER**](videoinfoheader.md) structure from the derived class.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




