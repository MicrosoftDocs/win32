---
title: Porting Clipping Planes
description: OpenGL implements clipping planes similarly to IRIS GL. In addition, in OpenGL you can query clipping planes. The following table lists IRIS GL clipping plane functions and their equivalent OpenGL functions.
ms.assetid: bfca59c3-b7ef-4545-8b8d-022ea782569b
keywords:
- IRIS GL porting,clipping planes
- porting from IRIS GL,clipping planes
- porting to OpenGL from IRIS GL,clipping planes
- OpenGL porting from IRIS GL,clipping planes
- clipping planes
ms.topic: article
ms.date: 05/31/2018
---

# Porting Clipping Planes

OpenGL implements clipping planes similarly to IRIS GL. In addition, in OpenGL you can query clipping planes. The following table lists IRIS GL clipping plane functions and their equivalent OpenGL functions.



| IRIS GL function                          | OpenGL function                                                                               | Meaning                                  |
|-------------------------------------------|-----------------------------------------------------------------------------------------------|------------------------------------------|
| **clipplane** (i, **CP\_ON**, params)     | [**glEnable**](glenable.md) ( GL\_CLIP\_PLANEi )                                             | Enables clipping on plane i.             |
| **clipplane**( i, **CP\_DEFINE**, plane ) | [**glClipPlane**](glclipplane.md) ( GL\_CLIP\_PLANEi, plane )                                | Defines clipping plane.                  |
|                                           | [**glGetClipPlane**](glgetclipplane.md)                                                      | Returns clipping plane equation.         |
|                                           | [**glIsEnabled**](glisenabled.md) ( GL\_CLIP\_PLANEi )                                       | Returns true if clip plane i is enabled. |
| **scrmask**                               | [**glScissor**](glscissor.md)                                                                | Defines the scissor box.                 |
| **getscrmask**                            | [**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) ( GL\_SCISSOR\_BOX ) | Returns the current scissor box.         |



 

To turn on the scissor test, call **glEnable** using GL\_SCISSOR\_BOX as the parameter.

??

 

 




