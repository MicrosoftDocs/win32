---
Description: Start time. By default, the value is set to zero.
ms.assetid: bafa69c3-ead0-4409-abbf-4e8cc325e5f9
title: CSourceSeekingm\_rtStart member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CSourceSeeking::m\_rtStart member

Start time. By default, the value is set to zero.

## Syntax


```C++
CRefTime m_rtStart;
```



## Remarks

Hold the **m\_pLock** critical section before accessing this variable.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceSeeking Class**](csourceseeking.md)
</dt> </dl>

 

 




