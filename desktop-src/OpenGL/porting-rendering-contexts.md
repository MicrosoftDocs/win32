---
title: Porting Rendering Contexts
description: Porting Rendering Contexts
ms.assetid: 8655a81b-9f13-4ee5-ba0d-9aa9da1bfd09
keywords:
- rendering contexts OpenGL ,porting
- OpenGL on Windows,rendering contexts
- porting to OpenGL,rendering contexts
- OpenGL porting,rendering contexts
ms.topic: article
ms.date: 05/31/2018
---

# Porting Rendering Contexts

The X Window System and Windows render through rendering contexts. Six GLX functions manage rendering contexts and five of them have an equivalent Windows function.

The following table lists the GLX rendering functions and their equivalent Windows functions.



| GLX rendering context function                                                                            | Windows rendering context function                                      |
|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| GLXContext**glXCopyContext**( Display *\*dpy*,GLXContext *src*,GLXContext *dst*,GLuint *mask*)            | Not applicable.                                                         |
| GLXContext**glXCreateContext**( Display *\*dpy*,XVisualInfo *\*vis*,GLXContext *shareList*,Bool *direct*) | HGLRC [**wglCreateContext**](/windows/desktop/api/wingdi/nf-wingdi-wglcreatecontext)( HDC *hdc*)          |
| void **glXDeleteContext**( Display *\*dpy*,GLXContext *ctx*)                                              | BOOL [**wglDeleteContext**](/windows/desktop/api/wingdi/nf-wingdi-wgldeletecontext)( HGLRC *hglrc*)       |
| GLXContext **glXGetCurrentContext**(*void*)                                                               | HGLRC [**wglGetCurrentContext**](/windows/desktop/api/wingdi/nf-wingdi-wglgetcurrentcontext)(*VOID*)      |
| GLXDrawable **glXGetCurrentDrawable**(*void*)                                                             | HDC [**wglGetCurrentDC**](/windows/desktop/api/wingdi/nf-wingdi-wglgetcurrentdc)(*VOID*)                  |
| Bool**glXMakeCurrent**( Display *\*dpy*,GLXDrawable *draw*,GLXContext *ctx*)                              | BOOL [**wglMakeCurrent**](/windows/desktop/api/wingdi/nf-wingdi-wglmakecurrent)( HDC *hdc*,HGLRC *hglrc*) |



 

Return types and other types have different names in the X Window System than in Windows. You can search for occurrences of GLXContext to help find parts of your code that need to be ported.

The following sections compare rendering context code samples in an X Window System program and the same code after it has been ported to Windows.

For more information on rendering contexts, see [Rendering Contexts](rendering-contexts.md).

 

 




