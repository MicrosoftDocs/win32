---
description: The OnWaitEnd method is called when a wait time ends.
ms.assetid: 283627bb-599c-4711-abc4-b5f92dfd29a5
title: CBaseVideoRenderer.OnWaitEnd method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseVideoRenderer.OnWaitEnd
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseVideoRenderer.OnWaitEnd method

The OnWaitEnd method is called when a wait time ends.

## Syntax


```C++
void OnWaitEnd();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This member function does only performance logging. It is called when the thread is awoken from waiting in the window, or when the next sample is due to be rendered. It could eventually be used to gather information that controls synchronization.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




