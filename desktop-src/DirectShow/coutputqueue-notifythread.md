---
description: The NotifyThread method notifies the thread that the queue contains data.
ms.assetid: d91cde3f-2876-4fb4-a124-f1460bba2cc9
title: COutputQueue.NotifyThread method (Outputq.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COutputQueue.NotifyThread
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# COutputQueue.NotifyThread method

The `NotifyThread` method notifies the thread that the queue contains data.

## Syntax


```C++
void NotifyThread();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Hold the critical section before calling this method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




