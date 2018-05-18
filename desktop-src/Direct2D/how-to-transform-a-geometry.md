---
title: How to Transform a Geometry
description: Shows how to transform a geometry using Direct2D.
ms.assetid: 'de434615-14b1-4b66-b09b-e90468e03d58'
---

# How to Transform a Geometry

To transform a geometry, you can either apply the transform to the render target by calling [**SetTransform**](id2d1rendertarget-settransform.md) or apply the transform to the geometry by calling [**CreateTransformedGeometry**](id2d1factory-createtransformedgeometry.md). Although both approaches transform a geometry, they have some fundamental differences. **CreateTransformedGeometry** affects the fill, but does not affect the stroke width. Further, **CreateTransformedGeometry** transforms the geometry alone without impacting other shapes on the render target, whereas [**SetTransform**](id2d1brush-settransform.md) applies the transform to all shapes on the render target.

This how-to topic describes how to transform a geometry by calling [**CreateTransformedGeometry**](id2d1factory-createtransformedgeometry-ptr-id2d1geometry-ref-d2d-matrix-3x2-f-ptr-ptr-id2d1transformedgeometry.md).

**To transform a geometry**

1.  Declare an [**ID2D1TransformedGeometry**](id2d1transformedgeometry.md) variable.
2.  Call the [**CreateTransformedGeometry**](id2d1factory-createtransformedgeometry-ptr-id2d1geometry-ref-d2d-matrix-3x2-f-ptr-ptr-id2d1transformedgeometry.md) method to create a transformed geometry.

The following code shows how to create an hour glass, transform the hour glass, and draw the original and resulting hour glasses.


```C++
// Create a path geometry.
if (SUCCEEDED(hr))
{
    hr = m_pD2DFactory->CreatePathGeometry(&amp;m_pPathGeometry);

    if (SUCCEEDED(hr))
    {
        // Write to the path geometry using the geometry sink.
        hr = m_pPathGeometry->Open(&amp;pSink);

        if (SUCCEEDED(hr))
        {
            pSink->BeginFigure(
                D2D1::Point2F(0, 0),
                D2D1_FIGURE_BEGIN_FILLED
                );

            pSink->AddLine(D2D1::Point2F(200, 0));

            pSink->AddBezier(
                D2D1::BezierSegment(
                    D2D1::Point2F(150, 50),
                    D2D1::Point2F(150, 150),
                    D2D1::Point2F(200, 200))
                );

            pSink->AddLine(D2D1::Point2F(0, 200));

            pSink->AddBezier(
                D2D1::BezierSegment(
                    D2D1::Point2F(50, 150),
                    D2D1::Point2F(50, 50),
                    D2D1::Point2F(0, 0))
                );

            pSink->EndFigure(D2D1_FIGURE_END_CLOSED);

            hr = pSink->Close();
        }
        SafeRelease(&amp;pSink);
    }
}

if (SUCCEEDED(hr))
{
    // Create a transformed geometry which is tilted at an angle to the previous geometry
    hr = m_pD2DFactory->CreateTransformedGeometry(
        m_pPathGeometry,
        D2D1::Matrix3x2F::Rotation(
            45.f,
            D2D1::Point2F(100, 100)),
        &amp;m_pTransformedGeometry
        );
}
```



 

 




