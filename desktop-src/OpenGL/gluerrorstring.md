---
title: gluErrorString function (Glu.h)
description: The gluErrorString function produces an error string from an OpenGL or GLU error code. The error string is ANSI only.
ms.assetid: 6d71a6d5-ac00-49f9-a56c-cfeeb88963eb
keywords:
- gluErrorString function OpenGL
topic_type:
- apiref
api_name:
- gluErrorString
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluErrorString function

The **gluErrorString** function produces an error string from an OpenGL or GLU error code. The error string is ANSI only.

## Syntax


```C++
const GLubyte* WINAPI gluErrorString(
   GLenum errCode
);
```



## Parameters

<dl> <dt>

*errCode* 
</dt> <dd>

An OpenGL or GLU error code.

</dd> </dl>

## Remarks

The **gluErrorString** function produces an error string from an OpenGL or GLU error code. The string is in an ISO Latin 1 format. For example, **gluErrorString**(GL\_OUT\_OF\_MEMORY) returns the string "out of memory".

The standard GLU error codes are GLU\_INVALID\_ENUM, GLU\_INVALID\_VALUE, and GLU\_OUT\_OF\_MEMORY. Certain other GLU functions can return specialized error codes through callbacks. For the list of OpenGL error codes, see [**glGetError**](glgeterror.md).

The **gluErrorString** function produces error strings in ANSI only. Whenever possible, use **gluErrorStringWIN**, which allows ANSI or Unicode error strings. This makes it easier to localize your program for use with another language.

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

[**glGetError**](glgeterror.md)
</dt> <dt>

[*gluNurbsCallback*](glunurbs.md)
</dt> <dt>

[*gluQuadricCallback*](gluquadric.md)
</dt> <dt>

[*gluTessCallback*](glutess.md)
</dt> </dl>

 

 





