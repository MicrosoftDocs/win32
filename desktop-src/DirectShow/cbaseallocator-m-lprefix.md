---
description: Prefix of each buffer, in bytes.
ms.assetid: 471b73bf-f959-41aa-84ba-324a2738dd0e
title: CBaseAllocator::m_lPrefix member (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_lPrefix
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseAllocator::m\_lPrefix member

Prefix of each buffer, in bytes. If the value is non-zero, each buffer pointer returned by the [**CBaseAllocator::GetBuffer**](cbaseallocator-getbuffer.md) method is preceded by a block of bytes of size *m\_lPrefix*. This memory block is called the *prefix*. The [**CBaseAllocator::m\_lSize**](cbaseallocator-m-lsize.md) member variable does not include the prefix value.

## Syntax


```C++
long m_lPrefix;
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

 

 




