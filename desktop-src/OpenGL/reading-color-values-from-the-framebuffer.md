---
title: Reading Color Values from the Framebuffer
description: When using functions that read back color values from the framebuffer, be aware of the differences between reading RGBA values and color-index values on true-color devices and on palette-based devices.
ms.assetid: 70a96f09-37e9-4dfe-a6e0-0223e0a04bac
keywords:
- OpenGL on Windows,reading color values from framebuffers
- reading color values from framebuffers OpenGL
- framebuffers,reading color values OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Reading Color Values from the Framebuffer

When using functions that read back color values from the framebuffer, be aware of the differences between reading RGBA values and color-index values on true-color devices and on palette-based devices.

On a true-color device:

-   RGBA values are limited to the channel in the device.
-   Color-index values are stored as RGBA values in the framebuffer. When using these values, you must perform an inverse translation from RGBA to the logical palette index. If two logical indexes have the same RGBA values, the wrong index can be returned.

On a palette-based device:

-   RGBA values are read from an index in the system palette. The logical index is obtained from an inverse table, and the RGBA components are extracted.
-   Color-index values are read from an index into the system palette and an inverse table is used to get the logical palette index.

 

 




