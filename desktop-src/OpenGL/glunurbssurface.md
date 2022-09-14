---
title: gluNurbsSurface function (Glu.h)
description: The gluNurbsSurface function defines the shape of a Non-Uniform Rational B-Spline (NURBS) surface.
ms.assetid: ee86376c-26ba-49a9-b0b0-4ca936b6614b
keywords:
- gluNurbsSurface function OpenGL
topic_type:
- apiref
api_name:
- gluNurbsSurface
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluNurbsSurface function

The **gluNurbsSurface** function defines the shape of a Non-Uniform Rational B-Spline ([NURBS](using-nurbs-curves-and-surfaces.md)) surface.

## Syntax


```C++
void WINAPI gluNurbsSurface(
   GLUnurbs *nobj,
   GLint    sknot_count,
   float    *sknot,
   GLint    tknot_count,
   GLfloat  *tknot,
   GLint    s_stride,
   GLint    t_stride,
   GLfloat  *ctlarray,
   GLint    sorder,
   GLint    torder,
   GLenum   type
);
```



## Parameters

<dl> <dt>

*nobj* 
</dt> <dd>

The NURBS object (created with [**gluNewNurbsRenderer**](glunewnurbsrenderer.md)).

</dd> <dt>

*sknot\_count* 
</dt> <dd>

The number of knots in the parametric *u* direction.

</dd> <dt>

*sknot* 
</dt> <dd>

An array of *sknot\_count* nondecreasing knot values in the parametric *u* direction.

</dd> <dt>

*tknot\_count* 
</dt> <dd>

The number of knots in the parametric *v* direction.

</dd> <dt>

*tknot* 
</dt> <dd>

An array of *tknot\_count* nondecreasing knot values in the parametric *v* direction.

</dd> <dt>

*s\_stride* 
</dt> <dd>

The offset (as a number of single precisionfloating-point values) between successive control points in the parametric *u* direction in *ctlarray*.

</dd> <dt>

*t\_stride* 
</dt> <dd>

The offset (in single precisionfloating-point values) between successive control points in the parametric *v* direction in *ctlarray*.

</dd> <dt>

*ctlarray* 
</dt> <dd>

An array containing control points for the NURBS surface. The offsets between successive control points in the parametric *u* and *v* directions are given by *s\_stride* and *t\_stride*.

</dd> <dt>

*sorder* 
</dt> <dd>

The order of the NURBS surface in the parametric *u* direction. The order is one more than the degree, hence a surface that is cubic in *u* has a *u* order of 4.

</dd> <dt>

*torder* 
</dt> <dd>

The order of the NURBS surface in the parametric *v* direction. The order is one more than the degree, hence a surface that is cubic in *v* has a *v* order of 4.

</dd> <dt>

*type* 
</dt> <dd>

The type of the surface. The *type* parameter can be any of the valid two-dimensional evaluator types (such as GL\_MAP2\_VERTEX\_3 or GL\_MAP2\_COLOR\_4).

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

Use **gluNurbsSurface** within a NURBS surface definition to describe the shape of a NURBS surface (before any trimming). To mark the beginning of a NURBS surface definition, use the [**gluBeginSurface**](glubeginsurface.md) function. To mark the end of a NURBS surface definition, use the [**gluEndSurface**](gluendsurface.md) function. Call **gluNurbsSurface** within a NURBS surface definition only.

You associate positional, texture, and color coordinates with a surface by presenting each as a separate **gluNurbsSurface** between a **gluBeginSurface**/**gluEndSurface** pair. Within a single **gluBeginSurface**/**gluEndSurface** pair, you can make only one call to **gluNurbsSurface** for color, position, and texture data. Make exactly one call to describe the position of the surface (a *type* of GL\_MAP2\_VERTEX\_3 or GL\_MAP2\_VERTEX\_4).

You can trim a NURBS surface by using the [**gluNurbsCurve**](glunurbscurve.md) and [**gluPwlCurve**](glupwlcurve.md) functions between calls to [**gluBeginTrim**](glubegintrim.md) and [**gluEndTrim**](gluendtrim.md).

A **gluNurbsSurface** with *sknot\_count* knots in the *u* direction and *tknot\_count* knots in the *v* direction with orders *sorder* and *torder* must have (*sknot\_count* -*sorder*) multipied by (*tknot\_count* -*torder*) control points.

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

[**gluBeginSurface**](glubeginsurface.md)
</dt> <dt>

[**gluBeginTrim**](glubegintrim.md)
</dt> <dt>

[**gluEndSurface**](gluendsurface.md)
</dt> <dt>

[**gluEndTrim**](gluendtrim.md)
</dt> <dt>

[**gluNewNurbsRenderer**](glunewnurbsrenderer.md)
</dt> <dt>

[**gluNurbsCurve**](glunurbscurve.md)
</dt> <dt>

[**gluPwlCurve**](glupwlcurve.md)
</dt> </dl>

 

 





