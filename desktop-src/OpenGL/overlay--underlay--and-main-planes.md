---
title: Overlay, Underlay, and Main Planes
description: You can use hardware layer planes (overlay and underlay planes) in your applications.
ms.assetid: fd9401b3-f2a8-4384-92e8-61b346216542
keywords:
- OpenGL on Windows,hardware layer planes
- hardware layer planes OpenGL
- overlay planes OpenGL
- underlay planes OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Overlay, Underlay, and Main Planes

You can use hardware layer planes (overlay and underlay planes) in your applications. With Windows, pixel formats describe the pixel configurations of a graphics device. Each pixel format describes the depth and other characteristics of the main color buffers and describes additional buffers (such as depth, accumulation, stencil, and auxiliary) that the main plane uses. Pixel formats are now extended to include overlay and underlay buffers.

Layer planes always have a front-left color buffer and also can include front-right and back color buffers. Each layer plane has a specific rendering context to render into the layer buffers. You cannot use GDI drawing functions in layer planes.

A window manages the color buffers of layer planes similarly to the way it manages main-plane color buffers. You can display multiple windows with overlay and/or underlay planes at the same time. You cannot have free-floating overlay windows that can move over any window in the main drawing plane. In addition, because it would obscure underlying planes in a window at all times, you cannot use hardware pop-up planes that have no transparent color.

Each layer plane in a window has an associated palette. You can set the palette of a color-index layer plane, but the palette of an RGBA color plane is fixed. You must realize the appropriate palette when a window is in the foreground. Layer planes have a transparent pixel color or index that enables any underlying layer planes to show through.

You can copy the state of a rendering context to another rendering context in a separate layer plane. You can also share display lists among rendering contexts in different layer planes.

The following functions are used with layer planes:

-   [**wglCopyContext**](/windows/desktop/api/wingdi/nf-wingdi-wglcopycontext)
-   [**wglCreateLayerContext**](/windows/desktop/api/wingdi/nf-wingdi-wglcreatelayercontext)
-   [**wglDescribeLayerPlane**](/windows/desktop/api/wingdi/nf-wingdi-wgldescribelayerplane)
-   [**wglGetLayerPaletteEntries**](/windows/desktop/api/wingdi/nf-wingdi-wglgetlayerpaletteentries)
-   [**wglRealizeLayerPalette**](/windows/desktop/api/wingdi/nf-wingdi-wglrealizelayerpalette)
-   [**wglSetLayerPaletteEntries**](/windows/desktop/api/wingdi/nf-wingdi-wglsetlayerpaletteentries)
-   [**wglSwapLayerBuffers**](/windows/desktop/api/wingdi/nf-wingdi-wglswaplayerbuffers)

 

 




