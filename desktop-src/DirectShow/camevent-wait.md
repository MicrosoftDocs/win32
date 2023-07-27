---
description: The Wait method blocks until the event is signaled, or until a time-out occurs.
ms.assetid: bcc13723-a59b-4e8a-bfc8-eadb6facf116
title: CAMEvent.Wait method (Wxutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMEvent.Wait
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CAMEvent.Wait method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `Wait` method blocks until the event is signaled, or until a time-out occurs.

## Syntax


```C++
BOOL Wait(
   DWORD dwTimeout = INFINITE
);
```



## Parameters

<dl> <dt>

*dwTimeout* 
</dt> <dd>

Optional time-out value, represented in milliseconds.

</dd> </dl>

## Return value

Returns **TRUE** if the event is signaled. Otherwise, returns **FALSE**.

## Remarks

For auto-reset events, the event is reset to a nonsignaled state when this method returns.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMEvent Class**](camevent.md)
</dt> </dl>

 

 




