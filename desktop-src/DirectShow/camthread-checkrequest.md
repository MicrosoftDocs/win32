---
description: The CheckRequest method checks if there is a request, without blocking.
ms.assetid: 46d0840e-a304-41e3-9016-9f35e404cd30
title: CAMThread.CheckRequest method (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMThread.CheckRequest
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAMThread.CheckRequest method

The `CheckRequest` method checks if there is a request, without blocking.

## Syntax


```C++
BOOL CheckRequest(
   DWORD *pParam
);
```



## Parameters

<dl> <dt>

*pParam* 
</dt> <dd>

Pointer to a variable that receives the value passed in the last call to the [**CAMThread::CallWorker**](camthread-callworker.md) method.

</dd> </dl>

## Return value

Returns **TRUE** if there is a pending request, or **FALSE** otherwise.

## Remarks

This method is a non-blocking version of the [**CAMThread::GetRequest**](camthread-getrequest.md) method.

If another thread is waiting on a call to CallWorker, this method retrieves the request parameter and returns **TRUE**. Otherwise, it returns **FALSE**. If the method returns **TRUE**, call the [**CAMThread::Reply**](camthread-reply.md) method to release the requesting thread.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMThread Class**](camthread.md)
</dt> </dl>

 

 




