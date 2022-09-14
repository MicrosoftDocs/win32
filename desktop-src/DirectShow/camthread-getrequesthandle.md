---
description: The GetRequestHandle method retrieves a handle to the event that is signaled by the CAMThread::CallWorker method.
ms.assetid: 6e4496ae-a635-4b55-ae7a-31748f21068b
title: CAMThread.GetRequestHandle method (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMThread.GetRequestHandle
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAMThread.GetRequestHandle method

The `GetRequestHandle` method retrieves a handle to the event that is signaled by the [**CAMThread::CallWorker**](camthread-callworker.md) method.

## Syntax


```C++
HANDLE GetRequestHandle() const;
```



## Parameters

This method has no parameters.

## Return value

Returns an event handle.

## Remarks

The CAMEvent class keeps a private manual-reset event, which is set by CallWorker and reset by the [**CAMThread::Reply**](camthread-reply.md) method.

If you call a function such as WaitForMultipleObjects, use GetRequestHandle to retrieve the event handle.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMThread Class**](camthread.md)
</dt> </dl>

 

 




