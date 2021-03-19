---
description: The Receive method receives the next media sample in the stream. This method overrides the CBaseInputPin::Receive method.
ms.assetid: b09140f0-2e3a-47b1-ace7-954043dd62eb
title: CRendererInputPin.Receive method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRendererInputPin.Receive
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CRendererInputPin.Receive method

The `Receive` method receives the next media sample in the stream. This method overrides the [**CBaseInputPin::Receive**](cbaseinputpin-receive.md) method.

## Syntax


```C++
HRESULT Receive(
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

Returns an **HRESULT** value.

## Remarks

This method calls the filter's [**CBaseRenderer::Receive**](cbaserenderer-receive.md) method, which handles the rendering. If that method fails, the pin sends an EC\_ERRORABORT event.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CRendererInputPin Class**](crendererinputpin.md)
</dt> </dl>

 

 




