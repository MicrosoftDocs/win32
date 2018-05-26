---
Description: Pointer to a critical section.
ms.assetid: 7d949b7f-a6a7-4ab5-b651-f85b70d55065
title: CBaseMediaFilterm\_pLock member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseMediaFilter::m\_pLock member

Pointer to a critical section.

## Syntax


```C++
CCritSec *m_pLock;
```



## Remarks

The critical section is held during state transitions ([**CBaseMediaFilter::Run**](cbasemediafilter-run.md), [**CBaseMediaFilter::Pause**](cbasemediafilter-pause.md), [**CBaseMediaFilter::Stop**](cbasemediafilter-stop.md)), when accessing the reference clock ([**CBaseMediaFilter::SetSyncSource**](cbasemediafilter-setsyncsource.md), [**CBaseMediaFilter::GetSyncSource**](cbasemediafilter-getsyncsource.md)), and in the [**CBaseMediaFilter::IsActive**](cbasemediafilter-isactive.md) method.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseMediaFilter Class**](cbasemediafilter.md)
</dt> </dl>

 

 




