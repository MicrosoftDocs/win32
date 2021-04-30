---
description: Pointer to a critical section object that protects the filter state.
ms.assetid: e733360d-ed95-493f-a85b-53d584681f60
title: CBasePin::m_pLock member (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_pLock
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBasePin::m\_pLock member

Pointer to a critical section object that protects the filter state.

## Syntax


```C++
CCritSec *m_pLock;
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> <dt>

[Threads and Critical Sections](threads-and-critical-sections.md)
</dt> </dl>

 

 




