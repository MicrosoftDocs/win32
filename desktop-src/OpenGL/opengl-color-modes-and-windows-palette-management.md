---
title: OpenGL Color Modes and Windows Palette Management
description: The Microsoft implementation of OpenGL in Windows supports two color pixel data modes RGBA and color-index modes. Windows provide two analogous ways of handling color true color and palette management.
ms.assetid: 4a731119-8704-4ae1-a564-4a1955051236
keywords:
- OpenGL on Windows,color modes
- OpenGL on Windows,palette management
- palette management OpenGL
- color modes OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# OpenGL Color Modes and Windows Palette Management

The Microsoft implementation of OpenGL in Windows supports two color pixel data modes: RGBA and color-index modes. Windows provide two analogous ways of handling color: true color and palette management.

True-color devices, able to accept 16, 24, or more bits of color information per pixel, can display tens of thousands, tens of millions, or more colors simultaneously. Complexities arise, however, when an application has to manage RGBA or color-index mode on a palette-type device. Palette-type devices, such as a 256-color VGA display, are limited in the number of colors they can display simultaneously. Applications must handle a number of tricky details to successfully use palette-type devices. Because color-index mode programs don't use a hardware palette, they are more difficult to use with true-color devices than programs using the RGBA mode.

 

 




