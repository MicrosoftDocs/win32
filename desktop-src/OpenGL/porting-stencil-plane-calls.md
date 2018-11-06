---
title: Porting Stencil Plane Calls
description: In OpenGL, you allocate stencil planes by requesting the appropriate pixel format with the OpenGL auxInitDisplayMode or ChoosePixelFormat.
ms.assetid: faea8a10-860a-4495-80fb-e83303e397df
keywords:
- IRIS GL porting,stencil planes
- porting from IRIS GL,stencil planes
- porting to OpenGL from IRIS GL,stencil planes
- OpenGL porting from IRIS GL,stencil planes
- stencil planes
ms.topic: article
ms.date: 05/31/2018
---

# Porting Stencil Plane Calls

In OpenGL, you allocate stencil planes by requesting the appropriate pixel format with the OpenGL **auxInitDisplayMode** or [**ChoosePixelFormat**](/windows/desktop/api/wingdi/nf-wingdi-choosepixelformat). functions. The following table lists IRIS GL functions that affect the stencil planes and their equivalent OpenGL functions.



| IRIS GL function             | OpenGL function                                         | Meaning                                                |
|------------------------------|---------------------------------------------------------|--------------------------------------------------------|
| **stensize**                 | **ChoosePixelFormat**                                   |                                                        |
| **stencil**( **TRUE**, ... ) | [**glEnable**](glenable.md) ( GL\_STENCIL\_TEST )      | Enables stencil tests.                                 |
| **stencil**                  | [**glStencilOp**](glstencilop.md)                      | Sets stencil test actions.                             |
| **stencil**(... func, ... )  | [**glStencilFunc**](glstencilfunc.md)                  | Sets function and reference value for stencil testing. |
| **swritemask**               | [**glStencilMask**](glstencilmask.md)                  | Specifies which stencil bits can be written.           |
|                              | [**glClearStencil**](glclearstencil.md)                | Specifies the clear value for the stencil buffer.      |
| **sclear**                   | [**glClear**](glclear.md) ( GL\_STENCIL\_BUFFER\_BIT ) |                                                        |



 

Stencil-comparison functions and stencil pass/fail operations are nearly equivalent in OpenGL and IRIS GL. The IRIS GL stencil-function flags are prefaced with SF; the OpenGL flags with GL. IRIS GL pass/fail operation flags are prefaced with ST; the OpenGL flags with GL.

 

 




