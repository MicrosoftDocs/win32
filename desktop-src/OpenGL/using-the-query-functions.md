---
title: Using the Query Functions
description: Using the Query Functions
ms.assetid: 5f874a0e-77c0-4009-a18f-a852d7ffe891
keywords:
- OpenGL,query functions
- query functions OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Using the Query Functions

There are four query functions for obtaining simple state variables and one for determining whether a particular state is enabled or disabled:

-   [**glGetBooleanv**](glgetbooleanv.md)
-   [**glGetIntegerv**](glgetintegerv.md)
-   [**glGetFloatv**](glgetfloatv.md)
-   [**glGetDoublev**](glgetdoublev.md)
-   [**glIsEnabled**](glisenabled.md)

The prototypes for the query functions are:

**void** **glGetBooleanv**(**GLenum** *pname* , **GLboolean \*** *params* );

**void** **glGetIntegerv**(**GLenum** *pname* , **GLint \*** *params* );

**void** **glGetFloatv**(**GLenum** *pname* , **GLfloat \*** *params* );

**void** **glGetDoublev**(**GLenum** *pname* , **GLdouble \*** *params* );

Respectively, the query functions obtain Boolean, integer, floating-point, or double-precision state variables. The *pname* parameter is a symbolic constant indicating the state variable to return, and *params* is a pointer to an array of the indicated type in which to place the returned data. The possible values for *pname* are listed in [OpenGL State Variables](opengl-state-variables.md). A type conversion is performed if necessary to return the desired variable as the requested data type.

The prototype for [**glIsEnabled**](glisenabled.md) is:

**GLboolean** **glIsEnabled**(GLenum *cap* );

If the mode specified by *cap* is enabled, **glIsEnabled** returns GL\_TRUE. If the mode specified by *cap* is disabled, **glIsEnabled** returns GL\_FALSE. The possible values for *cap* are listed in [OpenGL State Variables](opengl-state-variables.md).

Other specialized functions return specific state variables. To find out when to use these functions, see OpenGL State Variables and the *OpenGL Reference Manual*. For more information on OpenGL's error handling facility and the **glGetError** function, see [Error Handling](error-handling.md).

The functions that return specific state variables are:

-   [**glGetClipPlane**](glgetclipplane.md)
-   [**glGetError**](glgeterror.md)
-   [**glGetLight**](glgetlight.md)
-   [**glGetMap**](glgetmap.md)
-   [**glGetMaterial**](glgetmaterial.md)
-   [**glGetPixelMap**](glgetpixelmap.md)
-   [**glGetPolygonStipple**](glgetpolygonstipple.md)
-   [**glGetString**](glgetstring.md)
-   [**glGetTexEnv**](glgettexenv.md)
-   [**glGetTexGen**](glgettexgen.md)
-   [**glGetTexImage**](glgetteximage.md)
-   [**glGetTexLevelParameter**](glgettexlevelparameter.md)
-   [**glGetTexParameter**](glgettexparameter.md)

 

 




