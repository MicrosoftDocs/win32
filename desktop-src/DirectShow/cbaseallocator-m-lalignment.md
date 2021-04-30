---
description: Alignment of each buffer. The address of each buffer must be an even multiple of this value. The prefix must be calculated into the alignment; see CBaseAllocator::m\_lPrefix.
ms.assetid: 2b71b60a-feeb-4f09-bd56-e126eac8e150
title: CBaseAllocator::m_lAlignment member (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_lAlignment
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseAllocator::m\_lAlignment member

Alignment of each buffer. The address of each buffer must be an even multiple of this value. The prefix must be calculated into the alignment; see [**CBaseAllocator::m\_lPrefix**](cbaseallocator-m-lprefix.md).

## Syntax


```C++
long m_lAlignment;
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

 

 




