---
title: D1111 Using Layer When Clip Is Sufficient
ms.assetid: '07fe3c66-15be-408b-a30b-a7f52919c058'
description: 
keywords: ["D1111 Using Layer When Clip Is Sufficient Direct2D"]
topic_type:
- apiref
api_name:
- D1111 Using Layer When Clip Is Sufficient
api_type:
- NA
---

# D1111: Using Layer When Clip Is Sufficient

PERF - A layer is being used with a **NULL** opacity mask, 1.0 opacity, and an axis aligned rectangular geometric mask. The Push/Pop Clip API should achieve the same results with higher performance.

## Placeholders

<dl> <dt>

<span id="interface"></span><span id="INTERFACE"></span>*interface*
</dt> <dd>

The address of the interface.

</dd> </dl> 

|             |             |
|-------------|-------------|
| Error Level | Information |



 

## Examples

The following code uses the [**PushLayer**](id2d1rendertarget-push-layer.md) and [**PopLayer**](id2d1rendertarget-poplayer.md) when the layer contains only one primitive (a rectangle) and the fields of the [**D2D1\_LAYER\_PARAMETERS**](d2d1-layer-parameters.md) structure are set to defaults. For the default values of the **D2D1\_LAYER\_PARAMETERS** structure, see [**LayerParameter**](layerparameters.md).


```C++
        ID2D1Layer *m_pLayer;

        hr = m_pRenderTarget->CreateLayer(D2D1::SizeF(100, 100), &amp;m_pLayer);
        m_pRenderTarget->PushLayer(D2D1::LayerParameters(), m_pLayer);
        m_pRenderTarget->FillRectangle(D2D1::RectF(100, 50, 400, 160), m_pBlackBrush);
        m_pRenderTarget->PopLayer();
```



This example produces the following debug message:

``` syntax
DEBUG INFO - PERF - A layer is being used with a NULL opacity mask, 1.0 opacity, 
            and an axis aligned rectangular geometric mask.  
            The Push/Pop Clip API should achieve the same results with higher performance.
```

## Possible Causes

A layer was used when the [**PushAxisAlignedClip**](id2d1rendertarget-pushaxisalignedclip-ref-d2d-rect-f-d2d1-antialias-mode.md) and [**PopAxisAlignedClip**](id2d1rendertarget-popaxisalignedclip.md) methods would have sufficed.

 

 




