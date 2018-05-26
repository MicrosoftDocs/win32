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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Translating the GLX Library

OpenGL X Window System programs use the OpenGL Extension with the X Window System (GLX) library. The library is a set of functions and routines that initialize the pixel format, control rendering, and perform other OpenGL specific tasks. It connects the OpenGL library to the X Window System by managing window handles and rendering contexts. You must translate these functions to their equivalent Windows functions. The following table lists the X Window System GLX functions and their equivalent Windows functions.



| GLX/Xlib function         | Windows function                                                                                                                                       |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| **glXChooseVisual**       | [**ChoosePixelFormat**](/windows/win32/wingdi/nf-wingdi-choosepixelformat?branch=master)                                                                                                         |
| **glXCopyContext**        | Not applicable.                                                                                                                                        |
| **glXCreateContext**      | [**wglCreateContext**](/windows/win32/wingdi/nf-wingdi-wglcreatecontext?branch=master)                                                                                                           |
| **glXCreateGLXPixmap**    | [**CreateDIBitmap**](https://msdn.microsoft.com/library/windows/desktop/dd183491)[**CreateDIBSection**](https://msdn.microsoft.com/library/windows/desktop/dd183494)                                                                   |
| **glXDestroyContext**     | [**wglDeleteContext**](/windows/win32/wingdi/nf-wingdi-wgldeletecontext?branch=master)                                                                                                           |
| **glXDestroyGLXPixmap**   | [**DeleteObject**](https://msdn.microsoft.com/library/windows/desktop/dd183539)                                                                                                                   |
| **glXGetConfig**          | [**DescribePixelFormat**](/windows/win32/wingdi/nf-wingdi-describepixelformat?branch=master)                                                                                                     |
| **glXGetCurrentContext**  | [**wglGetCurrentContext**](/windows/win32/wingdi/nf-wingdi-wglgetcurrentcontext?branch=master)                                                                                                   |
| **glXGetCurrentDrawable** | [**wglGetCurrentDC**](/windows/win32/wingdi/nf-wingdi-wglgetcurrentdc?branch=master)                                                                                                             |
| **glXIsDirect**           | Not applicable.                                                                                                                                        |
| **glXMakeCurrent**        | [**wglMakeCurrent**](/windows/win32/wingdi/nf-wingdi-wglmakecurrent?branch=master)                                                                                                               |
| **glXQueryExtension**     | [**GetVersion**](https://msdn.microsoft.com/library/windows/desktop/ms724439)                                                                                                                      |
| **glXQueryVersion**       | [**GetVersion**](https://msdn.microsoft.com/library/windows/desktop/ms724439)                                                                                                                      |
| **glXSwapBuffers**        | [**SwapBuffers**](/windows/win32/wingdi/nf-wingdi-swapbuffers?branch=master)                                                                                                                     |
| **glXUseXFont**           | [**wglUseFontBitmaps**](/windows/win32/wingdi/nf-wingdi-wglusefontbitmapsa?branch=master)                                                                                                         |
| **XGetVisualInfo**        | [**GetPixelFormat**](/windows/win32/wingdi/nf-wingdi-getpixelformat?branch=master)                                                                                                               |
| **XCreateWindow**         | [**CreateWindow**](_win32_createwindow_cpp), [**CreateWindowEx**](_win32_createwindowex_cpp), [**GetDC**](https://msdn.microsoft.com/library/windows/desktop/dd144871), [**BeginPaint**](https://msdn.microsoft.com/library/windows/desktop/dd183362) |
| **XSync**                 | [**GdiFlush**](https://msdn.microsoft.com/library/windows/desktop/dd144844)                                                                                                                           |
| Not applicable.           | [**SetPixelFormat**](/windows/win32/wingdi/nf-wingdi-setpixelformat?branch=master)                                                                                                               |



 

Some GLX functions don't have an equivalent Windows function. To port these functions to Windows, rewrite your code to achieve the same functionality. For example, **glXWaitGL** has no equivalent Windows function but you can achieve the same result, executing any pending OpenGL commands, by calling [**glFinish**](glfinish.md).

The following topics describe how to port GLX functions that set the pixel format, and manage rendering contexts, pixmaps and bitmaps.

 

 




