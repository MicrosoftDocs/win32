---
description: The ShouldDrawSampleNow method determines if the video should be drawn without setting a timer advise link with the clock.
ms.assetid: 2cbefc66-0d99-4559-b210-3163cd413dbf
title: CBaseVideoRenderer.ShouldDrawSampleNow method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseVideoRenderer.ShouldDrawSampleNow
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseVideoRenderer.ShouldDrawSampleNow method

The `ShouldDrawSampleNow` method determines if the video should be drawn without setting a timer advise link with the clock.

## Syntax


```C++
virtual HRESULT ShouldDrawSampleNow(
   IMediaSample   *pMediaSample,
   REFERENCE_TIME *ptrStart,
   REFERENCE_TIME *ptrEnd
);
```



## Parameters

<dl> <dt>

*pMediaSample* 
</dt> <dd>

Pointer to the [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface for the sample.

</dd> <dt>

*ptrStart* 
</dt> <dd>

Pointer to the time to begin rendering.

</dd> <dt>

*ptrEnd* 
</dt> <dd>

Pointer to the time to stop rendering.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Returns S\_OK to mean draw at once without waiting, S\_FALSE to mean draw at time *ptrStart*, or an error to mean do not draw the sample; that is, skip it to save time.

## Remarks

This member function overrides [**CBaseRenderer::ShouldDrawSampleNow**](cbaserenderer-shoulddrawsamplenow.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




