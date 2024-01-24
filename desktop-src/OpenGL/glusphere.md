---
title: gluSphere function (Glu.h)
description: The gluSphere function draws a sphere.
ms.assetid: 0f1919c6-0551-4d50-b782-767dacc088cb
keywords:
- gluSphere function OpenGL
topic_type:
- apiref
api_name:
- gluSphere
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluSphere function

The **gluSphere** function draws a sphere.

## Syntax


```C++
void WINAPI gluSphere(
   GLUquadric *qobj,
   GLdouble   radius,
   GLint      slices,
   GLint      stacks
);
```



## Parameters

<dl> <dt>

*qobj* 
</dt> <dd>

The quadric object (created with [**gluNewQuadric**](glunewquadric.md)).

</dd> <dt>

*radius* 
</dt> <dd>

The radius of the sphere.

</dd> <dt>

*slices* 
</dt> <dd>

The number of subdivisions around the z-axis (similar to lines of longitude).

</dd> <dt>

*stacks* 
</dt> <dd>

The number of subdivisions along the z-axis (similar to lines of latitude).

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The **gluSphere** function draws a sphere of the given radius centered around the origin. The sphere is subdivided around the z-axis into slices and along the z-axis into stacks (similar to lines of longitude and latitude).

If the orientation is set to GLU\_OUTSIDE (with **gluQuadricOrientation**), any normals generated point away from the center of the sphere. Otherwise, they point toward the center of the sphere.

If texturing is turned on (with **gluQuadricTexture**): texture coordinates are generated so that *t* ranges from 0.0 at *z* = -*radius* to 1.0 at *z* = *radius* (*t* increases linearly along longitudinal lines); and *s* ranges from 0.0 at the positive y-axis, to 0.25 at the positive x-axis, to 0.5 at the negative y-axis, to 0.75 at the negative x-axis, and back to 1.0 at the positive y-axis.

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

[**gluCylinder**](glucylinder.md)
</dt> <dt>

[**gluDisk**](gludisk.md)
</dt> <dt>

[**gluNewQuadric**](glunewquadric.md)
</dt> <dt>

[**gluPartialDisk**](glupartialdisk.md)
</dt> <dt>

[**gluQuadricOrientation**](gluquadricorientation.md)
</dt> <dt>

[**gluQuadricTexture**](gluquadrictexture.md)
</dt> </dl>

 

 





