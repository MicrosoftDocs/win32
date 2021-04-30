---
description: Stop time. By default, the value is set to a very large number. The derived class can reset the value in its constructor, or when the filter is initialized.
ms.assetid: 1fddcf84-fd9a-4dad-892c-1b0abbb0ca55
title: CSourceSeeking::m_rtStop member (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_rtStop
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceSeeking::m\_rtStop member

Stop time. By default, the value is set to a very large number. The derived class can reset the value in its constructor, or when the filter is initialized.

## Syntax


```C++
CRefTime m_rtStop;
```



## Remarks

Hold the **m\_pLock** critical section before accessing this variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceSeeking Class**](csourceseeking.md)
</dt> </dl>

 

 




