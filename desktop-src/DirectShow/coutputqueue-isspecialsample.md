---
description: The IsSpecialSample method determines whether queued data is a control message.
ms.assetid: 33d9c7a2-3046-45a5-a9f5-8f33a03bbcdd
title: COutputQueue.IsSpecialSample method (Outputq.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COutputQueue.IsSpecialSample
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# COutputQueue.IsSpecialSample method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `IsSpecialSample` method determines whether queued data is a control message.

## Syntax


```C++
BOOL IsSpecialSample(
   IMediaSample *pSample
);
```



## Parameters

<dl> <dt>

*pSample* 
</dt> <dd>

Pointer to an item in the queue.

</dd> </dl>

## Return value

Returns **TRUE** if *pSample* is a control message, or **FALSE** otherwise.

## Remarks

The [**COutputQueue::QueueSample**](coutputqueue-queuesample.md) method can receive control messages in addition to media samples. A control message is a defined constant (cast to a LONG\_PTR type) that instructs the thread to perform an action. Control messages do not contain media data. For more information, see **COutputQueue::QueueSample**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




