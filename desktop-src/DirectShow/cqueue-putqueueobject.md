---
description: Puts an item onto the queue.
ms.assetid: 8ac41d80-e7d5-4b3f-9f09-c3d39c94c490
title: CQueue.PutQueueObject method (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CQueue.PutQueueObject
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CQueue.PutQueueObject method

Puts an item onto the queue.

## Syntax


```C++
void PutQueueObject(
   T object
);
```



## Parameters

<dl> <dt>

*object* 
</dt> <dd>

Object of type **T** (the template type).

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This method blocks until there is space in the queue for the item.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CQueue Class**](cqueue.md)
</dt> </dl>

 

 




