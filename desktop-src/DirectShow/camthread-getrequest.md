---
description: The GetRequest method waits for the next request.
ms.assetid: 9f275ee6-cb78-455a-b924-7337c8d2a6dd
title: CAMThread.GetRequest method (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMThread.GetRequest
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAMThread.GetRequest method

The `GetRequest` method waits for the next request.

## Syntax


```C++
DWORD GetRequest();
```



## Parameters

This method has no parameters.

## Return value

Returns a value that is defined by the derived class.

## Remarks

This method blocks until another thread calls the [**CAMThread::CallWorker**](camthread-callworker.md) method. Then it returns the parameter that was passed to CallWorker. Call the [**CAMThread::Reply**](camthread-reply.md) method to release the requesting thread.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMThread Class**](camthread.md)
</dt> </dl>

 

 




