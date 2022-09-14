---
title: gluPartialDisk function (Glu.h)
description: The gluPartialDisk function draws an arc of a disk.
ms.assetid: 46809c15-88c3-40fa-965a-7aeeedc1c598
keywords:
- gluPartialDisk function OpenGL
topic_type:
- apiref
api_name:
- gluPartialDisk
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluPartialDisk function

The **gluPartialDisk** function draws an arc of a disk.

## Syntax


```C++
void WINAPI gluPartialDisk(
   GLUquadric *qobj,
   GLdouble   innerRadius,
   GLdouble   outerRadius,
   GLint      slices,
   GLint      loops,
   GLdouble   startAngle,
   GLdouble   sweepAngle
);
```



## Parameters

<dl> <dt>

*qobj* 
</dt> <dd>

A quadric object (created with [**gluNewQuadric**](glunewquadric.md)).

</dd> <dt>

*innerRadius* 
</dt> <dd>

The inner radius of the partial disk (can be zero).

</dd> <dt>

*outerRadius* 
</dt> <dd>

The outer radius of the partial disk.

</dd> <dt>

*slices* 
</dt> <dd>

The number of subdivisions around the z-axis.

</dd> <dt>

*loops* 
</dt> <dd>

The number of concentric rings about the origin into which the partial disk is subdivided.

</dd> <dt>

*startAngle* 
</dt> <dd>

The starting angle, in degrees, of the disk portion.

</dd> <dt>

*sweepAngle* 
</dt> <dd>

The sweep angle, in degrees, of the disk portion.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The **gluPartialDisk** function renders a partial disk on the *z* = 0 plane. A partial disk is similar to a full disk, except that only the subset of the disk from *startAngle* through *startAngle* + *sweepAngle* is included (where 0 degrees is along the positive y-axis, 90 degrees is along the positive x-axis, 180 degrees is along the negative y-axis, and 270 degrees is along the negative x-axis).

The partial disk has a radius of *outerRadius* and contains a concentric circular hole with a radius of *innerRadius*. If *innerRadius* is zero, then no hole is generated. The partial disk is subdivided around the z-axis into slices (like pizza slices), and also about the z-axis into rings (as specified by *slices* and *loops*, respectively).

With respect to orientation, the positive z-side of the partial disk is considered to be outside (see [**gluQuadricOrientation**](gluquadricorientation.md)). This means that if the orientation is set to GLU\_OUTSIDE, then any normals generated point along the positive z-axis.

If you have turned on texturing (with [**gluQuadricTexture**](gluquadrictexture.md)), **gluPartialDisk** generates texture coordinates linearly such that where *r* = *outerRadius*, the value at (*r*, 0, 0) is (1, 0.5); at (0, *r*, 0) it is (0.5, 1); at (*r*, 0, 0) it is (0, 0.5); and at (0, *r*, 0) it is (0.5, 0).

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

[**gluQuadricOrientation**](gluquadricorientation.md)
</dt> <dt>

[**gluQuadricTexture**](gluquadrictexture.md)
</dt> <dt>

[**gluSphere**](glusphere.md)
</dt> </dl>

 

 





