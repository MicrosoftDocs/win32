---
description: The OnStopStreaming method is called when the filter stops streaming.
ms.assetid: d882fec8-09e1-4d36-a09c-44568e743da3
title: CBaseRenderer.OnStopStreaming method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.OnStopStreaming
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.OnStopStreaming method

The `OnStopStreaming` method is called when the filter stops streaming.

## Syntax


```C++
virtual HRESULT OnStopStreaming();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

The [**CBaseRenderer::StopStreaming**](cbaserenderer-stopstreaming.md) method calls this method. It does nothing in the base class, but the derived class can override it.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




