---
description: Pointer to a critical section that is used to serialize state changes.
ms.assetid: 4fecd9a6-54df-49d7-bf2f-5dcaef919ad7
title: CBaseFilter::m_pLock member (Amfilter.h)
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

# CBaseFilter::m\_pLock member

Pointer to a critical section that is used to serialize state changes.

## Syntax


```C++
CCritSec *m_pLock;
```



## Remarks

This variable is initialized in the class constructor; see [**CBaseFilter::CBaseFilter**](cbasefilter-cbasefilter.md).

Hold this critical section during state transitions, or when a method accesses the state over several operations. The base class holds the critical section in the following methods:

-   [**CBaseFilter::FindPin**](cbasefilter-findpin.md)
-   [**CBaseFilter::GetSyncSource**](cbasefilter-getsyncsource.md)
-   [**CBaseFilter::JoinFilterGraph**](cbasefilter-joinfiltergraph.md)
-   [**CBaseFilter::IsActive**](cbasefilter-isactive.md)
-   [**CBaseFilter::SetSyncSource**](cbasefilter-setsyncsource.md)
-   [**CBaseFilter::Pause**](cbasefilter-pause.md)
-   [**CBaseFilter::Run**](cbasefilter-run.md)
-   [**CBaseFilter::Stop**](cbasefilter-stop.md)

Do not hold this critical section during streaming operations (that is, when delivering samples to a downstream filter). Serialize streaming operations using a different critical section. Otherwise, it can cause deadlock.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseFilter Class**](cbasefilter.md)
</dt> <dt>

[Threads and Critical Sections](threads-and-critical-sections.md)
</dt> </dl>

 

 




