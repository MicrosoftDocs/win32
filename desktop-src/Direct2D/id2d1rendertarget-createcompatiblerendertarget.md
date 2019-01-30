---
title: ID2D1RenderTarget CreateCompatibleRenderTarget methods
description: Creates a new bitmap render target for use during intermediate offscreen drawing that is compatible with the current render target .
ms.assetid: '4a799a7c-0d2f-460f-99f9-24c6cf7c4537'
keywords: ["CreateCompatibleRenderTarget methods Direct2D"]
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
---

# ID2D1RenderTarget::CreateCompatibleRenderTarget methods

Creates a new bitmap render target for use during intermediate offscreen drawing that is compatible with the current render target .

### Overload list



| Method                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                            |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateCompatibleRenderTarget(D2D1\_SIZE\_F,D2D1\_SIZE\_U,D2D1\_PIXEL\_FORMAT,D2D1\_COMPATIBLE\_RENDER\_TARGET\_OPTIONS,ID2D1BitmapRenderTarget\*\*)**](https://msdn.microsoft.com/en-us/library/Dd371811(v=VS.85).aspx)       | Creates a bitmap render target for use during intermediate offscreen drawing that is compatible with the current render target.<br/>                                                                                                             |
| [**CreateCompatibleRenderTarget(D2D1\_SIZE\_F\*,D2D1\_SIZE\_U\*,D2D1\_PIXEL\_FORMAT\*,D2D1\_COMPATIBLE\_RENDER\_TARGET\_OPTIONS,ID2D1BitmapRenderTarget\*\*)**](https://msdn.microsoft.com/en-us/library/Dd371822(v=VS.85).aspx) | Creates a bitmap render target for use during intermediate offscreen drawing that is compatible with the current render target. <br/>                                                                                                            |
| [**CreateCompatibleRenderTarget(ID2D1BitmapRenderTarget\*\*)**](https://msdn.microsoft.com/en-us/library/Dd371825(v=VS.85).aspx)                                                                                                 | Creates a new bitmap render target for use during intermediate offscreen drawing that is compatible with the current render target and has the same size, DPI, and pixel format (but not alpha mode) as the current render target. <br/>         |
| [**CreateCompatibleRenderTarget(D2D1\_SIZE\_F,ID2D1BitmapRenderTarget\*\*)**](https://msdn.microsoft.com/en-us/library/Dd371819(v=VS.85).aspx)                                                                                   | Creates a new bitmap render target for use during intermediate offscreen drawing that is compatible with the current render target and has the same pixel format (but not alpha mode) as the current render target. <br/>                        |
| [**CreateCompatibleRenderTarget(D2D1\_SIZE\_F,D2D1\_SIZE\_U,ID2D1BitmapRenderTarget\*\*)**](https://msdn.microsoft.com/en-us/library/Dd371817(v=VS.85).aspx)                                                                     | Creates a bitmap render target for use during intermediate off-screen drawing that is compatible with the current render target. The new bitmap render target has the same pixel format (but not alpha mode) as the current render target. <br/> |
| [**CreateCompatibleRenderTarget(D2D1\_SIZE\_F,D2D1\_SIZE\_U,D2D1\_PIXEL\_FORMAT,ID2D1BitmapRenderTarget\*\*)**](https://msdn.microsoft.com/en-us/library/Dd371814(v=VS.85).aspx)                                                 | Creates a bitmap render target for use during intermediate offscreen drawing that is compatible with the current render target. <br/>                                                                                                            |



## Examples

The following example uses the **CreateCompatibleRenderTarget** method to create an [**ID2D1BitmapRenderTarget**](https://msdn.microsoft.com/en-us/library/Dd371146(v=VS.85).aspx) and uses it to draw a grid pattern. The grid pattern is used as the source of an [**ID2D1BitmapBrush**](https://msdn.microsoft.com/en-us/library/Dd371122(v=VS.85).aspx).


```C++
HRESULT DemoApp::CreateGridPatternBrush(
    ID2D1RenderTarget *pRenderTarget,
    ID2D1BitmapBrush **ppBitmapBrush
    )
{
    // Create a compatible render target.
    ID2D1BitmapRenderTarget *pCompatibleRenderTarget = NULL;
    HRESULT hr = pRenderTarget->CreateCompatibleRenderTarget(
        D2D1::SizeF(10.0f, 10.0f),
        &amp;pCompatibleRenderTarget
        );
    if (SUCCEEDED(hr))
    {
        // Draw a pattern.
        ID2D1SolidColorBrush *pGridBrush = NULL;
        hr = pCompatibleRenderTarget->CreateSolidColorBrush(
            D2D1::ColorF(D2D1::ColorF(0.93f, 0.94f, 0.96f, 1.0f)),
            &amp;pGridBrush
            );
        if (SUCCEEDED(hr))
        {
            pCompatibleRenderTarget->BeginDraw();
            pCompatibleRenderTarget->FillRectangle(D2D1::RectF(0.0f, 0.0f, 10.0f, 1.0f), pGridBrush);
            pCompatibleRenderTarget->FillRectangle(D2D1::RectF(0.0f, 0.1f, 1.0f, 10.0f), pGridBrush);
            pCompatibleRenderTarget->EndDraw();

            // Retrieve the bitmap from the render target.
            ID2D1Bitmap *pGridBitmap = NULL;
            hr = pCompatibleRenderTarget->GetBitmap(&amp;pGridBitmap);
            if (SUCCEEDED(hr))
            {
                // Choose the tiling mode for the bitmap brush.
                D2D1_BITMAP_BRUSH_PROPERTIES brushProperties =
                    D2D1::BitmapBrushProperties(D2D1_EXTEND_MODE_WRAP, D2D1_EXTEND_MODE_WRAP);

                // Create the bitmap brush.
                hr = m_pRenderTarget->CreateBitmapBrush(pGridBitmap, brushProperties, ppBitmapBrush);

                pGridBitmap->Release();
            }

            pGridBrush->Release();
        }

        pCompatibleRenderTarget->Release();
    }

    return hr;
}
```



The following code example uses the brush to paint a pattern.


```C++
// Paint a grid background.
m_pRenderTarget->FillRectangle(
    D2D1::RectF(0.0f, 0.0f, renderTargetSize.width, renderTargetSize.height),
    m_pGridPatternBitmapBrush
    );
```



Code has been omitted from this example.

## Requirements



|                    |                                                                                     |
|--------------------|-------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D2d1.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1RenderTarget**](https://msdn.microsoft.com/en-us/library/Dd371260(v=VS.85).aspx)
</dt> </dl>

�

�





