---
description: Flag that indicates whether the quality has changed.
ms.assetid: 9084ab1d-b6a0-4e87-a653-86e64c74b07f
title: CTransformFilter::m_bQualityChanged member (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_bQualityChanged
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformFilter::m\_bQualityChanged member

Flag that indicates whether the quality has changed. The first time that the filter drops a sample, it sends an [**EC\_QUALITY\_CHANGE**](ec-quality-change.md) event to the filter graph manager and sets this flag to **TRUE**. It does not send this event again until the filter stops and restarts, even if it continues to drop samples in the meantime.

## Syntax


```C++
BOOL m_bQualityChanged;
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




