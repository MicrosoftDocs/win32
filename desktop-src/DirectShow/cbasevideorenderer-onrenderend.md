---
Description: The OnRenderEnd method performs smoothing for cases where the rendering time varies due to interruptions.
ms.assetid: 561b3306-0c41-4f04-b73a-78e7b4038e86
title: CBaseVideoRenderer.OnRenderEnd method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CBaseVideoRenderer.OnRenderEnd method

The `OnRenderEnd` method performs smoothing for cases where the rendering time varies due to interruptions.

## Syntax


```C++
void OnRenderEnd(
   IMediaSample *pMediaSample
);
```



## Parameters

<dl> <dt>

*pMediaSample* 
</dt> <dd>

Pointer to the media sample.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This member function should be called just after drawing an image.

This member function overrides [**CBaseRenderer::OnRenderEnd**](cbaserenderer-onrenderend.md).

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




