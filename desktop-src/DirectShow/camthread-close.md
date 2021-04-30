---
description: The Close method waits for the thread to exit, then releases its resources.
ms.assetid: 57e27ff7-3665-416e-8a6e-660483c5aed2
title: CAMThread.Close method (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMThread.Close
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAMThread.Close method

The `Close` method waits for the thread to exit, then releases its resources.

## Syntax


```C++
void Close();
```



## Parameters

This method has no parameters.

## Return value

No return value.

## Remarks

Before calling this method, you must provide a way for the thread to exit. For example, in your [**CAMThread::ThreadProc**](camthread-threadproc.md) method, define a request that signals the thread to exit. Then call the [**CAMThread::CallWorker**](camthread-callworker.md) method with that value.

The [**~ CAMThread**](camthread--camthread.md) destructor method calls this method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMThread Class**](camthread.md)
</dt> </dl>

 

 




