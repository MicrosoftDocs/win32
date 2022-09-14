---
description: The WaitForReceiveToComplete method waits for the CBaseRenderer::Receive method to complete.
ms.assetid: 3c722680-e54b-4ba1-8e98-36647cd027bc
title: CBaseRenderer.WaitForReceiveToComplete method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.WaitForReceiveToComplete
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.WaitForReceiveToComplete method

The `WaitForReceiveToComplete` method waits for the [**CBaseRenderer::Receive**](cbaserenderer-receive.md) method to complete.

## Syntax


```C++
void WaitForReceiveToComplete();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The [**CBaseRenderer::Stop**](cbaserenderer-stop.md) and [**CBaseRenderer::BeginFlush**](cbaserenderer-beginflush.md) methods call this method to synchronize the state change with the **Receive** method.

Specifically, this method dispatches messages while it waits for the [**CBaseRenderer::m\_bInReceive**](cbaserenderer-m-binreceive.md) flag to become **FALSE**. The flag becomes **TRUE** in the [**CBaseRenderer::PrepareReceive**](cbaserenderer-preparereceive.md) method and switches back to **FALSE** after the **Receive** method calls the [**CBaseRenderer::PrepareRender**](cbaserenderer-preparerender.md) method. The derived class can use **PrepareRender** to set the palette. Waiting for **PrepareRender** to complete ensures that palette-change messages are dispatched before the state change occurs. This avoids a potential deadlock.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




