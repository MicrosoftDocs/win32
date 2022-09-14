---
description: Sample start time. This value is valid only if the CMediaSample::m\_dwFlags member variable contains the AM\_SAMPLE\_TIMEVALID flag.
ms.assetid: 31af979b-4c10-4f15-aa8a-90807b5cc156
title: CMediaSample::m_Start member (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_Start
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaSample::m\_Start member

Sample start time. This value is valid only if the [**CMediaSample::m\_dwFlags**](cmediasample-m-dwflags.md) member variable contains the AM\_SAMPLE\_TIMEVALID flag.

## Syntax


```C++
REFERENCE_TIME m_Start;
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




