---
description: The InputPin method retrieves a pointer to the filter's input pin.
ms.assetid: 533a962e-225d-4f10-a9c3-1464bea512ba
title: CTransInPlaceFilter.InputPin method (Transip.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransInPlaceFilter.InputPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransInPlaceFilter.InputPin method

The `InputPin` method retrieves a pointer to the filter's input pin.

## Syntax


```C++
CTransInPlaceInputPin* InputPin();
```



## Parameters

This method has no parameters.

## Return value

Returns the [**CTransformFilter::m\_pInput**](ctransformfilter-m-pinput.md) member variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceFilter Class**](ctransinplacefilter.md)
</dt> </dl>

 

 




