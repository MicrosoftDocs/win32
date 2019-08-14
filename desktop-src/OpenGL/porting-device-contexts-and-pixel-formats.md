---
title: Porting Device Contexts and Pixel Formats
description: Porting Device Contexts and Pixel Formats
ms.assetid: b60cac27-1e2e-4da5-81c4-69446b92f820
keywords:
- porting to OpenGL,pixels
- OpenGL porting,pixels
ms.topic: article
ms.date: 05/31/2018
---

# Porting Device Contexts and Pixel Formats

Each window in the Microsoft implementation of OpenGL for Windows has its own current pixel format. A pixel format is defined by a [**PIXELFORMATDESCRIPTOR**](/windows/win32/api/wingdi/ns-wingdi-pixelformatdescriptor) data structure. Because each window has its own pixel format, you obtain a device context, set the pixel format of the device context, and then create an OpenGL rendering context for the device context. The rendering context automatically uses the pixel format of its device context.

The X Window System also uses a data structure, **XVisualInfo**, to specify the properties of pixels in a window. **XVisualInfo** structures contain a **Visual** data structure that describes how color resources are used in a specific screen.

In the X Window System, **XVisualInfo** is used to create a window by setting the window to the pixel format you want. The returned structure is used to create the window and a rendering context. In Windows, you first create a window and get a handle to a device context (HDC) of the window. The HDC is then used to set the pixel format for the window. The rendering context uses the pixel format of the window.

The following table compares the X Window System and GLX visual functions with their equivalent Windows pixel format functions.



| X window/GLX visual function                                                                                     | Windows pixel format function                                                                                                      |
|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| XVisualInfo\***glXChooseVisual**( Display *\*dpy*,int *screen*,int *\*attribList*)                               | int [**ChoosePixelFormat**](/windows/desktop/api/wingdi/nf-wingdi-choosepixelformat)( HDC *hdc*,PIXELFORMATDESCRIPTOR *\*ppfd*)                                      |
| int **glXGetConfig**( Display *\*dpy*,XVisualInfo *\*vis*,int *\*attribList*,int *\*value*)                      | int [**DescribePixelFormat**](/windows/desktop/api/wingdi/nf-wingdi-describepixelformat)( HDC *hdc*,int *iPixelFormat*,UINT *nBytes*,LPPIXELFORMATDESCRIPTOR *ppfd*) |
| XVisualInfo\***XGetVisualInfo**( Display *\*dpy*,long *vinfo\_mask*,XVisualInfo *\*vinfo\_templ*,int *\*nitems*) | int [**GetPixelFormat**](/windows/desktop/api/wingdi/nf-wingdi-getpixelformat)( HDC *hdc*)                                                                           |
| The *visual* returned by **glxChooseVisual** is used when a window is created.                                   | BOOL [**SetPixelFormat**](/windows/desktop/api/wingdi/nf-wingdi-setpixelformat)( HDC *hdc*,int *iPixelFormat*,PIXELFORMATDESCRIPTOR *\*ppfd*)                        |



 

The following sections give examples of pixel format code fragments for an X Window System program, and the same code after it has been ported to Windows.

-   [GLX Pixel Format Code Sample](glx-pixel-format-code-sample.md)
-   [Windows Pixel Format Code Sample](win32-pixel-format-code-sample.md)

For more information on pixel formats, see [Pixel Formats](pixel-formats.md).

 

 




