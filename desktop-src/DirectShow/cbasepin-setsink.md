---
Description: 'The SetSink method sets an external quality manager. This method implements the IQualityControl::SetSink method.'
ms.assetid: '714e6839-954e-4231-824d-72a45f270f59'
title: 'CBasePin.SetSink method'
---

# CBasePin.SetSink method

The `SetSink` method sets an external quality manager. This method implements the [**IQualityControl::SetSink**](iqualitycontrol-setsink.md) method.

## Syntax


```C++
HRESULT SetSink(
   IQualityControl *piqc
);
```



## Parameters

<dl> <dt>

*piqc* 
</dt> <dd>

Pointer to the [**IQualityControl**](iqualitycontrol.md) interface of the quality manager.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

Call this method to redirect quality-control messages to an external quality manager. For more information, see [Quality-Control Management](quality-control-management.md).

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




