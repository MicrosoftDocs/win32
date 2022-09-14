---
title: gluDeleteNurbsRenderer function (Glu.h)
description: The gluDeleteNurbsRenderer function destroys a Non-Uniform Rational B-Spline (NURBS) object.
ms.assetid: 77063dcb-90b8-47e4-8b00-e1c46cf4f712
keywords:
- gluDeleteNurbsRenderer function OpenGL
topic_type:
- apiref
api_name:
- gluDeleteNurbsRenderer
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluDeleteNurbsRenderer function

The **gluDeleteNurbsRenderer** function destroys a Non-Uniform Rational B-Spline ([NURBS](using-nurbs-curves-and-surfaces.md)) object.

## Syntax


```C++
void WINAPI gluDeleteNurbsRenderer(
   GLUnurbs *nobj
);
```



## Parameters

<dl> <dt>

*nobj* 
</dt> <dd>

The NURBS object to be destroyed (created with **gluNewNurbsRenderer**).

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The **gluDeleteNurbsRenderer** function destroys the NURBS object and frees any memory that it used. After you have called **gluDeleteNurbsRenderer**, you cannot use *nobj* again.

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

[**gluNewNurbsRenderer**](glunewnurbsrenderer.md)
</dt> </dl>

 

 





