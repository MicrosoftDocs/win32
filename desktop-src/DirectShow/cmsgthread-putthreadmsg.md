---
description: Queues a request for execution by the worker thread.
ms.assetid: a854f962-143d-4776-bf98-119d003867df
title: CMsgThread.PutThreadMsg method (Msgthrd.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMsgThread.PutThreadMsg
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CMsgThread.PutThreadMsg method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Queues a request for execution by the worker thread.

## Syntax


```C++
void PutThreadMsg(
   UINT     uMsg,
   DWORD    dwMsgFlags,
   LPVOID   lpMsgParam,
   CAMEvent *pEvent = NULL
);
```



## Parameters

<dl> <dt>

*uMsg* 
</dt> <dd>

Request code.

</dd> <dt>

*dwMsgFlags* 
</dt> <dd>

Optional flags parameter.

</dd> <dt>

*lpMsgParam* 
</dt> <dd>

Optional pointer to a data block containing additional parameters or return values. Must be statically or heap-allocated and not automatic.

</dd> <dt>

*pEvent* 
</dt> <dd>

Optional pointer to an event object to be signaled upon completion.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This member function queues a request for execution by the worker thread. The parameters of this member function will be queued (in a [**CMsg**](cmsg.md) object) and passed to the [**CMsgThread::ThreadMessageProc**](cmsgthread-threadmessageproc.md) member function of the worker thread. This member function returns immediately after queuing the request and does not wait for the thread to fulfill the request. The **CMsgThread::ThreadMessageProc** member function of the derived class defines the four parameters.

This member function uses a multithread safe list, so multiple calls to this member function from different threads can be made safely.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Msgthrd.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMsgThread Class**](cmsgthread.md)
</dt> </dl>

 

 




