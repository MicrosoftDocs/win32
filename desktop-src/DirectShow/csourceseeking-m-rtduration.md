---
Description: Duration of the stream. By default, the value is set to the value of the CSourceSeekingm\_rtStop member variable.
ms.assetid: a87b321e-3179-4485-969b-bf12cb634b43
title: CSourceSeekingm\_rtDuration member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

 

 




