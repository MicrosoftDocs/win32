---
title: glRectfv function (Gl.h)
description: The glRectfv function draws a rectangle.
ms.assetid: 2053890e-bae7-4c06-98e7-5ce4314fe95c
keywords:
- glRectfv function OpenGL
topic_type:
- apiref
api_name:
- glRectfv
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glRectfv function

The [**glRectfv**](glrectdv.md) function draws a rectangle.

## Syntax


```C++
void WINAPI glRectfv(
   const GLfloat *v1,
   const GLfloat *v2
);
```



## Parameters

<dl> <dt>

*v1* 
</dt> <dd>

A pointer to one vertex of a rectangle.

</dd> <dt>

*v2* 
</dt> <dd>

a pointer to the opposite vertex of the rectangle.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error code can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glRectf** function supports efficient specification of rectangles as two corner points. Each rectangle command takes four arguments, organized either as two consecutive pairs of (*x*, *y*) coordinates, or as two pointers to arrays, each containing an (*x*, *y*) pair. The resulting rectangle is defined in the *z* = 0 plane.

The **glRectf**(*x1,* *y1,* *x2,* *y2*) function is exactly equivalent to the following sequence:

**glBegin**(GL\_POLYGON);

**glVertex2**( *x1,* *y1* );

**glVertex2**( *x2,* *y1* );

**glVertex2**( *x2,* *y2* );

**glVertex2**( *x1,* *y2* );

**glEnd**( );

Notice that if the second vertex is above and to the right of the first vertex, the rectangle is constructed with a counterclockwise winding.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Gl.h</dt> </dl>         |
| Library<br/>                  | <dl> <dt>Opengl32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Opengl32.dll</dt> </dl> |



## See also

<dl> <dt>

[**glBegin**](glbegin.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glVertex**](glvertex-functions.md)
</dt> </dl>

 

 





