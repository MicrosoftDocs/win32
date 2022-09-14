---
title: Using Tessellation Objects
description: As a complex polygon is being described and tessellated, it requires associated data, such as the vertices, edges, and callback functions.
ms.assetid: b6102e25-280c-4d0d-9350-d0038d1a0306
keywords:
- OpenGL Utility (GLU),tessellation objects
- GLU (OpenGL Utility),tessellation objects
- tessellation objects OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Using Tessellation Objects

As a complex polygon is being described and tessellated, it requires associated data, such as the vertices, edges, and callback functions. All this data is tied to a single tessellation object. To tessellate a polygon, you first use the [**gluNewTess**](glunewtess.md) function which creates a new tessellation object and returns a pointer to it. A null pointer is returned if the function fails.

If you no longer need a tessellation object, you can delete it and free all associated memory with [**gluDeleteTess**](gludeletetess.md).

You can reuse a single tessellation object for all your tessellations. This object is required only because library functions may need to do their own tessellations, and they should be able to do so without interfering with any tessellation that your program is performing. Multiple tessellation objects are also useful if you want to use different sets of callbacks for different tessellations. Typically, however, you allocate a single tessellation object and use it for all the tessellations. There's no real need to free it, because it uses a small amount of memory. On the other hand, if you're writing a library function that uses GLU tessellation, be careful to free any tessellation objects you create.

 

 




