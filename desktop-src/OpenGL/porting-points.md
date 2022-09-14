---
title: Porting Points
description: OpenGL has no command to draw a single point. Otherwise, porting point functions is straightforward. The following table lists IRIS GL functions for drawing points and their equivalent OpenGL functions.
ms.assetid: 348c7767-321a-43c6-bc88-7dc00f426f50
keywords:
- IRIS GL porting,points
- porting from IRIS GL,points
- porting to OpenGL from IRIS GL,points
- OpenGL porting from IRIS GL,points
- drawing functions,points
- points
ms.topic: article
ms.date: 05/31/2018
---

# Porting Points

OpenGL has no command to draw a single point. Otherwise, porting point functions is straightforward. The following table lists IRIS GL functions for drawing points and their equivalent OpenGL functions.



| IRIS GL function           | OpenGL function                                                   | Meaning                                                                                                                                              |
|----------------------------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| **pnt**                    |                                                                   | Draws a single point.                                                                                                                                |
| **bgnpoint**, **endpoint** | [**glBegin**](glbegin.md) ( GL\_POINTS ), [**glEnd**](glend.md) | Interprets vertices as points.                                                                                                                       |
| **pntsize**                | [**glPointSize**](glpointsize.md)                                | Sets point size in pixels.                                                                                                                           |
| **pntsmooth**              | [**glEnable**](glenable.md) ( GL\_POINT\_SMOOTH )                | Turns on point antialiasing. (For more information on point antialiasing, see [Porting Antialiasing Functions](porting-antialiasing-functions.md).) |



 

For information about related get functions, see [**glPointSize**](glpointsize.md).

??

 

 




