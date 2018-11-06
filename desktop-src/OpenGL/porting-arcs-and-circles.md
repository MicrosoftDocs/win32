---
title: Porting Arcs and Circles
description: With OpenGL, filled arcs and circles are drawn with the same calls as unfilled arcs and circles. The following table lists the IRIS GL arc and circle functions and their equivalent OpenGL (GLU) functions.
ms.assetid: b3458192-9cb6-4376-8136-45467584d3d4
keywords:
- IRIS GL porting,arcs
- porting from IRIS GL,arcs
- porting to OpenGL from IRIS GL,arcs
- OpenGL porting from IRIS GL,arcs
- drawing functions,arcs
- IRIS GL porting,circles
- porting from IRIS GL,circles
- porting to OpenGL from IRIS GL,circles
- OpenGL porting from IRIS GL,circles
- drawing functions,circles
ms.topic: article
ms.date: 05/31/2018
---

# Porting Arcs and Circles

With OpenGL, filled arcs and circles are drawn with the same calls as unfilled arcs and circles. The following table lists the IRIS GL arc and circle functions and their equivalent OpenGL (GLU) functions.



| IRIS GL function | OpenGL function                          | Meaning                 |
|------------------|------------------------------------------|-------------------------|
| **arcarcf**      | [**gluPartialDisk**](glupartialdisk.md) | Draws an arc.           |
| **circcircf**    | [**gluDisk**](gludisk.md)               | Draws a circle or disk. |



 

You can do some things with OpenGL arcs and circles that you can't do with IRIS GL. OpenGL calls arcs and circles, disks and partial disks respectively.

When porting arcs and circles, keep the following points about OpenGL in mind:

-   Angles are measured in degrees, and not in tenths of degrees.
-   The start angle is measured from the positive y-axis, and not from the x-axis.
-   The sweep angle is now clockwise instead of counterclockwise.

??

 

 




