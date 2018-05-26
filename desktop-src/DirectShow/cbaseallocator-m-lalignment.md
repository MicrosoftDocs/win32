---
Description: Alignment of each buffer. The address of each buffer must be an even multiple of this value. The prefix must be calculated into the alignment; see CBaseAllocatorm\_lPrefix.
ms.assetid: 2b71b60a-feeb-4f09-bd56-e126eac8e150
title: CBaseAllocatorm\_lAlignment member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseAllocator::m\_lAlignment member

Alignment of each buffer. The address of each buffer must be an even multiple of this value. The prefix must be calculated into the alignment; see [**CBaseAllocator::m\_lPrefix**](cbaseallocator-m-lprefix.md).

## Syntax


```C++
long m_lAlignment;
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

 

 




