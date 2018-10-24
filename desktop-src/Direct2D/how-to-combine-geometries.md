---
title: How to Combine Geometries
description: Shows how to combine two geometries using Direct2D.
ms.assetid: c5413e59-ae73-4797-b4ad-3a78ad700634
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How to Combine Geometries

This topic describes how to combine two geometries. Direct2D supports four modes for combining geometries: Union, Intersect, XOR, and Exclude. These modes are specified in the [**D2D1\_COMBINE\_MODE**](/windows/desktop/api/d2d1/ne-d2d1-d2d1_combine_mode) enum type.

**To combine two geometries by using any of the four modes**

1.  Declare a path geometry: a variable of type [**ID2D1PathGeometry**](https://msdn.microsoft.com/en-us/library/Dd371512(v=VS.85).aspx) that will store the result of geometry combination.
2.  Declare a geometry sink: a variable of type [**ID2D1GeometrySink**](https://msdn.microsoft.com/en-us/library/Dd316592(v=VS.85).aspx) that will store the path geometry.
3.  Create the path geometry object by calling the [**ID2D1Factory::CreatePathGeometry**](https://msdn.microsoft.com/en-us/library/Dd371282(v=VS.85).aspx) method.
4.  Open the geometry sink object by calling the [**ID2D1PathGeometry::Open**](https://msdn.microsoft.com/en-us/library/Dd371522(v=VS.85).aspx) method.
5.  Use one of the four modes to combine the two geometries by calling the [**ID2D1EllipseGeometry::CombineWithGeometry**](https://msdn.microsoft.com/en-us/library/Dd316627(v=VS.85).aspx) method.
6.  Close the geometry sink object.

The following code declares the variables of type [**ID2D1PathGeometry**](https://msdn.microsoft.com/en-us/library/Dd371512(v=VS.85).aspx) and **ID2D1GeometrySink**.


```C++
    ID2D1PathGeometry *m_pPathGeometryUnion;
    ID2D1PathGeometry *m_pPathGeometryIntersect;
    ID2D1PathGeometry *m_pPathGeometryXOR;
    ID2D1PathGeometry *m_pPathGeometryExclude;
```



The following code uses each of the four modes to combine the two [**ID2D1EllipseGeometry**](https://msdn.microsoft.com/en-us/library/Dd371239(v=VS.85).aspx) objects and performs the following actions:

-   Creates two ellipses, m\_spEllipseGeometryOne and m\_spEllipseGeometryTwo.
-   Creates a path geometry object.
-   Opens a geometry sink object.
-   Combines the two ellipses.
-   Closes the geometry sink object.


```C++
HRESULT DemoApp::CreateGeometryResources()
{
    HRESULT hr = S_OK;
    ID2D1GeometrySink *pGeometrySink = NULL;

    // Create the first ellipse geometry to merge.
    const D2D1_ELLIPSE circle1 = D2D1::Ellipse(
        D2D1::Point2F(75.0f, 75.0f),
        50.0f,
        50.0f
        );

    hr = m_pD2DFactory->CreateEllipseGeometry(
        circle1,
        &m_pCircleGeometry1
        );

    if (SUCCEEDED(hr))
    {
        // Create the second ellipse geometry to merge.
        const D2D1_ELLIPSE circle2 = D2D1::Ellipse(
            D2D1::Point2F(125.0f, 75.0f),
            50.0f,
            50.0f
            );

        hr = m_pD2DFactory->CreateEllipseGeometry(circle2, &m_pCircleGeometry2);
    }


    if (SUCCEEDED(hr))
    {
        //
        // Use D2D1_COMBINE_MODE_UNION to combine the geometries.
        //
        hr = m_pD2DFactory->CreatePathGeometry(&m_pPathGeometryUnion);

        if (SUCCEEDED(hr))
        {
            hr = m_pPathGeometryUnion->Open(&pGeometrySink);

            if (SUCCEEDED(hr))
            {
                hr = m_pCircleGeometry1->CombineWithGeometry(
                    m_pCircleGeometry2,
                    D2D1_COMBINE_MODE_UNION,
                    NULL,
                    NULL,
                    pGeometrySink
                    );
            }

            if (SUCCEEDED(hr))
            {
                hr = pGeometrySink->Close();
            }

            SafeRelease(&pGeometrySink);
        }
    }

    if (SUCCEEDED(hr))
    {
        //
        // Use D2D1_COMBINE_MODE_INTERSECT to combine the geometries.
        //
        hr = m_pD2DFactory->CreatePathGeometry(&m_pPathGeometryIntersect);

        if (SUCCEEDED(hr))
        {
            hr = m_pPathGeometryIntersect->Open(&pGeometrySink);

            if (SUCCEEDED(hr))
            {
                hr = m_pCircleGeometry1->CombineWithGeometry(
                    m_pCircleGeometry2,
                    D2D1_COMBINE_MODE_INTERSECT,
                    NULL,
                    NULL,
                    pGeometrySink
                    );
            }

            if (SUCCEEDED(hr))
            {
                hr = pGeometrySink->Close();
            }

            SafeRelease(&pGeometrySink);
        }
    }

    if (SUCCEEDED(hr))
    {
        //
        // Use D2D1_COMBINE_MODE_XOR to combine the geometries.
        //
        hr = m_pD2DFactory->CreatePathGeometry(&m_pPathGeometryXOR);

        if (SUCCEEDED(hr))
        {
            hr = m_pPathGeometryXOR->Open(&pGeometrySink);

            if (SUCCEEDED(hr))
            {
                hr = m_pCircleGeometry1->CombineWithGeometry(
                    m_pCircleGeometry2,
                    D2D1_COMBINE_MODE_XOR,
                    NULL,
                    NULL,
                    pGeometrySink
                    );
            }

            if (SUCCEEDED(hr))
            {
                hr = pGeometrySink->Close();
            }

            SafeRelease(&pGeometrySink);
        }
    }

    if (SUCCEEDED(hr))
    {
        //
        // Use D2D1_COMBINE_MODE_EXCLUDE to combine the geometries.
        //
        hr = m_pD2DFactory->CreatePathGeometry(&m_pPathGeometryExclude);

        if (SUCCEEDED(hr))
        {
            hr = m_pPathGeometryExclude->Open(&pGeometrySink);

            if (SUCCEEDED(hr))
            {
                hr = m_pCircleGeometry1->CombineWithGeometry(
                    m_pCircleGeometry2,
                    D2D1_COMBINE_MODE_EXCLUDE,
                    NULL,
                    NULL,
                    pGeometrySink
                    );
            }

            if (SUCCEEDED(hr))
            {
                hr = pGeometrySink->Close();
            }

            SafeRelease(&pGeometrySink);
        }
    }

    return hr;
}
```



This code produces the output shown in the following illustration.

![illustration of two geometries and four modes for combining the geometries (union, intersection, xor, and exclude)](images/combine-modes.png)

## Related topics

<dl> <dt>

[**D2D1\_COMBINE\_MODE**](/windows/desktop/api/d2d1/ne-d2d1-d2d1_combine_mode)
</dt> <dt>

[**ID2D1EllipseGeometry**](https://msdn.microsoft.com/en-us/library/Dd371239(v=VS.85).aspx)
</dt> <dt>

[**ID2D1PathGeometry**](https://msdn.microsoft.com/en-us/library/Dd371512(v=VS.85).aspx)
</dt> <dt>

**ID2D1GeometrySink**
</dt> </dl>

 

 




