---
title: OpenGL Function Names
description: Many OpenGL functions are variations of each other, differing mostly in the data types of their arguments.
ms.assetid: 2d30e2e4-9671-4e57-962d-0328b13159f3
keywords:
- OpenGL,function names
- function names OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# OpenGL Function Names

Many OpenGL functions are variations of each other, differing mostly in the data types of their arguments. Some functions differ in the number of related arguments and whether those arguments can be specified as a vector or must be specified separately in a list. For example, if you use the **glVertex2f** function, you need to supply x- and y-coordinates as 32-bit floating-point numbers; with **glVertex3sv**, you must supply an array of three short (16-bit) integer values for x, y, and z. Only the base name of the function is used in the topics that follow. An asterisk indicates that there may be more to the actual function name than is shown. For example, [glVertex\*](glvertex-functions.md) stands for all the variations of the function you use to specify vertices: **glVertex2d**, **glVertex2f**, **glVertex2i**, and so on.

The effect of an OpenGL function can vary depending on whether certain modes are enabled. For example, you need to enable lighting if the lighting-related functions are to produce a properly lit object. To enable a particular mode, use the [**glEnable**](glenable.md) function and supply the appropriate constant to identify the mode (for example, GL\_LIGHTING). To disable a mode, use [**glDisable**](gldisable.md). See **glEnable** for a complete list of the modes that can be enabled.

 

 




