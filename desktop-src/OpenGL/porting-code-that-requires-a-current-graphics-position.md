---
title: Port code that needs a current graphics position
description: OpenGL does not maintain a current graphics position. IRIS GL functions that depend on the current graphics position, such as move, draw, and rmv, have no equivalents in OpenGL.
ms.assetid: d6c42d9c-6fbb-4b72-8097-285d19b619c2
keywords:
- IRIS GL porting,current graphics position
- porting from IRIS GL,current graphics position
- porting to OpenGL from IRIS GL,current graphics position
- OpenGL porting from IRIS GL,current graphics position
- current graphics position
- raster positions
ms.topic: article
ms.date: 05/31/2018
---

# Port code that needs a current graphics position

OpenGL does not maintain a current graphics position. IRIS GL functions that depend on the current graphics position, such as **move**, **draw**, and **rmv**, have no equivalents in OpenGL.

Older versions of IRIS GL included drawing commands that relied upon the current graphics position, though their use has been discouraged. You will need to rewrite your code if you relied on the current graphics position in any way, or used any of the following routines:

-   **draw** and **move**
-   **pmv**, **pdr**, and **pclos**
-   **rdr**, **rmv**, **rpdr**, and **rpmv**
-   **getgpos**

OpenGL has a concept of raster position that corresponds to IRIS GL's current character position. For more information on raster positioning, see [Porting Pixel Operations](porting-pixel-operations.md).

This topic includes information on the following.

-   [Porting Screen and Buffer Clearing Commands](porting-screen-and-buffer-clearing-commands.md)
-   [Porting Matrix and Transformation Functions](porting-matrix-and-transformation-functions.md)
-   [Porting MSINGLE Mode Code](porting-msingle-mode-code.md)
-   [Porting Functions that Get Matrices and Transformations](porting-functions-that-get-matrices-and-transformations.md)
-   [Porting Viewports, Screenmasks, and Scrboxes](porting-viewports--screenmasks--and-scrboxes.md)
-   [Porting Clipping Planes](porting-clipping-planes.md)

 

 




