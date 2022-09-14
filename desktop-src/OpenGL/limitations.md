---
title: Limitations
description: Limitations
ms.assetid: 5f41620d-dde0-4e82-92f0-ada9d4acf127
keywords:
- OpenGL on Windows,limitations
ms.topic: article
ms.date: 05/31/2018
---

# Limitations

The generic implementation has the following limitations:

-   Printing.

    You can print an OpenGL image directly to a printer using metafiles only. For more information, see [Printing an OpenGL Image](printing-an-opengl-image.md).

-   OpenGL and GDI graphics cannot be mixed in a double-buffered window.

    An application can directly draw both OpenGL graphics and GDI graphics into a single-buffered window, but not into a double-buffered window.

-   There are no per-window hardware color palettes.

    Windows has a single system hardware color palette, which applies to the whole screen. An OpenGL window cannot have its own hardware palette, but can have its own logical palette. To do so, it must become a palette-aware application. For more information, see [OpenGL Color Modes and Windows Palette Management](opengl-color-modes-and-windows-palette-management.md).

-   There is no direct support for the Clipboard, dynamic data exchange (DDE), or OLE.

    A window with OpenGL graphics does not directly support these Windows capabilities. There are workarounds, however, for using the Clipboard. For more information, see [Copying an OpenGL Image to the Clipboard](copying-an-opengl-image-to-the-clipboard.md).

-   The Inventor 2.0 C++ class library is not included.

    The Inventor class library, built on top of OpenGL, provides higher-level constructs for programming 3-D graphics. It is not included in the current version of Microsoft's implementation of OpenGL for Windows.

-   There is no support for the following pixel format features: stereoscopic images, alpha bitplanes, and auxiliary buffers.

    There is, however, support for several ancillary buffers including: stencil buffer, accumulation buffer, back buffer (double buffering), overlay and underlay plane buffer, and depth (z-axis) buffer.

 

 




