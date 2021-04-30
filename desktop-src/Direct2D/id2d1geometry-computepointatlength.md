---
title: ID2D1Geometry ComputePointAtLength methods
description: Calculates the point and tangent vector at the specified distance along the \ 160;geometry.
ms.assetid: b76aa3db-2967-4baa-a449-f664b080fb74
keywords:
- ComputePointAtLength methods Direct2D
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
api_name: 
---

# ID2D1Geometry::ComputePointAtLength methods

Calculates the point and tangent vector at the specified distance along the geometry.

### Overload list



| Method                                                                                                                                                                                                        | Description                                                                                                                                                                                        |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ComputePointAtLength(FLOAT,D2D1\_MATRIX\_3X2\_F&,D2D1\_POINT\_2F\*,D2D1\_POINT\_2F\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1geometry-computepointatlength(float_constd2d1_matrix_3x2_f__d2d1_point_2f_d2d1_point_2f))              | Calculates the point and tangent vector at the specified distance along the geometry after it has been transformed by the specified matrix and flattened using the default tolerance.<br/>   |
| [**ComputePointAtLength(FLOAT,D2D1\_MATRIX\_3X2\_F\*,D2D1\_POINT\_2F\*,D2D1\_POINT\_2F\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1geometry-computepointatlength(float_constd2d1_matrix_3x2_f_d2d1_point_2f_d2d1_point_2f))             | Calculates the point and tangent vector at the specified distance along the geometry after it has been transformed by the specified matrix and flattened using the default tolerance.<br/>   |
| [**ComputePointAtLength(FLOAT,D2D1\_MATRIX\_3X2\_F&,FLOAT,D2D1\_POINT\_2F\*,D2D1\_POINT\_2F\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1geometry-combinewithgeometry(id2d1geometry_d2d1_combine_mode_constd2d1_matrix_3x2_f_float_id2d1simplifiedgeometrysink))  | Calculates the point and tangent vector at the specified distance along the geometry after it has been transformed by the specified matrix and flattened using the specified tolerance.<br/> |
| [**ComputePointAtLength(FLOAT,D2D1\_MATRIX\_3X2\_F\*,FLOAT,D2D1\_POINT\_2F\*,D2D1\_POINT\_2F\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1geometry-computepointatlength(float_constd2d1_matrix_3x2_f_float_d2d1_point_2f_d2d1_point_2f)) | Calculates the point and tangent vector at the specified distance along the geometry after it has been transformed by the specified matrix and flattened using the specified tolerance.<br/> |



## Examples

The following code example shows how to use **ComputePointAtLength** to calculate the point and tangent vector at the specified distance along the geometry.


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
    &point, 
    &tangent); 
```



## Requirements



| Requirement | Value |
|--------------------|-------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1Geometry**](/windows/win32/api/d2d1/nn-d2d1-id2d1geometry)
</dt> </dl>

 

