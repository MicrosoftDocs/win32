---
Description: 'The CompleteConnect method completes a connection to an output pin. This method overrides the CBasePin::CompleteConnect method.'
ms.assetid: '32d95815-e018-4724-8cf3-8cd093ede517'
title: 'CRendererInputPin.CompleteConnect method'
---

# CRendererInputPin.CompleteConnect method

The `CompleteConnect` method completes a connection to an output pin. This method overrides the [**CBasePin::CompleteConnect**](cbasepin-completeconnect.md) method.

## Syntax


```C++
HRESULT CompleteConnect(
   IPin *pReceivePin
);
```



## Parameters

<dl> <dt>

*pReceivePin* 
</dt> <dd>

Pointer to the output pin's [**IPin**](ipin.md) interface

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CRendererInputPin Class**](crendererinputpin.md)
</dt> </dl>

 

 




