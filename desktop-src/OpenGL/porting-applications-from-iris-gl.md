---
title: Porting Applications from IRIS GL
description: Porting Applications from IRIS GL
ms.assetid: d410b516-76a1-4cab-a843-801aa6215db5
keywords:
- OpenGL on Windows,IRIS GL porting
- porting to OpenGL,IRIS GL
- OpenGL porting,IRIS GL
ms.topic: article
ms.date: 05/31/2018
---

# Porting Applications from IRIS GL

This section lists important differences between IRIS GL and OpenGL and describes the basic steps for porting code from IRIS GL to OpenGL. For a complete list of the differences between IRIS GL and Open GL, see [IRIS GL and OpenGL Differences](iris-gl-and-opengl-differences.md).

Porting IRIS GL programs to OpenGL for Windows requires considerably more work than converting OpenGL programs from the X Window System. While IRIS GL programs are designed to run with specific hardware and software, OpenGL was designed for portability among various systems.

The following table lists some of the key differences between OpenGL and IRIS GL programs.



| OpenGL code                                                                                                                                              | IRIS GL code                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Operating system independent; contains no functions for windowing, event handling, buffer allocation/management, and so on.                              | Dependent on operating system; windowing-system functions are mixed with rendering functions. There is no windows manager in IRIS GL. |
| Uses a standard, common naming convention. OpenGL functions and defined types begin with a "gl" prefix to prevent conflicts with other libraries.        | Does not use a common naming convention for functions and defined types.                                                              |
| Manages state variables (such as color, fog, texture, lighting, and so on) directly and consistently. Does not use tables to load state-variable values. | Uses tables to manage state variables and must bind variables to table values.                                                        |
| Display lists cannot be edited.                                                                                                                          | Display lists can be edited.                                                                                                          |
| Does not provide a file format for fonts.                                                                                                                | Provides functions to handle fonts and text strings and a file format for fonts.                                                      |
| Includes a GL Utility (GLU) library that contains additional functions and routines (such as NURBS and quadratic rendering routines).                    | Does not support the GLU library.                                                                                                     |



 

**Use the following general procedure to port your IRIS GL programs to OpenGL**

1.  Rewrite any code that makes calls to a window manager, window configuration, device, or event, or where you load a color map to equivalent Windows code. Rewriting an application from one operating system to another can be complex and difficult. This subject is beyond the scope of this section.
2.  Locate any code that uses IRIS GL functions and routines. Translate these functions to their equivalent OpenGL functions. For a complete listing of IRIS GL functions and routines and their equivalent OpenGL counterparts, see [OpenGL Functions and Their IRIS GL Equivalents](opengl-functions-and-their-iris-gl-equivalents.md).
3.  Change IRIS GL code as described in [Special IRIS GL Porting Issues](special-iris-gl-porting-issues.md).

<!-- -->

1.  Rewrite any code that makes calls to a window manager, window configuration, device, or event, or where you load a color map to equivalent Windows code. Rewriting an application from one operating system to another can be complex and difficult. This subject is beyond the scope of this section.
2.  Locate any code that uses IRIS GL functions and routines. Translate these functions to their equivalent OpenGL functions. For a complete listing of IRIS GL functions and routines and their equivalent OpenGL counterparts, see [OpenGL Functions and Their IRIS GL Equivalents](opengl-functions-and-their-iris-gl-equivalents.md).
3.  Change IRIS GL code as described in [Special IRIS GL Porting Issues](special-iris-gl-porting-issues.md).

 

 




