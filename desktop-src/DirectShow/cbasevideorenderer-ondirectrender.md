---
description: The OnDirectRender method collects timing information that controls synchronization and quality control.
ms.assetid: ed617fac-b2c6-4a3a-ac91-77e2d7cce981
title: CBaseVideoRenderer.OnDirectRender method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseVideoRenderer.OnDirectRender
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
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

Pointer to the [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface of the media sample.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Call this method instead of [**OnRenderStart**](cbasevideorenderer-onrenderstart.md) and [**OnRenderEnd**](cbasevideorenderer-onrenderend.md). This method is used by the DirectDraw video renderer.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




