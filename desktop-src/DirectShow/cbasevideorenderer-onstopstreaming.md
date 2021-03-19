---
description: The OnStopStreaming method is called at the end of streaming to fix times for the property page report.
ms.assetid: 92174edb-2f6c-4bad-91c5-769aaebcc495
title: CBaseVideoRenderer.OnStopStreaming method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseVideoRenderer.OnStopStreaming
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseVideoRenderer.OnStopStreaming method

The `OnStopStreaming` method is called at the end of streaming to fix times for the property page report.

## Syntax


```C++
HRESULT OnStopStreaming();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value.

## Remarks

This member function is called twice, once when pausing and again when the stream is actually stopped.

This member function overrides [**CBaseRenderer::OnStopStreaming**](cbaserenderer-onstopstreaming.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




