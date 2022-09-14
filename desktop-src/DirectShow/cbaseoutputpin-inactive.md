---
description: CBaseOutputPin.Inactive method - The Inactive method notifies the pin that the filter is no longer active.
ms.assetid: 14a020de-2102-4d49-8a34-d59abe6698d1
title: CBaseOutputPin.Inactive method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseOutputPin.Inactive
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseOutputPin.Inactive method

The `Inactive` method notifies the pin that the filter is no longer active.

## Syntax


```C++
HRESULT Inactive();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible values include those listed in the following table.



| Return code                                                                                          | Description                                  |
|------------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                 | Success.<br/>                          |
| <dl> <dt>**VFW\_E\_NO\_ALLOCATOR**</dt> </dl> | No memory allocator is available.<br/> |



 

## Remarks

This method overrides the [**CBasePin::Inactive**](cbasepin-inactive.md) method. It calls the [**IMemAllocator::Decommit**](/windows/desktop/api/Strmif/nf-strmif-imemallocator-decommit) method to decommit the memory allocator.

If you override this method, call the base-class method from your overriding method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseOutputPin Class**](cbaseoutputpin.md)
</dt> </dl>

 

 




