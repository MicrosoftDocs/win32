---
description: The Free method is called during a decommit operation.
ms.assetid: 71a84730-ca71-4418-bf76-52fd42fc7a5a
title: CMemAllocator.Free method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMemAllocator.Free
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMemAllocator.Free method

The `Free` method is called during a decommit operation. This method implements the pure virtual [**CBaseAllocator::Free**](cbaseallocator-free.md) method, but does nothing. The buffer memory is not actually released until the **CMemAllocator** object is destroyed. The destructor method calls [**CMemAllocator::ReallyFree**](cmemallocator-reallyfree.md) to release the memory.

## Syntax


```C++
void Free();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMemAllocator Class**](cmemallocator.md)
</dt> </dl>

 

 




