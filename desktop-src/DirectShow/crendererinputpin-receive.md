---
Description: The Receive method receives the next media sample in the stream. This method overrides the CBaseInputPinReceive method.
ms.assetid: b09140f0-2e3a-47b1-ace7-954043dd62eb
title: CRendererInputPin.Receive method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Pointer to the sample's [**IMediaSample**](/windows/win32/Strmif/nn-strmif-imediasample?branch=master) interface.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This method calls the filter's [**CBaseRenderer::Receive**](cbaserenderer-receive.md) method, which handles the rendering. If that method fails, the pin sends an EC\_ERRORABORT event.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CRendererInputPin Class**](crendererinputpin.md)
</dt> </dl>

 

 




