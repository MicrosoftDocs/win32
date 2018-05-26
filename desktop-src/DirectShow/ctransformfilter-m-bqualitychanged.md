---
Description: Flag that indicates whether the quality has changed.
ms.assetid: 9084ab1d-b6a0-4e87-a653-86e64c74b07f
title: CTransformFilterm\_bQualityChanged member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CTransformFilter::m\_bQualityChanged member

Flag that indicates whether the quality has changed. The first time that the filter drops a sample, it sends an [**EC\_QUALITY\_CHANGE**](ec-quality-change.md) event to the filter graph manager and sets this flag to **TRUE**. It does not send this event again until the filter stops and restarts, even if it continues to drop samples in the meantime.

## Syntax


```C++
BOOL m_bQualityChanged;
```



## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




