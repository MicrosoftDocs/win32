---
title: Porting Color, Shading, and Writemask Code
description: Porting Color, Shading, and Writemask Code
ms.assetid: ffcf33b2-c3b8-4e89-9c2f-085b98cbb496
keywords:
- IRIS GL porting,color
- porting from IRIS GL,color
- porting to OpenGL from IRIS GL,color
- OpenGL porting from IRIS GL,color
- IRIS GL porting,shading
- porting from IRIS GL,shading
- porting to OpenGL from IRIS GL,shading
- OpenGL porting from IRIS GL,shading
- IRIS GL porting,writemask
- porting from IRIS GL,writemask
- porting to OpenGL from IRIS GL,writemask
- OpenGL porting from IRIS GL,writemask
ms.topic: article
ms.date: 05/31/2018
---

# Porting Color, Shading, and Writemask Code

When porting color, shading, and writemask code to OpenGL, keep the following points in mind:

-   Though you can set color-map indexes with the OpenGL [glIndex](glindex-functions.md) function, OpenGL does not have a function for loading color-map indexes.
-   Color values are normalized to their data type. (For information about color values, see [glColor](glcolor-functions.md)).
-   There is no simple equivalent for **cpack**.
-   You may have to translate code that includes the **c** or **color** functions to [**glClearColor**](glclearcolor.md) or [**glClearIndex**](glclearindex.md) instead of **glColor** or **glIndex**.
-   The RGBA writemask applies to each component but not for each bit.
-   IRIS GL provides defined color constants: BLACK, BLUE, RED, GREEN, MAGENTA, CYAN, YELLOW, and WHITE. OpenGL does not provide these constants.

This topic includes information on the following.

-   [Porting Color Calls](porting-color-calls.md)
-   [Porting Shading Models](porting-shading-models.md)

 

 




