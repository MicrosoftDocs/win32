---
description: The RecordFrameLateness method records how timely the rendering occurred and gathers statistics for the property page.
ms.assetid: 9d4b90d7-b529-40cc-a0fd-6635163fb7dd
title: CBaseVideoRenderer.RecordFrameLateness method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseVideoRenderer.RecordFrameLateness
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseVideoRenderer.RecordFrameLateness method

The `RecordFrameLateness` method records how timely the rendering occurred and gathers statistics for the property page.

## Syntax


```C++
virtual void RecordFrameLateness(
   int trLate,
   int trFrame
);
```



## Parameters

<dl> <dt>

*trLate* 
</dt> <dd>

Value indicating how late the sample was beyond its due time, in reference time units.

</dd> <dt>

*trFrame* 
</dt> <dd>

Interframe time, in reference time units.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




