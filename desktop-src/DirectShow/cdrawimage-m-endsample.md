---
description: The m\_EndSample member variable specifies the stop time of the most recent sample.
ms.assetid: 694815b6-8da5-4174-b2c7-7d686a557c6c
title: CDrawImage::m_EndSample member (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_EndSample
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDrawImage::m\_EndSample member

The `m_EndSample` member variable specifies the stop time of the most recent sample.

## Syntax


```C++
CRefTime m_EndSample;
```



## Remarks

The value is only valid inside the [**CDrawImage::DisplaySampleTimes**](cdrawimage-displaysampletimes.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> </dl>

 

 




