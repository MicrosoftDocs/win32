---
description: The ThreadProc method is the thread procedure.
ms.assetid: 2d991f15-afea-4843-bc68-aeb5ca69d28b
title: CAMThread.ThreadProc method (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMThread.ThreadProc
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAMThread.ThreadProc method

The `ThreadProc` method is the thread procedure.

## Syntax


```C++
virtual DWORD ThreadProc() = 0;
```



## Parameters

This method has no parameters.

## Return value

Returns a **DWORD** value whose meaning is defined by the derived class.

## Remarks

This is a pure virtual method. Implement this method in your derived class to supply a thread procedure. When the [**CAMThread::Create**](camthread-create.md) method creates a thread, it gives the address of the [**CAMThread::InitialThreadProc**](camthread-initialthreadproc.md) method, which in turn calls your ThreadProc method.

Typically, your ThreadProc method will enter a loop that retrieves requests (by calling the [**CAMThread::GetRequest**](camthread-getrequest.md) or [**CAMThread::CheckRequest**](camthread-checkrequest.md) methods) and processes data.

When this method returns, the thread exits.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMThread Class**](camthread.md)
</dt> </dl>

 

 




