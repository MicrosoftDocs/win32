---
title: Performing Selection and Feedback
description: Performing Selection and Feedback
ms.assetid: 908114b3-ac0e-4fd5-ad28-137e6af7ffc7
keywords:
- OpenGL,selection
- OpenGL,feedback
- OpenGL,rendering
- selection mode OpenGL
- feedback mode OpenGL
- rendering mode OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Performing Selection and Feedback

Selection, feedback, and rendering are mutually exclusive modes of operation. Rendering is the normal, default mode during which fragments are produced by rasterization.

In selection and feedback modes, no fragments are produced; therefore, no framebuffer modification occurs. In selection mode, you can determine which primitives will be drawn into some region of a window; in feedback mode, information about primitives that will be rasterized is fed back to the application.

You select among these three modes with [**glRenderMode**](glrendermode.md).

-   [Selection](selection.md)
-   [Feedback](feedback.md)
-   [Selection and Feedback Reference](selection-and-feedback-reference.md)

 

 




