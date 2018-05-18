---
Description: 'The EndFlush method ends a flush operation. This method implements the IPin::EndFlush method.'
ms.assetid: 'c5c76cf8-1ca1-4fef-8776-7f4dcca32939'
title: 'CBaseOutputPin.EndFlush method'
---

# CBaseOutputPin.EndFlush method

The `EndFlush` method ends a flush operation. This method implements the [**IPin::EndFlush**](ipin-endflush.md) method.

## Syntax


```C++
HRESULT EndFlush();
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

 

 




