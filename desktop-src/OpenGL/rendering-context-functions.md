---
title: Rendering Context Functions
description: Five WGL functions manage rendering contexts, as described in the following table.
ms.assetid: e03ec03d-2a85-49de-a2be-fe81a5ec5f7f
keywords:
- WGL functions,rendering contexts
ms.topic: article
ms.date: 05/31/2018
---

# Rendering Context Functions

Five WGL functions manage rendering contexts, as described in the following table.



| WGL Function                                         | Description                                                                                  |
|------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [**wglCreateContext**](/windows/desktop/api/wingdi/nf-wingdi-wglcreatecontext)         | Creates a new rendering context.                                                             |
| [**WglMakeCurrent**](/windows/desktop/api/wingdi/nf-wingdi-wglmakecurrent)             | Sets a thread's current rendering context.                                                   |
| [**WglGetCurrentContext**](/windows/desktop/api/wingdi/nf-wingdi-wglgetcurrentcontext) | Obtains a handle to a thread's current rendering context.                                    |
| [**WglGetCurrentDC**](/windows/desktop/api/wingdi/nf-wingdi-wglgetcurrentdc)           | Obtains a handle to the device context associated with a thread's current rendering context. |
| [**WglDeleteContext**](/windows/desktop/api/wingdi/nf-wingdi-wgldeletecontext)         | Deletes a rendering context.                                                                 |



 

The [**wglCreateContext**](/windows/desktop/api/wingdi/nf-wingdi-wglcreatecontext) function takes a device context handle as its parameter and returns a rendering context handle. The created rendering context is suitable for drawing on the device referenced by the device context handle. In particular, its pixel format is the same as the device context's pixel format. After you create a rendering context, you can release or dispose of the device context. See [Device Contexts](/windows/desktop/gdi/device-contexts) for more details on creating, obtaining, releasing, and disposing of a device context.

> [!Note]  
> The device context sent to [**wglCreateContext**](/windows/desktop/api/wingdi/nf-wingdi-wglcreatecontext) must be a display device context, a memory device context, or a color printer device context that uses four or more bits per pixel. The device context cannot be a monochrome printer device context.

 

The [**wglMakeCurrent**](/windows/desktop/api/wingdi/nf-wingdi-wglmakecurrent) function takes a rendering context handle and a device context handle as parameters. All subsequent OpenGL calls made by the thread are made through that rendering context, and are drawn on the device referenced by that device context. The device context does not have to be the same one passed to **wglCreateContext** when the rendering context was created, but it must be on the same device and have the same pixel format. The call to **wglMakeCurrent** creates an association between the supplied rendering context and device context. You cannot release or dispose of the device context associated with a current rendering context until after you make the rendering context not current.

Once a thread has a current rendering context, it can make OpenGL graphics calls. All calls must pass through a rendering context. Nothing happens if you make OpenGL graphics calls from a thread that lacks a current rendering context.

The [**wglGetCurrentContext**](/windows/desktop/api/wingdi/nf-wingdi-wglgetcurrentcontext) function takes no parameters, and returns a handle to the calling thread's current rendering context. If the thread has no current rendering context, the return value is **NULL**.

When you obtain a handle to the device context associated with a thread's current rendering context by calling [**wglGetCurrentDC**](/windows/desktop/api/wingdi/nf-wingdi-wglgetcurrentdc), the association is created when a rendering context is made current.

You can break the association between a current rendering context and a thread by calling [**wglMakeCurrent**](/windows/desktop/api/wingdi/nf-wingdi-wglmakecurrent) with either of two handles:

-   A **null** rendering context handle
-   A handle other than the one originally called

After calling [**wglMakeCurrent**](/windows/desktop/api/wingdi/nf-wingdi-wglmakecurrent) with the rendering context handle parameter set to **NULL**, the calling thread has no current rendering context. The rendering context is released from its connection to the thread, and the rendering context's association to a device context ends. OpenGL flushes all drawing commands, and may release some resources. No OpenGL drawing will be done until the next call to **wglMakeCurrent**, because the thread can make no OpenGL graphics calls until it regains a current rendering context.

The second way to break the association between a rendering context and a thread is to call **wglMakeCurrent** with a different rendering context. After such a call, the calling thread has a new current rendering context, the former current rendering context is released from its connection to the thread, and the former current rendering context's association to a device context ends.

The [**wglDeleteContext**](/windows/desktop/api/wingdi/nf-wingdi-wgldeletecontext) function takes a single parameter, the handle to the rendering context to be deleted. Before calling **wglDeleteContext**, make the rendering context not current by calling [**wglMakeCurrent**](/windows/desktop/api/wingdi/nf-wingdi-wglmakecurrent), and delete or release the associated device context by calling [DeleteDC](/windows/desktop/api/wingdi/nf-wingdi-deletedc) or [ReleaseDC](/windows/desktop/api/winuser/nf-winuser-releasedc) as appropriate.

It is an error for a thread to delete a rendering context that is another thread's current rendering context. However, if a rendering context is the calling thread's current rendering context, **wglDeleteContext** flushes all OpenGL drawing commands and makes the rendering context not current before deleting it. In this case, relying on **wglDeleteContext** to make a rendering context not current requires the programmer to delete or release the associated device context.

 

 