---
Description: Duration of the stream. By default, the value is set to the value of the CSourceSeeking::m\_rtStop member variable.
ms.assetid: a87b321e-3179-4485-969b-bf12cb634b43
title: CSourceSeeking::m\_rtDuration member
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CSourceSeeking::m\_rtDuration member

Duration of the stream. By default, the value is set to the value of the [**CSourceSeeking::m\_rtStop**](csourceseeking-m-rtstop.md) member variable.

## Syntax


```C++
CRefTime m_rtDuration;
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

 

 




