---
title: Porting Triangles
description: You can draw three types of triangles in OpenGL separate triangles, triangle strips, and triangle fans.
ms.assetid: 48617892-c9a0-4c67-b42e-afa4243023e7
keywords:
- IRIS GL porting,triangles
- porting from IRIS GL,triangles
- porting to OpenGL from IRIS GL,triangles
- OpenGL porting from IRIS GL,triangles
- drawing functions,triangles
- triangles
ms.topic: article
ms.date: 05/31/2018
---

# Porting Triangles

You can draw three types of triangles in OpenGL: separate triangles, triangle strips, and triangle fans.

OpenGL has no equivalent for the IRIS GL **swaptmesh** function. You can achieve the same effect using a combination of triangles, triangle strips, and triangle fans.

The following table lists the IRIS GL functions for drawing triangles and their equivalent OpenGL functions.



| IRIS GL function           | Equivalent glBegin parameter | Meaning                                       |
|----------------------------|------------------------------|-----------------------------------------------|
|                            | GL\_TRIANGLES                | Triples of vertices interpreted as triangles. |
| **bgntmesh**, **endtmesh** | GL\_TRIANGLE\_STRIP          | Linked strips of triangles.                   |
|                            | GL\_TRIANGLE\_FAN            | Linked fans of triangles.                     |



 

??

 

 




