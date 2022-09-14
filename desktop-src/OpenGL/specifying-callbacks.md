---
title: Specifying Callbacks
description: You can specify up to five callback functions for a tessellation.
ms.assetid: b49a8400-8111-450d-a2d7-c313a898a213
keywords:
- OpenGL Utility (GLU),specifying callback functions
- GLU (OpenGL Utility),specifying callback functions
ms.topic: article
ms.date: 05/31/2018
---

# Specifying Callbacks

You can specify up to five callback functions for a tessellation. Any functions that you do not specify are not called during the tessellation, and you do not get any information they might have returned. You specify the callback functions with [*gluTessCallback*](glutess.md).

The **gluTessCallback** function associates the callback function *fn* with the tessellation object *tessobj*. The type of the callback is determined by the parameter *type*, which can be **GLU\_BEGIN**, **GLU\_EDGE\_FLAG**, **GLU\_VERTEX**, **GLU\_END**, or **GLU\_ERROR**. The five possible callback functions have the following prototypes.



| Callback function   | Prototype                                    |
|---------------------|----------------------------------------------|
| **GLU\_BEGIN**      | **void** **begin**(**GLenum***type* );       |
| **GLU\_EDGE\_FLAG** | **void** **edgeFlag**(**GLboolean***flag* ); |
| **GLU\_VERTEX**     | **void** **vertex**(**void \****data* );     |
| **GLU\_END**        | **void** **end**( *void* );                  |
| **GLU\_ERROR**      | **void** **error**(**GLenum***errno* );      |



 

To change a callback function, call [*gluTessCallback*](glutess.md) with the new function. To eliminate a callback function without replacing it with a new one, pass **gluTessCallback** a null pointer for the appropriate function.

As tessellation proceeds, the callback functions are called in a manner similar to the way you would use the OpenGL functions [**glBegin**](glbegin.md), [glEdgeFlag](gledgeflag-functions.md), [glVertex](glvertex-functions.md), and [**glEnd**](glend.md).

The **GLU\_BEGIN** callback function is invoked with one of three possible parameters:

-   GL\_TRIANGLE\_FAN
-   GL\_TRIANGLE\_STRIP
-   GL\_TRIANGLES

After calling the **GLU\_BEGIN** callback function, and before calling the callback function associated with **GLU\_END**, some combination of the **GLU\_EDGE\_FLAG** and **GLU\_VERTEX** callbacks is invoked. The associated vertices and edge flags are interpreted exactly as they are in OpenGL between **glBegin**(GL\_TRIANGLE\_FAN), **glBegin**(GL\_TRIANGLE\_STRIP), or **glBegin**(GL\_TRIANGLES**)** and the matching **glEnd**.

Because edge flags make no sense in a triangle fan or triangle strip, if there is a callback function associated with **GLU\_EDGE\_FLAG**, the **GLU\_BEGIN** callback is called only with **GL\_TRIANGLES**. The **GLU\_EDGE\_FLAG** callback function works analogously to the OpenGL [glEdgeFlag](gledgeflag-functions.md) function.

If there is an error during the tessellation, the error callback function is invoked. The error callback function is passed a GLU error number. You can obtain a character string describing the error with the [**gluErrorString**](gluerrorstring.md) function.

 

 




