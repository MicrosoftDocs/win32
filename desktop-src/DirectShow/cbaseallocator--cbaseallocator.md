---
description: Destructor method.
ms.assetid: b1e5653f-d72f-4cde-a8c9-d25763434374
title: CBaseAllocator.~CBaseAllocator destructor (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseAllocator.~CBaseAllocator
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseAllocator.~CBaseAllocator destructor

Destructor method.

## Syntax


```C++
~CBaseAllocator();
```



## Remarks

Always call the [**CBaseAllocator::Decommit**](cbaseallocator-decommit.md) method before destroying the object. The base-class destructor cannot call **Decommit**, because that method calls the pure virtual method [**CBaseAllocator::Free**](cbaseallocator-free.md). Derived classes should override this destructor and call **Decommit**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseAllocator Class**](cbaseallocator.md)
</dt> </dl>

 

 




