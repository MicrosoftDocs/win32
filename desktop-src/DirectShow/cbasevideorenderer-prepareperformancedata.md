---
description: The PreparePerformanceData method sets the m\_trLate and m\_trFrame values of the current frame.
ms.assetid: c4c5701b-eccd-4259-a1d1-7c5000f6b2df
title: CBaseVideoRenderer.PreparePerformanceData method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseVideoRenderer.PreparePerformanceData
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseVideoRenderer.PreparePerformanceData method

The `PreparePerformanceData` method sets the **m\_trLate** and **m\_trFrame** values of the current frame.

## Syntax


```C++
void PreparePerformanceData(
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

## Remarks

This member function sets **m\_trLate** to the value of *trLate* and **m\_trFrame** to the value of *trFrame*.

When the [**CBaseVideoRenderer::RecordFrameLateness**](cbasevideorenderer-recordframelateness.md) member function is called from either [**CBaseVideoRenderer::OnRenderStart**](cbasevideorenderer-onrenderstart.md) or [**CBaseVideoRenderer::OnDirectRender**](cbasevideorenderer-ondirectrender.md), it passes the values of **m\_trLate** and **m\_trFrame** for it to update the statistics. `PreparePerformanceData` is called from [**CBaseVideoRenderer::OnWaitEnd**](cbasevideorenderer-onwaitend.md) to set these data member values.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




