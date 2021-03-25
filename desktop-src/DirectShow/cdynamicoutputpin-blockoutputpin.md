---
description: The BlockOutputPin method blocks the pin.
ms.assetid: 49f6b8da-a8b2-482d-b70d-2c68a1b45a10
title: CDynamicOutputPin.BlockOutputPin method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDynamicOutputPin.BlockOutputPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDynamicOutputPin.BlockOutputPin method

The `BlockOutputPin` method blocks the pin. While the pin is blocked, the [**CDynamicOutputPin::StartUsingOutputPin**](cdynamicoutputpin-startusingoutputpin.md) method waits for the pin to become unblocked. The blocked state prevents the output pin from delivering samples, changing its output format, or reconnecting itself.

## Syntax


```C++
void BlockOutputPin();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

Before calling this method, hold the [**CDynamicOutputPin::m\_BlockStateLock**](cdynamicoutputpin-m-blockstatelock.md) critical section. Do not call this method if a streaming thread is using the pin, either to deliver data or to change the connection. To check whether a streaming thread is using the pin, call the [**CDynamicOutputPin::StreamingThreadUsingOutputPin**](cdynamicoutputpin-streamingthreadusingoutputpin.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 




