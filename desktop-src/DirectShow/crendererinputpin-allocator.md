---
description: The Allocator method retrieves a pointer to the memory allocator.
ms.assetid: ac262502-eadc-482c-bc58-1e942889f0a7
title: CRendererInputPin.Allocator method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRendererInputPin.Allocator
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CRendererInputPin.Allocator method

The `Allocator` method retrieves a pointer to the memory allocator.

## Syntax


```C++
IMemAllocator* Allocator() const;
```



## Parameters

This method has no parameters.

## Return value

Returns a pointer to the allocator's [**IMemAllocator**](/windows/desktop/api/Strmif/nn-strmif-imemallocator) interface, or **NULL**.

## Remarks

This method returns the [**CBaseInputPin::m\_pAllocator**](cbaseinputpin-m-pallocator.md) member variable. The method does not increment the reference count on the interface. This method is strictly an accessor method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CRendererInputPin Class**](crendererinputpin.md)
</dt> </dl>

 

 




