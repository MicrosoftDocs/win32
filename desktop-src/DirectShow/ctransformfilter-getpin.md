---
description: The GetPin method retrieves a pin.
ms.assetid: 5d278ef0-e5ce-439e-93b1-fec988c55854
title: CTransformFilter.GetPin method (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformFilter.GetPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformFilter.GetPin method

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

Number of the specified pin, indexed from zero. On this filter, pin 0 is the input pin, and pin 1 is the output pin.

</dd> </dl>

## Return value

Returns a pointer to the [**CBasePin**](cbasepin.md) object that implements the pin, or **NULL** if the method fails.

## Remarks

This method implements the pure virtual [**CBaseFilter::GetPin**](cbasefilter-getpin.md) method. The first time the method is called, it creates both pins.

This method does not increment the reference count on the returned pin, so the returned pin does not have an outstanding reference count. If the caller needs to keep a reference on the pin, it should call the **IUnknown::AddRef** method on the pin.

If the filter uses the default [**CTransformInputPin**](ctransforminputpin.md) and [**CTransformOutputPin**](ctransformoutputpin.md) pins, you probably do not need to override this method. If the filter uses pins that extend those classes, however, you must override this method to create pins of that type.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




