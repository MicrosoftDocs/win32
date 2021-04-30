---
description: Critical section object that protects the filter state. The CSource::pStateLock helper method returns a pointer to this member variable.
ms.assetid: faaf5fea-54bc-4856-9bca-3ed420c491e4
title: CSource::m_cStateLock member (Source.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_cStateLock
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSource::m\_cStateLock member

Critical section object that protects the filter state. The [**CSource::pStateLock**](csource--pstatelock.md) helper method returns a pointer to this member variable.

## Syntax


```C++
CCritSec m_cStateLock;
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSource Class**](csource.md)
</dt> </dl>

 

 




