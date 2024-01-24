---
title: Porting Polygons and Quadrilaterals
description: Keep the following points in mind when porting polygons and quadrilaterals
ms.assetid: 2b752437-caf9-4336-a906-d06b2aa8bb04
keywords:
- IRIS GL porting,quadrilaterals
- porting from IRIS GL,quadrilaterals
- porting to OpenGL from IRIS GL,quadrilaterals
- OpenGL porting from IRIS GL,quadrilaterals
- drawing functions,quadrilaterals
- quadrilaterals
- IRIS GL porting,polygons
- porting from IRIS GL,polygons
- porting to OpenGL from IRIS GL,polygons
- OpenGL porting from IRIS GL,polygons
- drawing functions,polygons
- polygons,porting from IRIS GL
ms.topic: article
ms.date: 05/31/2018
---

# Porting Polygons and Quadrilaterals

Keep the following points in mind when porting polygons and quadrilaterals:

-   There is no direct equivalent for **concave**(**TRUE**). Instead you can use the tessellation routines in the GLU, described in [Tessellating Polygons](tessellating-polygons.md).
-   Polygon modes are set differently.
-   These polygon drawing functions have no direct equivalents in OpenGL: the **poly** family of routines; the **polf** family of routines; **pmv**, **pdr**, and **pclos**; **rpmv** and **rpdr**; **splf**; and **spclos**.

If your IRIS GL code uses these functions, you'll have to rewrite the code using [**glBegin**](glbegin.md)( GL\_POLYGON ).

The following table lists the IRIS GL polygon drawing functions and their equivalent OpenGL functions.



| IRIS GL function         | OpenGL function                                                    | Meaning                                                 |
|--------------------------|--------------------------------------------------------------------|---------------------------------------------------------|
| **bgnpolygonendpolygon** | [**glBegin**](glbegin.md) ( GL\_POLYGON )[**glEnd**](glend.md)   | Vertices define boundary of a simple convex polygon.    |
|                          | **glBegin**( GL\_QUADS )**glEnd**<br/>                       | Interprets quadruples of vertices as quadrilaterals.    |
| **bgnqstripendqstrip**   | [**glBegin**](glbegin.md) ( GL\_QUAD\_STRIP )**glEnd**<br/> | Interprets vertices as linked strips of quadrilaterals. |
|                          | [glEdgeFlag](gledgeflag-functions.md)                             |                                                         |
| **polymode**             | [**glPolygonMode**](glpolygonmode.md)                             | Sets polygon drawing mode.                              |
| **rectrectf**<br/> | [glRect](glrect-functions.md)                                     | Draws a rectangle.                                      |
| **sboxsboxf**<br/> |                                                                    | Draws a screen-aligned rectangle.                       |



 

??

## Porting Polygon Modes

The OpenGL function [**glPolygonMode**](glpolygonmode.md) lets you specify which side of a polygon (the back or the front) the mode applies to. Its syntax is:

``` syntax
void glPolygonMode( GLenum face, GLenum mode ); 
 
```

where face is one of:



|GLenum value                      |  Meaning                                                          |
|----------------------|------------------------------------------------------------|
| GL\_FRONT            | mode which applies to front-facing polygons                |
| GL\_BACK             | mode which applies to back-facing polygons                 |
| GL\_FRONT\_AND\_BACK | mode which applies to both front- and back-facing polygons |



 

The GL\_FRONT\_AND\_BACK mode is equivalent to the IRIS GL **polymode** function. The following table lists IRIS GL polygon modes and their equivalent OpenGL modes.



| IRIS GL mode | OpenGL mode | Meaning                                       |
|--------------|-------------|-----------------------------------------------|
| PYM\_POINT   | GL\_POINT   | Draws vertices as points.                     |
| PYM\_LINE    | GL\_LINE    | Draws boundary edges as line segments.        |
| PYM\_FILL    | GL\_FILL    | Draws polygon interior filled.                |
| PYM\_HOLLOW  |             | Fills only interior pixels at the boundaries. |



 

## Porting Polygon Stipples

When porting IRIS GL polygon stipples, keep the following points in mind:

-   OpenGL doesn't use tables for polygon stipples; only one stipple pattern is kept. You can use display lists to store different stipple patterns.
-   The OpenGL polygon stipple bitmap size is always a 32x32 bit pattern.
-   Stipple encoding is affected by [**glPixelStore**](glpixelstore-functions.md).

For more information on porting polygon stipples, see [Porting Pixel Operations](porting-pixel-operations.md).

The following table lists IRIS GL polygon stipple functions and their equivalent OpenGL functions.



