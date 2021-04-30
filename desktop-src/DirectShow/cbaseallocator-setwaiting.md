---
description: The SetWaiting method increments the count of waiting threads.
ms.assetid: 4aec6177-fb32-44be-a58e-41a4f4aaf4f2
title: CBaseAllocator.SetWaiting method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseAllocator.SetWaiting
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseAllocator.SetWaiting method

The `SetWaiting` method increments the count of waiting threads.

## Syntax


```C++
void SetWaiting();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method increments the [**CBaseAllocator::m\_lWaiting**](cbaseallocator-m-lwaiting.md) member variable. If a thread is blocked in the [**CBaseAllocator::GetBuffer**](cbaseallocator-getbuffer.md) method, the allocator calls `SetWaiting` and then waits for the [**CBaseAllocator::m\_hSem**](cbaseallocator-m-hsem.md) semaphore to be signaled. The [**CBaseAllocator::ReleaseBuffer**](cbaseallocator-releasebuffer.md) method signals the semaphore and sets *m\_lWaiting* back to zero.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseAllocator Class**](cbaseallocator.md)
</dt> </dl>

 

 




