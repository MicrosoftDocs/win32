---
description: The PeekAllocator method returns a pointer to the pin's allocator. The method does not increment the reference count on the interface.
ms.assetid: 67f1b872-4ae2-4fbe-9240-801ef8ae1e5b
title: CTransInPlaceInputPin.PeekAllocator method (Transip.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransInPlaceInputPin.PeekAllocator
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransInPlaceInputPin.PeekAllocator method

The `PeekAllocator` method returns a pointer to the pin's allocator. The method does not increment the reference count on the interface.

## Syntax


```C++
IMemAllocator* PeekAllocator();
```



## Parameters

This method has no parameters.

## Return value

Returns the [**CBaseInputPin::m\_pAllocator**](cbaseinputpin-m-pallocator.md) member variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceInputPin Class**](ctransinplaceinputpin.md)
</dt> </dl>

 

 




