---
Description: The IsEndOfStreamDelivered method queries whether the EC\_COMPLETE event has been delivered to the filter graph manager.
ms.assetid: 13138626-35b0-4da1-9c7e-5d22d86ad2e3
title: CBaseRenderer.IsEndOfStreamDelivered method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseRenderer.IsEndOfStreamDelivered method

The `IsEndOfStreamDelivered` method queries whether the EC\_COMPLETE event has been delivered to the filter graph manager.

## Syntax


```C++
BOOL IsEndOfStreamDelivered();
```



## Parameters

This method has no parameters.

## Return value

Returns the [**CBaseRenderer::m\_bEOSDelivered**](cbaserenderer-m-beosdelivered.md) flag.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




