---
Description: The Active method is called when the state is switched to paused or running.
ms.assetid: 2913bc81-572d-4ee1-a1b6-9e1638e04c9d
title: CBaseRenderer.Active method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CBaseRenderer.Active method

The `Active` method is called when the state is switched to paused or running.

## Syntax


```C++
virtual HRESULT Active();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

The input pin calls this method from its own [**CRendererInputPin::Active**](crendererinputpin-active.md) method. This method does nothing in the base class.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




