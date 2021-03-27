---
description: The OnWaitStart method updates times spent waiting and not waiting.
ms.assetid: 3f2e2bf2-f205-4b59-b969-cf8c2136437d
title: CBaseVideoRenderer.OnWaitStart method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseVideoRenderer.OnWaitStart
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseVideoRenderer.OnWaitStart method

The `OnWaitStart` method updates times spent waiting and not waiting.

## Syntax


```C++
void OnWaitStart();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This member function is called when starting to wait for a rendering event. It is used only for performance measurements.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




