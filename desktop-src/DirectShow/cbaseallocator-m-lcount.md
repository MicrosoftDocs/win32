---
description: Number of buffers to provide.
ms.assetid: 73f87b14-4346-4909-bd1e-c4981cde403d
title: CBaseAllocator::m_lCount member (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_lCount
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseAllocator::m\_lCount member

Number of buffers to provide. The [**CBaseAllocator::SetProperties**](cbaseallocator-setproperties.md) method sets this value. The buffers are not allocated until the [**CBaseAllocator::Commit**](cbaseallocator-commit.md) method is called. The current number of allocated buffers is specified by the [**CBaseAllocator::m\_lAllocated**](cbaseallocator-m-lallocated.md) member variable.

## Syntax


```C++
long m_lCount;
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseAllocator Class**](cbaseallocator.md)
</dt> </dl>

 

 




