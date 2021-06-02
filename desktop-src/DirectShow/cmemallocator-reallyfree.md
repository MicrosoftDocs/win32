---
description: The ReallyFree method releases the memory for the buffers.
ms.assetid: c5c5d09f-b4f2-4a06-9309-3b2a8b8f8f1f
title: CMemAllocator.ReallyFree method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMemAllocator.ReallyFree
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMemAllocator.ReallyFree method

The `ReallyFree` method releases the memory for the buffers.

## Syntax


```C++
void ReallyFree();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The [**CMemAllocator**](cmemallocator.md) class holds memory until the object is deleted.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMemAllocator Class**](cmemallocator.md)
</dt> </dl>

 

 




