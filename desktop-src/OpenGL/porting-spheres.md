---
title: Porting Spheres
description: When porting spheres to OpenGL, keep the following points in mind
ms.assetid: ca6bb515-076d-45fc-bcdd-3d71877560fb
keywords:
- IRIS GL porting,spheres
- porting from IRIS GL,spheres
- porting to OpenGL from IRIS GL,spheres
- OpenGL porting from IRIS GL,spheres
- drawing functions,spheres
- spheres
ms.topic: article
ms.date: 05/31/2018
---

# Porting Spheres

When porting spheres to OpenGL, keep the following points in mind:

-   You cannot control the type of primitives used to draw the sphere. You can control drawing precision in another way: use the slices and stacks parameters. Slices are longitudinal; stacks are latitudinal.
-   Spheres are drawn centered at the origin. Instead of specifying the location, as you do with the IRIS GL **sphdraw** function, precede a call to the GLU [**gluSphere**](glusphere.md) function with a translation.
-   The sphere library is not yet available for OpenGL.

The following table lists the IRIS GL functions for drawing spheres and their equivalent GLU functions where available.



| IRIS GL function | GLU function                                 | Meaning                                       |
|------------------|----------------------------------------------|-----------------------------------------------|
| **sphobj**       | [**gluNewQuadric**](glunewquadric.md)       | Creates a new sphere object.                  |
| **sphfree**      | [**gluDeleteQuadric**](gludeletequadric.md) | Deletes sphere object and free memory used.   |
| **sphdraw**      | [**gluSphere**](glusphere.md)               | Draws a sphere.                               |
| **sphmode**      |                                              | Sets sphere attributes.                       |
| **sphrotmatrix** |                                              | Controls sphere orientation.                  |
| **sphgnpolys**   |                                              | Returns number of polygons in current sphere. |



 

??

 

 




