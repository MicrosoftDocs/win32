---
description: The OnRenderEnd method is called after a sample is rendered.
ms.assetid: c9b3a3b2-a5c0-4a08-9e55-53c27a4d1032
title: CBaseRenderer.OnRenderEnd method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.OnRenderEnd
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.OnRenderEnd method

The `OnRenderEnd` method is called after a sample is rendered.

## Syntax


```C++
virtual void OnRenderEnd(
   IMediaSample *pMediaSample
);
```



## Parameters

<dl> <dt>

*pMediaSample* 
</dt> <dd>

Pointer to the sample's [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The [**CBaseRenderer::Render**](cbaserenderer-render.md) method calls this method. It does nothing in the base class, but the derived class can override it; for example, to collect quality-control data.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




