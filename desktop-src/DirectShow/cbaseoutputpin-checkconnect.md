---
Description: 'The CheckConnect method determines whether a pin connection is suitable.'
ms.assetid: '50ab59ad-8ff7-4d7b-add3-b59203d93307'
title: 'CBaseOutputPin.CheckConnect method'
---

# CBaseOutputPin.CheckConnect method

The `CheckConnect` method determines whether a pin connection is suitable.

## Syntax


```C++
HRESULT CheckConnect(
   IPin *pPin
);
```



## Parameters

<dl> <dt>

*pPin* 
</dt> <dd>

Pointer to the input pin's [**IPin**](ipin.md) interface.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values.



| Return code                                                                                               | Description                                                                 |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                      | Success.<br/>                                                         |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl>             | Input pin does not support [**IMemInputPin**](imeminputpin.md).<br/> |
| <dl> <dt>**VFW\_E\_INVALID\_DIRECTION**</dt> </dl> | Pin directions are not compatible.<br/>                               |



 

## Remarks

This method calls the base-class [**CBasePin::CheckConnect**](cbasepin-checkconnect.md) method, and then queries the input pin for its [**IMemInputPin**](imeminputpin.md) interface.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseOutputPin Class**](cbaseoutputpin.md)
</dt> </dl>

 

 




