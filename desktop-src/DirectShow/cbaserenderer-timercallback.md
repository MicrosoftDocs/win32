---
description: The TimerCallback method is a callback method for the end-of-stream timer event.
ms.assetid: ed43d07a-1ece-43ab-8753-ab14fa388946
title: CBaseRenderer.TimerCallback method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.TimerCallback
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.TimerCallback method

The `TimerCallback` method is a callback method for the end-of-stream timer event.

## Syntax


```C++
void TimerCallback();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The [**CBaseRenderer::SendEndOfStream**](cbaserenderer-sendendofstream.md) method uses a timer event to schedule EC\_COMPLETE notifications. The **CBaseRenderer::TimerCallback** method is the callback function for the timer event. The `TimerCallback` method calls **SendEndOfStream** again, and **SendEndOfStream** determines whether to send the EC\_COMPLETE notification or set another timer.

The [**CBaseRenderer::ResetEndOfStreamTimer**](cbaserenderer-resetendofstreamtimer.md) method cancels the timer event.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




