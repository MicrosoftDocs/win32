---
Description: 'The GetPinCount method retrieves the number of pins on the filter.'
ms.assetid: '29039ada-fccd-4890-b36b-3dd5c0bbdc3e'
title: 'CTransformFilter.GetPinCount method'
---

# CTransformFilter.GetPinCount method

The `GetPinCount` method retrieves the number of pins on the filter.

## Syntax


```C++
virtual int GetPinCount();
```



## Parameters

This method has no parameters.

## Return value

Returns 2.

## Remarks

This method overrides the [**CBaseFilter::GetPinCount**](cbasefilter-getpincount.md) method. The **CTransformFilter** class supports exactly one input pin and one output pin.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




