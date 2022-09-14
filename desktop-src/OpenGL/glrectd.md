---
title: glRectd function (Gl.h)
description: The glRectd function draws a rectangle.
ms.assetid: d5574c22-7ae1-4040-9b95-769693fa41e3
keywords:
- glRectd function OpenGL
topic_type:
- apiref
api_name:
- glRectd
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glRectd function

The **glRectd** function draws a rectangle.

## Syntax


```C++
void WINAPI glRectd(
   GLdouble x1,
   GLdouble y1,
   GLdouble x2,
   GLdouble y2
);
```



## Parameters

<dl> <dt>

*x1* 
</dt> <dd>

The *x* coordinate of the vertex of a rectangle.

</dd> <dt>

*y1* 
</dt> <dd>

The *y* coordinate of the vertex of a rectangle.

</dd> <dt>

*x2* 
</dt> <dd>

The *x* coordinate of the opposite vertex of the rectangle.

</dd> <dt>

*y2* 
</dt> <dd>

The *y* coordinate of the opposite vertex of the rectangle.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error code can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glRectd** function supports efficient specification of rectangles as two corner points. Each rectangle command takes four arguments, organized either as two consecutive pairs of (*x*, *y*) coordinates, or as two pointers to arrays, each containing an (*x*, *y*) pair. The resulting rectangle is defined in the *z* = 0 plane.

The **glRectd**(*x1,* *y1,* *x2,* *y2*) function is exactly equivalent to the following sequence:

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

 

 





