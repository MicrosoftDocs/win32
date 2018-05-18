---
title: ID2D1Geometry CombineWithGeometry methods
description: Combines this geometry with the specified geometry and stores the result in an ID2D1SimplifiedGeometrySink.
ms.assetid: '5bb45c54-c551-4b54-ae91-41d2c57b9570'
keywords: ["CombineWithGeometry methods Direct2D"]
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
---

# ID2D1Geometry::CombineWithGeometry methods

Combines this geometry with the specified geometry and stores the result in an [**ID2D1SimplifiedGeometrySink**](id2d1simplifiedgeometrysink.md).

### Overload list



| Method                                                                                                                                                                                                                                                          | Description                                                                                                                                                    |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CombineWithGeometry(ID2D1Geometry\*,D2D1\_COMBINE\_MODE,D2D1\_MATRIX\_3X2\_F&,ID2D1SimplifiedGeometrySink\*)**](id2d1geometry-combinewithgeometry-ptr-id2d1geometry-d2d1-combine-mode-ref-d2d-matrix-3x2-f-ptr-id2d1simplifiedgeometrysink.md)              | Combines this geometry with the specified geometry and stores the result in an [**ID2D1SimplifiedGeometrySink**](id2d1simplifiedgeometrysink.md).<br/>  |
| [**CombineWithGeometry(ID2D1Geometry\*,D2D1\_COMBINE\_MODE,D2D1\_MATRIX\_3X2\_F\*,ID2D1SimplifiedGeometrySink\*)**](id2d1geometry-combinewithgeometry-ptr-id2d1geometry-d2d1-combine-mode-ptr-d2d-matrix-3x2-f-ptr-id2d1simplifiedgeometrysink.md)             | Combines this geometry with the specified geometry and stores the result in an [**ID2D1SimplifiedGeometrySink**](id2d1simplifiedgeometrysink.md).<br/>  |
| [**CombineWithGeometry(ID2D1Geometry\*,D2D1\_COMBINE\_MODE,D2D1\_MATRIX\_3X2\_F&,FLOAT,ID2D1SimplifiedGeometrySink\*)**](id2d1geometry-combinewithgeometry-ptr-id2d1geometry-d2d1-combine-mode-ref-d2d-matrix-3x2-f-float-ptr-id2d1simplifiedgeometrysink.md)  | Combines this geometry with the specified geometry and stores the result in an [**ID2D1SimplifiedGeometrySink**](id2d1simplifiedgeometrysink.md).<br/>  |
| [**CombineWithGeometry(ID2D1Geometry\*,D2D1\_COMBINE\_MODE,D2D1\_MATRIX\_3X2\_F\*,FLOAT,ID2D1SimplifiedGeometrySink\*)**](id2d1geometry-combinewithgeometry-ptr-id2d1geometry-d2d1-combine-mode-ptr-d2d-matrix-3x2-f-float-ptr-id2d1simplifiedgeometrysink.md) | Combines this geometry with the specified geometry and stores the result in an [**ID2D1SimplifiedGeometrySink**](id2d1simplifiedgeometrysink.md). <br/> |



## Examples

The following code uses each of the different combine modes to combine two [**ID2D1EllipseGeometry**](id2d1ellipsegeometry.md) objects.


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
        &amp;m_pCircleGeometry1
        );

    if (SUCCEEDED(hr))
    {
        // Create the second ellipse geometry to merge.
        const D2D1_ELLIPSE circle2 = D2D1::Ellipse(
            D2D1::Point2F(125.0f, 75.0f),
            50.0f,
            50.0f
            );

        hr = m_pD2DFactory->CreateEllipseGeometry(circle2, &amp;m_pCircleGeometry2);
    }


    if (SUCCEEDED(hr))
    {
        //
        // Use D2D1_COMBINE_MODE_UNION to combine the geometries.
        //
        hr = m_pD2DFactory->CreatePathGeometry(&amp;m_pPathGeometryUnion);

        if (SUCCEEDED(hr))
        {
            hr = m_pPathGeometryUnion->Open(&amp;pGeometrySink);

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

            SafeRelease(&amp;pGeometrySink);
        }
    }

    if (SUCCEEDED(hr))
    {
        //
        // Use D2D1_COMBINE_MODE_INTERSECT to combine the geometries.
        //
        hr = m_pD2DFactory->CreatePathGeometry(&amp;m_pPathGeometryIntersect);

        if (SUCCEEDED(hr))
        {
            hr = m_pPathGeometryIntersect->Open(&amp;pGeometrySink);

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

            SafeRelease(&amp;pGeometrySink);
        }
    }

    if (SUCCEEDED(hr))
    {
        //
        // Use D2D1_COMBINE_MODE_XOR to combine the geometries.
        //
        hr = m_pD2DFactory->CreatePathGeometry(&amp;m_pPathGeometryXOR);

        if (SUCCEEDED(hr))
        {
            hr = m_pPathGeometryXOR->Open(&amp;pGeometrySink);

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

            SafeRelease(&amp;pGeometrySink);
        }
    }

    if (SUCCEEDED(hr))
    {
        //
        // Use D2D1_COMBINE_MODE_EXCLUDE to combine the geometries.
        //
        hr = m_pD2DFactory->CreatePathGeometry(&amp;m_pPathGeometryExclude);

        if (SUCCEEDED(hr))
        {
            hr = m_pPathGeometryExclude->Open(&amp;pGeometrySink);

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

            SafeRelease(&amp;pGeometrySink);
        }
    }

    return hr;
}
```



This code produces the output shown in the following illustration.

![illustration of two ellipses combined by using four geometry combine modes (union, intersect, xor, and exclude)](images/combine-modes.png)

## Requirements



|                    |                                                                                     |
|--------------------|-------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1Geometry**](id2d1geometry.md)
</dt> </dl>

 

 





