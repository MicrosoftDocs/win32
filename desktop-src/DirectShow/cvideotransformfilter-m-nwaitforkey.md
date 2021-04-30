---
description: The current maximum number of delta frames to drop.
ms.assetid: d14c594e-55ab-42c2-bdb0-6829f71d02dd
title: CVideoTransformFilter::m_nWaitForKey member (Vtrans.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_nWaitForKey
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CVideoTransformFilter::m\_nWaitForKey member

The current maximum number of delta frames to drop. While this variable is greater than zero, the filter will drop frames until it reaches a key frame. For each frame that is dropped, the filter decrements this variable by one, which prevents the filter from dropping an excessive number of frames. After 30 delta frames in a row with no key frames, the filter will start delivering frames again.

## Syntax


```C++
int m_nWaitForKey;
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Vtrans.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CVideoTransformFilter Class**](cvideotransformfilter.md)
</dt> </dl>

 

 




