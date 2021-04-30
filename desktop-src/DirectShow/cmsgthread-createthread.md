---
description: Creates a thread.
ms.assetid: 40785522-dc6e-41af-8b27-9e8875a0dd84
title: CMsgThread.CreateThread method (Msgthrd.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMsgThread.CreateThread
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMsgThread.CreateThread method

Creates a thread.

## Syntax


```C++
BOOL CreateThread();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the following values.



| Return code                                                                              | Description                                     |
|------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>****TRUE****</dt> </dl>  | Thread was successfully created.<br/>     |
| <dl> <dt>****FALSE****</dt> </dl> | Thread was not successfully created.<br/> |



 

## Remarks

The thread will loop, blocking until a request is queued (through the [**CMsgThread::PutThreadMsg**](cmsgthread-putthreadmsg.md) member function) and then calling the [**CMsgThread::ThreadMessageProc**](cmsgthread-threadmessageproc.md) member function with each message.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Msgthrd.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMsgThread Class**](cmsgthread.md)
</dt> </dl>

 

 




