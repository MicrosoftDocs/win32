---
title: Pixel Formats
description: Pixel Formats
ms.assetid: '2e179340-c487-4b72-a22e-078b800af11d'
keywords:
- OpenGL on Windows,pixels
ms.topic: article
ms.date: 05/31/2018
---

# Pixel Formats

A *pixel format* specifies several properties of an OpenGL drawing surface. Some of the properties specified by a pixel format are:

-   Whether the pixel buffer is single- or double-buffered.
-   Whether the pixel data is in RGBA or color-index form.
-   The number of bits used to store color data.
-   The number of bits used for the depth (z-axis) buffer.
-   The number of bits used for the stencil buffer.
-   The number of overlay and underlay planes.
-   Various visibility masks.

Microsoft's implementation of OpenGL for Windows uses the [**PIXELFORMATDESCRIPTOR**](/windows/win32/api/wingdi/ns-wingdi-pixelformatdescriptor) data structure to convey pixel format data. The structure's members specify the preceding properties and several others.

A given device context can support several pixel formats. Windows identifies the pixel formats that a device context supports with consecutive one-based index values (1, 2, 3, 4, and so on). A device context can have just one current pixel format, chosen from the set of pixel formats it supports.

Each window has its own current pixel format in OpenGL in Windows. This means, for example, that an application can simultaneously display RGBA and color-index OpenGL windows, or single- and double-buffered OpenGL windows. This per-window pixel format capability is limited to OpenGL windows.

Typically, you obtain a device context, set the device context's pixel format, and then create an OpenGL rendering context suitable for that device.

> [!Note]  
> You set the pixel format before creating a rendering context because the rendering context inherits the device context's pixel format.

 

## Related topics

<dl> <dt>

[Pixel Format Functions](pixel-format-functions.md)
</dt> </dl>

 

 




