---
title: Fragments
description: Fragments
ms.assetid: bc400251-32c4-4477-ba0c-a0046fe85327
keywords:
- OpenGL,fragments
- OpenGL processing pipeline,fragments
- fragments OpenGL
- framebuffers,fragments modifying pixels
ms.topic: article
ms.date: 05/31/2018
---

# Fragments

A fragment produced by rasterization modifies the corresponding pixel in the framebuffer only if it passes the following tests:

-   [Pixel ownership test](pixel-ownership-test.md)
-   [Scissor test](scissor-test.md)
-   [Alpha test](alpha-test.md)
-   [Stencil test](stencil-test.md)
-   [Depth-buffer test](depth-buffer-test.md)

If it passes, the fragment's data can replace the existing framebuffer values, or you can combine it with existing data in the framebuffer, depending on the state of certain modes. You can combine the fragment with data in the framebuffer by:

-   [Blending](blending.md)
-   [Dithering](dithering.md)
-   [Logical operations](logical-operations.md)

 

 




