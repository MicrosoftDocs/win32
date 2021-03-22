---
description: The GetPin method retrieves a pin.
ms.assetid: 665e1aaf-4491-4241-94c6-6ea356d7a665
title: CBaseRenderer.GetPin method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.GetPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.GetPin method

The `GetPin` method retrieves a pin.

## Syntax


```C++
virtual CBasePin* GetPin(
   int n
);
```



## Parameters

<dl> <dt>

*n* 
</dt> <dd>

Number of the specified pin. Must be zero.

</dd> </dl>

## Return value

Returns the [**CBaseRenderer::m\_pInputPin**](cbaserenderer-m-pinputpin.md) pointer.

## Remarks

This method implements the [**CBaseFilter::GetPin**](cbasefilter-getpin.md) method, which is pure virtual in the **CBaseFilter** class. The filter supports exactly one pin (the input pin). The first time this method is called, it creates the pin as a new [**CRendererInputPin**](crendererinputpin.md) object.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




