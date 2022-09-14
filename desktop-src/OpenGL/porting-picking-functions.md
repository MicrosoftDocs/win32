---
title: Porting Picking Functions
description: All IRIS GL picking functions have OpenGL equivalents, with the exception of clearhitcode. The following table lists the IRIS GL picking functions and their equivalent OpenGL functions.
ms.assetid: f8fbd0c2-14bf-47bc-be7f-eeef346dbac1
keywords:
- IRIS GL porting,picking
- porting from IRIS GL,picking
- porting to OpenGL from IRIS GL,picking
- OpenGL porting from IRIS GL,picking
- picking
ms.topic: article
ms.date: 05/31/2018
---

# Porting Picking Functions

All IRIS GL picking functions have OpenGL equivalents, with the exception of **clearhitcode**. The following table lists the IRIS GL picking functions and their equivalent OpenGL functions.



| IRIS GL function                | OpenGL function                                                                           | Meaning                                |
|---------------------------------|-------------------------------------------------------------------------------------------|----------------------------------------|
| **clearhitcode**                | Not supported.                                                                            | Clears global variable and hitcode.    |
| **pickselect**<br/>       | [**glRenderMode**](glrendermode.md) ( GL\_SELECT )                                       | Switches to selection or picking mode. |
| **endpickendselect**<br/> | [**glRenderMode**](glrendermode.md) ( GL\_RENDER )                                       | Switches to rendering mode.            |
| **picksize**                    | [**gluPickMatrix**](glupickmatrix.md)[**glSelectBuffer**](glselectbuffer.md)<br/> | Sets the return array.                 |
| **initnames**                   | [**glInitNames**](glinitnames.md)                                                        |                                        |
| **pushnamepopname**<br/>  | [**glPushName**](glpushname.md)[**glPopName**](glpopname.md)<br/>                 |                                        |
| **loadname**                    | [**glLoadName**](glloadname.md)                                                          |                                        |



 

For more information on picking, see [**gluPickMatrix**](glupickmatrix.md).

 

 





