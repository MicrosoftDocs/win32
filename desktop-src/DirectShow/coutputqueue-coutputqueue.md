---
description: COutputQueue.COutputQueue constructor - Constructor method.
ms.assetid: 672c0337-0c36-4f53-9125-d02fe8b36b1c
title: COutputQueue.COutputQueue constructor (Outputq.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COutputQueue.COutputQueue
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# COutputQueue.COutputQueue constructor

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Constructor method.

## Syntax


```C++
COutputQueue(
   IPin    *pInputPin,
   HRESULT *phr,
   BOOL    bAuto = TRUE,
   BOOL    bQueue = TRUE,
   LONG    lBatchSize = 1,
   BOOL    bBatchExact = FALSE,
   LONG    lListSize = DEFAULTCACHE,
   DWORD   dwPriority = THREAD_PRIORITY_NORMAL
);
```



## Parameters

<dl> <dt>

*pInputPin* 
</dt> <dd>

Pointer to the [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface of the input pin. The object will deliver samples to this pin.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to an **HRESULT** return code. Set the value to S\_OK before calling this method. On return, *phr* receives a value that indicates the success or failure of the method.

</dd> <dt>

*bAuto* 
</dt> <dd>

Flag that specifies whether the object decides when to create a queue. If **TRUE**, the object creates a queue only if the input pin might block. If **FALSE**, the *bQueue* parameter specifies whether to create a queue.

</dd> <dt>

*bQueue* 
</dt> <dd>

If *bAuto* is **TRUE**, this parameter is ignored. If *bAuto* is **FALSE**, this flag specifies whether to create a queue.

</dd> <dt>

*lBatchSize* 
</dt> <dd>

Maximum number of samples to deliver in one batch.

</dd> <dt>

*bBatchExact* 
</dt> <dd>

Flag that specifies whether to use exact batch sizes. If **TRUE**, the object waits for *lBatchSize* samples before delivering them to the input pin. If **FALSE**, the object delivers samples as it receives them.

</dd> <dt>

*lListSize* 
</dt> <dd>

Cache size for the queue. The default value, DEFAULTCACHE, is a constant defined for the [**CBaseList**](cbaselist.md) class.

</dd> <dt>

*dwPriority* 
</dt> <dd>

Priority of the thread that delivers samples.

</dd> </dl>

## Remarks

If *bAuto* is **TRUE**, the object calls the [**IMemInputPin::ReceiveCanBlock**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receivecanblock) method on the downstream pin. If **ReceiveCanBlock** returns S\_OK (meaning the pin might block on [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) calls), the object creates a thread for delivering samples. Otherwise, it does not create a thread.

If *bAuto* is **FALSE**, the value of *bQueue* determines whether to create a thread.

If the object creates a thread, it assigns the thread handle to the [**COutputQueue::m\_hThread**](coutputqueue-m-hthread.md) member variable. The thread procedure is [**COutputQueue::InitialThreadProc**](coutputqueue-initialthreadproc.md), and the thread parameter is a pointer to this. The object also creates a queue for holding samples, which is given by the [**COutputQueue::m\_List**](coutputqueue-m-list.md) member variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




