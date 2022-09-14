---
title: gluCylinder function (Glu.h)
description: The gluCylinder function draws a cylinder.
ms.assetid: 43329d2f-50bb-46ea-85cb-22956d0df375
keywords:
- gluCylinder function OpenGL
topic_type:
- apiref
api_name:
- gluCylinder
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluCylinder function

The **gluCylinder** function draws a cylinder.

## Syntax


```C++
void WINAPI gluCylinder(
   GLUquadric *qobj,
   GLdouble   baseRadius,
   GLdouble   topRadius,
   GLdouble   height,
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

*baseRadius* 
</dt> <dd>

The radius of the cylinder at *z* = 0.

</dd> <dt>

*topRadius* 
</dt> <dd>

The radius of the cylinder at *z* = *height*.

</dd> <dt>

*height* 
</dt> <dd>

The height of the cylinder.

</dd> <dt>

*slices* 
</dt> <dd>

The number of subdivisions around the z-axis.

</dd> <dt>

*stacks* 
</dt> <dd>

The number of subdivisions along the z-axis.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The **gluCylinder** function draws a cylinder oriented along the z-axis. The base of the cylinder is placed at *z* = 0, and the top at *z* = *height*. Like a sphere, a cylinder is subdivided around the z-axis into slices, and along the z-axis into stacks.

Note that if *topRadius* is set to zero, then this routine will generate a cone.

If the orientation is set to GLU\_OUTSIDE (with [**gluQuadricOrientation**](gluquadricorientation.md)), then any generated normals point away from the z-axis. Otherwise, they point toward the z-axis.

If texturing is turned on (with [**gluQuadricTexture**](gluquadrictexture.md)): texture coordinates are generated so that *t* ranges linearly from 0.0 at *z* = 0 to 1.0 at *z* = *height*; and *s* ranges from 0.0 at the positive y-axis, to 0.25 at the positive x-axis, to 0.5 at the negative y-axis, to 0.75 at the negative x-axis, and back to 1.0 at the positive y-axis.

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

[**gluDisk**](gludisk.md)
</dt> <dt>

[**gluNewQuadric**](glunewquadric.md)
</dt> <dt>

[**gluPartialDisk**](glupartialdisk.md)
</dt> <dt>

[**gluQuadricOrientation**](gluquadricorientation.md)
</dt> <dt>

[**gluQuadricTexture**](gluquadrictexture.md)
</dt> <dt>

[**gluSphere**](glusphere.md)
</dt> </dl>

 

 





