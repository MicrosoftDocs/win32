---
title: Transforming to Window Coordinates
description: Before clip coordinates are converted to window coordinates, they are divided by the value of w to yield normalized device coordinates.
ms.assetid: 4c2d0bf6-89e8-485a-9080-c0599f989943
keywords:
- OpenGL processing pipeline,converting to window coordinates
- converting to window coordinates OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Transforming to Window Coordinates

Before clip coordinates are converted to window coordinates, they are divided by the value of *w* to yield normalized device coordinates. The viewport transformation applied to these normalized coordinates produces window coordinates. You control the viewport, which determines the area of the on-screen window that displays an image, with [**glDepthRange**](gldepthrange.md) and [**glViewport**](glviewport.md).

 

 




