---
title: Choosing and Setting a Best-Match Pixel Format
description: This topic explains the procedure for matching a device context to a pixel format.
ms.assetid: 7b974fb5-e34d-4781-858c-572c4e7754bc
keywords:
- OpenGL on Windows,pixels
- best-match pixel format OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Choosing and Setting a Best-Match Pixel Format

This topic explains the procedure for matching a device context to a pixel format.

**To obtain a device context's best match to a pixel format**

1.  Specify the desired pixel format in a [**PIXELFORMATDESCRIPTOR**](/windows/win32/api/wingdi/ns-wingdi-pixelformatdescriptor) structure.
2.  Call [**ChoosePixelFormat**](/windows/desktop/api/wingdi/nf-wingdi-choosepixelformat).

    The **ChoosePixelFormat** function returns a pixel format index, which you can then pass to [**SetPixelFormat**](/windows/desktop/api/wingdi/nf-wingdi-setpixelformat) to set the best pixel format match as the device context's current pixel format.

The following code sample shows how to carry out the above steps.


```C++
PIXELFORMATDESCRIPTOR pfd = { 
    sizeof(PIXELFORMATDESCRIPTOR),    // size of this pfd  
    1,                                // version number  
    PFD_DRAW_TO_WINDOW |              // support window  
    PFD_SUPPORT_OPENGL |              // support OpenGL  
    PFD_DOUBLEBUFFER,                 // double buffered  
    PFD_TYPE_RGBA,                    // RGBA type  
    24,                               // 24-bit color depth  
    0, 0, 0, 0, 0, 0,                 // color bits ignored  
    0,                                // no alpha buffer  
    0,                                // shift bit ignored  
    0,                                // no accumulation buffer  
    0, 0, 0, 0,                       // accum bits ignored  
    32,                               // 32-bit z-buffer      
    0,                                // no stencil buffer  
    0,                                // no auxiliary buffer  
    PFD_MAIN_PLANE,                   // main layer  
    0,                                // reserved  
    0, 0, 0                           // layer masks ignored  
}; 
HDC  hdc; 
int  iPixelFormat; 
 
// get the device context's best, available pixel format match  
iPixelFormat = ChoosePixelFormat(hdc, &pfd); 
 
// make that match the device context's current pixel format  
SetPixelFormat(hdc, iPixelFormat, &pfd);
```



 

 




