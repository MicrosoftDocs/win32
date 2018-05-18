---
Description: 'The Pause method pauses the filter. This method implements the IMediaFilter::Pause method.'
ms.assetid: 'cfb7d532-6c00-49a1-a48d-4dadaca39a0f'
title: 'CBaseFilter.Pause method'
---

# CBaseFilter.Pause method

The `Pause` method pauses the filter. This method implements the [**IMediaFilter::Pause**](imediafilter-pause.md) method.

## Syntax


```C++
HRESULT Pause();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK if successful, or an **HRESULT** value indicating the cause of the error.

## Remarks

This method calls the [**CBasePin::Active**](cbasepin-active.md) method on each of the filter's connected pins.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> </dl>

 

 




