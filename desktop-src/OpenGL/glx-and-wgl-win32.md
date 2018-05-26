---
title: GLX and WGL/Windows
description: Some of the WGL functions and Windows functions are more or less analogous to GLX X Window functions. The following list shows GLX functions and their corresponding WGL/Windows functions, if available.
ms.assetid: 428c0fdc-a541-4720-908f-99f0539d9f4b
keywords:
- OpenGL on Windows,GLX functions
- GLX functions OpenGL
- WGL functions,compared to GLX functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GLX and WGL/Windows

Some of the WGL functions and Windows functions are more or less analogous to GLX X Window functions. The following list shows GLX functions and their corresponding WGL/Windows functions, if available.



| GLX Functions             | WGL/Windows Functions                                                                                                                                       |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **glXChooseVisual**       | [**ChoosePixelFormat**](/windows/win32/wingdi/nf-wingdi-choosepixelformat?branch=master)                                                                                                              |
| **glXCopyContext**        |                                                                                                                                                             |
| **glXCreateContext**      | [**wglCreateContext**](/windows/win32/wingdi/nf-wingdi-wglcreatecontext?branch=master)                                                                                                                |
| **glXCreateGLXPixmap**    | [**CreateDIBitmap**](https://msdn.microsoft.com/library/windows/desktop/dd183491) / [**CreateDIBSection**](https://msdn.microsoft.com/library/windows/desktop/dd183494)                                                                     |
| **glXDestroyContext**     | [**wglDeleteContext**](/windows/win32/wingdi/nf-wingdi-wgldeletecontext?branch=master)                                                                                                                |
| **glXDestroyGLXPixmap**   | [**DeleteObject**](https://msdn.microsoft.com/library/windows/desktop/dd183539)                                                                                                                        |
| **glXGetConfig**          | [**DescribePixelFormat**](/windows/win32/wingdi/nf-wingdi-describepixelformat?branch=master)                                                                                                          |
| **glXGetCurrentContext**  | [**wglGetCurrentContext**](/windows/win32/wingdi/nf-wingdi-wglgetcurrentcontext?branch=master)                                                                                                        |
| **glXGetCurrentDrawable** | [**wglGetCurrentDC**](/windows/win32/wingdi/nf-wingdi-wglgetcurrentdc?branch=master)                                                                                                                  |
| **glXIsDirect**           |                                                                                                                                                             |
| **glXMakeCurrent**        | [**wglMakeCurrent**](/windows/win32/wingdi/nf-wingdi-wglmakecurrent?branch=master)                                                                                                                    |
| **glXQueryExtension**     | [**GetVersion**](https://msdn.microsoft.com/library/windows/desktop/ms724439)                                                                                                                           |
| **glXQueryVersion**       | [**GetVersion**](https://msdn.microsoft.com/library/windows/desktop/ms724439)                                                                                                                           |
| **glXSwapBuffers**        | [**SwapBuffers**](/windows/win32/wingdi/nf-wingdi-swapbuffers?branch=master)                                                                                                                          |
| **glXUseXFont**           | [**wglUseFontBitmaps**](/windows/win32/wingdi/nf-wingdi-wglusefontbitmapsa?branch=master) / [**wglUseFontOutlines**](/windows/win32/wingdi/nf-wingdi-wglusefontoutlinesa?branch=master)                                                           |
| **glXWaitGL**             |                                                                                                                                                             |
| **glXWaitX**              |                                                                                                                                                             |
| **XGetVisualInfo**        | [**GetPixelFormat**](/windows/win32/wingdi/nf-wingdi-getpixelformat?branch=master)                                                                                                                    |
| **XCreateWindow**         | [**CreateWindow**](_win32_createwindow_cpp) / [**CreateWindowEx**](_win32_createwindowex_cpp) and [**GetDC**](https://msdn.microsoft.com/library/windows/desktop/dd144871) / [**BeginPaint**](https://msdn.microsoft.com/library/windows/desktop/dd183362) |
| **XSync**                 | [**GdiFlush**](https://msdn.microsoft.com/library/windows/desktop/dd144844)                                                                                                                                |
|                           | [**SetPixelFormat**](/windows/win32/wingdi/nf-wingdi-setpixelformat?branch=master)                                                                                                                    |
|                           | [**wglGetProcAddress**](/windows/win32/wingdi/nf-wingdi-wglgetprocaddress?branch=master)                                                                                                              |
|                           | [**wglShareLists**](/windows/win32/wingdi/nf-wingdi-wglsharelists?branch=master)                                                                                                                      |



 

For more information, refer to the *Porting Guide*.

 

 




