---
title: Framebuffer Operations
description: To select the buffer into which color values are written, use glDrawBuffer.
ms.assetid: 5469a183-1dc0-4ec2-bd7e-54060b5a2876
keywords:
- OpenGL processing pipeline,framebuffer operations
- framebuffers,operations
ms.topic: article
ms.date: 05/31/2018
---

# Framebuffer Operations

To select the buffer into which color values are written, use [**glDrawBuffer**](gldrawbuffer.md). You use four different functions to mask the writing of bits to each of the logical framebuffers after all per-fragment operations have been performed:

-   [**glIndexMask**](glindexmask.md)
-   [**glColorMask**](glcolormask.md)
-   [**glDepthMask**](gldepthmask.md)
-   [**glStencilMask**](glstencilmask.md)

The [**glAccum**](glaccum.md) function controls the operation of the accumulation buffer. Finally, [**glClear**](glclear.md) sets every pixel in a specified subset of the buffers to the value specified with [**glClearColor**](glclearcolor.md), [**glClearIndex**](glclearindex.md), [**glClearDepth**](glcleardepth.md), [**glClearStencil**](glclearstencil.md), or [**glClearAccum**](glclearaccum.md).

 

 




