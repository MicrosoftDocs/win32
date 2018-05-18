---
title: ID2D1Geometry CompareWithGeometry methods
description: Describes the intersection between this geometry and the specified geometry.
ms.assetid: '75ddd674-b50b-4d34-b291-9e7e65828304'
keywords: ["CompareWithGeometry methods Direct2D"]
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
---

# ID2D1Geometry::CompareWithGeometry methods

Describes the intersection between this geometry and the specified geometry.

### Overload list



| Method                                                                                                                                                                                                            | Description                                                                                                                                                      |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CompareWithGeometry(ID2D1Geometry\*,D2D1\_MATRIX\_3X2\_F&,D2D1\_GEOMETRY\_RELATION\*)**](id2d1geometry-comparewithgeometry-ptr-id2d1geometry-ref-d2d-matrix-3x2-f-ptr-d2d1-geometry-relation.md)              | Describes the intersection between this geometry and the specified geometry. The comparison is performed using the default flattening tolerance.<br/>      |
| [**CompareWithGeometry(ID2D1Geometry\*,D2D1\_MATRIX\_3X2\_F\*,D2D1\_GEOMETRY\_RELATION\*)**](id2d1geometry-comparewithgeometry-ptr-id2d1geometry-ptr-d2d-matrix-3x2-f-ptr-d2d1-geometry-relation.md)             | Describes the intersection between this geometry and the specified geometry. The comparison is performed using the default flattening tolerance.<br/>      |
| [**CompareWithGeometry(ID2D1Geometry\*,D2D1\_MATRIX\_3X2\_F&,FLOAT,D2D1\_GEOMETRY\_RELATION\*)**](id2d1geometry-comparewithgeometry-ptr-id2d1geometry-ref-d2d-matrix-3x2-f-float-ptr-d2d1-geometry-relation.md)  | Describes the intersection between this geometry and the specified geometry. The comparison is performed using the specified flattening tolerance.<br/>    |
| [**CompareWithGeometry(ID2D1Geometry\*,D2D1\_MATRIX\_3X2\_F\*,FLOAT,D2D1\_GEOMETRY\_RELATION\*)**](id2d1geometry-comparewithgeometry-ptr-id2d1geometry-ptr-d2d-matrix-3x2-f-float-ptr-d2d1-geometry-relation.md) | Describes the intersection between this geometry and the specified geometry. The comparison is performed by using the specified flattening tolerance.<br/> |



## Remarks

When interpreting the returned *relation* value, it is important to remember that the member [**D2D1\_GEOMETRY\_RELATION\_IS\_CONTAINED**](d2d1-geometry-relation.md) of the **D2D1\_GEOMETRY\_RELATION** enumeration type means that this geometry is contained inside *inputGeometry*, not that this geometry contains *inputGeometry*.

For more information about how to interpret other possible return values, see [**D2D1\_GEOMETRY\_RELATION**](d2d1-geometry-relation.md).

## Requirements



|                    |                                                                                     |
|--------------------|-------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1Geometry**](id2d1geometry.md)
</dt> </dl>

 

 





