---
description: The CQueue class template implements a simple, statically sized queue.
ms.assetid: 5a4f0bcf-24ed-427d-898d-f3ddc6a35b59
title: CQueue class (Wxutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CQueue
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CQueue class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **CQueue** class template implements a simple, statically sized queue.



| Public Methods                                  | Description                             |
|-------------------------------------------------|-----------------------------------------|
| [**CQueue**](cqueue-cqueue.md)                 | Constructor method.                     |
| [**~CQueue**](cqueue--cqueue.md)               | Destructor method.                      |
| [**GetQueueObject**](cqueue-getqueueobject.md) | Retrieves the next item from the queue. |
| [**PutQueueObject**](cqueue-putqueueobject.md) | Puts an item onto the queue.            |



 

## Remarks

The class constructor specifies the size of the queue. Use the [**CQueue::PutQueueObject**](cqueue-putqueueobject.md) to put an item on the queue, and the [**CQueue::GetQueueObject**](cqueue-getqueueobject.md) method to dequeues an item. If the queue is full, the **PutQueueObject** method blocks until an item is dequeued. If the queue is empty, the **GetQueueObject** blocks until an item is queued. The template parameter specifies the type of item. For example:


```
CQueue<int> number_queue;
number_queue.PutQueueObject(7);
```



The class uses two semaphores to control queuing operations, a "get" semaphore and a "put" semaphore. The [**GetQueueObject**](cqueue-getqueueobject.md) method waits on the "get" semaphore (using the **WaitForSingleObject** function) and releases the "put" semaphore (using the **ReleaseSemaphore** function). The [**PutQueueObject**](cqueue-putqueueobject.md) method waits on the "put" semaphore and releases the "get" semaphore. The class uses a critical section to serialize queuing operations among multiple threads.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




