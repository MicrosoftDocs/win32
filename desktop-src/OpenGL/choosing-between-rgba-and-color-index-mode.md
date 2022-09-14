---
title: Choosing Between RGBA and Color-Index Mode
description: In general, use the RGBA mode for your OpenGL applications; it provides more flexibility than the color-index mode for effects such as shading, lighting, color mapping, fog, antialiasing, and blending.
ms.assetid: 13644a7c-bdc6-4dac-ba16-4723c72b15e5
keywords:
- OpenGL on Windows,RGBA mode
- OpenGL on Windows,color-index mode
- RGBA mode OpenGL
- color-index mode OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Choosing Between RGBA and Color-Index Mode

In general, use the RGBA mode for your OpenGL applications; it provides more flexibility than the color-index mode for effects such as shading, lighting, color mapping, fog, antialiasing, and blending.

Consider using the color-index mode in the following cases:

-   If you have a limited number of bitplanes available; the color-index mode can produce less-coarse shading than the RGBA mode.
-   If you are not concerned about using "real" colors; for example, using several colors in a topographic map to designate relative elevations.
-   When you're porting an existing application that uses color-index mode extensively.
-   When you want to use color-map animation and effects in your application. (This is not possible on true-color devices.)

 

 




