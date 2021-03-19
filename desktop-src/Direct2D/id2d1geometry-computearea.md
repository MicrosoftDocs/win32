---
title: ID2D1Geometry ComputeArea methods
description: Computes the area of the geometry.
ms.assetid: 655f11bc-7435-4d23-b4b1-3d7c2110aa48
keywords:
- ComputeArea methods Direct2D
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

# ID2D1Geometry::ComputeArea methods

Computes the area of the geometry.

### Overload list



| Method                                                                                                                      | Description                                                                                                                                      |
|:----------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ComputeArea(D2D1\_MATRIX\_3X2\_F&,FLOAT\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1geometry-computearea(constd2d1_matrix_3x2_f__float))              | Computes the area of the geometry after it has been transformed by the specified matrix and flattened using the default tolerance.<br/>    |
| [**ComputeArea(D2D1\_MATRIX\_3X2\_F\*,FLOAT\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1geometry-computearea(constd2d1_matrix_3x2_f_float))             | Computes the area of the geometry after it has been transformed by the specified matrix and flattened by using the default tolerance.<br/> |
| [**ComputeArea(D2D1\_MATRIX\_3X2\_F&,FLOAT,FLOAT\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1geometry-computearea(constd2d1_matrix_3x2_f__float_float))  | Computes the area of the geometry after it has been transformed by the specified matrix and flattened using the specified tolerance.<br/>  |
| [**ComputeArea(D2D1\_MATRIX\_3X2\_F\*,FLOAT,FLOAT\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1geometry-computearea(constd2d1_matrix_3x2_f_float)) | Computes the area of the geometry after it has been transformed by the specified matrix and flattened using the specified tolerance.<br/>  |



## Examples

The following code example uses **ComputeArea** to compute the area of a specified circle (**m\_pCircleGeometry1**).


```C++
float area;

// Compute the area of circle1
hr = m_pCircleGeometry1->ComputeArea(
    D2D1::IdentityMatrix(),
    &area
    );
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

 

