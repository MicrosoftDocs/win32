---
title: Deleting a Rendering Context
description: The following code sample shows how to delete an OpenGL rendering context when an OpenGL window is closed. It is a continuation of the scenario used in Creating a Rendering Context and Making It Current.
ms.assetid: 562c4698-f5bb-418a-8479-0df07e9834e5
keywords:
- OpenGL on Windows,rendering contexts
- rendering contexts OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Deleting a Rendering Context

The following code sample shows how to delete an OpenGL rendering context when an OpenGL window is closed. It is a continuation of the scenario used in [Creating a Rendering Context and Making It Current](creating-a-rendering-context-and-making-it-current.md).


```C++
// a window is about to be destroyed  
case WM_DESTROY: 
    { 
    // local variables  
    HGLRC    hglrc; 
    HDC      hdc ; 
 
    // if the thread has a current rendering context ...  
    if(hglrc = wglGetCurrentContext()) { 
 
        // obtain its associated device context  
        hdc = wglGetCurrentDC() ; 
 
        // make the rendering context not current  
        wglMakeCurrent(NULL, NULL) ; 
 
        // release the device context  
        ReleaseDC (hwnd, hdc) ; 
 
        // delete the rendering context  
        wglDeleteContext(hglrc); 
 
        }
```



 

 




