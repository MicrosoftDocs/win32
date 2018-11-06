---
title: How to Create a Solid Color Brush
description: Shows how to create a solid color brush using Direct2D.
ms.assetid: 70700b82-2294-46be-b1c0-fc89def441e2
ms.topic: article
ms.date: 05/31/2018
---

# How to Create a Solid Color Brush

To create a solid color brush, use the [**ID2DRenderTarget::CreateSolidColorBrush**](/windows/desktop/api/d2d1/nf-d2d1-createsolidcolorbrush) method and specify the color with which you want to paint. Some of the **CreateSolidColorBrush** overloads also enable you to specify the opacity of the brush.

The following code shows how to create a solid yellow-green brush to fill a square, and a solid black brush to draw the outline of the square. The code produces the output shown in the following illustration.

![illustration of a rectangle filled with a solid yellow-green color](images/brushes-ovw-solidcolor.png)

1.  Declare two [**ID2D1SolidColorBrush**](https://msdn.microsoft.com/en-us/library/Dd371871(v=VS.85).aspx) pointers: one for painting black and one for painting yellow green.
    ```C++
        ID2D1SolidColorBrush *m_pBlackBrush;
        ID2D1SolidColorBrush *m_pYellowGreenBrush;
    ```

    

2.  Call the [**CreateSolidColorBrush**](/windows/desktop/api/d2d1/nf-d2d1-createsolidcolorbrush) method to create the brushes:
    ```C++
    if (SUCCEEDED(hr))
    {
        hr = m_pRenderTarget->CreateSolidColorBrush(
            D2D1::ColorF(D2D1::ColorF::Black, 1.0f),
            &m_pBlackBrush
            );
    }

    // Create a solid color brush with its rgb value 0x9ACD32.
    if (SUCCEEDED(hr))
    {
        hr = m_pRenderTarget->CreateSolidColorBrush(
            D2D1::ColorF(D2D1::ColorF(0x9ACD32, 1.0f)),  
            &m_pYellowGreenBrush
            );
    }
    ```

    

3.  Call the [**FillRectangle**](https://msdn.microsoft.com/en-us/library/Dd371954(v=VS.85).aspx) method to paint the interior of the rectangle with the yellow green brush and the [**DrawRectangle**](https://msdn.microsoft.com/en-us/library/Dd371902(v=VS.85).aspx) method to paint the outline of the rectangle with the black brush:
    ```C++
    m_pRenderTarget->FillRectangle(&rcBrushRect, m_pYellowGreenBrush);
    m_pRenderTarget->DrawRectangle(&rcBrushRect, m_pBlackBrush, 1, NULL);
    ```

    

## Related topics

<dl> <dt>

[Direct2D Reference](reference.md)
</dt> </dl>

 

 




