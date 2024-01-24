---
title: gluTessNormal function (Glu.h)
description: The gluTessNormal function specifies a normal for a polygon.
ms.assetid: 8c3a90d3-760d-4a0a-9808-a797383fcc42
keywords:
- gluTessNormal function OpenGL
topic_type:
- apiref
api_name:
- gluTessNormal
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluTessNormal function

The **gluTessNormal** function specifies a normal for a polygon.

## Syntax


```C++
void WINAPI gluTessNormal(
   GLUtesselator *tess,
   GLdouble      x,
   GLdouble      y,
   GLdouble      z
);
```



## Parameters

<dl> <dt>

*tess* 
</dt> <dd>

The tessellation object (created with [**gluNewTess**](glunewtess.md)).

</dd> <dt>

*x* 
</dt> <dd>

The x-coordinate component of a normal.

</dd> <dt>

*y* 
</dt> <dd>

The y-coordinate component of a normal.

</dd> <dt>

*z* 
</dt> <dd>

The z-coordinate component of a normal.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The **gluTessNormal** function describes a normal for a polygon that you define. All input data is projected onto a plane perpendicular to one of the three coordinate axes before tessellation, and all output triangles are oriented counterclockwise with respect to the normal. (To obtain clockwise orientation, reverse the sign of the supplied normal). For example, if you know that all polygons lie in the x-y plane, call **gluTessNormal**(tess, 0.0, 0.0, 1.0) before rendering any polygons.

If the supplied normal is (0.0, 0.0, 0.0) (the default value), the normal is determined as follows:

1.  The direction of the normal, up to its sign, is found by fitting a plane to the vertexes, without regard to how the vertexes are connected. It is expected that the input data lies approximately in the plane; otherwise projection perpendicular to one of the three coordinate axes can change the geometry substantially.
2.  The sign of the normal is chosen so that the sum of the signed areas of all input contours is nonnegative (where a counterclockwise contour has positive area).

The supplied normal persists until another call to **gluTessNormal** changes it.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Glu.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Glu32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Glu32.dll</dt> </dl> |



## See also

<dl> <dt>

[**gluNewTess**](glunewtess.md)
</dt> <dt>

[**gluTessBeginPolygon**](glutessbeginpolygon.md)
</dt> <dt>

[**gluTessEndPolygon**](glutessendpolygon.md)
</dt> </dl>

 

 





