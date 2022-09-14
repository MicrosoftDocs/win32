---
description: The StreamingThreadUsingOutputPin method determines whether any thread is performing a streaming operation on the pin.
ms.assetid: b6432a11-4e8b-4eb4-ad8e-aaff9398641b
title: CDynamicOutputPin.StreamingThreadUsingOutputPin method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDynamicOutputPin.StreamingThreadUsingOutputPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDynamicOutputPin.StreamingThreadUsingOutputPin method

The StreamingThreadUsingOutputPin method determines whether any thread is performing a streaming operation on the pin.

## Syntax


```C++
virtual bool StreamingThreadUsingOutputPin();
```



## Parameters

This method has no parameters.

## Return value

Returns **TRUE** if a thread is performing a streaming operation on the pin. Otherwise, returns **FALSE**.

## Remarks

If any threads have successfully returned from the [**CDynamicOutputPin::StartUsingOutputPin**](cdynamicoutputpin-startusingoutputpin.md) method and have not made a corresponding call to the [**CDynamicOutputPin::StopUsingOutputPin**](cdynamicoutputpin-stopusingoutputpin.md) method, this method returns **TRUE**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 




