---
title: Handling Errors (OpenGL)
description: The gluErrorString function retrieves error strings that correspond to OpenGL or GLU error codes.
ms.assetid: 59f93c1c-9d15-4980-b246-19257c66b6b8
keywords:
- OpenGL Utility (GLU),error codes
- GLU (OpenGL Utility),error codes
ms.topic: article
ms.date: 05/31/2018
---

# Handling Errors (OpenGL)

The **gluErrorString** function retrieves error strings that correspond to OpenGL or GLU error codes. The currently defined OpenGL error codes are described in [**glGetError**](glgeterror.md). The GLU error codes are listed in [**gluErrorString**](gluerrorstring.md), [*gluTessCallback*](glutess.md), [*gluQuadricCallback*](gluquadric.md), and [*gluNurbsCallback*](glunurbs.md).

The return value for **gluErrorString** is a pointer to a descriptive string that corresponds to the OpenGL, GLU, or GLX error number passed in the *errorCode* parameter. The defined error codes are described in the *OpenGL Reference Manual* along with the function or function that can generate them.

 

 




