---
description: The TimerCallback method is a callback method for the end-of-stream timer event.
ms.assetid: ed43d07a-1ece-43ab-8753-ab14fa388946
title: CBaseRenderer.TimerCallback method (Renbase.h)
ms.topic: reference
ms.date: 4/26/2023
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
ms.custom: UpdateFrequency5
---

# CBaseRenderer.TimerCallback method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




