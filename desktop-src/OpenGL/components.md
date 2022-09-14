---
title: Components
description: Components
ms.assetid: 9fbd957d-ee6b-475f-8a04-51effa206ad5
keywords:
- OpenGL on Windows,components
ms.topic: article
ms.date: 05/31/2018
---

# Components

Microsoft's implementation of OpenGL in Windows includes the following components:

-   The full set of current OpenGL commands

    OpenGL contains a library of core functions for 3-D graphics operations. These basic functions are used to manage object shape description, matrix transformation, lighting, coloring, texture, clipping, bitmaps, fog, and antialiasing. The names for these core functions have a "gl" prefix.

    Many of the OpenGL commands have several variants, which differ in the number and type of their parameters. Counting all the variants, there are more than 300 OpenGL commands.

-   The OpenGL Utility (GLU) library

    This library of auxiliary functions complements the core OpenGL functions. The commands manage texture support, coordinate transformation, polygon tessellation, rendering spheres, cylinders and disks, NURBS (Non-Uniform Rational B-Spline) curves and surfaces, and error handling.

-   The OpenGL Programming Guide Auxiliary library

    This is a simple, platform-independent library of functions for managing windows, handling input events, drawing classic 3-D objects, managing a background process, and running a program. The window management and input routines provide a base level of functionality with which you can quickly get started programming in OpenGL.

    Do not use them, however, in a production application. Here are some reasons for this warning:

    -   The message loop is in the library code.
    -   There is no way to add handlers for additional WM\* messages.
    -   There is very little support for logical palettes.

    The library is described and used in the *OpenGL Programming Guide*.

-   The WGL functions

    This set of functions connects OpenGL to the Windows windowing system. The functions manage rendering contexts, display lists, extension functions, and font bitmaps. The WGL functions are analogous to the GLX extensions that connect OpenGL to the X Window System. The names for these functions have a "wgl" prefix.

-   New Windows functions for pixel formats and double buffering

    These functions support per-window pixel formats and double buffering (for smooth image changes) of windows. These new functions apply only to OpenGL graphics windows.

 

 




