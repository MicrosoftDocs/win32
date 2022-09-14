---
description: The OnStartStreaming method resets all times that control streaming.
ms.assetid: a2bb07f2-6880-4030-96c5-d146982dfe66
title: CBaseVideoRenderer.OnStartStreaming method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseVideoRenderer.OnStartStreaming
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseVideoRenderer.OnStartStreaming method

The `OnStartStreaming` method resets all times that control streaming.

## Syntax


```C++
HRESULT OnStartStreaming();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value.

## Remarks

This member function overrides [**CBaseRenderer::OnStartStreaming**](cbaserenderer-onstartstreaming.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




