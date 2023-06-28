---
description: The ResetEndOfStreamTimer method cancels the timer that schedules EC\_COMPLETE notifications.
ms.assetid: 9d423241-1401-4181-8fbf-c409a1e8abdd
title: CBaseRenderer.ResetEndOfStreamTimer method (Renbase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.ResetEndOfStreamTimer
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseRenderer.ResetEndOfStreamTimer method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `ResetEndOfStreamTimer` method cancels the timer that schedules [**EC\_COMPLETE**](ec-complete.md) notifications.

## Syntax


```C++
void ResetEndOfStreamTimer();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> <dt>

[**CBaseRenderer::SendEndOfStream**](cbaserenderer-sendendofstream.md)
</dt> <dt>

[**CBaseRenderer::TimerCallback**](cbaserenderer-timercallback.md)
</dt> </dl>

 

 




