---
title: ID2D1Geometry ComputePointAtLength methods
description: Calculates the point and tangent vector at the specified distance along the \ 160;geometry.
ms.assetid: 'b76aa3db-2967-4baa-a449-f664b080fb74'
keywords: ["ComputePointAtLength methods Direct2D"]
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
---

# ID2D1Geometry::ComputePointAtLength methods

Calculates the point and tangent vector at the specified distance along the geometry.

### Overload list



| Method                                                                                                                                                                                                        | Description                                                                                                                                                                                        |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ComputePointAtLength(FLOAT,D2D1\_MATRIX\_3X2\_F&,D2D1\_POINT\_2F\*,D2D1\_POINT\_2F\*)**](id2d1geometry-computepointatlength-float-ref-d2d-matrix-3x2-f-ptr-d2d-point-2f-ptr-d2d-point-2f.md)              | Calculates the point and tangent vector at the specified distance along the geometry after it has been transformed by the specified matrix and flattened using the default tolerance.<br/>   |
| [**ComputePointAtLength(FLOAT,D2D1\_MATRIX\_3X2\_F\*,D2D1\_POINT\_2F\*,D2D1\_POINT\_2F\*)**](id2d1geometry-computepointatlength-float-ptr-d2d-matrix-3x2-f-ptr-d2d-point-2f-ptr-d2d-point-2f.md)             | Calculates the point and tangent vector at the specified distance along the geometry after it has been transformed by the specified matrix and flattened using the default tolerance.<br/>   |
| [**ComputePointAtLength(FLOAT,D2D1\_MATRIX\_3X2\_F&,FLOAT,D2D1\_POINT\_2F\*,D2D1\_POINT\_2F\*)**](id2d1geometry-computepointatlength-float-ref-d2d-matrix-3x2-f-float-ptr-d2d-point-2f-ptr-d2d-point-2f.md)  | Calculates the point and tangent vector at the specified distance along the geometry after it has been transformed by the specified matrix and flattened using the specified tolerance.<br/> |
| [**ComputePointAtLength(FLOAT,D2D1\_MATRIX\_3X2\_F\*,FLOAT,D2D1\_POINT\_2F\*,D2D1\_POINT\_2F\*)**](id2d1geometry-computepointatlength-float-ptr-d2d-matrix-3x2-f-float-ptr-d2d-point-2f-ptr-d2d-point-2f.md) | Calculates the point and tangent vector at the specified distance along the geometry after it has been transformed by the specified matrix and flattened using the specified tolerance.<br/> |



## Examples

The following code example shows how to use **ComputePointAtLength** to calculate the point and tangent vector at the specified distance along the geometry.


```C++
D2D1_POINT_2F point;
D2D1_POINT_2F tangent;
```




```C++
// Ask the geometry to give us the point that corresponds with the
// length at the current time.
hr = m_pPathGeometry->ComputePointAtLength(
    length, 
    NULL, 
    &amp;point, 
    &amp;tangent); 
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

 

 





