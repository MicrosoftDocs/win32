---
title: Blending
description: Blending combines a fragment's R, G, B, and A values with those stored in the framebuffer at the corresponding location.
ms.assetid: 02a78ce3-bb0a-4e9c-a2b1-6da8e95bcee5
keywords:
- OpenGL processing pipeline,blending
- blending OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Blending

Blending combines a fragment's R, G, B, and A values with those stored in the framebuffer at the corresponding location. The blending, which is performed only in RGBA mode, depends on the alpha value of the fragment and that of the corresponding currently stored pixel; it may also depend on the RGB values. You control blending with [**glBlendFunc**](glblendfunc.md), with which you indicate the source and destination blending factors.

 

 




