---
description: The WaitMsg method waits for the event to be signaled, while dispatching sent messages.
ms.assetid: 5cab98ca-f9f3-4c7c-9ce2-8e16109d8fbb
title: CAMMsgEvent.WaitMsg method (Wxutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMMsgEvent.WaitMsg
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CAMMsgEvent.WaitMsg method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `WaitMsg` method waits for the event to be signaled, while dispatching sent messages.

## Syntax


```C++
BOOL WaitMsg(
   DWORD dwTimeOut = INFINITE
);
```



## Parameters

<dl> <dt>

*dwTimeOut* 
</dt> <dd>

Optional time-out value, in milliseconds.

</dd> </dl>

## Return value

Returns **TRUE** if the event is signaled, or **FALSE** if the time-out occurred.

## Remarks

This method calls the PeekMessage function to process messages. Call this method instead of [**CAMEvent::Wait**](camevent-wait.md) if your thread needs to process messages while waiting for an event. If the thread does not process messages and another thread sends a message, deadlock could occur.

For example, suppose you create a thread and then block until the thread initializes. If the thread sends a message to your window by calling the SendMessage function, it will result in a deadlock. This is because SendMessage does not return until the message has been processed. Calling WaitMsg allows the SendMessage call to return, preventing the deadlock.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMMsgEvent Class**](cammsgevent.md)
</dt> </dl>

 

 




