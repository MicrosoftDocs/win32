---
title: GLX and WGL/Windows
description: Some of the WGL functions and Windows functions are more or less analogous to GLX X Window functions. The following list shows GLX functions and their corresponding WGL/Windows functions, if available.
ms.assetid: 428c0fdc-a541-4720-908f-99f0539d9f4b
keywords:
- OpenGL on Windows,GLX functions
- GLX functions OpenGL
- WGL functions,compared to GLX functions
ms.topic: article
ms.date: 05/31/2018
---

# GLX and WGL/Windows

Some of the WGL functions and Windows functions are more or less analogous to GLX X Window functions. The following list shows GLX functions and their corresponding WGL/Windows functions, if available.



| GLX Functions             | WGL/Windows Functions                                                                                                                                       |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **glXChooseVisual**       | [**ChoosePixelFormat**](/windows/desktop/api/wingdi/nf-wingdi-choosepixelformat)                                                                                                              |
| **glXCopyContext**        |                                                                                                                                                             |
| **glXCreateContext**      | [**wglCreateContext**](/windows/desktop/api/wingdi/nf-wingdi-wglcreatecontext)                                                                                                                |
| **glXCreateGLXPixmap**    | [**CreateDIBitmap**](/windows/desktop/api/wingdi/nf-wingdi-createdibitmap) / [**CreateDIBSection**](/windows/desktop/api/wingdi/nf-wingdi-createdibsection)                                                                     |
| **glXDestroyContext**     | [**wglDeleteContext**](/windows/desktop/api/wingdi/nf-wingdi-wgldeletecontext)                                                                                                                |
| **glXDestroyGLXPixmap**   | [**DeleteObject**](/windows/desktop/api/wingdi/nf-wingdi-deleteobject)                                                                                                                        |
| **glXGetConfig**          | [**DescribePixelFormat**](/windows/desktop/api/wingdi/nf-wingdi-describepixelformat)                                                                                                          |
| **glXGetCurrentContext**  | [**wglGetCurrentContext**](/windows/desktop/api/wingdi/nf-wingdi-wglgetcurrentcontext)                                                                                                        |
| **glXGetCurrentDrawable** | [**wglGetCurrentDC**](/windows/desktop/api/wingdi/nf-wingdi-wglgetcurrentdc)                                                                                                                  |
| **glXIsDirect**           |                                                                                                                                                             |
| **glXMakeCurrent**        | [**wglMakeCurrent**](/windows/desktop/api/wingdi/nf-wingdi-wglmakecurrent)                                                                                                                    |
| **glXQueryExtension**     | [**GetVersion**](/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getversion)                                                                                                                           |
| **glXQueryVersion**       | [**GetVersion**](/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getversion)                                                                                                                           |
| **glXSwapBuffers**        | [**SwapBuffers**](/windows/desktop/api/wingdi/nf-wingdi-swapbuffers)                                                                                                                          |
| **glXUseXFont**           | [**wglUseFontBitmaps**](/windows/desktop/api/wingdi/nf-wingdi-wglusefontbitmapsa) / [**wglUseFontOutlines**](/windows/desktop/api/wingdi/nf-wingdi-wglusefontoutlinesa)                                                           |
| **glXWaitGL**             |                                                                                                                                                             |
| **glXWaitX**              |                                                                                                                                                             |
| **XGetVisualInfo**        | [**GetPixelFormat**](/windows/desktop/api/wingdi/nf-wingdi-getpixelformat)                                                                                                                    |
| **XCreateWindow**         | [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa) / [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) and [**GetDC**](/windows/desktop/api/winuser/nf-winuser-getdc) / [**BeginPaint**](/windows/desktop/api/winuser/nf-winuser-beginpaint) |
| **XSync**                 | [**GdiFlush**](/windows/desktop/api/wingdi/nf-wingdi-gdiflush)                                                                                                                                |
|                           | [**SetPixelFormat**](/windows/desktop/api/wingdi/nf-wingdi-setpixelformat)                                                                                                                    |
|                           | [**wglGetProcAddress**](/windows/desktop/api/wingdi/nf-wingdi-wglgetprocaddress)                                                                                                              |
|                           | [**wglShareLists**](/windows/desktop/api/wingdi/nf-wingdi-wglsharelists)                                                                                                                      |



 

For more information, refer to the *Porting Guide*.

 

 