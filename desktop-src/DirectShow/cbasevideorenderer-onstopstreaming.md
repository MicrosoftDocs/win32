---
Description: 'The OnStopStreaming method is called at the end of streaming to fix times for the property page report.'
ms.assetid: '92174edb-2f6c-4bad-91c5-769aaebcc495'
title: 'CBaseVideoRenderer.OnStopStreaming method'
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



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




