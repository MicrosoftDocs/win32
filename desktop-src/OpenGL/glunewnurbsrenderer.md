---
title: gluNewNurbsRenderer function (Glu.h)
description: The gluNewNurbsRenderer function creates a Non-Uniform Rational B-Spline (NURBS) object.
ms.assetid: f47badb0-6b75-4bfd-9771-516668d9e255
keywords:
- gluNewNurbsRenderer function OpenGL
topic_type:
- apiref
api_name:
- gluNewNurbsRenderer
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluNewNurbsRenderer function

The **gluNewNurbsRenderer** function creates a Non-Uniform Rational B-Spline ([NURBS](using-nurbs-curves-and-surfaces.md)) object.

## Syntax


```C++
GLUnurbs* WINAPI gluNewNurbsRenderer(void);
```



## Parameters

This function has no parameters.

## Remarks

The **gluNewNurbsRenderer** function creates and returns a pointer to a new NURBS object. Refer to this object when calling NURBS rendering and control functions. A return value of zero means there is not enough memory to allocate to the object.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Glu.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Glu32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Glu32.dll</dt> </dl> |



## See also

<dl> <dt>

[**gluBeginCurve**](glubegincurve.md)
</dt> <dt>

[**gluBeginSurface**](glubeginsurface.md)
</dt> <dt>

[**gluBeginTrim**](glubegintrim.md)
</dt> <dt>

[**gluDeleteNurbsRenderer**](gludeletenurbsrenderer.md)
</dt> <dt>

[*gluNurbsCallback*](glunurbs.md)
</dt> <dt>

[**gluNurbsProperty**](glunurbsproperty.md)
</dt> </dl>

 

 





