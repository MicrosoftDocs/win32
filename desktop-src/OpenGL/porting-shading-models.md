---
title: Porting Shading Models
description: Like IRIS GL, OpenGL lets you switch between smooth (Gouraud) shading and flat shading. The following table lists the IRIS GL shading and dithering functions and their equivalent OpenGL functions.
ms.assetid: 93e8f437-381f-4620-ad6f-52ce830d99b6
keywords:
- IRIS GL porting,shading
- porting from IRIS GL,shading
- porting to OpenGL from IRIS GL,shading
- OpenGL porting from IRIS GL,shading
- smooth shading
- Gouraud shading
- flat shading
ms.topic: article
ms.date: 05/31/2018
---

# Porting Shading Models

Like IRIS GL, OpenGL lets you switch between smooth (Gouraud) shading and flat shading. The following table lists the IRIS GL shading and dithering functions and their equivalent OpenGL functions.



| IRIS GL function                                   | OpenGL function                                                                                    | Meaning                      |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------|------------------------------|
| **shademodel**(FLAT)                               | [**glShadeModel**](glshademodel.md) ( GL\_FLAT )                                                  | Does flat shading.           |
| **shademodel**(GOURAUD)                            | **glShadeModel**( GL\_SMOOTH )                                                                     | Does smooth shading.         |
| **getsm**                                          | [**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) ( GL\_SHADE\_MODEL )      | Returns current shade model. |
| **dither**(DT\_ON) **dither**(DT\_OFF) <br/> | [**glEnable**](glenable.md) ( GL\_DITHER )[**glDisable**](gldisable.md)( GL\_DITHER )<br/> | Turns dithering on/off.      |



 

??

 

 





