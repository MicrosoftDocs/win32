---
title: Translating the GLX Library
description: Translating the GLX Library
ms.assetid: '040fe6f1-f6ba-4dfa-b294-447efd686361'
keywords: ["OpenGL on Windows,GLX library", "porting to OpenGL,GLX library", "OpenGL porting,GLX library", "GLX library OpenGL", "Xlib functions OpenGL"]
---

# Translating the GLX Library

OpenGL X Window System programs use the OpenGL Extension with the X Window System (GLX) library. The library is a set of functions and routines that initialize the pixel format, control rendering, and perform other OpenGL specific tasks. It connects the OpenGL library to the X Window System by managing window handles and rendering contexts. You must translate these functions to their equivalent Windows functions. The following table lists the X Window System GLX functions and their equivalent Windows functions.



| GLX/Xlib function         | Windows function                                                                                                                                       |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| **glXChooseVisual**       | [**ChoosePixelFormat**](choosepixelformat.md)                                                                                                         |
| **glXCopyContext**        | Not applicable.                                                                                                                                        |
| **glXCreateContext**      | [**wglCreateContext**](wglcreatecontext.md)                                                                                                           |
| **glXCreateGLXPixmap**    | [**CreateDIBitmap**](https://msdn.microsoft.com/library/windows/desktop/dd183491)[**CreateDIBSection**](https://msdn.microsoft.com/library/windows/desktop/dd183494)                                                                   |
| **glXDestroyContext**     | [**wglDeleteContext**](wgldeletecontext.md)                                                                                                           |
| **glXDestroyGLXPixmap**   | [**DeleteObject**](https://msdn.microsoft.com/library/windows/desktop/dd183539)                                                                                                                   |
| **glXGetConfig**          | [**DescribePixelFormat**](describepixelformat.md)                                                                                                     |
| **glXGetCurrentContext**  | [**wglGetCurrentContext**](wglgetcurrentcontext.md)                                                                                                   |
| **glXGetCurrentDrawable** | [**wglGetCurrentDC**](wglgetcurrentdc.md)                                                                                                             |
| **glXIsDirect**           | Not applicable.                                                                                                                                        |
| **glXMakeCurrent**        | [**wglMakeCurrent**](wglmakecurrent.md)                                                                                                               |
| **glXQueryExtension**     | [**GetVersion**](https://msdn.microsoft.com/library/windows/desktop/ms724439)                                                                                                                      |
| **glXQueryVersion**       | [**GetVersion**](https://msdn.microsoft.com/library/windows/desktop/ms724439)                                                                                                                      |
| **glXSwapBuffers**        | [**SwapBuffers**](swapbuffers.md)                                                                                                                     |
| **glXUseXFont**           | [**wglUseFontBitmaps**](wglusefontbitmaps.md)                                                                                                         |
| **XGetVisualInfo**        | [**GetPixelFormat**](getpixelformat.md)                                                                                                               |
| **XCreateWindow**         | [**CreateWindow**](_win32_createwindow_cpp), [**CreateWindowEx**](_win32_createwindowex_cpp), [**GetDC**](https://msdn.microsoft.com/library/windows/desktop/dd144871), [**BeginPaint**](https://msdn.microsoft.com/library/windows/desktop/dd183362) |
| **XSync**                 | [**GdiFlush**](https://msdn.microsoft.com/library/windows/desktop/dd144844)                                                                                                                           |
| Not applicable.           | [**SetPixelFormat**](setpixelformat.md)                                                                                                               |



 

Some GLX functions don't have an equivalent Windows function. To port these functions to Windows, rewrite your code to achieve the same functionality. For example, **glXWaitGL** has no equivalent Windows function but you can achieve the same result, executing any pending OpenGL commands, by calling [**glFinish**](glfinish.md).

The following topics describe how to port GLX functions that set the pixel format, and manage rendering contexts, pixmaps and bitmaps.

 

 




