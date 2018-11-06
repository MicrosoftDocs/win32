---
title: Using NURBS Curves and Surfaces
description: Non-Uniform Rational B-Spline (NURBS) functions provide general and powerful descriptions of curves and surfaces in two and three dimensions, converting the curves and surfaces to OpenGL evaluators.
ms.assetid: 0b55659d-9fa2-47fc-ae15-0c296bd94dcb
keywords:
- OpenGL Utility (GLU),Non-Uniform Rational B-Spline (NURBS)
- GLU (OpenGL Utility),Non-Uniform Rational B-Spline (NURBS)
- Non-Uniform Rational B-Spline (NURBS) OpenGL
- NURBS (Non-Uniform Rational B-Spline) OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Using NURBS Curves and Surfaces

Non-Uniform Rational B-Spline (NURBS) functions provide general and powerful descriptions of curves and surfaces in two and three dimensions, converting the curves and surfaces to OpenGL evaluators. The NURBS functions can represent geometry in many computer-aided mechanical design systems. They can render curves and surfaces in a variety of styles, and they can automatically handle adaptive subdivision that tessellates the domain into smaller triangles in regions of high curvature and near silhouette edges. NURBS functions fall into the following categories.

To manage a NURBS object, use:

-   [**gluNewNurbsRenderer**](glunewnurbsrenderer.md) (create a NURBS object)
-   [**gluDeleteNurbsRenderer**](gludeletenurbsrenderer.md) (deletes a NURBS object)
-   [*gluNurbsCallback*](glunurbs.md) (establishes an error-handling function)

To specify the desired curves, use:

-   [**gluBeginCurve**](glubegincurve.md)
-   [**gluNurbsCurve**](glunurbscurve.md)
-   [**gluEndCurve**](gluendcurve.md)

To specify the desired surfaces, use:

-   [**gluBeginSurface**](glubeginsurface.md)
-   [**gluNurbsSurface**](glunurbssurface.md)
-   [**gluEndSurface**](gluendsurface.md)

You can also specify a trimming region, which defines a subset of the NURBS surface domain to be evaluated so you can create surfaces that have smooth boundaries or that contain holes.

To specify the trimming region, use:

-   [**gluBeginTrim**](glubegintrim.md)
-   [**gluPwlCurve**](glupwlcurve.md)
-   [**gluNurbsCurve**](glunurbscurve.md)
-   [**gluEndTrim**](gluendtrim.md)

As with quadric objects, you can control how NURBS curves and surfaces are rendered. You can determine:

-   Whether to discard a curve or surface whose control polyhedron lies outside the current viewport.
-   The maximum length (in pixels) of edges of polygons used to render curves and surfaces.
-   Whether you will take the projection matrix, modelview matrix, and viewport from the OpenGL server or supply them explictly with [**gluLoadSamplingMatrices**](gluloadsamplingmatrices.md).

Use [**gluNurbsProperty**](glunurbsproperty.md) to set these properties, or use the default values. You can query a NURBS object about its rendering style with [**gluGetNurbsProperty**](glugetnurbsproperty.md).

 

 




