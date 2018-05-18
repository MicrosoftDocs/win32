---
Description: 'The Render method renders a sample.'
ms.assetid: '82b47777-2900-4821-ab79-1856da432832'
title: 'CBaseRenderer.Render method'
---

# CBaseRenderer.Render method

The `Render` method renders a sample.

## Syntax


```C++
virtual Render(
   IMediaSample *pMediaSample
);
```



## Parameters

<dl> <dt>

*pMediaSample* 
</dt> <dd>

Pointer to the sample's [**IMediaSample**](imediasample.md) interface.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those in the following table.



| Return code                                                                             | Description                                                      |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | The filter is stopped, or *pMediaSample* is **NULL**.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                                              |



 

## Remarks

This method calls the pure virtual method [**CBaseRenderer::DoRenderSample**](cbaserenderer-dorendersample.md), which does the real work. The derived class must implement **DoRenderSample**.

Immediately before calling **DoRenderSample**, this method calls the [**CBaseRenderer::OnRenderStart**](cbaserenderer-onrenderstart.md) method. Immediately after, it calls the [**CBaseRenderer::OnRenderEnd**](cbaserenderer-onrenderend.md) method. The derived class can override those two methods as needed.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




