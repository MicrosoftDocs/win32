---
title: Pixels
description: Fragments are converted to pixels in the framebuffer.
ms.assetid: '1925b455-ae6e-4f95-899c-4bcac641f549'
keywords:
- OpenGL,pixels
- OpenGL processing pipeline,pixels
- pixels OpenGL
- framebuffers,converting fragments to pixels
ms.topic: article
ms.date: 05/31/2018
---

# Pixels

Fragments are converted to pixels in the framebuffer. The framebuffer is organized into a set of logical buffers the color, depth, stencil, and accumulation buffers. The color buffer itself consists of a front left, front right, back left, back right, and some number of auxiliary buffers. You can issue functions to control these buffers, and directly read or copy pixels from them. (Note that the particular OpenGL context you're using may not provide all these buffers.)

-   [Framebuffer Operations](framebuffer-operations.md)
-   [Reading or Copying Pixels](reading-or-copying-pixels.md)
-   [Pixels Reference](pixels-reference.md)

 

 




