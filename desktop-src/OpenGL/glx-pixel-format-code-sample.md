---
title: GLX Pixel Format Code Sample
description: The code sample below shows how an X Window System OpenGL program uses GLX visual/pixel formatting functions.
ms.assetid: f01193a9-c0ff-4399-a86e-06bb4603b3f1
keywords:
- porting to OpenGL,pixels
- OpenGL porting,pixels
- X Window System,pixels
- GLX functions,pixels
- pixels,GLX sample
ms.topic: article
ms.date: 05/31/2018
---

# GLX Pixel Format Code Sample

The code sample below shows how an X Window System OpenGL program uses GLX visual/pixel formatting functions.


```C++
/* X globals, defines, and prototypes */ 
Display *dpy; 
Window glwin; 
static int attributes[] = {GLX_DEPTH_SIZE, 16, GLX_DOUBLEBUFFER, None}; 
        
    /* find an OpenGL-capable Color Index visual with depth buffer */ 
    vi = glXChooseVisual(dpy, DefaultScreen(dpy), attributes); 
    if (vi == NULL) { 
        fprintf(stderr, "could not get visual\n"); 
        exit(1); 
    }
```



The Visual can be used to create a window and a rendering context.

 

 




