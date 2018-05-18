---
Description: 'The BreakConnect method releases the pin from a connection.'
ms.assetid: '73b228a9-0a59-4647-b400-c33fa06c7e34'
title: 'CBaseInputPin.BreakConnect method'
---

# CBaseInputPin.BreakConnect method

The `BreakConnect` method releases the pin from a connection.

## Syntax


```C++
HRESULT BreakConnect();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK if successful, or an **HRESULT** value indicating the cause of the error.

## Remarks

This method overrides the [**CBasePin::BreakConnect**](cbasepin-breakconnect.md) method. It decommits the allocator and releases the [**IMemAllocator**](imemallocator.md) interface.

If you override this method, call the base-class method from your overriding method. Otherwise, you might cause memory leaks.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseInputPin Class**](cbaseinputpin.md)
</dt> </dl>

 

 




