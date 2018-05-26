---
Description: Number of buffers to provide.
ms.assetid: 73f87b14-4346-4909-bd1e-c4981cde403d
title: CBaseAllocatorm\_lCount member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseAllocator::m\_lCount member

Number of buffers to provide. The [**CBaseAllocator::SetProperties**](cbaseallocator-setproperties.md) method sets this value. The buffers are not allocated until the [**CBaseAllocator::Commit**](cbaseallocator-commit.md) method is called. The current number of allocated buffers is specified by the [**CBaseAllocator::m\_lAllocated**](cbaseallocator-m-lallocated.md) member variable.

## Syntax


```C++
long m_lCount;
```



## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseAllocator Class**](cbaseallocator.md)
</dt> </dl>

 

 




