---
Description: The GetRenderEvent method retrieves the event that schedules rendering.
ms.assetid: da0272f6-6a1d-4c07-a907-822227b56305
title: CBaseRenderer.GetRenderEvent method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseRenderer.GetRenderEvent method

The `GetRenderEvent` method retrieves the event that schedules rendering.

## Syntax


```C++
CAMEvent* GetRenderEvent();
```



## Parameters

This method has no parameters.

## Return value

Returns a pointer to the [**CBaseRenderer::m\_RenderEvent**](cbaserenderer-m-renderevent.md) event.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




