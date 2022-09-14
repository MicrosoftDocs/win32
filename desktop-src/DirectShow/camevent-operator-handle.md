---
description: Retrieves the event handle. This operator is not supported as an L-value.
ms.assetid: 9000d6d1-bbca-44ac-8808-0b3b827086c5
title: CAMEvent.operator HANDLE method (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMEvent.operator
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAMEvent.operator HANDLE method

Retrieves the event handle. This operator is not supported as an L-value.

## Syntax


```C++
 operator HANDLE() const;
```



## Parameters

This method has no parameters.

## Return value

Returns the [**CAMEvent::m\_hEvent**](camevent-m-hevent.md) member variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMEvent Class**](camevent.md)
</dt> </dl>

 

 