| IRIS GL function | OpenGL function                                    | Meaning                                               |
|------------------|----------------------------------------------------|-------------------------------------------------------|
| **defpattern**   | [**glPolygonStipple**](glpolygonstipple.md)       | Sets the stipple pattern.                             |
| **setpattern**   |                                                    | OpenGL keeps only one polygon stipple pattern.        |
| **getpattern**   | [**glGetPolygonStipple**](glgetpolygonstipple.md) | Returns the stipple bitmap (used to return an index). |



 

In OpenGL, you enable and disable polygon stippling by passing GL\_POLYGON\_STIPPLE as a parameter for [**glEnable**](glenable.md) and [**glDisable**](gldisable.md).

The following OpenGL code sample demonstrates polygon stippling:


```C++
void display(void) 
{ 
    GLubyte fly[] = { 
      0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
      0x03, 0x80, 0x01, 0xC0, 0x06, 0xC0, 0x03, 0x60, 
      0x04, 0x60, 0x06, 0x20, 0x04, 0x30, 0x0C, 0x20, 
      0x04, 0x18, 0x18, 0x20, 0x04, 0x0C, 0x30, 0x20, 
      0x04, 0x06, 0x60, 0x20, 0x44, 0x03, 0xC0, 0x22, 
      0x44, 0x01, 0x80, 0x22, 0x44, 0x01, 0x80, 0x22, 
      0x44, 0x01, 0x80, 0x22, 0x44, 0x01, 0x80, 0x22, 
      0x44, 0x01, 0x80, 0x22, 0x44, 0x01, 0x80, 0x22, 
      0x66, 0x01, 0x80, 0x66, 0x33, 0x01, 0x80, 0xCC, 
      0x19, 0x81, 0x81, 0x98, 0x0C, 0xC1, 0x83, 0x30, 
      0x07, 0xe1, 0x87, 0xe0, 0x03, 0x3f, 0xfc, 0xc0, 
      0x03, 0x31, 0x8c, 0xc0, 0x03, 0x33, 0xcc, 0xc0, 
      0x06, 0x64, 0x26, 0x60, 0x0c, 0xcc, 0x33, 0x30, 
      0x18, 0xcc, 0x33, 0x18, 0x10, 0xc4, 0x23, 0x08, 
      0x10, 0x63, 0xC6, 0x08, 0x10, 0x30, 0x0c, 0x08, 
      0x10, 0x18, 0x18, 0x08, 0x10, 0x00, 0x00, 0x08 
    }; 
    GLubyte halftone[] = { 
      0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55, 
      0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55, 
      0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55, 
      0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55, 
      0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55, 
      0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55, 
      0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55, 
      0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55, 
      0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55, 
      0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55, 
      0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55, 
      0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55, 
      0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55, 
      0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55, 
      0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55, 
      0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55 
    }; 
 
    glClear (GL_COLOR_BUFFER_BIT); 
 
/*  draw all polygons in white*/ 
    glColor3f (1.0, 1.0, 1.0); 
 
/*  draw one solid, unstippled rectangle,*/ 
/*  then two stippled rectangles*/ 
    glRectf (25.0, 25.0, 125.0, 125.0); 
    glEnable (GL_POLYGON_STIPPLE); 
    glPolygonStipple (fly); 
    glRectf (125.0, 25.0, 225.0, 125.0); 
    glPolygonStipple (halftone); 
    glRectf (225.0, 25.0, 325.0, 125.0); 
    glDisable (GL_POLYGON_STIPPLE); 
 
    glFlush (); 
}
```



## Porting Tessellated Polygons

In IRIS GL, you use **concave**(**TRUE**) and then **bgnpolygon** to draw concave polygons. The OpenGL GLU includes functions you can use to draw concave polygons.

**To draw a concave polygon with OpenGL**

1.  Create a tessellation object.
2.  Define callbacks that will be used to process the triangles generated by the tessellator.
3.  Specify the concave polygon to be tessellated.

The following table lists the OpenGL functions for drawing tessellated polygons.



| OpenGL GLU function                        | Meaning                                                            |
|--------------------------------------------|--------------------------------------------------------------------|
| [**gluNewTess**](glunewtess.md)           | Creates a new tessellation object.                                 |
| [**gluDeleteTess**](gludeletetess.md)     | Deletes a tessellation object.                                     |
| [*gluTessCallback*](glutess.md)           |                                                                    |
| [**gluBeginPolygon**](glubeginpolygon.md) | Begins the polygon specification.                                  |
| [**gluTessVertex**](glutessvertex.md)     | Specifies a polygon vertex in a contour.                           |
| [**gluNextContour**](glunextcontour.md)   | Indicates that the next series of vertices describe a new contour. |
| [**gluEndPolygon**](gluendpolygon.md)     | Ends the polygon specification.                                    |



 

 

 





