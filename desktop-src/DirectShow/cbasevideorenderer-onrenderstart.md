---
description: The OnRenderStart method sets information for rendering.
ms.assetid: 698fe778-e2cb-4b87-a668-084b6c12c71f
title: CBaseVideoRenderer.OnRenderStart method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseVideoRenderer.OnRenderStart
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseVideoRenderer.OnRenderStart method

The `OnRenderStart` method sets information for rendering.

## Syntax


```C++
void OnRenderStart(
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

This member function retrieves the current clock time from the system and stores it in a member variable to be used when the drawing is complete. The function also performs performance logging. This member function should be called just before drawing starts.

This member function overrides [**CBaseRenderer::OnRenderStart**](cbaserenderer-onrenderstart.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseVideoRenderer Class**](cbasevideorenderer.md)
</dt> </dl>

 

 




