---
title: Translating the GLX Library
description: Translating the GLX Library
ms.assetid: 040fe6f1-f6ba-4dfa-b294-447efd686361
keywords:
- OpenGL on Windows,GLX library
- porting to OpenGL,GLX library
- OpenGL porting,GLX library
- GLX library OpenGL
- Xlib functions OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Translating the GLX Library

OpenGL X Window System programs use the OpenGL Extension with the X Window System (GLX) library. The library is a set of functions and routines that initialize the pixel format, control rendering, and perform other OpenGL specific tasks. It connects the OpenGL library to the X Window System by managing window handles and rendering contexts. You must translate these functions to their equivalent Windows functions. The following table lists the X Window System GLX functions and their equivalent Windows functions.



| GLX/Xlib function         | Windows function                                                                                                                                       |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| **glXChooseVisual**       | [**ChoosePixelFormat**](/windows/desktop/api/wingdi/nf-wingdi-choosepixelformat)                                                                                                         |
| **glXCopyContext**        | Not applicable.                                                                                                                                        |
| **glXCreateContext**      | [**wglCreateContext**](/windows/desktop/api/wingdi/nf-wingdi-wglcreatecontext)                                                                                                           |
| **glXCreateGLXPixmap**    | [**CreateDIBitmap**](/windows/desktop/api/wingdi/nf-wingdi-createdibitmap)[**CreateDIBSection**](/windows/desktop/api/wingdi/nf-wingdi-createdibsection)                                                                   |
| **glXDestroyContext**     | [**wglDeleteContext**](/windows/desktop/api/wingdi/nf-wingdi-wgldeletecontext)                                                                                                           |
| **glXDestroyGLXPixmap**   | [**DeleteObject**](/windows/desktop/api/wingdi/nf-wingdi-deleteobject)                                                                                                                   |
| **glXGetConfig**          | [**DescribePixelFormat**](/windows/desktop/api/wingdi/nf-wingdi-describepixelformat)                                                                                                     |
| **glXGetCurrentContext**  | [**wglGetCurrentContext**](/windows/desktop/api/wingdi/nf-wingdi-wglgetcurrentcontext)                                                                                                   |
| **glXGetCurrentDrawable** | [**wglGetCurrentDC**](/windows/desktop/api/wingdi/nf-wingdi-wglgetcurrentdc)                                                                                                             |
| **glXIsDirect**           | Not applicable.                                                                                                                                        |
| **glXMakeCurrent**        | [**wglMakeCurrent**](/windows/desktop/api/wingdi/nf-wingdi-wglmakecurrent)                                                                                                               |
| **glXQueryExtension**     | [**GetVersion**](/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getversion)                                                                                                                      |
| **glXQueryVersion**       | [**GetVersion**](/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getversion)                                                                                                                      |
| **glXSwapBuffers**        | [**SwapBuffers**](/windows/desktop/api/wingdi/nf-wingdi-swapbuffers)                                                                                                                     |
| **glXUseXFont**           | [**wglUseFontBitmaps**](/windows/desktop/api/wingdi/nf-wingdi-wglusefontbitmapsa)                                                                                                         |
| **XGetVisualInfo**        | [**GetPixelFormat**](/windows/desktop/api/wingdi/nf-wingdi-getpixelformat)                                                                                                               |
| **XCreateWindow**         | [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa), [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa), [**GetDC**](/windows/desktop/api/winuser/nf-winuser-getdc), [**BeginPaint**](/windows/desktop/api/winuser/nf-winuser-beginpaint) |
| **XSync**                 | [**GdiFlush**](/windows/desktop/api/wingdi/nf-wingdi-gdiflush)                                                                                                                           |
| Not applicable.           | [**SetPixelFormat**](/windows/desktop/api/wingdi/nf-wingdi-setpixelformat)                                                                                                               |



 

Some GLX functions don't have an equivalent Windows function. To port these functions to Windows, rewrite your code to achieve the same functionality. For example, **glXWaitGL** has no equivalent Windows function but you can achieve the same result, executing any pending OpenGL commands, by calling [**glFinish**](glfinish.md).

The following topics describe how to port GLX functions that set the pixel format, and manage rendering contexts, pixmaps and bitmaps.

 

 