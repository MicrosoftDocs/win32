---
title: ID2D1Geometry CompareWithGeometry methods
description: Describes the intersection between this geometry and the specified geometry.
ms.assetid: 75ddd674-b50b-4d34-b291-9e7e65828304
keywords:
- CompareWithGeometry methods Direct2D
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

# ID2D1Geometry::CompareWithGeometry methods

Describes the intersection between this geometry and the specified geometry.

### Overload list



| Method                                                                                                                                                                                                            | Description                                                                                                                                                      |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CompareWithGeometry(ID2D1Geometry\*,D2D1\_MATRIX\_3X2\_F&,D2D1\_GEOMETRY\_RELATION\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1geometry-comparewithgeometry(id2d1geometry_constd2d1_matrix_3x2_f__d2d1_geometry_relation))              | Describes the intersection between this geometry and the specified geometry. The comparison is performed using the default flattening tolerance.<br/>      |
| [**CompareWithGeometry(ID2D1Geometry\*,D2D1\_MATRIX\_3X2\_F\*,D2D1\_GEOMETRY\_RELATION\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1geometry-comparewithgeometry(id2d1geometry_constd2d1_matrix_3x2_f_d2d1_geometry_relation))             | Describes the intersection between this geometry and the specified geometry. The comparison is performed using the default flattening tolerance.<br/>      |
| [**CompareWithGeometry(ID2D1Geometry\*,D2D1\_MATRIX\_3X2\_F&,FLOAT,D2D1\_GEOMETRY\_RELATION\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1geometry-comparewithgeometry(id2d1geometry_constd2d1_matrix_3x2_f__float_d2d1_geometry_relation))  | Describes the intersection between this geometry and the specified geometry. The comparison is performed using the specified flattening tolerance.<br/>    |
| [**CompareWithGeometry(ID2D1Geometry\*,D2D1\_MATRIX\_3X2\_F\*,FLOAT,D2D1\_GEOMETRY\_RELATION\*)**](/windows/win32/api/d2d1/nf-d2d1-id2d1geometry-comparewithgeometry(id2d1geometry_constd2d1_matrix_3x2_f_float_d2d1_geometry_relation)) | Describes the intersection between this geometry and the specified geometry. The comparison is performed by using the specified flattening tolerance.<br/> |



## Remarks

When interpreting the returned *relation* value, it is important to remember that the member [**D2D1\_GEOMETRY\_RELATION\_IS\_CONTAINED**](/windows/desktop/api/d2d1/ne-d2d1-d2d1_geometry_relation) of the **D2D1\_GEOMETRY\_RELATION** enumeration type means that this geometry is contained inside *inputGeometry*, not that this geometry contains *inputGeometry*.

For more information about how to interpret other possible return values, see [**D2D1\_GEOMETRY\_RELATION**](/windows/desktop/api/d2d1/ne-d2d1-d2d1_geometry_relation).

## Requirements



| Requirement | Value |
|--------------------|-------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1Geometry**](/windows/win32/api/d2d1/nn-d2d1-id2d1geometry)
</dt> </dl>

 

