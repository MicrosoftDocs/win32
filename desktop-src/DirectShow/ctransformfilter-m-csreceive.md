---
description: Critical section that protects the streaming state. For more information, see Data Flow for Filter Developers.
ms.assetid: f77c3129-ca25-47b8-8a6e-3a07169701af
title: CTransformFilter::m_csReceive member (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_csReceive
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformFilter::m\_csReceive member

Critical section that protects the streaming state. For more information, see [Data Flow for Filter Developers](data-flow-for-filter-developers.md).

## Syntax


```C++
CCritSec m_csReceive;
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

 

 




