---
description: The SetAllocator method specifies an allocator for the connection.
ms.assetid: 6b8e80f9-3b0d-498f-b1b0-bae491c25e81
title: CTransInPlaceOutputPin.SetAllocator method (Transip.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransInPlaceOutputPin.SetAllocator
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransInPlaceOutputPin.SetAllocator method

The `SetAllocator` method specifies an allocator for the connection.

## Syntax


```C++
void SetAllocator(
   IMemAllocator *pAllocator
);
```



## Parameters

<dl> <dt>

*pAllocator* 
</dt> <dd>

Pointer to the allocator's [**IMemAllocator**](/windows/desktop/api/Strmif/nn-strmif-imemallocator) interface.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The output pin for this filter never provides an allocator. This method specifies the allocator for the output pin. It sets the value of the [**CBaseOutputPin::m\_pAllocator**](cbaseoutputpin-m-pallocator.md) member variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceOutputPin Class**](ctransinplaceoutputpin.md)
</dt> </dl>

 

 




