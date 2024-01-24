---
title: gluPickMatrix function (Glu.h)
description: The gluPickMatrix function defines a picking region.
ms.assetid: 2f57345c-17a0-4716-8ab8-170aaed2b4f9
keywords:
- gluPickMatrix function OpenGL
topic_type:
- apiref
api_name:
- gluPickMatrix
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluPickMatrix function

The **gluPickMatrix** function defines a picking region.

## Syntax


```C++
void WINAPI gluPickMatrix(
   GLdouble x,
   GLdouble y,
   GLdouble height,
   GLdouble width,
   GLint    viewport[4]
);
```



## Parameters

<dl> <dt>

*x* 
</dt> <dd>

The x window coordinate of a picking region.

</dd> <dt>

*y* 
</dt> <dd>

The y window coordinate of a picking region.

</dd> <dt>

*height* 
</dt> <dd>

The height of the picking region in window coordinates.

</dd> <dt>

*width* 
</dt> <dd>

The width of the picking region in window coordinates.

</dd> <dt>

*viewport* 
</dt> <dd>

The current viewport (as from a [**glGetIntegerv**](glgetintegerv.md) call).

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The **gluPickMatrix** function creates a projection matrix you can use to restrict drawing to a small region of the viewport.

1.  Use **gluPickMatrix** to restrict drawing to a small region around the cursor.
2.  Enter selection mode (with [**glRenderMode**](glrendermode.md)), and then rerender the scene.

    All primitives that would have been drawn near the cursor are identified and stored in the selection buffer.

The matrix created by **gluPickMatrix** is multiplied by the current matrix just as if [**glMultMatrix**](glmultmatrix.md) were called with the generated matrix.

1.  Call [**glLoadIdentity**](glloadidentity.md) to load an identity matrix onto the perspective matrix stack.
2.  Call **gluPickMatrix**.
3.  Call a function (such as [**gluPerspective**](gluperspective.md)) to multiply the perspective matrix by the pick matrix.

When using **gluPickMatrix** to pick Non-Uniform Rational B-Spline ([NURBS](using-nurbs-curves-and-surfaces.md)), be careful to turn off the NURBS property, GLU\_AUTO\_LOAD\_MATRIX. If GLU\_AUTO\_LOAD\_MATRIX is not turned off, any NURBS surface rendered is subdivided differently with the pick matrix from how it was subdivided without the pick matrix.

## Examples

When rendering a scene as follows:


```
glMatrixMode(GL_PROJECTION);  
glLoadIdentity( );  
gluPerspective(. . .);  
glMatrixMode(GL_MODELVIEW);  
/* Draw the scene */
```



the following code selects a portion of the viewport:


```
glMatrixMode(GL_PROJECTION);  
glLoadIdentity( );  
gluPickMatrix(x, y, width, height, viewport);  
gluPerspective(. . .);  
glMatrixMode(GL_MODELVIEW);  
/* Draw the scene */
```



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

[**glGetIntegerv**](glgetintegerv.md)
</dt> <dt>

[**glLoadIdentity**](glloadidentity.md)
</dt> <dt>

[**glMultMatrix**](glmultmatrix.md)
</dt> <dt>

[**glRenderMode**](glrendermode.md)
</dt> <dt>

[**gluPerspective**](gluperspective.md)
</dt> </dl>

 

 





