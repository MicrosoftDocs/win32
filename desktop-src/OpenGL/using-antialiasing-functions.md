---
title: Using Antialiasing Functions
description: The following table lists IRIS GL antialiasing functions and their equivalent OpenGL functions.
ms.assetid: d54990b6-5645-4389-82ca-7d7f0a7fd7e9
keywords:
- IRIS GL porting,antialiasing
- porting from IRIS GL,antialiasing
- porting to OpenGL from IRIS GL,antialiasing
- OpenGL porting from IRIS GL,antialiasing
- antialiasing
ms.topic: article
ms.date: 05/31/2018
---

# Using Antialiasing Functions

The following table lists IRIS GL antialiasing functions and their equivalent OpenGL functions.



| IRIS GL function | OpenGL function                                      | Meaning                           |
|------------------|------------------------------------------------------|-----------------------------------|
| **pntsmooth**    | [**glEnable**](glenable.md) ( GL\_POINT\_SMOOTH )   | Enables antialiasing of points.   |
| **linesmooth**   | **glEnable**( GL\_LINE\_SMOOTH )                     | Enables antialiasing of lines.    |
| **polysmooth**   | [**glEnable**](glenable.md) ( GL\_POLYGON\_SMOOTH ) | Enables antialiasing of polygons. |



 

Use the equivalent [**glDisable**](gldisable.md) calls to turn off antialiasing.

In IRIS GL, you can control the quality of the antialiasing by calling:


```C++
linesmooth(SML_ON + SML_SMOOTHER);
```



OpenGL provides similar controluse [**glHint**](glhint.md):


```C++
glHint(GL_POINT_SMOOTH_HINT, hintMode); 
glHint(GL_LINE_SMOOTH_HINT, hintMode); 
glHint(GL_POLYGON_SMOOTH_HINT, hintMode);
```



where *hintMode* is one of the following:

-   GL\_NICEST (Use the highest quality smoothing.)
-   GL\_FASTEST (Use the most efficient smoothing.)
-   GL\_DONT\_CARE

IRIS GL also permits end-correction by calling:


```C++
linesmooth(SML_ON +  SML_END_CORRECT);
```



OpenGL has no equivalent for this function.

 

 




