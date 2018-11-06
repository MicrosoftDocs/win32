---
title: Porting Lines
description: Porting IRIS GL code that draws lines is fairly straightforward, though you should note the differences in the way OpenGL stipples. The following table lists IRIS GL functions for drawing lines and their equivalent OpenGL functions.
ms.assetid: de5fd544-5a64-44b5-8976-b96867e4006d
keywords:
- IRIS GL porting,lines
- porting from IRIS GL,lines
- porting to OpenGL from IRIS GL,lines
- OpenGL porting from IRIS GL,lines
- drawing functions,lines
- lines
ms.topic: article
ms.date: 05/31/2018
---

# Porting Lines

Porting IRIS GL code that draws lines is fairly straightforward, though you should note the differences in the way OpenGL stipples. The following table lists IRIS GL functions for drawing lines and their equivalent OpenGL functions.



| IRIS GL function                               | OpenGL function                                                                                         | Meaning                                                                                                                                      |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| **bgnclosedline**,**endclosedline**<br/> | [**glBegin**](glbegin.md) ( GL\_LINE\_LOOP )[**glEnd**](glend.md)<br/>                          | Draws a closed line.                                                                                                                         |
| **bgnline**                                    | [**glBegin**](glbegin.md) ( GL\_LINE\_STRIP )                                                          | Draws line segments.                                                                                                                         |
| **linewidth**                                  | [**glLineWidth**](gllinewidth.md)                                                                      | Sets line width.                                                                                                                             |
| **getlwidth**                                  | [**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) ( GL\_LINE\_WIDTH )            | Returns current line width.                                                                                                                  |
| **deflinestyle**,**setlinestyle**<br/>   | [**glLineStipple**](gllinestipple.md)                                                                  | Specifies a line stipple pattern.                                                                                                            |
| **lsrepeat**                                   | factor argument of **glLineStipple**                                                                    | Sets a repeat factor for the line style.                                                                                                     |
| **getlstyle**                                  | [**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) ( GL\_LINE\_STIPPLE\_PATTERN ) | Returns line stipple pattern.                                                                                                                |
| **getlsrepeat**                                | [**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) ( GL\_LINE\_STIPPLE\_REPEAT )  | Returns repeat factor.                                                                                                                       |
| **linesmooth**, **smoothline**                 | [**glEnable**](glenable.md) ( GL\_LINE\_SMOOTH )                                                       | Turns on line antialiasing (For more information on antialiasing, see [Porting Antialiasing Functions](porting-antialiasing-functions.md).) |



 

OpenGL doesn't use tables for line stipples; it maintains only one line-stipple pattern. You can use [**glPushAttrib**](glpushattrib.md) and [**glPopAttrib**](glpopattrib.md) to switch between different stipple patterns.

Older IRIS GL line style functions (such as **draw**, **lsbackup**, **getlsbackup**, and so on) are not supported by OpenGL.

For information on drawing antialiased lines, see [Porting Antialiasing Functions](porting-antialiasing-functions.md).

??

 

 





