---
title: Porting X Window System Applications
description: Porting X Window System Applications
ms.assetid: 730602f3-12af-430d-a105-0efdd3fd43b4
keywords:
- OpenGL on Windows,porting
- porting to OpenGL,X Window System
- OpenGL porting,X Window System
ms.topic: article
ms.date: 05/31/2018
---

# Porting X Window System Applications

Like Windows, the X Window System is an event-handling, message-based system that uses window controls and menus. The OpenGL code in your X Window System application is probably located in areas that roughly correspond to where it will appear when you port it to Windows. Most of your OpenGL code will not change, but you must rewrite any code that is specific to the X Window System.

**Use the following general procedure to port your X Window System OpenGL programs to Windows**

1.  Rewrite the X Window System specific code using equivalent Windows code. Locate window-creation and event-handling code. The X Window System and Windows are event-handling, message-based windowing systems, which makes it easier to determine where to make the appropriate changes. (However, especially for large applications, rewriting an application from one operating system to another can be a complex and difficult undertaking.)
2.  Locate any code that uses GLX functions. These are the functions you'll translate to their equivalent Windows functions.
3.  Translate GLX pixel format functions and Visual/Drawable functions to appropriate Windows/OpenGL pixel format and device context functions.
4.  Translate GLX rendering context functions to Windows/OpenGL rendering context functions.
5.  Translate GLX Pixmap functions to equivalent Windows functions.
6.  Translate GLX framebuffer and other GLX functions to the appropriate Windows functions.

 

 




