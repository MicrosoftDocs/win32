---
title: ID2D1RenderTarget CreateLayer methods (D2d1.h)
description: Creates a layer resource that can be used with this render target and its compatible render targets.
ms.assetid: 074e9ffb-c5f2-4e7b-94c7-d457bf07c0b7
keywords:
- CreateLayer methods Direct2D
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
ms.date: 07/02/2019
ms.topic: reference
---

# ID2D1RenderTarget::CreateLayer methods

Creates a layer resource that can be used with this render target and its compatible render targets.

### Overload list



| Method                                                                                                                 | Description                                                                                                                                                    |
|:-----------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateLayer(ID2D1Layer\*\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-createlayer(id2d1layer))                                | Creates a layer resource that can be used with this render target and its compatible render targets. <br/>                                               |
| [**CreateLayer(D2D1\_SIZE\_F,ID2D1Layer\*\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-createlayer(d2d1_size_f_id2d1layer))       | Creates a layer resource that can be used with this render target and its compatible render targets. The new layer has the specified initial size. <br/> |
| [**CreateLayer(D2D1\_SIZE\_F\*,ID2D1Layer\*\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-createlayer(d2d1_size_f_id2d1layer)) | Creates a layer resource that can be used with this render target and its compatible render targets. The new layer has the specified initial size. <br/> |



## Remarks

The layer automatically resizes itself, as needed.

## Examples

The following example uses a layer to clip a bitmap to a geometric mask. For the complete example, see [How to Clip to a Geometric Mask](how-to-clip-with-layers.md).


```C++
HRESULT DemoApp::RenderWithLayer(ID2D1RenderTarget *pRT)
{
    HRESULT hr = S_OK;

    // Create a layer.
    ID2D1Layer *pLayer = NULL;
    hr = pRT->CreateLayer(NULL, &amp;pLayer);

    if (SUCCEEDED(hr))
    {
        pRT->SetTransform(D2D1::Matrix3x2F::Translation(350, 50));

        // Push the layer with the geometric mask.
        pRT->PushLayer(
            D2D1::LayerParameters(D2D1::InfiniteRect(), m_pPathGeometry),
            pLayer
            );
            
  
        pRT->DrawBitmap(m_pOrigBitmap, D2D1::RectF(0, 0, 200, 133));
        pRT->FillRectangle(D2D1::RectF(0.f, 0.f, 25.f, 25.f), m_pSolidColorBrush);  
        pRT->FillRectangle(D2D1::RectF(25.f, 25.f, 50.f, 50.f), m_pSolidColorBrush);
        pRT->FillRectangle(D2D1::RectF(50.f, 50.f, 75.f, 75.f), m_pSolidColorBrush); 
        pRT->FillRectangle(D2D1::RectF(75.f, 75.f, 100.f, 100.f), m_pSolidColorBrush);    
        pRT->FillRectangle(D2D1::RectF(100.f, 100.f, 125.f, 125.f), m_pSolidColorBrush); 
        pRT->FillRectangle(D2D1::RectF(125.f, 125.f, 150.f, 150.f), m_pSolidColorBrush);    
        

        pRT->PopLayer();
    }

    SafeRelease(&amp;pLayer);

    return hr;
}
```



## Requirements



| Requirement | Value |
|--------------------|-------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D2d1.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[Layers Overview](direct2d-layers-overview.md)
</dt> <dt>

[**ID2D1RenderTarget**](/windows/win32/api/d2d1/nn-d2d1-id2d1rendertarget)
</dt> </dl>

�

�
