---
title: Porting NURBS Objects
description: OpenGL treats NURBS as objects, similar to the way it treats quadrics you create a NURBS object and then specify how it should be rendered. The following table lists the OpenGL GLU functions for managing NURBS objects.
ms.assetid: baddf81b-219f-44bb-aa17-37404028b258
keywords:
- IRIS GL porting,NURBS objects
- porting from IRIS GL,NURBS objects
- porting to OpenGL from IRIS GL,NURBS objects
- OpenGL porting from IRIS GL,NURBS objects
- NURBS objects
- NURBS (Non-Uniform Rational B-Spline)
- Non-Uniform Rational B-Spline (NURBS)
ms.topic: article
ms.date: 05/31/2018
---

# Porting NURBS Objects

OpenGL treats NURBS as objects, similar to the way it treats quadrics: you create a NURBS object and then specify how it should be rendered. The following table lists the OpenGL GLU functions for managing NURBS objects.



| OpenGL GLU function                                      | Meaning                                                        |
|----------------------------------------------------------|----------------------------------------------------------------|
| [**gluNewNurbsRenderer**](glunewnurbsrenderer.md)       | Creates a new NURBS object.                                    |
| [**gluDeleteNurbsRenderer**](gludeletenurbsrenderer.md) | Deletes a NURBS object.                                        |
| [*gluNurbsCallback*](glunurbs.md)                       | Associates a callback with a NURBS object, for error handling. |



 

When porting IRIS GL NURBS code to OpenGL, keep the following points in mind:

-   NURBS control points are floats, not doubles.
-   The stride parameter is counted in floats, not bytes.
-   If you're using lighting and you're not specifying normals, call [**glEnable**](glenable.md) with GL\_AUTO\_NORMAL as the parameter to generate normals automatically.

??

 

 




