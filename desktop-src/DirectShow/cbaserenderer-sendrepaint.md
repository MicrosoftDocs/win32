---
description: The SendRepaint method sends a repaint event to the filter graph manager.
ms.assetid: 78e5c46c-ca5d-4c5d-9dfc-992ce6b150ad
title: CBaseRenderer.SendRepaint method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.SendRepaint
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.SendRepaint method

The `SendRepaint` method sends a repaint event to the filter graph manager.

## Syntax


```C++
void SendRepaint();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method sends an [**EC\_REPAINT**](ec-repaint.md) event to the filter graph manager if the following conditions are true:

-   The input pin is connected.
-   The filter is not flushing data.
-   The end-of-stream was not reached.
-   The [**CBaseRenderer::m\_bAbort**](cbaserenderer-m-babort.md) flag is **FALSE**.
-   The [**CBaseRenderer::m\_bRepaintStatus**](cbaserenderer-m-brepaintstatus.md) flag is **TRUE**.

Depending on the state of the graph, the EC\_REPAINT event can cause the upstream filter to re-send a sample; the filter graph to seek to its current location; or the filter graph manager to pause momentarily. (See [**EC\_REPAINT**](ec-repaint.md).) This event is potentially inefficient, so it should be used sparingly. However, video renderers sometimes need to refresh the display.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




