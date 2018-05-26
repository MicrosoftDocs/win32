---
Description: Critical section object that protects the filter state. The CSourcepStateLock helper method returns a pointer to this member variable.
ms.assetid: faaf5fea-54bc-4856-9bca-3ed420c491e4
title: CSourcem\_cStateLock member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CSource::m\_cStateLock member

Critical section object that protects the filter state. The [**CSource::pStateLock**](csource--pstatelock.md) helper method returns a pointer to this member variable.

## Syntax


```C++
CCritSec m_cStateLock;
```



## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSource Class**](csource.md)
</dt> </dl>

 

 




