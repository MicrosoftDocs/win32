---
description: The Ready method signals that a state transition is complete.
ms.assetid: 01328281-cf25-43fd-9f9c-e55fccbac217
title: CBaseRenderer.Ready method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.Ready
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.Ready method

The `Ready` method signals that a state transition is complete.

## Syntax


```C++
void Ready();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method causes the [**CBaseRenderer::GetState**](cbaserenderer-getstate.md) method to return S\_OK, which indicates that the filter has completed the transition to its current state. The filter calls this method whenever it completes a state transition.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> <dt>

[**CBaseRenderer::CheckReady**](cbaserenderer-checkready.md)
</dt> <dt>

[**CBaseRenderer::NotReady**](cbaserenderer-notready.md)
</dt> </dl>

 

 




