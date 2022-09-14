---
title: Porting bgn/end Commands
description: IRIS GL uses the begin/end paradigm but has a different function for each graphics primitive.
ms.assetid: 4191344b-614a-42d6-8a31-7a708f17371e
keywords:
- IRIS GL porting,bgn/end commands
- porting from IRIS GL,bgn/end commands
- porting to OpenGL from IRIS GL,bgn/end commands
- OpenGL porting from IRIS GL,bgn/end commands
- drawing functions,bgn/end commands
- bgn/end commands
ms.topic: article
ms.date: 05/31/2018
---

# Porting bgn/end Commands

IRIS GL uses the begin/end paradigm but has a different function for each graphics primitive. For example, you probably use **bgnpolygon** and **endpolygon** to draw polygons, and **bgnline** and **endline** to draw lines. In OpenGL, you use the [**glBegin**](glbegin.md) / [**glEnd**](glend.md) structure for both. In OpenGL you draw most geometric objects by enclosing a series of functions that specify vertices, normals, textures, and colors between pairs of **glBegin** and **glEnd** calls. For example:

``` syntax
void glBegin( GLenum mode) ; 
   /* vertex list, colors, normals, textures, materials */ 
void glEnd( void );
```

The **glBegin** function takes a single parameter that specifies the drawing mode, and thus the primitive. Here's an OpenGL code sample that draws a polygon and then a line:

``` syntax
glBegin( GL_POLYGON ) ; 
   glVertex2f(20.0, 10.0); 
   glVertex2f(10.0, 30.0); 
   glVertex2f(20.0, 50.0); 
   glVertex2f(40.0, 50.0); 
   glVertex2f(50.0, 30.0); 
   glVertex2f(40.0, 10.0); 
glEnd(); 
glBegin( GL_LINES ) ; 
   glVertex2i(100,100); 
   glVertex2i(500,500); 
glEnd();
```

With OpenGL, you draw different geometric objects by specifying different parameters for [**glBegin**](glbegin.md). The following table lists the OpenGL **glBegin** parameters that correspond to equivalent IRIS GL functions.



| IRIS GL function  | Value of glBegin mode | Meaning                                                                                  |
|-------------------|-----------------------|------------------------------------------------------------------------------------------|
| **bgnpoint**      | GL\_POINTS            | Individual points.                                                                       |
| **bgnline**       | GL\_LINE\_STRIP       | Series of connected line segments.                                                       |
| **bgnclosedline** | GL\_LINE\_LOOP        | Series of connected line segments, with a segment added between first and last vertices. |
|                   | GL\_LINES             | Pairs of vertices interpreted as individual line segments.                               |
| **bgnpolygon**    | GL\_POLYGON           | Boundary of a simple convex polygon.                                                     |
|                   | GL\_TRIANGLES         | Triples of vertices interpreted as triangles.                                            |
| **bgntmesh**      | GL\_TRIANGLE\_STRIP   | Linked strips of triangles.                                                              |
|                   | GL\_TRIANGLE\_FAN     | Linked fans of triangles.                                                                |
|                   | GL\_QUADS             | Quadruples of vertices interpreted as quadrilaterals.                                    |
| **bgnqstrip**     | GL\_QUAD\_STRIP       | Linked strips of quadrilaterals.                                                         |



 

For a detailed discussion of the differences between triangle meshes, strips, and fans, see [Porting Triangles](porting-triangles.md).

There is no limit to the number of vertices you can specify between a [**glBegin**](glbegin.md) / [**glEnd**](glend.md) pair.

In addition to specifying vertices inside a **glBegin** / **glEnd** pair, you can specify a current normal, current texture coordinates, and a current color. The following table lists the commands valid inside a **glBegin** / **glEnd** pair.



| IRIS GL function        | OpenGL function                                                      | Meaning                                          |
|-------------------------|----------------------------------------------------------------------|--------------------------------------------------|
| **v2**, **v3**, **v4**  | [glVertex](glvertex-functions.md)                                   | Sets vertex coordinates.                         |
| **RGBcolor**, **cpack** | [glColor](glcolor-functions.md)                                     | Sets current color.                              |
| **color**               | [glIndex](glindex-functions.md)                                     | Sets current color index.                        |
| **n3f**                 | [glNormal](glnormal-functions.md)                                   | Sets normal vector coordinates.                  |
|                         | [glEvalCoord](glevalcoord-functions.md)                             | Evaluates enabled one- and two-dimensional maps. |
| **callobj**             | [**glCallList**](glcalllist.md), [**glCallLists**](glcalllists.md) | Executes display list(s).                        |
| **t2**                  | [glTexCoord](gltexcoord-functions.md)                               | Sets texture coordinates.                        |
|                         | [glEdgeFlag](gledgeflag-functions.md)                               | Controls drawing edges.                          |
| **lmbind**              | [glMaterial](glmaterial-functions.md)                               | Sets material properties.                        |



 

> [!Note]
>
> If you use any OpenGL function other than those listed in the preceding table inside a [**glBegin**](glbegin.md) / [**glEnd**](glend.md) pair, you'll get unpredictable results, or possibly an error.

 

 

 




