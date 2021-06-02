---
description: Sample end time. This value is valid only if the CMediaSample::m\_dwFlags member variable contains the AM\_SAMPLE\_STOPVALID flag.
ms.assetid: 01488984-579b-49e0-923e-bfbeba96b4d8
title: CMediaSample::m_End member (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_End
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaSample::m\_End member

Sample end time. This value is valid only if the [**CMediaSample::m\_dwFlags**](cmediasample-m-dwflags.md) member variable contains the AM\_SAMPLE\_STOPVALID flag.

## Syntax


```C++
REFERENCE_TIME m_End;
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

 

 




