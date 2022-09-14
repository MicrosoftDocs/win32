---
title: GLX Rendering Context Code Sample
description: The following code sample shows how an X Window System OpenGL program uses GLX rendering context functions.
ms.assetid: 6cee5e5f-ee2f-4fe4-a988-402802e4a1b8
keywords:
- rendering contexts
- porting to OpenGL,rendering contexts
- OpenGL porting,rendering contexts
- X Window System,rendering contexts
- GLX functions,rendering contexts
ms.topic: article
ms.date: 05/31/2018
---

# GLX Rendering Context Code Sample

The following code sample shows how an X Window System OpenGL program uses GLX rendering context functions.


```C++
Display *dpy;             /* display variable */ 
XVisualInfo *vi;          /* visual variable */ 
Window win;               /* window variable */ 
GLXDrawable drawable;     /* drawable variable */ 
GLXContext cx, cxTemp;    /* rendering context variables */ 
 
/* Code to open a display and get a visual. */ 
        
/* Create a GLX context. */ 
cx = glXCreateContext(dpy, vi, 0, GL_FALSE); 
if (!cx) { 
    fprintf(stderr, "Cannot create context.\n"); 
    exit(-1); 
} 
        
        .    
/* Connect the context to the window. */ 
glXMakeCurrent(dpy, win, cx); 
        
        .    
/* When it's time to destroy the rendering context. . . */ 
cx = glXGetCurrentContext; 
glXDestroyContext(dpy, cx);
```



 

 




