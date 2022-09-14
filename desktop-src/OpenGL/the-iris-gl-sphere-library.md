---
title: The IRIS GL Sphere Library
description: OpenGL does not support the IRIS GL sphere library. You can replace your sphere library calls with quadrics routines from the GLU library. For more information about the GLU library, see the Open GL Programming Guide and OpenGL Utility Library.
ms.assetid: 2b7e6a3d-d2d0-4b54-8dff-8c4d6b113007
keywords:
- IRIS GL porting,sphere library
- porting from IRIS GL,sphere library
- porting to OpenGL from IRIS GL,sphere library
- OpenGL porting from IRIS GL,sphere library
- drawing functions,sphere library
- sphere library
ms.topic: article
ms.date: 05/31/2018
---

# The IRIS GL Sphere Library

OpenGL does not support the IRIS GL sphere library. You can replace your sphere library calls with quadrics routines from the GLU library. For more information about the GLU library, see the *Open GL Programming Guide* and [OpenGL Utility Library](opengl-utility-library.md).

The following table lists the OpenGL quadrics functions.



| OpenGL function                                        | Meaning                                                          |
|--------------------------------------------------------|------------------------------------------------------------------|
| [**gluNewQuadric**](glunewquadric.md)                 | Creates a new quadric object.                                    |
| [**gluDeleteQuadric**](gludeletequadric.md)           | Deletes a quadric object.                                        |
| [*gluQuadricCallback*](gluquadric.md)                 | Associates a callback with a quadric object, for error handling. |
| [**gluQuadricNormals**](gluquadricnormals.md)         | Specifies normals: no normals, one per face, or one per vertex.  |
| [**gluQuadricOrientation**](gluquadricorientation.md) | Specifies direction of normals: outward or inward.               |
| [**gluQuadricTexture**](gluquadrictexture.md)         | Turns texture-coordinate generation on or off.                   |
| [**gluQuadricDrawstyle**](gluquadricdrawstyle.md)     | Specifies drawing style: polygons, lines, points, and so on.     |
| [**gluSphere**](glusphere.md)                         | Draws a sphere.                                                  |
| [**gluCylinder**](glucylinder.md)                     | Draws a cylinder or cone.                                        |
| [**gluPartialDisk**](glupartialdisk.md)               | Draws an arc.                                                    |
| [**gluDisk**](gludisk.md)                             | Draws a circle or disk.                                          |



 

You can use one quadric object for all quadrics you want to render in similar ways. The following code sample uses two quadric objects to draw four quadrics, two of them textured.


```C++
GLUquadricObj    *texturedQuad, *plainQuad; 
 
texturedQuad = gluNewQuadric(void); 
gluQuadricTexture(texturedQuad, GL_TRUE); 
gluQuadricOrientation(texturedQuad, GLU_OUTSIDE); 
gluQuadricDrawStyle(texturedQuad, GLU_FILL); 
 
plainQuad = gluNewQuadric(void); 
gluQuadricDrawStyle(plainQuad, GLU_LINE); 
 
glColor3f (1.0, 1.0, 1.0); 
 
gluSphere(texturedQuad, 5.0, 20, 20); 
glTranslatef(10.0, 10.0, 0.0); 
gluCylinder(texturedQuad, 2.5, 5, 5, 10, 10); 
glTranslatef(10.0, 10.0, 0.0); 
gluDisk(plainQuad, 2.0, 5.0, 10, 10); 
glTranslatef(10.0, 10.0, 0.0); 
gluSphere(plainQuad, 5.0, 20, 20);
```



 

 




