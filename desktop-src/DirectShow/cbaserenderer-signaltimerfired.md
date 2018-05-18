---
Description: 'The SignalTimerFired method clears the timer identifier used to schedule rendering.'
ms.assetid: 'b8ae362e-fcda-4888-be32-8fb910d0f0db'
title: 'CBaseRenderer.SignalTimerFired method'
---

# CBaseRenderer.SignalTimerFired method

The `SignalTimerFired` method clears the timer identifier used to schedule rendering.

## Syntax


```C++
virtual void SignalTimerFired();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The filter calls this method when the rendering timer activates (see [**CBaseRenderer::WaitForRenderTime**](cbaserenderer-waitforrendertime.md)) or when the timer is canceled (see [**CBaseRenderer::CancelNotification**](cbaserenderer-cancelnotification.md)). The method resets the [**CBaseRenderer::m\_dwAdvise**](cbaserenderer-m-dwadvise.md) member variable to zero.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




