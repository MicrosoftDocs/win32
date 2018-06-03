---
Description: The OnReceiveFirstSample method is called when the filter receives a sample while paused.
ms.assetid: 5bd481bf-a62d-4d3c-b875-b94298d12730
title: CBaseRenderer.OnReceiveFirstSample method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CBaseRenderer.OnReceiveFirstSample method

The `OnReceiveFirstSample` method is called when the filter receives a sample while paused.

## Syntax


```C++
virtual void OnReceiveFirstSample(
   IMediaSample *pMediaSample
);
```



## Parameters

<dl> <dt>

*pMediaSample* 
</dt> <dd>

Pointer to the sample's [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The [**CBaseRenderer::Receive**](cbaserenderer-receive.md) method calls this method. It does nothing in the base class, but the derived class can override it. This method is intended primarily for video renderers. When a video renderer is paused, it typically displays the first sample as a still image.

Seeking the graph while paused also causes this method to be called.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




