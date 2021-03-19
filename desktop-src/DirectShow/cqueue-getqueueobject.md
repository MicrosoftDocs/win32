---
description: Retrieves the next item from the queue.
ms.assetid: 406ae640-5903-427d-91f9-8b01beb1aaa7
title: CQueue.GetQueueObject method (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CQueue.GetQueueObject
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CQueue.GetQueueObject method

Retrieves the next item from the queue.

## Syntax


```C++
T GetQueueObject();
```



## Parameters

This method has no parameters.

## Return value

Returns an object of type **T** (the template type).

## Remarks

This method blocks until an item is available on the queue.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CQueue Class**](cqueue.md)
</dt> </dl>

 

 




