---
description: The CompleteStateChange method determines whether a transition to the paused state is complete.
ms.assetid: 505a0b31-deaa-46be-91e6-f9bc8e47dd3a
title: CBaseRenderer.CompleteStateChange method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.CompleteStateChange
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.CompleteStateChange method

The `CompleteStateChange` method determines whether a transition to the paused state is complete.

## Syntax


```C++
virtual HRESULT CompleteStateChange(
   FILTER_STATE OldState
);
```



## Parameters

<dl> <dt>

*OldState* 
</dt> <dd>

State prior to the transition.

</dd> </dl>

## Return value

Returns S\_OK if the transition is complete. Otherwise, returns S\_FALSE.

## Remarks

The [**CBaseRenderer::Pause**](cbaserenderer-pause.md) method calls this method to update the state-transition status. In general, the transition to paused does not finish until the filter receives a sample. However, in some situations the transition completes immediately: for example, if the filter is unconnected, or if the end of the stream was reached. This method checks the various criteria and then calls the [**CBaseRenderer::Ready**](cbaserenderer-ready.md) method or the [**CBaseRenderer::NotReady**](cbaserenderer-notready.md) method to update the transition status.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




