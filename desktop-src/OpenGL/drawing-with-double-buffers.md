---
title: Drawing with Double Buffers
description: Double buffers smooth the transition between one image and another on the screen.
ms.assetid: 10801cc7-d26c-4bfd-95c0-f352a1c7a1f5
keywords:
- OpenGL on Windows,double buffers
- double buffers OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Drawing with Double Buffers

Double buffers smooth the transition between one image and another on the screen. Swapping buffers typically comes at the end of a sequence of drawing commands. By default, the Microsoft implementation of OpenGL in Windows draws to the off-screen buffer; when drawing is complete, you call the [**SwapBuffers**](/windows/desktop/api/wingdi/nf-wingdi-swapbuffers) function to copy the off-screen buffer to the on-screen buffer. The following code sample prepares to draw, calls a drawing function, and then copies the completed image on to the screen if double buffering is available.


```C++
void myRedraw(void) 
{ 
    // set up for drawing commands  
    glMatrixMode(GL_PROJECTION); 
    glLoadIdentity(); 
    gluPerspective(45, 1.0, 0.1, 100.0); 
 
    // draw our objects  
    myDrawAllObjects(GL_FALSE); 
 
    // if we're double-buffering ...  
    if (bDoubleBuffering)  
 
        // ...draw the copied image to the screen  
        SwapBuffers(hdc); 
}
```



The following code sample obtains a window device context, renders a scene, copies the image to the screen (to show the rendering), and then releases the device context.


```C++
hdc = GetDC(hwnd); 
mySceneRenderingFunction(); 
SwapBuffers(hdc); 
ReleaseDC(hWnd, hdc);
```



 

 




