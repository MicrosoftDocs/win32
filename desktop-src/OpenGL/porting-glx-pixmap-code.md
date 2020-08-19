---
title: Porting GLX Pixmap Code
description: Porting GLX Pixmap Code
ms.assetid: 5b87d26d-b3ea-4f90-9456-d3f7da462948
keywords:
- pixmaps
- OpenGL on Windows,pixmaps
- porting to OpenGL,pixmaps
- OpenGL porting,pixmaps
ms.topic: article
ms.date: 05/31/2018
---

# Porting GLX Pixmap Code

The X Window System uses *pixmaps*, which are off-screen virtual drawing surfaces in the form of a three-dimensional array of bits. You can think of a pixmap as a stack of bitmaps: a two-dimensional array of pixels with each pixel having a value from 0 to 2N1 where N is the depth of the pixmap.

For OpenGL programs you use the GLX functions, **glXCreateGLXPixmap** and **glXDestroyGLXPixmap**, to create and destroy GLX pixmaps used for off-screen rendering.

Windows uses device-independent bitmaps that serve the same function as X Window System pixmaps. Use the standard Windows bitmap functions to create and destroy bitmaps.

The following table lists the GLX pixmap functions and their equivalent Windows bitmap functions.



| GLX pixmap and font function                                                          | Windows bitmap and font function                                                                                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GLXPixmap**glXCreateGLXPixmap**( Display *\*dpy*,XVisualInfo *\*vis*,Pixmap *pixmap*) | HBITMAP [CreateDIBitmap](/windows/desktop/api/wingdi/nf-wingdi-createdibitmap) HDC *hdc*,LPBITMAPINFOHEADER *lpbmih*,DWORD *fdwInit*,CONST BYTE *\*lpbInit*,LPBITMAPINFO *lpbmi*,UINT *fuUsage***)**HBITMAP [CreateDIBSection](/windows/desktop/api/wingdi/nf-wingdi-createdibsection) HDC *hdc*,LPBITMAPINFO *lpbmi*,DWORD *fInit*,DWORD *iUsage*)<br/> |
| void **glXDestroyGLXPixmap**( Display *\*dpy*,GLXPixmap *pix*)                        | BOOL [DeleteObject](/windows/desktop/api/wingdi/nf-wingdi-deleteobject)( HGDIOBJ *hObject*)                                                                                                                                                                                                                                  |



 

 

