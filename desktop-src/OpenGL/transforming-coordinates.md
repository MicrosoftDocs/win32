---
title: Transforming Coordinates
description: The OpenGL Utility library (GLU) provides several commonly used matrix transformation functions.
ms.assetid: 9ca32be8-3bc0-4fca-a58c-69a4800c3c55
keywords:
- OpenGL Utility (GLU),matrix transformation functions
- GLU (OpenGL Utility),matrix transformation functions
- matrix transformation functions OpenGL
- OpenGL Utility (GLU),transforming coordinates
- GLU (OpenGL Utility),transforming coordinates
- transforming coordinates OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Transforming Coordinates

The OpenGL Utility library (GLU) provides several commonly used matrix transformation functions. You can set up a two-dimensional orthographic viewing region with [**gluOrtho2D**](gluortho2d.md), a standard perspective view volume using [**gluPerspective**](gluperspective.md), or a view volume that is centered on a specified eyepoint with [**gluLookAt**](glulookat.md). Each of these functions creates the desired matrix and applies it to the current matrix using [**glMultMatrix**](glmultmatrix.md).

The [**gluPickMatrix**](glupickmatrix.md) function simplifies selection of a picking matrix by creating a matrix that restricts drawing to a small region of the viewport. If you re-render the scene in selection mode after this matrix has been applied, all objects that would be drawn near the cursor will be selected, and information about them will be stored in the selection buffer. For more information about selection mode, see "Performing Selection and Feedback" [Performing Selection and Feedback](performing-selection-and-feedback.md).

To determine where in the window an object is being drawn, use [**gluProject**](gluproject.md), which converts the specified object coordinates *objx*, *objy*, and *objz* into window coordinates using *modelMatrix*, *projMatrix*, and *viewport*. The result is stored in *winx*, *winy*, and *winz*. If the function succeeds, the return value is GL\_TRUE. If the function fails, the return value is GL\_FALSE.

The [**gluUnProject**](gluunproject.md) function performs the inverse conversion: it transforms the specified window coordinates *winx*, *winy*, and *winz* into object coordinates using *modelMatrix*, *projMatrix*, and *viewport*. The result is stored in *objx*, *objy*, and *objz*. If the function succeeds, the return value is GL\_TRUE. If the function fails, the return value is GL\_FALSE.

 

 




