---
Description: 'The ResetEndOfStream method resets the end-of-stream flags.'
ms.assetid: '80f6d49b-a825-4c3c-b693-7b1d9298f541'
title: 'CBaseRenderer.ResetEndOfStream method'
---

# CBaseRenderer.ResetEndOfStream method

The `ResetEndOfStream` method resets the end-of-stream flags.

## Syntax


```C++
virtual HRESULT ResetEndOfStream();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

This method clears the previous end-of-stream condition. At that point, the filter can receive new data. The [**CBaseRenderer::Stop**](cbaserenderer-stop.md) and [**CBaseRenderer::BeginFlush**](cbaserenderer-beginflush.md) methods call this method.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




