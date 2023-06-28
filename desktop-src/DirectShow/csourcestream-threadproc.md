---
description: The ThreadProc method is the thread procedure for the worker thread. This method implements the pure virtual CAMThread::ThreadProc method.
ms.assetid: 8e66b609-d795-45a8-8fe5-774c659ee350
title: CSourceStream.ThreadProc method (Source.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceStream.ThreadProc
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CSourceStream.ThreadProc method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `ThreadProc` method is the thread procedure for the worker thread. This method implements the pure virtual [**CAMThread::ThreadProc**](camthread-threadproc.md) method.

## Syntax


```C++
virtual DWORD ThreadProc();
```



## Parameters

This method has no parameters.

## Return value

Returns 0 if the thread completed successfully or 1 otherwise. If the return value is 1, the thread's resources might still be allocated.

## Remarks

This method waits indefinitely for thread requests, by calling the [**CAMThread::GetRequest**](camthread-getrequest.md) method. If it receives a [**CSourceStream::Run**](csourcestream-run.md) or [**CSourceStream::Pause**](csourcestream-pause.md) request, it calls the [**CSourceStream::DoBufferProcessingLoop**](csourcestream-dobufferprocessingloop.md) method. The **DoBufferProcessingLoop** method pushes data until it receives a [**CSourceStream::Stop**](csourcestream-stop.md) request. The thread procedure exits when it receives a [**CSourceStream::Exit**](csourcestream-exit.md) request.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceStream Class**](csourcestream.md)
</dt> </dl>

 

 




