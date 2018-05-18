---
Description: 'The OnStartStreaming method is called when the filter begins streaming.'
ms.assetid: '02a5b334-f6c4-4cba-8882-c6b36d97feb3'
title: 'CBaseRenderer.OnStartStreaming method'
---

# CBaseRenderer.OnStartStreaming method

The `OnStartStreaming` method is called when the filter begins streaming.

## Syntax


```C++
virtual HRESULT OnStartStreaming();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

The [**CBaseRenderer::StartStreaming**](cbaserenderer-startstreaming.md) method calls this method. It does nothing in the base class, but the derived class can override it.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




