---
title: Porting Viewports, Screenmasks, and Scrboxes
description: The following IRIS GL viewport functions have no OpenGL equivalent
ms.assetid: 223e9b5b-1ddd-45a6-8489-b262d0207a5a
keywords:
- IRIS GL porting,viewport functions
- porting from IRIS GL,viewport functions
- porting to OpenGL from IRIS GL,viewport functions
- OpenGL porting from IRIS GL,viewport functions
- viewport functions
ms.topic: article
ms.date: 05/31/2018
---

# Porting Viewports, Screenmasks, and Scrboxes

The following IRIS GL viewport functions have no OpenGL equivalent:

-   **reshapeviewport**
-   **scrbox**
-   **getscrbox**

With the IRIS GL **viewport** function, you specify the x coordinates (in pixels) for the left and right of a viewport rectangle and the y coordinates for the top and bottom. With the OpenGL [**glViewport**](glviewport.md) function, however, you specify the x and y coordinates (in pixels) of the lower-left corner of the viewport rectangle along with its width and height.

The following table lists IRIS GL viewport functions and their equivalent OpenGL functions.



| IRIS GL function                          | OpenGL function                                                                                         | Meaning                      |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------|------------------------------|
| **viewport** ( left, right, bottom, top ) | [**glViewport**](glviewport.md) ( x, y, width, height )                                                | Sets the viewport.           |
| **popviewportpushviewport**<br/>    | [**glPopAttrib**](glpopattrib.md)[**glPushAttrib**](glpushattrib.md) ( GL\_VIEWPORT\_BIT )<br/> | Pushes and pops the stack.   |
| **getviewport**                           | [**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) ( GL\_VIEWPORT )               | Returns viewport dimensions. |



 

??

 

 





