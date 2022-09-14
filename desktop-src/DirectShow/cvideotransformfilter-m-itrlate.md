---
description: Indicates how late the samples are arriving at the renderer, in reference time units. Syntax.
ms.assetid: 7b30fbe1-5e57-4aa4-8e87-ddd584f186e4
title: CVideoTransformFilter::m_itrLate member (Vtrans.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_itrLate
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CVideoTransformFilter::m\_itrLate member

Indicates how late the samples are arriving at the renderer, in reference time units. Syntax

## Syntax


```C++
int m_itrLate;
```



## Remarks

When the filter receives a quality message from downstream, it stores the lateness value in this variable. As the filter drops frames, it updates this value by subtracting the duration of each frame.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Vtrans.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CVideoTransformFilter Class**](cvideotransformfilter.md)
</dt> </dl>

 

 




