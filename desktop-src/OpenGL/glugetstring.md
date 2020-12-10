---
title: gluGetString function (Glu.h)
description: The gluGetString function gets a string that describes the GLU version number or supported GLU extension calls.
ms.assetid: e6d9ce03-3218-4145-8bb5-3989afe62436
keywords:
- gluGetString function OpenGL
topic_type:
- apiref
api_name:
- gluGetString
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluGetString function

The **gluGetString** function gets a string that describes the GLU version number or supported GLU extension calls.

## Syntax


```C++
const GLubyte* WINAPI gluGetString(
   GLenum name
);
```



## Parameters

<dl> <dt>

*name* 
</dt> <dd>

Either the version number of GLU (GLU\_VERSION) or available vendor-specific extension calls (GLU\_EXTENSIONS).

</dd> </dl>

## Remarks

The **gluGetString** function returns a pointer to a static, null-terminated string. When *name* is GLU\_VERSION, the returned string is a value that represents the version number of GLU. The format of the version number is as follows:

``` syntax
<version number><space><vendor-specific information> 
(for example, "1.2.11 Microsoft Windows")
```

The version number has the form "major\_number.minor\_number" or "major\_number.minor\_number.release\_number". The vendor-specific information is optional, and the format and contents depend on the implementation.

When *name* is GLU\_EXTENSIONS, the returned string contains a list of names of supported GLU extensions that are separated by spaces. The format of the returned list of names is as follows:

``` syntax
<extension_name><space><extension_name><space> . . .
(for example, "GLU_NURBS GL_TESSELATION")
```

The extension names cannot contain any spaces.

The **gluGetString** function is valid for GLU version 1.1 or later.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Glu.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Glu32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Glu32.dll</dt> </dl> |



 

 





