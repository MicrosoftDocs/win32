---
Description: The GetVideoFormat method retrieves a video sample that represents the current video format.
ms.assetid: f7457c5b-037c-4a63-963e-0fc6086609a4
title: CBaseControlVideo.GetVideoFormat method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseControlVideo.GetVideoFormat method

The `GetVideoFormat` method retrieves a video sample that represents the current video format.

## Syntax


```C++
virtual VIDEOINFOHEADER* GetVideoFormat() = 0;
```



## Parameters

This method has no parameters.

## Return value

Returns a pointer to a [**VIDEOINFOHEADER**](/windows/win32/amvideo/ns-amvideo-tagvideoinfoheader?branch=master) structure that contains the current video format.

## Remarks

To return and check certain information through [**IBasicVideo**](/windows/win32/Control/nn-control-ibasicvideo?branch=master), the object must know the current video format. It gets this information by calling this pure virtual method that derived classes must override. This member function is called by the following [**CBaseControlVideo**](cbasecontrolvideo.md) member functions.

-   [**CBaseControlVideo::OnVideoSizeChange**](cbasecontrolvideo-onvideosizechange.md)
-   [**CBaseControlVideo::get\_AvgTimePerFrame**](cbasecontrolvideo-get-avgtimeperframe.md)
-   [**CBaseControlVideo::get\_BitRate**](cbasecontrolvideo-get-bitrate.md)
-   [**CBaseControlVideo::get\_BitErrorRate**](cbasecontrolvideo-get-biterrorrate.md)
-   [**CBaseControlVideo::get\_VideoWidth**](cbasecontrolvideo-get-videowidth.md)
-   [**CBaseControlVideo::get\_VideoHeight**](cbasecontrolvideo-get-videoheight.md)
-   [**CBaseControlVideo::GetVideoPaletteEntries**](cbasecontrolvideo-getvideopaletteentries.md)
-   [**CBaseControlVideo::GetVideoSize**](cbasecontrolvideo-getvideosize.md)

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseControlVideo Class**](cbasecontrolvideo.md)
</dt> </dl>

 

 




