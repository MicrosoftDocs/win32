---
title: Porting greset
description: OpenGL replaces the IRIS GL function, greset, with the functions, glPushAttrib and glPopAttrib.
ms.assetid: 348e8b18-4f12-45d1-a4d2-6533a983236b
keywords:
- IRIS GL porting,state variables
- porting from IRIS GL,state variables
- porting to OpenGL from IRIS GL,state variables
- OpenGL porting from IRIS GL,state variables
- state variables
- IRIS GL porting,greset function
- porting from IRIS GL,greset function
- porting to OpenGL from IRIS GL,greset function
- OpenGL porting from IRIS GL,greset function
ms.topic: article
ms.date: 05/31/2018
---

# Porting greset

OpenGL replaces the IRIS GL function, **greset**, with the functions, [**glPushAttrib**](glpushattrib.md) and [**glPopAttrib**](glpopattrib.md). Use these functions to save and restore groups of state variables. For example,

``` syntax
void glPushAttrib( GLbitfield mask );
```

This example takes a bitwise OR of symbolic constants, indicating which groups of state variables to push onto an attribute stack. Each constant refers to a group of state variables. The following table shows the attribute groups with their equivalent symbolic constant names. For a complete list of the OpenGL state variables associated with each constant, see [**glPushAttrib**](glpushattrib.md).



| Attribute                       | Constant                  |
|---------------------------------|---------------------------|
| accumulation buffer clear value | GL\_ACCUM\_BUFFER\_BIT    |
| color buffer                    | GL\_COLOR\_BUFFER\_BIT    |
| current                         | GL\_CURRENT\_BIT          |
| depth buffer                    | GL\_DEPTH\_BUFFER\_BIT    |
| enable                          | GL\_ENABLE\_BIT           |
| evaluators                      | EGL\_VAL\_BIT             |
| fog                             | GL\_FOG\_BIT              |
| GL\_LIST\_BASE setting          | GL\_LIST\_BIT             |
| hint variables                  | GL\_HINT\_BIT             |
| lighting variables              | GL\_LIGHTING\_BIT         |
| line drawing mode               | GL\_LINE\_BIT             |
| pixel mode variables            | GL\_PIXEL\_MODE\_BIT      |
| point variables                 | GL\_POINT\_BIT            |
| polygon                         | GL\_POLYGON\_BIT          |
| polygon stipple                 | GL\_POLYGON\_STIPPLE\_BIT |
| scissor                         | GL\_SCISSOR\_BIT          |
| stencil buffer                  | GL\_STENCIL\_BUFFER\_BIT  |
| texture                         | GL\_TEXTURE\_BIT          |
| transform                       | GL\_TRANSFORM\_BIT        |
| viewport                        | GL\_VIEWPORT\_BIT         |
|                                 | GL\_ALL\_ATTRIB\_BITS     |



 

To restore the values of the state variables to those saved with the last [**glPushAttrib**](glpushattrib.md), simply call [**glPopAttrib**](glpopattrib.md). The variables you didn't save will remain unchanged. The attribute stack has a finite depth of at least 16.

 

 




