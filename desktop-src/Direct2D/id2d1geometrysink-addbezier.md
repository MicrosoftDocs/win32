---
title: ID2D1GeometrySink AddBezier methods (D2d1.h)
description: Creates a cubic Bezier curve between the current point and the specified end point and adds it to the geometry sink.
ms.assetid: d1e228eb-dac6-485d-b3c9-69b2bd45e531
keywords:
- AddBezier methods Direct2D
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
ms.date: 07/02/2019
ms.topic: reference
---

# ID2D1GeometrySink::AddBezier methods

Creates a cubic Bezier curve between the current point and the specified end point and adds it to the geometry sink.

### Overload list



| Method                                                                                            | Description                                                                                    |
|:--------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------|
| [**AddBezier(D2D1\_BEZIER\_SEGMENT&)**](/windows/win32/api/d2d1/nf-d2d1-id2d1geometrysink-addbezier(constd2d1_bezier_segment_))  | Creates a cubic Bezier curve between the current point and the specified end point.<br/> |
| [**AddBezier(D2D1\_BEZIER\_SEGMENT\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1geometrysink-addbezier(constd2d1_bezier_segment)) | Creates a cubic Bezier curve between the current point and the specified endpoint.<br/>  |



## Examples

The following example creates an [**ID2D1PathGeometry**](/windows/win32/api/d2d1/nn-d2d1-id2d1pathgeometry), retrieves a sink, and uses it to define an hourglass shape. For the complete example, see [How to Draw and Fill a Complex Shape](how-to-draw-and-fill-a-complex-shape.md).


```C++
ID2D1GeometrySink *pSink = NULL;



// Create a path geometry.
if (SUCCEEDED(hr))
{
    hr = m_pD2DFactory->CreatePathGeometry(&m_pPathGeometry);

    if (SUCCEEDED(hr))
    {
        // Write to the path geometry using the geometry sink.
        hr = m_pPathGeometry->Open(&pSink);

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
        SafeRelease(&pSink);
    }
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

[**ID2D1GeometrySink**](/windows/win32/api/d2d1/nn-d2d1-id2d1geometrysink)
</dt> </dl>

�

�
