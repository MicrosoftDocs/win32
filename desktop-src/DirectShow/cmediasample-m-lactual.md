---
description: Length of the valid data in the buffer, in bytes. The value must be equal to or less than the size of the buffer, specified by the CMediaSample::m\_cbBuffer member variable.
ms.assetid: 75610043-fe0b-4cd0-9fd6-292f25040d72
title: CMediaSample::m_lActual member (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_lActual
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaSample::m\_lActual member

Length of the valid data in the buffer, in bytes. The value must be equal to or less than the size of the buffer, specified by the [**CMediaSample::m\_cbBuffer**](cmediasample-m-cbbuffer.md) member variable.

## Syntax


```C++
LONG m_lActual;
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

 

 




