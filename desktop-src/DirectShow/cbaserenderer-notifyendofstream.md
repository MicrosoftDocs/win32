---
description: The NotifyEndOfStream method posts an EC\_COMPLETE event to the filter graph manager.
ms.assetid: 9eec5b65-654d-4b2e-be39-93225a7674a5
title: CBaseRenderer.NotifyEndOfStream method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.NotifyEndOfStream
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.NotifyEndOfStream method

The `NotifyEndOfStream` method posts an [**EC\_COMPLETE**](ec-complete.md) event to the filter graph manager.

## Syntax


```C++
void NotifyEndOfStream();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> <dt>

[**CBaseRenderer::EndOfStream**](cbaserenderer-endofstream.md)
</dt> <dt>

[**CBaseRenderer::SendEndOfStream**](cbaserenderer-sendendofstream.md)
</dt> </dl>

 

 




