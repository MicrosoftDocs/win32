---
title: Porting NURBS Curves
description: The OpenGL functions for drawing NURBS curves are very similar to the IRIS GL functions. You specify knot sequences and control points using a gluNurbsCurve function, which must be contained within a gluBeginCurve / gluEndCurve pair.
ms.assetid: 954e8029-06bd-4072-9b84-53ecba1d05da
keywords:
- IRIS GL porting,NURBS curves
- porting from IRIS GL,NURBS curves
- porting to OpenGL from IRIS GL,NURBS curves
- OpenGL porting from IRIS GL,NURBS curves
- NURBS curves
- curves
- IRIS GL porting,curves
- porting from IRIS GL,curves
- porting to OpenGL from IRIS GL,curves
- OpenGL porting from IRIS GL,curves
- NURBS (Non-Uniform Rational B-Spline)
- Non-Uniform Rational B-Spline (NURBS)
ms.topic: article
ms.date: 05/31/2018
---

# Porting NURBS Curves

The OpenGL functions for drawing NURBS curves are very similar to the IRIS GL functions. You specify knot sequences and control points using a [**gluNurbsCurve**](glunurbscurve.md) function, which must be contained within a [**gluBeginCurve**](glubegincurve.md) / [**gluEndCurve**](gluendcurve.md) pair.

The following table lists the IRIS GL functions for drawing NURBS curves and their equivalent OpenGL functions.



| IRIS GL function | OpenGL function                        | Meaning                     |
|------------------|----------------------------------------|-----------------------------|
| **bgncurve**     | [**gluBeginCurve**](glubegincurve.md) | Begins a curve definition.  |
| **nurbscurve**   | [**gluNurbsCurve**](glunurbscurve.md) | Specifies curve attributes. |
| **endcurve**     | [**gluEndCurve**](gluendcurve.md)     | Ends a curve definition.    |



 

Associate position, texture, and color coordinates by presenting each as a separate **gluNurbsCurve** inside the begin/end pair. You can make no more than one call to **gluNurbsCurve** for each piece of color, position, and texture data within a single **gluBeginCurve/gluEndCurve** pair. You must make exactly one call to describe the position of the curve (a GL\_MAP1\_VERTEX\_3 or GL\_MAP1\_VERTEX\_4 description). When you call **gluEndCurve**, the curve is tessellated into line segments and then rendered.

The following table lists IRIS GL and OpenGL NURBS curve types.



| IRIS GL type | OpenGL type                  | Meaning                                 |
|--------------|------------------------------|-----------------------------------------|
| N\_V3D       | GL\_MAP1\_VERTEX\_3          | Polynomial curve.                       |
| N\_V3DR      | GL\_MAP1\_VERTEX\_4          | Rational curve.                         |
|              | GL\_MAP1\_TEXTURE\_COORD\_\* | Control points are texture coordinates. |
|              | GL\_MAP1\_NORMAL             | Control points are normals.             |



 

For more information on available evaluator types, see [**glMap1**](glmap1.md).

??

 

 




