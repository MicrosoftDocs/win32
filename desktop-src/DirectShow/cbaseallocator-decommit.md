---
description: The Decommit method decommits the allocator. This method implements the IMemAllocator::Decommit method.
ms.assetid: 0c8d44e0-17ea-4f7f-be44-f9ae2e34fbef
title: CBaseAllocator.Decommit method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseAllocator.Decommit
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseAllocator.Decommit method

The `Decommit` method decommits the allocator. This method implements the [**IMemAllocator::Decommit**](/windows/desktop/api/Strmif/nf-strmif-imemallocator-decommit) method.

## Syntax


```C++
HRESULT Decommit();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

After this method is called, calls to the [**CBaseAllocator::GetBuffer**](cbaseallocator-getbuffer.md) method will fail. As samples are released, they get returned to the free list. When the last sample is returned, the allocator calls the [**CBaseAllocator::Free**](cbaseallocator-free.md) method, which releases the allocated memory. (In the base class, **Free** is a pure virtual method.)

In addition, this method releases any threads that are blocked on **GetBuffer** calls. The calls to **GetBuffer** fail.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseAllocator Class**](cbaseallocator.md)
</dt> </dl>

 

 




