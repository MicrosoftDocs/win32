---
title: Rendering Simple Surfaces
description: The GLU library includes a set of functions for drawing various simple surfaces (spheres, cylinders, disks, and parts of disks) in a variety of styles and orientations. These functions are described in detail in the OpenGL Reference Manual.
ms.assetid: 403bdf8d-de4c-49e2-87d0-11109061b4c2
keywords:
- OpenGL Utility (GLU),simple surfaces
- GLU (OpenGL Utility),simple surfaces
- simple surfaces OpenGL
- OpenGL Utility (GLU),spheres
- GLU (OpenGL Utility),spheres
- spheres OpenGL
- OpenGL Utility (GLU),cylinders
- GLU (OpenGL Utility),cylinders
- cylinders OpenGL
- OpenGL Utility (GLU),disks
- GLU (OpenGL Utility),disks
- disks OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Rendering Simple Surfaces

The GLU library includes a set of functions for drawing various simple surfaces (spheres, cylinders, disks, and parts of disks) in a variety of styles and orientations. These functions are described in detail in the *OpenGL Reference Manual*.

**To render simple surfaces**

1.  Create a quadric object with [**gluNewQuadric**](glunewquadric.md).

    To destroy this object when you're finished with it, use [**gluDeleteQuadric**](gludeletequadric.md).

2.  Specify the desired rendering style, as listed below, with the appropriate function (unless you're satisfied with the default values):
    -   Whether surface normals should be generated, and if so, whether there should be one normal per vertex or one normal per face: [**gluQuadricNormals**](gluquadricnormals.md)
    -   Whether texture coordinates should be generated: [**gluQuadricTexture**](gluquadrictexture.md)
    -   Which side of the quadric should be considered the outside and which the inside: [**gluQuadricOrientation**](gluquadricorientation.md)
    -   Whether the quadric should be drawn as a set of polygons, lines, or points: [**gluQuadricDrawStyle**](gluquadricdrawstyle.md)
3.  After specifying the rendering style, invoke the rendering function for the desired type of quadric object: [**gluSphere**](glusphere.md), [**gluCylinder**](glucylinder.md), [**gluDisk**](gludisk.md), or [**gluPartialDisk**](glupartialdisk.md).

    If an error occurs during rendering, the error-handling function you've specified with [*gluQuadricCallBack*](gluquadric.md) is invoked.

Use the *\*Radius*, *height*, and similar arguments, rather than the [**glScale**](glscale.md) function, to scale the quadrics, so that you don't have to renormalize any unit-length normals that are generated. To force lighting calculations at a finer granularity, especially if the material specularity is high, set the *loops* and *stacks* arguments to values other than 1.

 

 




