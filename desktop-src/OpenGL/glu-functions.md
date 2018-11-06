---
title: GLU Functions
description: GLU Functions
ms.assetid: 8304a291-1a26-42bc-8887-386732980722
keywords:
- OpenGL,GLU library functions
- OpenGL reference,GLU library functions
- GLU library,functions
- OpenGL Utility (GLU),functions
ms.topic: article
ms.date: 05/31/2018
---

# GLU Functions

This section includes reference pages, in alphabetical order, for all OpenGL Utility Library functions. For background information about these functions, see [OpenGL Utility Library](opengl-utility-library.md).



| Function                                                                                           | Description                                                                                              |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**gluBeginCurve**](glubegincurve.md), [**gluEndCurve**](gluendcurve.md)                         | Delimit a Non-Uniform Rational B-Spline ([NURBS](using-nurbs-curves-and-surfaces.md)) curve definition. |
| [**gluBeginPolygon**](glubeginpolygon.md), [**gluEndPolygon**](gluendpolygon.md)                 | Delimit a polygon description.                                                                           |
| [**gluBeginSurface**](glubeginsurface.md), [**gluEndSurface**](gluendsurface.md)                 | Delimit a NURBS surface definition.                                                                      |
| [**gluBeginTrim**](glubegintrim.md), [**gluEndTrim**](gluendtrim.md)                             | Delimit a NURBS trimming loop definition.                                                                |
| [**gluBuild1DMipmaps**](glubuild1dmipmaps.md)                                                     | Creates 1-D mipmaps.                                                                                     |
| [**gluBuild2DMipmaps**](glubuild2dmipmaps.md)                                                     | Creates 2-D mipmaps.                                                                                     |
| [**gluCylinder**](glucylinder.md)                                                                 | Draws a cylinder.                                                                                        |
| [**gluDeleteNurbsRenderer**](gludeletenurbsrenderer.md)                                           | Destroys a NURBS object.                                                                                 |
| [**gluDeleteQuadric**](gludeletequadric.md)                                                       | Destroys a quadric object.                                                                               |
| [**gluDeleteTess**](gludeletetess.md)                                                             | Destroys a tessellation object.                                                                          |
| [**gluDisk**](gludisk.md)                                                                         | Draws a disk.                                                                                            |
| [**gluErrorString**](gluerrorstring.md)                                                           | Produces an error string from an OpenGL or GLU error code. The error string is ANSI only.                |
| [**gluGetNurbsProperty**](glugetnurbsproperty.md)                                                 | Retrieves a NURBS property.                                                                              |
| [**gluGetString**](glugetstring.md)                                                               | Retrieves a string that describes the GLU version number or supported GLU extension calls.               |
| [**gluGetTessProperty**](glugettessproperty.md)                                                   | Retrieves a tessellation object property.                                                                |
| [**gluLoadSamplingMatrices**](gluloadsamplingmatrices.md)                                         | Loads NURBS sampling and culling matrices.                                                               |
| [**gluLookAt**](glulookat.md)                                                                     | Defines a viewing transformation.                                                                        |
| [**gluNewNurbsRenderer**](glunewnurbsrenderer.md)                                                 | Creates a NURBS object.                                                                                  |
| [**gluNewQuadric**](glunewquadric.md)                                                             | Creates a quadric object.                                                                                |
| [**gluNewTess**](glunewtess.md)                                                                   | Creates a tessellation object.                                                                           |
| [**gluNextContour**](glunextcontour.md)                                                           | Marks the beginning of another contour.                                                                  |
| [*gluNurbsCallback*](glunurbs.md)                                                                 | Defines a callback for a NURBS object.                                                                   |
| [**gluNurbsCurve**](glunurbscurve.md)                                                             | Defines the shape of a NURBS curve.                                                                      |
| [**gluNurbsProperty**](glunurbsproperty.md)                                                       | Sets a NURBS property.                                                                                   |
| [**gluNurbsSurface**](glunurbssurface.md)                                                         | Defines the shape of a NURBS surface.                                                                    |
| [**gluOrtho2D**](gluortho2d.md)                                                                   | Defines a 2-D orthographic projection matrix.                                                            |
| [**gluPartialDisk**](glupartialdisk.md)                                                           | Draws an arc of a disk.                                                                                  |
| [**gluPerspective**](gluperspective.md)                                                           | Sets up a perspective projection matrix.                                                                 |
| [**gluPickMatrix**](glupickmatrix.md)                                                             | Defines a picking region.                                                                                |
| [**gluProject**](gluproject.md)                                                                   | Maps object coordinates to window coordinates.                                                           |
| [**gluPwlCurve**](glupwlcurve.md)                                                                 | Describes a piecewise linear NURBS trimming curve.                                                       |
| [*gluQuadricCallback*](gluquadric.md)                                                             | Defines a callback for a quadric object.                                                                 |
| [**gluQuadricDrawStyle**](gluquadricdrawstyle.md)                                                 | Specifies the draw style desired for quadrics.                                                           |
| [**gluQuadricNormals**](gluquadricnormals.md)                                                     | Specifies what kind of normals are to be used for quadrics.                                              |
| [**gluQuadricOrientation**](gluquadricorientation.md)                                             | Specifies inside or outside orientation for quadrics.                                                    |
| [**gluQuadricTexture**](gluquadrictexture.md)                                                     | Specifies whether quadrics are to be textured.                                                           |
| [**gluScaleImage**](gluscaleimage.md)                                                             | Scales an image to an arbitrary size.                                                                    |
| [**gluSphere**](glusphere.md)                                                                     | Draws a sphere.                                                                                          |
| [**gluTessBeginContour**](glutessbegincontour.md), [**gluTessEndContour**](glutessendcontour.md) | Delimit a contour description.                                                                           |
| [**gluTessBeginPolygon**](glutessbeginpolygon.md), [**gluTessEndPolygon**](glutessendpolygon.md) | Delimit a polygon description.                                                                           |
| [*gluTessCallback*](glutess.md)                                                                   | Defines a callback for a tessellation object.                                                            |
| [**gluTessNormal**](glutessnormal.md)                                                             | Specifies a normal for a polygon.                                                                        |
| [**gluTessProperty**](glutessproperty.md)                                                         | Sets the property of a tessellation object.                                                              |
| [**gluTessVertex**](glutessvertex.md)                                                             | Specifies a vertex on a polygon.                                                                         |
| [**gluUnProject**](gluunproject.md)                                                               | Maps window coordinates to object coordinates.                                                           |



 

 

 




