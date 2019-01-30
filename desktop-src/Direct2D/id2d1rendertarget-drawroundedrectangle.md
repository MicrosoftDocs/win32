---
title: ID2D1RenderTarget DrawRoundedRectangle methods
description: Draws the outline of the specified rounded rectangle using the specified stroke style.
ms.assetid: 'd718c355-ffd8-4a7f-90f3-9a10d37a19c8'
keywords: ["DrawRoundedRectangle methods Direct2D"]
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
---

# ID2D1RenderTarget::DrawRoundedRectangle methods

Draws the outline of the specified rounded rectangle using the specified stroke style.

### Overload list



| Method                                                                                                                                                                                              | Description                                                                                       |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|
| [**DrawRoundedRectangle(D2D1\_ROUNDED\_RECT&,ID2D1Brush\*,FLOAT,ID2D1StrokeStyle\*)**](https://msdn.microsoft.com/en-us/library/Dd371910(v=VS.85).aspx)  | Draws the outline of the specified rounded rectangle using the specified stroke style.<br/> |
| [**DrawRoundedRectangle(D2D1\_ROUNDED\_RECT\*,ID2D1Brush\*,FLOAT,ID2D1StrokeStyle\*)**](https://msdn.microsoft.com/en-us/library/Dd371908(v=VS.85).aspx) | Draws the outline of the specified rounded rectangle using the specified stroke style.<br/> |



## Remarks

This method doesn't return an error code if it fails. To determine whether a drawing operation (such as **DrawRoundedRectangle**) failed, check the result returned by the [**ID2D1RenderTarget::EndDraw**](https://msdn.microsoft.com/en-us/library/Dd371924(v=VS.85).aspx) or [**ID2D1RenderTarget::Flush**](https://msdn.microsoft.com/en-us/library/Dd316801(v=VS.85).aspx) methods.

## Examples

The following example uses the **DrawRoundedRectangle** and [**FillRoundedRectangle**](https://msdn.microsoft.com/en-us/library/Dd742852(v=VS.85).aspx) methods to outline and fill a rounded rectangle. This example produces the output shown in the following illustration.

![illustration of four rounded rectangles with different stroke styles and fills](images/drawroundedrectangle-scr.png)


```C++
//  Called whenever the application needs to display the client
//  window.
HRESULT DrawAndFillRoundedRectangleExample::OnRender()
{
    HRESULT hr;

    // Create the render target and brushes if they
    // don't already exists.
    hr = CreateDeviceResources();

    if (SUCCEEDED(hr))
    {
        // Retrieve the size of the render target.
        D2D1_SIZE_F renderTargetSize = m_pRenderTarget->GetSize();

        m_pRenderTarget->BeginDraw();
        m_pRenderTarget->SetTransform(D2D1::Matrix3x2F::Identity());
        m_pRenderTarget->Clear(D2D1::ColorF(D2D1::ColorF::White));

        // Paint a grid background.
        m_pRenderTarget->FillRectangle(
            D2D1::RectF(0.0f, 0.0f, renderTargetSize.width, renderTargetSize.height),
            m_pGridPatternBitmapBrush
            );

        // Define a rounded rectangle.
        D2D1_ROUNDED_RECT roundedRect = D2D1::RoundedRect(
            D2D1::RectF(20.f, 20.f, 150.f, 100.f),
            10.f,
            10.f
            );

        // Draw the rectangle.
        m_pRenderTarget->DrawRoundedRectangle(roundedRect, m_pBlackBrush, 10.f);

        // Apply a translation transform.
        m_pRenderTarget->SetTransform(D2D1::Matrix3x2F::Translation(200.f, 0.f));

        // Draw the rounded rectangle again, this time with a dashed stroke.
        m_pRenderTarget->DrawRoundedRectangle(roundedRect, m_pBlackBrush, 10.f, m_pStrokeStyle);

        // Apply another translation transform.
        m_pRenderTarget->SetTransform(D2D1::Matrix3x2F::Translation(0.f, 150.f));

        // Draw, then fill the rounded rectangle.
        m_pRenderTarget->DrawRoundedRectangle(roundedRect, m_pBlackBrush, 10.f, m_pStrokeStyle);
        m_pRenderTarget->FillRoundedRectangle(roundedRect, m_pSilverBrush);

        // Apply another translation transform.
        m_pRenderTarget->SetTransform(D2D1::Matrix3x2F::Translation(200.f, 150.f));

        // Fill, then draw the rounded rectangle.
        m_pRenderTarget->FillRoundedRectangle(roundedRect, m_pSilverBrush);
        m_pRenderTarget->DrawRoundedRectangle(roundedRect, m_pBlackBrush, 10.f, m_pStrokeStyle);

        hr = m_pRenderTarget->EndDraw();

        if (hr == D2DERR_RECREATE_TARGET)
        {
            hr = S_OK;
            DiscardDeviceResources();
        }
    }

    return hr;
}
```



## Requirements



|                    |                                                                                     |
|--------------------|-------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D2d1.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1RenderTarget**](https://msdn.microsoft.com/en-us/library/Dd371260(v=VS.85).aspx)
</dt> <dt>

[How to Draw and Fill a Basic Shape](how-to-draw-an-ellipse.md)
</dt> <dt>

[**D2D1::RoundedRect**](https://msdn.microsoft.com/en-us/library/Dd316917(v=VS.85).aspx)
</dt> </dl>

�

�





