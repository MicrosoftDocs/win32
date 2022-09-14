---
description: Pointer to a critical section object.
ms.assetid: dc791bc4-857c-4a79-9aa8-3c5974c23483
title: CSourceSeeking::m_pLock member (Ctlutil.h)
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

# CSourceSeeking::m\_pLock member

Pointer to a critical section object. The `CSourceSeeking` class uses this critical section to synchronize access to the start and stop times, duration, and rate variables. This variable is initialized in the constructor method; see [**CSourceSeeking::CSourceSeeking**](csourceseeking-csourceseeking.md).

## Syntax


```C++
CCritSec *m_pLock;
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceSeeking Class**](csourceseeking.md)
</dt> </dl>

 

 




