---
description: The SetPopEvent method specifies an event that is signaled whenever the object removes a sample from the queue.
ms.assetid: 147a09b9-14d3-4739-843a-1bfb19d2d052
title: COutputQueue.SetPopEvent method (Outputq.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COutputQueue.SetPopEvent
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# COutputQueue.SetPopEvent method

The `SetPopEvent` method specifies an event that is signaled whenever the object removes a sample from the queue.

## Syntax


```C++
void SetPopEvent(
   HANDLE hEvent
);
```



## Parameters

<dl> <dt>

*hEvent* 
</dt> <dd>

Handle to an event created by the caller.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Outputq.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**COutputQueue Class**](coutputqueue.md)
</dt> </dl>

 

 




