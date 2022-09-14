---
description: The Check method checks whether the event is set, without blocking.
ms.assetid: b8e55798-fd8e-4442-bc35-08887d8a3129
title: CAMEvent.Check method (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMEvent.Check
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAMEvent.Check method

The `Check` method checks whether the event is set, without blocking.

## Syntax


```C++
BOOL Check();
```



## Parameters

This method has no parameters.

## Remarks

Returns **TRUE** if the event is set, or **FALSE** otherwise. This method calls the [**CAMEvent::Wait**](camevent-wait.md) method with a time-out of zero. If the object is an auto-reset event, this method resets the event.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMEvent Class**](camevent.md)
</dt> </dl>

 

 




