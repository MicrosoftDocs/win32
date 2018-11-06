---
title: Creating a Rendering Context and Making It Current
description: The following code sample shows how to create an OpenGL rendering context in response to a WM\_CREATE message.
ms.assetid: eacf0475-6845-48f9-b016-7f0150679419
keywords:
- OpenGL on Windows,rendering contexts
- rendering contexts
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Rendering Context and Making It Current

The following code sample shows how to create an OpenGL rendering context in response to a WM\_CREATE message. Notice that you set up the pixel format before creating the rendering context. Also notice that in this scenario the device context is not released locally; you release it when the window is closed, after making the rendering context not current. For more information, see [Deleting a Rendering Context](deleting-a-rendering-context.md). Finally, notice that you can use local variables for the device context and rendering context handles, because with the [**wglGetCurrentContext**](/windows/desktop/api/wingdi/nf-wingdi-wglgetcurrentcontext) and [**wglGetCurrentDC**](/windows/desktop/api/wingdi/nf-wingdi-wglgetcurrentdc) functions you can obtain handles to those contexts as needed.

``` syntax
// a window has been created, but is not yet visible  
case WM_CREATE: 
    { 
    // local variables  
    HDC      hdc ; 
    HGLRC    hglrc ; 
 
    // obtain a device context for the window  
    hdc = GetDC(hWnd); 
     
    // set an appropriate pixel format   
    myPixelFormatSetupFunction(hdc); 
 
    // if we can create a rendering context ...   
    if (hglrc = wglCreateContext( hdc ) ) { 
 
        // try to make it the thread's current rendering context  
        bHaveCurrentRC = wglMakeCurrent(hdc, hglrc) ; 
 
        } 
 
    // perform miscellaneous other WM_CREATE chores ...  
 
    }  
    break;
```

 

 




