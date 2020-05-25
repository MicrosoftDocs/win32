---
title: How to Create a Linear Gradient Brush
description: Shows how to create a linear gradient brush using Direct2D.
ms.assetid: 3cf5acc6-2f17-49d4-aca5-a84a846d1749
ms.topic: article
ms.date: 05/31/2018
ms.custom: "seodec18"
---

# How to Create a Linear Gradient Brush

To create a linear gradient brush, use the [**CreateLinearGradientBrush**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-createlineargradientbrush(constd2d1_linear_gradient_brush_properties__id2d1gradientstopcollection_id2d1lineargradientbrush)) method and specify the linear gradient brush properties and the gradient stop collection. Some overloads enable you to specify the brush properties. The following code shows how to create a linear gradient brush to fill a circle, and a solid black brush to draw the outline of the circle.

The code produces the output shown in the following illustration.

![illustration of a square filled with a linear gradient brush](images/brushes-ovw-lineargradient.png)

1.  Declare a variable of type [**ID2D1LinearGradientBrush**](https://msdn.microsoft.com/library/Dd371488(v=VS.85).aspx).
    ```C++
        ID2D1LinearGradientBrush *m_pLinearGradientBrush;
    ```

    

2.  Use the [**ID2D1RenderTarget::CreateGradientStopCollection**](https://msdn.microsoft.com/library/Dd371832(v=VS.85).aspx) method to create the [**ID2D1GradientStopCollection**](https://msdn.microsoft.com/library/Dd316783(v=VS.85).aspx) collection with a declared array of [**D2D1\_GRADIENT\_STOP**](/windows/desktop/api/d2d1/ns-d2d1-d2d1_gradient_stop) structures, as shown in the following code.
    > [!Note]  
    > Starting with Windows 8, you can use the [**ID2D1DeviceContext::CreateGradientStopCollection**](https://msdn.microsoft.com/library/Hh404502(v=VS.85).aspx) method to create a [**ID2D1GradientStopCollection1**](https://msdn.microsoft.com/library/Hh446792(v=VS.85).aspx) collection instead. This interface adds high-color gradients and the interpolation of gradients in either straight or prmultiplied colors. See the **ID2DDeviceContext::CreateGradientStopCollection** page for more information.

     

    ```C++
    // Create an array of gradient stops to put in the gradient stop
    // collection that will be used in the gradient brush.
    ID2D1GradientStopCollection *pGradientStops = NULL;

    D2D1_GRADIENT_STOP gradientStops[2];
    gradientStops[0].color = D2D1::ColorF(D2D1::ColorF::Yellow, 1);
    gradientStops[0].position = 0.0f;
    gradientStops[1].color = D2D1::ColorF(D2D1::ColorF::ForestGreen, 1);
    gradientStops[1].position = 1.0f;
    // Create the ID2D1GradientStopCollection from a previously
    // declared array of D2D1_GRADIENT_STOP structs.
    hr = m_pRenderTarget->CreateGradientStopCollection(
        gradientStops,
        2,
        D2D1_GAMMA_2_2,
        D2D1_EXTEND_MODE_CLAMP,
        &pGradientStops
        );
    ```

    

3.  Use the [**ID2D1RenderTarget::CreateLinearGradientBrush**](https://docs.microsoft.com/windows/desktop/api/d2d1/nf-d2d1-id2d1rendertarget-createlineargradientbrush(constd2d1_linear_gradient_brush_properties__constd2d1_brush_properties__id2d1gradientstopcollection_id2d1lineargradientbrush)) to create a linear gradient brush, fill the square with the brush, and draw the square with the black color brush.
    ```C++
    // The line that determines the direction of the gradient starts at
    // the upper-left corner of the square and ends at the lower-right corner.

    if (SUCCEEDED(hr))
    {
        hr = m_pRenderTarget->CreateLinearGradientBrush(
            D2D1::LinearGradientBrushProperties(
                D2D1::Point2F(0, 0),
                D2D1::Point2F(150, 150)),
            pGradientStops,
            &m_pLinearGradientBrush
            );
    }
    ```

    

    ```C++
    m_pRenderTarget->FillRectangle(&rcBrushRect, m_pLinearGradientBrush);
    m_pRenderTarget->DrawRectangle(&rcBrushRect, m_pBlackBrush, 1, NULL);
    ```

    

## Related topics

<dl> <dt>

[Direct2D Reference](reference.md)
</dt> </dl>

 

 




