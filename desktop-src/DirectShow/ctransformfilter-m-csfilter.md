---
description: Critical section that protects the filter state. For more information, see Data Flow for Filter Developers.
ms.assetid: 75b9c8b0-e911-41fd-8d07-b854dbe25551
title: CTransformFilter::m_csFilter member (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_csFilter
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformFilter::m\_csFilter member

Critical section that protects the filter state. For more information, see [Data Flow for Filter Developers](data-flow-for-filter-developers.md).

## Syntax


```C++
CCritSec m_csFilter;
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

 

 




