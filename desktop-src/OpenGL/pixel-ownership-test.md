---
title: Pixel Ownership Test
description: The pixel ownership test determines whether the current OpenGL context owns the pixel in the framebuffer corresponding to a particular fragment.
ms.assetid: aa9428a6-cc05-4df4-ba31-444f999006a8
keywords:
- OpenGL processing pipeline,pixel ownership test
- pixel ownership test OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Pixel Ownership Test

The pixel ownership test determines whether the current OpenGL context owns the pixel in the framebuffer corresponding to a particular fragment. If so, the fragment proceeds to the next test. If not, the window system determines whether the fragment is discarded or whether any further fragment operations will be performed with that fragment. With this test, the window system controls behavior when, for example, an OpenGL window is obscured.

 

 




