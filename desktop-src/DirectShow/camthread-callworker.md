---
description: The CallWorker method signals the thread with a request.
ms.assetid: 51431688-bf55-4778-afc0-91b6ab336aa3
title: CAMThread.CallWorker method (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMThread.CallWorker
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAMThread.CallWorker method

The `CallWorker` method signals the thread with a request.

## Syntax


```C++
DWORD CallWorker(
   DWORD dwParam
);
```



## Parameters

<dl> <dt>

*dwParam* 
</dt> <dd>

Request parameter. The derived class defines the meaning of the parameter.

</dd> </dl>

## Return value

Returns a value that is defined by the derived class.

## Remarks

The [**CAMThread::GetRequest**](camthread-getrequest.md) and [**CAMThread::CheckRequest**](camthread-checkrequest.md) methods retrieve the value of the *dwParam* parameter. The GetRequest method blocks until `CallWorker` is called.

This method blocks until the [**CAMThread::Reply**](camthread-reply.md) method is called. The return value is the parameter given to Reply.

This method holds the [**CAMThread::m\_AccessLock**](camthread-m-accesslock.md) lock to serialize requests. Therefore, do call this method from the thread itself or from any member function that executes in the context of the thread.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMThread Class**](camthread.md)
</dt> </dl>

 

 




