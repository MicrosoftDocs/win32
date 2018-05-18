---
Description: 'The Inactive method notifies the pin that the filter has stopped.'
ms.assetid: 'f7efb67b-cc3f-47c4-a8ba-b2365aef0d96'
title: 'CDynamicOutputPin.Inactive method'
---

# CDynamicOutputPin.Inactive method

The `Inactive` method notifies the pin that the filter has stopped.

## Syntax


```C++
HRESULT Inactive();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK if successful, or an **HRESULT** value indicating the cause of the failure.

## Remarks

This method overrides the [**CBaseOutputPin::Inactive**](cbaseoutputpin-inactive.md) method. It sets the [**CDynamicOutputPin::m\_hStopEvent**](cdynamicoutputpin-m-hstopevent.md) event.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 




