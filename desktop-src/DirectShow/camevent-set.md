---
description: The Set method signals the event.
ms.assetid: dfcb1601-aa65-47f5-ae3c-f13fcd7b1398
title: CAMEvent.Set method (Wxutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMEvent.Set
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CAMEvent.Set method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `Set` method signals the event.

## Syntax


```C++
void Set();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The behavior depends on whether the object is an auto-reset event or a manual-reset event:

-   **Auto-reset**: If any threads are waiting on this event, one thread is released and the event is reset. If no threads are waiting on this event, the event remains signaled.
-   **Manual-reset**: All the threads waiting on this event are released. The event remains signaled.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMEvent Class**](camevent.md)
</dt> </dl>

 

 




