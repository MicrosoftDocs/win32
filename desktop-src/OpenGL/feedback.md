---
title: Feedback
description: In feedback mode, each primitive to be rasterized generates a block of values that is copied into the feedback array.
ms.assetid: 92f14fe2-71f7-4b59-94a5-9669e986fb30
keywords:
- feedback mode,OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Feedback mode

In feedback mode, each primitive to be rasterized generates a block of values that is copied into the feedback array. Supply this array with [**glFeedbackBuffer**](glfeedbackbuffer.md), which you must call before putting OpenGL into feedback mode. Each block of values begins with a code indicating the primitive type, followed by values that describe the primitive's vertices and associated data. Entries are also written for bitmaps and pixel rectangles. Values are not guaranteed to be written into the feedback array until you call [**glRenderMode**](glrendermode.md) to take OpenGL out of feedback mode. You can use [**glPassThrough**](glpassthrough.md) to supply a marker that is returned in feedback mode as if it were a primitive.

 

 




