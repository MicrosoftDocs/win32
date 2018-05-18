---
title: ID2D1Geometry Outline methods
description: Computes the outline of the geometry and writes the result to an ID2D1SimplifiedGeometrySink.
ms.assetid: 'ec92db79-a1aa-4661-9e75-45a1763af370'
keywords: ["Outline methods Direct2D"]
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
---

# ID2D1Geometry::Outline methods

Computes the outline of the geometry and writes the result to an [**ID2D1SimplifiedGeometrySink**](id2d1simplifiedgeometrysink.md).

### Overload list



| Method                                                                                                                                                          | Description                                                                                                                                      |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Outline(D2D1\_MATRIX\_3X2\_F&,ID2D1SimplifiedGeometrySink\*)**](id2d1geometry-outline-ref-d2d-matrix-3x2-f-ptr-id2d1simplifiedgeometrysink.md)              | Computes the outline of the geometry and writes the result to an [**ID2D1SimplifiedGeometrySink**](id2d1simplifiedgeometrysink.md). <br/> |
| [**Outline(D2D1\_MATRIX\_3X2\_F\*,ID2D1SimplifiedGeometrySink\*)**](id2d1geometry-outline-ptr-d2d-matrix-3x2-f-ptr-id2d1simplifiedgeometrysink.md)             | Computes the outline of the geometry and writes the result to an [**ID2D1SimplifiedGeometrySink**](id2d1simplifiedgeometrysink.md).<br/>  |
| [**Outline(D2D1\_MATRIX\_3X2\_F&,FLOAT,ID2D1SimplifiedGeometrySink\*)**](id2d1geometry-outline-ref-d2d-matrix-3x2-f-float-ptr-id2d1simplifiedgeometrysink.md)  | Computes the outline of the geometry and writes the result to an [**ID2D1SimplifiedGeometrySink**](id2d1simplifiedgeometrysink.md).<br/>  |
| [**Outline(D2D1\_MATRIX\_3X2\_F\*,FLOAT,ID2D1SimplifiedGeometrySink\*)**](id2d1geometry-outline-ptr-d2d-matrix-3x2-f-float-ptr-id2d1simplifiedgeometrysink.md) | Computes the outline of the geometry and writes the result to an [**ID2D1SimplifiedGeometrySink**](id2d1simplifiedgeometrysink.md).<br/>  |



## Remarks

The [**Outline**](id2d1geometry-outline-ref-d2d-matrix-3x2-f-ptr-id2d1simplifiedgeometrysink.md) method allows the caller to produce a geometry with an equivalent fill to the input geometry, with the following additional properties:

-   The output geometry contains no transverse intersections; that is, segments may touch, but they never cross.
-   The outermost figures in the output geometry are all oriented counterclockwise.
-   The output geometry is fill-mode invariant; that is, the fill of the geometry does not depend on the choice of the fill mode. For more information about the fill mode, see [**D2D1\_FILL\_MODE**](d2d1-fill-mode.md).

Additionally, the [**Outline**](id2d1geometry-outline-ref-d2d-matrix-3x2-f-ptr-id2d1simplifiedgeometrysink.md) method can be useful in removing redundant portions of said geometries to simplify complex geometries. It can also be useful in combination with [**ID2D1GeometryGroup**](id2d1geometrygroup.md) to create unions among several geometries simultaneously.

## Examples

The following code shows how to use **Outline** to construct an equivalent geometry with no self-intersections. It uses the default flattening tolerance and hence should not be used with very small geometries.


```C++
HRESULT D2DOutline(
    ID2D1Geometry *pGeometry,
    ID2D1Geometry **ppGeometry
    )
{
    HRESULT hr;
    ID2D1Factory *pFactory = NULL;
    pGeometry->GetFactory(&amp;pFactory);

    ID2D1PathGeometry *pPathGeometry = NULL;
    hr = pFactory->CreatePathGeometry(&amp;pPathGeometry);

    if (SUCCEEDED(hr))
    {
        ID2D1GeometrySink *pSink = NULL;
        hr = pPathGeometry->Open(&amp;pSink);

        if (SUCCEEDED(hr))
        {
            hr = pGeometry->Outline(NULL, pSink);

            if (SUCCEEDED(hr))
            {
                hr = pSink->Close();

                if (SUCCEEDED(hr))
                {
                    *ppGeometry = pPathGeometry;
                    (*ppGeometry)->AddRef();
                }
            }
            pSink->Release();
        }
        pPathGeometry->Release();
    }

    pFactory->Release();

    return hr;
}
```



## Requirements



|                    |                                                                                     |
|--------------------|-------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1Geometry**](id2d1geometry.md)
</dt> </dl>

 

 





