---
description: The PrepareRender method is called before the filter renders a sample.
ms.assetid: 0b137da9-eac0-469f-b457-719a36569c82
title: CBaseRenderer.PrepareRender method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.PrepareRender
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.PrepareRender method

The `PrepareRender` method is called before the filter renders a sample.

## Syntax


```C++
virtual void PrepareRender();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The filter calls this method before it calls the [**CBaseRenderer::OnReceiveFirstSample**](cbaserenderer-onreceivefirstsample.md) method or the [**CBaseRenderer::Render**](cbaserenderer-render.md) method. `PrepareRender` does not do anything in the base class. The derived class can override it to perform any actions required before rendering. For example, a video renderer can override this method to realize its palette.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




