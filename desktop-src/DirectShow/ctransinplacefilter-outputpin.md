---
description: The OutputPin method retrieves a pointer to the filter's output pin.
ms.assetid: 8c8c125e-553d-43c5-bc63-a0c7d5b01260
title: CTransInPlaceFilter.OutputPin method (Transip.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransInPlaceFilter.OutputPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransInPlaceFilter.OutputPin method

The `OutputPin` method retrieves a pointer to the filter's output pin.

## Syntax


```C++
CTransInPlaceOutputPin* OutputPin();
```



## Parameters

This method has no parameters.

## Return value

Returns the [**CTransformFilter::m\_pOutput**](ctransformfilter-m-poutput.md) member variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceFilter Class**](ctransinplacefilter.md)
</dt> </dl>

 

 




