---
description: The Free method releases all of the buffer memory. This method is called when the owning filter decommits the allocator, after the last media sample is released.
ms.assetid: dd1e6c4d-762a-4caf-902b-015c6c9fdb4d
title: CBaseAllocator.Free method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseAllocator.Free
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseAllocator.Free method

The `Free` method releases all of the buffer memory. This method is called when the owning filter decommits the allocator, after the last media sample is released.

## Syntax


```C++
virtual void Free() = 0;
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

After the [**Decommit**](cbaseallocator-decommit.md) method is called, the allocator calls this method when it releases the last media sample. The derived class must implement this method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseAllocator Class**](cbaseallocator.md)
</dt> </dl>

 

 




