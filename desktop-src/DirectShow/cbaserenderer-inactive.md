---
Description: The Inactive method is called when the state is switched to stopped.
ms.assetid: 2bad81ef-d2a4-4c20-a49b-e40e5097b430
title: CBaseRenderer.Inactive method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseRenderer.Inactive method

The `Inactive` method is called when the state is switched to stopped.

## Syntax


```C++
virtual HRESULT Inactive();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

The input pin calls this method from its own [**CRendererInputPin::Inactive**](crendererinputpin-inactive.md) method. The filter calls the [**CBaseRenderer::ClearPendingSample**](cbaserenderer-clearpendingsample.md) method to release the most recent sample.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




