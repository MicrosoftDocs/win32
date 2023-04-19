---
title: gluOrtho2D function (Glu.h)
description: The gluOrtho2D function defines a 2-D orthographic projection matrix.
ms.assetid: ba83fb5c-e5c7-4486-a815-a1aff0469757
keywords:
- gluOrtho2D function OpenGL
topic_type:
- apiref
api_name:
- gluOrtho2D
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluOrtho2D function

The **gluOrtho2D** function defines a 2-D orthographic projection matrix.

## Syntax


```C++
void WINAPI gluOrtho2D(
   GLdouble left,
   GLdouble right,
   GLdouble bottom,
   GLdouble top,
);
```



## Parameters

<dl> <dt>

*left* 
</dt> <dd>

The coordinate for the left vertical clipping plane.

</dd> <dt>

*right* 
</dt> <dd>

The coordinate for the right vertical clipping plane.

</dd> <dt>

*top* 
</dt> <dd>

The coordinate for the top horizontal clipping plane.

</dd>  <dt>

*bottom* 
</dt> <dd>

The coordinate for the bottom horizontal clipping plane.

</dd></dl>

## Return value

This function does not return a value.

## Remarks

The **gluOrtho2D** function sets up a two-dimensional orthographic viewing region. This is equivalent to calling [**glOrtho**](glortho.md) with zNear = -1 and zFar = 1.

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

[**glOrtho**](glortho.md)
</dt> <dt>

[**gluPerspective**](gluperspective.md)
</dt> </dl>

 

 





