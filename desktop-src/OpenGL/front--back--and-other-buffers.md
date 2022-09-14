---
title: Front, Back, and Other Buffers
description: OpenGL stores and manipulates pixel data in a framebuffer.
ms.assetid: 4af6a5e4-cc62-49e5-a4d5-e54b1348e8fe
keywords:
- OpenGL on Windows,buffers
- framebuffers OpenGL
- color buffers OpenGL
- depth buffers OpenGL
- accumulation buffers OpenGL
- stencil buffers OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Front, Back, and Other Buffers

OpenGL stores and manipulates pixel data in a framebuffer. The framebuffer consists of a set of logical buffers: color, depth, accumulation, and stencil buffers. The color buffer itself consists of a set of logical buffers; this set can include a front-left, a front-right, a back-left, a back-right, and some number of auxiliary buffers. A particular pixel format or OpenGL implementation may not supply all of these buffers. For example, the current version of Microsoft's implementation of OpenGL in Windows does not support stereoscopic images, so a pixel format cannot have left and right color buffers. In addition, the current version does not support auxiliary buffers. For more information on OpenGL buffers and the OpenGL functions that operate on them, see the *OpenGL Reference Manual* and the *OpenGL Programming Guide*.

Microsoft's implementation of OpenGL in Windows supports double buffering of images. This is a technique in which an application draws pixels to an off-screen buffer, and then, when that image is ready for display, copies the contents of the off-screen buffer to an on-screen buffer. Double buffering enables smooth image changes, which are especially important for animated images.

Two color buffers are available to applications that use double buffering: a front buffer and a back buffer. By default, drawing commands are directed to the back buffer (the off-screen buffer), while the front buffer is displayed on the screen. When the off-screen buffer is ready for display, you call [**SwapBuffers**](/windows/desktop/api/wingdi/nf-wingdi-swapbuffers), and Windows copies the contents of the off-screen buffer to the on-screen buffer.

The generic implementation uses a device-independent bitmap (DIB) as the back buffer and the screen display as the front buffer. Hardware devices and their drivers may use different approaches.

Double buffering is a pixel-format property. To request double buffering for a pixel format, set the PFD\_DOUBLEBUFFER flag in the [**PIXELFORMATDESCRIPTOR**](/windows/win32/api/wingdi/ns-wingdi-pixelformatdescriptor) data structure in a call to [**ChoosePixelFormat**](/windows/desktop/api/wingdi/nf-wingdi-choosepixelformat).

The OpenGL core function, [**glDrawBuffer**](gldrawbuffer.md), selects buffers for writing and clearing.

## Related topics

<dl> <dt>

[Buffer Functions](buffer-functions.md)
</dt> </dl>

 

 




