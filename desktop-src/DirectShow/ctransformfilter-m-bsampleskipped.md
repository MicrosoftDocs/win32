---
description: Flag that indicates whether the most recent sample was dropped. If the Receive method drops a sample, it sets the value to TRUE.
ms.assetid: 6143f948-75b0-47c6-9951-4c18c0773857
title: CTransformFilter::m_bSampleSkipped member (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_bSampleSkipped
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformFilter::m\_bSampleSkipped member

Flag that indicates whether the most recent sample was dropped. If the [**Receive**](ctransformfilter-receive.md) method drops a sample, it sets the value to **TRUE**.

## Syntax


```C++
BOOL m_bSampleSkipped;
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

 

 




