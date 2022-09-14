---
description: The NotReady method signals that a state transition is not yet complete.
ms.assetid: 85529a22-5343-4c22-b282-31c0e7ff0f5f
title: CBaseRenderer.NotReady method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.NotReady
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.NotReady method

The `NotReady` method signals that a state transition is not yet complete.

## Syntax


```C++
void NotReady();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method causes the [**CBaseRenderer::GetState**](cbaserenderer-getstate.md) method to return VFW\_S\_STATE\_INTERMEDIATE, which indicates that the filter is still transitioning to its current state. The filter calls this method whenever a state transition is pending. (This occurs when the filter pauses, until it receives a sample.)

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> <dt>

[**CheckReady**](cbaserenderer-checkready.md)
</dt> <dt>

[**Ready**](cbaserenderer-ready.md)
</dt> </dl>

 

 




