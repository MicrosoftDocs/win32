---
description: The ThrottleWait method inserts a wait period after each frame.
ms.assetid: 69306093-f5db-4170-b30f-e33cfa448e9f
title: CBaseVideoRenderer.ThrottleWait method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseVideoRenderer.ThrottleWait
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseVideoRenderer.ThrottleWait method

The `ThrottleWait` method inserts a wait period after each frame.

## Syntax


```C++
void ThrottleWait();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This member function waits for a time period obtained from the **m\_trThrottle** data member.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




