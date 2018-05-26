---
Description: The OnDirectRender method collects timing information that controls synchronization and quality control.
ms.assetid: ed617fac-b2c6-4a3a-ac91-77e2d7cce981
title: CBaseVideoRenderer.OnDirectRender method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseVideoRenderer.OnDirectRender method

The **OnDirectRender** method collects timing information that controls synchronization and quality control.

## Syntax


```C++
virtual HRESULT OnDirectRender(
   IMediaSample *pMediaSample
);
```



## Parameters

<dl> <dt>

*pMediaSample* 
</dt> <dd>

Pointer to the [**IMediaSample**](/windows/win32/Strmif/nn-strmif-imediasample?branch=master) interface of the media sample.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Call this method instead of [**OnRenderStart**](cbasevideorenderer-onrenderstart.md) and [**OnRenderEnd**](cbasevideorenderer-onrenderend.md). This method is used by the DirectDraw video renderer.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




