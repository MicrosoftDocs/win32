---
description: The QueueSample method queues a sample.
ms.assetid: f34c0689-5afb-4941-bc3a-e4765fbbe525
title: COutputQueue.QueueSample method (Outputq.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COutputQueue.QueueSample
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# COutputQueue.QueueSample method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `QueueSample` method queues a sample.

## Syntax


```C++
void QueueSample(
   IMediaSample *pSample
);
```



## Parameters

<dl> <dt>

*pSample* 
</dt> <dd>

Pointer to the sample's [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method adds a sample to the tail of the queue. Hold the critical section before calling this method, and call it only when the object is using a thread to deliver samples. To determine if the object is using a thread, call the [**COutputQueue::IsQueued**](coutputqueue-isqueued.md) method.

This method can also be used to put control messages onto the queue. A control message is a defined constant (cast to a LONG\_PTR type) that instructs the thread to perform some action. The **COutputQueue** class defines the control messages shown in the following table.



| Label | Value |
|---------------|----------------------------------------|
| Message       | Action                                 |
| EOS\_PACKET   | Deliver an end-of-stream notification. |
| NEW\_SEGMENT  | Deliver a new segment.                 |
| RESET\_PACKET | Reset the state of the queue.          |
| SEND\_PACKET  | Send a partial batch of samples.       |



 

This is a protected method, which the **COutputQueue** class uses internally.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




