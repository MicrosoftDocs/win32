---
description: The SendNotifyWindow method notifies the upstream filter of the video window handle.
ms.assetid: f46390b1-d03a-4520-8c1d-b3f870d3bb0b
title: CBaseRenderer.SendNotifyWindow method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.SendNotifyWindow
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.SendNotifyWindow method

The `SendNotifyWindow` method notifies the upstream filter of the video window handle.

## Syntax


```C++
void SendNotifyWindow(
   IPin *pPin,
   HWND hwnd
);
```



## Parameters

<dl> <dt>

*pPin* 
</dt> <dd>

Pointer to the [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface of the upstream filter's output pin.

</dd> <dt>

*hwnd* 
</dt> <dd>

Handle to the video window, or **NULL**.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

If the output pin of the upstream filter supports the [**IMediaEventSink**](/windows/desktop/api/Strmif/nn-strmif-imediaeventsink) interface, this method sends it the [**EC\_NOTIFY\_WINDOW**](ec-notify-window.md) event code along with the window handle.

Video renderers can override their [**CBaseRenderer::CompleteConnect**](cbaserenderer-completeconnect.md) methods to call this method. It provides a mechanism for informing the upstream filter of the window handle. If you do this, override the [**CBaseRenderer::BreakConnect**](cbaserenderer-breakconnect.md) method as well, and call `SendNotifyWindow` with a **NULL** handle.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




