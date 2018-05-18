---
Description: 'The BeginFlush method begins a flush operation. Implements the IPin::BeginFlush method.'
ms.assetid: 'f16c8337-5b7f-47e8-810d-00ffb3b5a1b4'
title: 'CBaseOutputPin.BeginFlush method'
---

# CBaseOutputPin.BeginFlush method

The `BeginFlush` method begins a flush operation. Implements the [**IPin::BeginFlush**](ipin-beginflush.md) method.

## Syntax


```C++
HRESULT BeginFlush();
```



## Parameters

This method has no parameters.

## Return value

Returns E\_UNEXPECTED.

## Remarks

This method should only be called on input pins, so the **CBaseOutputPin** implementation returns E\_UNEXPECTED.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseOutputPin Class**](cbaseoutputpin.md)
</dt> </dl>

 

 




