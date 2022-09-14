---
description: Flag that indicates whether the filter has sent an end-of-stream notification.
ms.assetid: 93f897de-04bb-4de4-a612-39b27c7d6f6c
title: CTransformFilter::m_bEOSDelivered member (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_bEOSDelivered
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformFilter::m\_bEOSDelivered member

Flag that indicates whether the filter has sent an end-of-stream notification.

## Syntax


```C++
BOOL m_bEOSDelivered;
```



## Remarks

If the filter pauses when it does not have an input connection, it sends an end-of-stream notification downstream and sets this flag to **TRUE**. The end-of-stream notification ensures that the downstream filter does not wait for samples. Note that the filter's [**EndOfStream**](ctransformfilter-endofstream.md) method does not set this flag.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




