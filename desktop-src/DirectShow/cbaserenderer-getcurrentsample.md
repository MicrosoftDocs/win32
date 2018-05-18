---
Description: 'The GetCurrentSample method retrieves the current sample.'
ms.assetid: 'cfdc66e3-7d32-47b7-87f6-99dd9513c93b'
title: 'CBaseRenderer.GetCurrentSample method'
---

# CBaseRenderer.GetCurrentSample method

The `GetCurrentSample` method retrieves the current sample.

## Syntax


```C++
virtual IMediaSample* GetCurrentSample();
```



## Parameters

This method has no parameters.

## Return value

Returns a pointer to the sample's [**IMediaSample**](imediasample.md) interface, or **NULL** if no sample is available.

## Remarks

Unless the method returns **NULL**, the method calls **AddRef** on the [**IMediaSample**](imediasample.md) pointer before returning it. The caller must release the pointer. (By implication, you must assign the return value to a variable, so that you can release it later.)

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




