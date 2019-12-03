---
title: ID2D1RenderTarget PushLayer methods (D2d1\_1.h)
description: Adds the specified layer to the render target so that it receives all subsequent drawing operations until PopLayer is called.
ms.assetid: 9336662c-e94e-40ba-adbe-066d704958bc
keywords:
- PushLayer methods Direct2D
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
ms.date: 07/02/2019
ms.topic: reference
---

# ID2D1RenderTarget::PushLayer methods

Adds the specified layer to the render target so that it receives all subsequent drawing operations until [**PopLayer**](https://msdn.microsoft.com/en-us/library/Dd316852(v=VS.85).aspx) is called.

### Overload list



| Method                                                                                                                            | Description                                                                                                                                                                     |
|:----------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PushLayer(D2D1\_LAYER\_PARAMETERS&,ID2D1Layer\*)**](https://msdn.microsoft.com/en-us/library/Dd316869(v=VS.85).aspx)  | Adds the specified layer to the render target so that it receives all subsequent drawing operations until [**PopLayer**](https://msdn.microsoft.com/en-us/library/Dd316852(v=VS.85).aspx) is called. <br/> |
| [**PushLayer(D2D1\_LAYER\_PARAMETERS\*,ID2D1Layer\*)**](https://msdn.microsoft.com/en-us/library/Dd316865(v=VS.85).aspx) | Adds the specified layer to the render target so that it receives all subsequent drawing operations until [**PopLayer**](https://msdn.microsoft.com/en-us/library/Dd316852(v=VS.85).aspx) is called. <br/> |



## Remarks

The [**PushLayer**](https://msdn.microsoft.com/en-us/library/Dd316869(v=VS.85).aspx) method enables a caller to begin redirecting rendering to a layer. All rendering operations are valid in a layer. The location of the layer is affected by the world transform set on the render target.

Each **PushLayer** must have a matching [**PopLayer**](https://msdn.microsoft.com/en-us/library/Dd316852(v=VS.85).aspx) call. If there are more **PopLayer** calls than **PushLayer** calls, the render target is placed into an error state. If [**Flush**](https://msdn.microsoft.com/en-us/library/Dd316801(v=VS.85).aspx) is called before all outstanding layers are popped, the render target is placed into an error state, and an error is returned. The error state can be cleared by a call to [**EndDraw**](https://msdn.microsoft.com/en-us/library/Dd371924(v=VS.85).aspx).

A particular [**ID2D1Layer**](https://msdn.microsoft.com/en-us/library/Dd371483(v=VS.85).aspx) resource can be active only at one time. In other words, you cannot call a [**PushLayer**](https://msdn.microsoft.com/en-us/library/Dd316869(v=VS.85).aspx) method, and then immediately follow with another **PushLayer** method with the same layer resource. Instead, you must call the second **PushLayer** method with different layer resources.

For an example, see [How to Clip a Region with Layers](how-to-clip-with-layers.md).

This method doesn't return an error code if it fails. To determine whether a drawing operation (such as **PushLayer**) failed, check the result returned by the [**ID2D1RenderTarget::EndDraw**](https://msdn.microsoft.com/en-us/library/Dd371924(v=VS.85).aspx) or [**ID2D1RenderTarget::Flush**](https://msdn.microsoft.com/en-us/library/Dd316801(v=VS.85).aspx) methods.

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



|                    |                                                                                                       |
|--------------------|-------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D2d1\_1.h (include D2d1.h)</dt> </dl> |
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl>                   |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl>                   |



## See also

<dl> <dt>

[**ID2D1RenderTarget**](https://msdn.microsoft.com/en-us/library/Dd371260(v=VS.85).aspx)
</dt> <dt>

[Layers Overview](direct2d-layers-overview.md)
</dt> </dl>

�

�





