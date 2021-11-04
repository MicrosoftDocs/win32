---
description: The Reply method replies to a request.
ms.assetid: 90e91b99-6a1c-46a2-b83d-eba483f1832a
title: CAMThread.Reply method (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMThread.Reply
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAMThread.Reply method

The `Reply` method replies to a request.

## Syntax


```C++
void Reply(
   DWORD dw
);
```



## Parameters

<dl> <dt>

*dw* 
</dt> <dd>

Value to return in the [**CAMThread::CallWorker**](camthread-callworker.md) method.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The CallWorker method blocks until this method is called. The *dw* parameter supplies the return value for CallWorker. Call this method in your thread procedure after you retrieve a request, to release the requesting thread.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMThread Class**](camthread.md)
</dt> </dl>

 

 




