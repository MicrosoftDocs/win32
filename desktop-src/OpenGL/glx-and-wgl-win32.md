---
title: GLX and WGL/Windows
description: Some of the WGL functions and Windows functions are more or less analogous to GLX X Window functions. The following list shows GLX functions and their corresponding WGL/Windows functions, if available.
ms.assetid: '428c0fdc-a541-4720-908f-99f0539d9f4b'
keywords: ["OpenGL on Windows,GLX functions", "GLX functions OpenGL", "WGL functions,compared to GLX functions"]
---

# GLX and WGL/Windows

Some of the WGL functions and Windows functions are more or less analogous to GLX X Window functions. The following list shows GLX functions and their corresponding WGL/Windows functions, if available.



| GLX Functions             | WGL/Windows Functions                                                                                                                                       |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **glXChooseVisual**       | [**ChoosePixelFormat**](choosepixelformat.md)                                                                                                              |
| **glXCopyContext**        |                                                                                                                                                             |
| **glXCreateContext**      | [**wglCreateContext**](wglcreatecontext.md)                                                                                                                |
| **glXCreateGLXPixmap**    | [**CreateDIBitmap**](https://msdn.microsoft.com/library/windows/desktop/dd183491) / [**CreateDIBSection**](https://msdn.microsoft.com/library/windows/desktop/dd183494)                                                                     |
| **glXDestroyContext**     | [**wglDeleteContext**](wgldeletecontext.md)                                                                                                                |
| **glXDestroyGLXPixmap**   | [**DeleteObject**](https://msdn.microsoft.com/library/windows/desktop/dd183539)                                                                                                                        |
| **glXGetConfig**          | [**DescribePixelFormat**](describepixelformat.md)                                                                                                          |
| **glXGetCurrentContext**  | [**wglGetCurrentContext**](wglgetcurrentcontext.md)                                                                                                        |
| **glXGetCurrentDrawable** | [**wglGetCurrentDC**](wglgetcurrentdc.md)                                                                                                                  |
| **glXIsDirect**           |                                                                                                                                                             |
| **glXMakeCurrent**        | [**wglMakeCurrent**](wglmakecurrent.md)                                                                                                                    |
| **glXQueryExtension**     | [**GetVersion**](https://msdn.microsoft.com/library/windows/desktop/ms724439)                                                                                                                           |
| **glXQueryVersion**       | [**GetVersion**](https://msdn.microsoft.com/library/windows/desktop/ms724439)                                                                                                                           |
| **glXSwapBuffers**        | [**SwapBuffers**](swapbuffers.md)                                                                                                                          |
| **glXUseXFont**           | [**wglUseFontBitmaps**](wglusefontbitmaps.md) / [**wglUseFontOutlines**](wglusefontoutlines.md)                                                           |
| **glXWaitGL**             |                                                                                                                                                             |
| **glXWaitX**              |                                                                                                                                                             |
| **XGetVisualInfo**        | [**GetPixelFormat**](getpixelformat.md)                                                                                                                    |
| **XCreateWindow**         | [**CreateWindow**](_win32_createwindow_cpp) / [**CreateWindowEx**](_win32_createwindowex_cpp) and [**GetDC**](https://msdn.microsoft.com/library/windows/desktop/dd144871) / [**BeginPaint**](https://msdn.microsoft.com/library/windows/desktop/dd183362) |
| **XSync**                 | [**GdiFlush**](https://msdn.microsoft.com/library/windows/desktop/dd144844)                                                                                                                                |
|                           | [**SetPixelFormat**](setpixelformat.md)                                                                                                                    |
|                           | [**wglGetProcAddress**](wglgetprocaddress.md)                                                                                                              |
|                           | [**wglShareLists**](wglsharelists.md)                                                                                                                      |



 

For more information, refer to the *Porting Guide*.

 

 




