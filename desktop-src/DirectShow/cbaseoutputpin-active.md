---
Description: 'The Active method notifies the pin that the filter is now active.'
ms.assetid: '35df4305-0e2c-4ee1-bc63-db5aec864c46'
title: 'CBaseOutputPin.Active method'
---

# CBaseOutputPin.Active method

The `Active` method notifies the pin that the filter is now active.

## Syntax


```C++
HRESULT Active();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible values include those listed in the following table.



| Return code                                                                                          | Description                           |
|------------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                 | Success.<br/>                   |
| <dl> <dt>**VFW\_E\_NO\_ALLOCATOR**</dt> </dl> | No allocator is available.<br/> |



 

## Remarks

This method overrides the [**CBasePin::Active**](cbasepin-active.md) method. It calls the [**IMemAllocator::Commit**](imemallocator-commit.md) method on the allocator, to allocate memory for buffers.

If you override this method, call the base-class method from your overriding method.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseOutputPin Class**](cbaseoutputpin.md)
</dt> </dl>

 

 




