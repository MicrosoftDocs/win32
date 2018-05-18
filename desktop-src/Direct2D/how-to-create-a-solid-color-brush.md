---
title: How to Create a Solid Color Brush
description: Shows how to create a solid color brush using Direct2D.
ms.assetid: '70700b82-2294-46be-b1c0-fc89def441e2'
---

# How to Create a Solid Color Brush

To create a solid color brush, use the [**ID2DRenderTarget::CreateSolidColorBrush**](id2d1rendertarget-createsolidcolorbrush.md) method and specify the color with which you want to paint. Some of the **CreateSolidColorBrush** overloads also enable you to specify the opacity of the brush.

The following code shows how to create a solid yellow-green brush to fill a square, and a solid black brush to draw the outline of the square. The code produces the output shown in the following illustration.

![illustration of a rectangle filled with a solid yellow-green color](images/brushes-ovw-solidcolor.png)

1.  Declare two [**ID2D1SolidColorBrush**](id2d1rendertarget-createsolidcolorbrush-ref-color-f-ptr-ptr-id2d1solidcolorbrush.md) pointers: one for painting black and one for painting yellow green.
    ```C++
        ID2D1SolidColorBrush *m_pBlackBrush;
        ID2D1SolidColorBrush *m_pYellowGreenBrush;
    ```

    

2.  Call the [**CreateSolidColorBrush**](id2d1rendertarget-createsolidcolorbrush.md) method to create the brushes:
    ```C++
    if (SUCCEEDED(hr))
    {
        hr = m_pRenderTarget->CreateSolidColorBrush(
            D2D1::ColorF(D2D1::ColorF::Black, 1.0f),
            &amp;m_pBlackBrush
            );
    }

    // Create a solid color brush with its rgb value 0x9ACD32.
    if (SUCCEEDED(hr))
    {
        hr = m_pRenderTarget->CreateSolidColorBrush(
            D2D1::ColorF(D2D1::ColorF(0x9ACD32, 1.0f)),  
            &amp;m_pYellowGreenBrush
            );
    }
    ```

    

3.  Call the [**FillRectangle**](id2d1rendertarget-fillrectangle-ref-d2d-rect-f-ptr-id2d1brush.md) method to paint the interior of the rectangle with the yellow green brush and the [**DrawRectangle**](id2d1rendertarget-drawrectangle-ref-d2d-rect-f-ptr-id2d1brush-float-ptr-id2d1strokestyle.md) method to paint the outline of the rectangle with the black brush:
    ```C++
    m_pRenderTarget->FillRectangle(&amp;rcBrushRect, m_pYellowGreenBrush);
    m_pRenderTarget->DrawRectangle(&amp;rcBrushRect, m_pBlackBrush, 1, NULL);
    ```

    

## Related topics

<dl> <dt>

[Direct2D Reference](reference.md)
</dt> </dl>

 

 




