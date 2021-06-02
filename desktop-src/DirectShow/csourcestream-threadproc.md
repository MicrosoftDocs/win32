---
description: The ThreadProc method is the thread procedure for the worker thread. This method implements the pure virtual CAMThread::ThreadProc method.
ms.assetid: 8e66b609-d795-45a8-8fe5-774c659ee350
title: CSourceStream.ThreadProc method (Source.h)
ms.topic: reference
ms.date: 05/31/2018
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
---

# CSourceStream.ThreadProc method

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

 

 




