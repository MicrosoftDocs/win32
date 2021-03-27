---
description: The InitialThreadProc method calls the COutputQueue::ThreadProc method when the thread is created.
ms.assetid: 6093f0c3-ec58-418d-bb8c-618163c43ac7
title: COutputQueue.InitialThreadProc method (Outputq.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COutputQueue.InitialThreadProc
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# COutputQueue.InitialThreadProc method

The `InitialThreadProc` method calls the [**COutputQueue::ThreadProc**](coutputqueue-threadproc.md) method when the thread is created.

## Syntax


```C++
static DWORD WINAPI InitialThreadProc(
   LPVOID pv
);
```



## Parameters

<dl> <dt>

*pv* 
</dt> <dd>

`this` pointer.

</dd> </dl>

## Return value

Returns the value returned by the [**COutputQueue::ThreadProc**](coutputqueue-threadproc.md) method.

## Remarks

This method is the thread procedure for the object's worker thread. The object's `this` pointer is the thread parameter. The method dereferences this to call **ThreadProc**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




