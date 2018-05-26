---
Description: The DoRenderSample method renders a sample.
ms.assetid: cf06192c-44c0-4d88-a20e-6501ea48cbfd
title: CBaseRenderer.DoRenderSample method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseRenderer.DoRenderSample method

The `DoRenderSample` method renders a sample.

## Syntax


```C++
virtual HRESULT DoRenderSample(
   IMediaSample *pMediaSample
) = 0;
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

The derived class must implement this method. The behavior depends entirely on the type of filter being implemented. A video renderer, for example, would draw the video image contained in the sample.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




