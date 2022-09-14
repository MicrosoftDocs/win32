---
title: glClipPlane function (Gl.h)
description: The glClipPlane function specifies a plane against which all geometry is clipped.
ms.assetid: b70d2c30-7502-4399-8c08-5ec9a2a1919c
keywords:
- glClipPlane function OpenGL
topic_type:
- apiref
api_name:
- glClipPlane
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glClipPlane function

The **glClipPlane** function specifies a plane against which all geometry is clipped.

## Syntax


```C++
void WINAPI glClipPlane(
         GLenum   plane,
   const GLdouble *equation
);
```



## Parameters

<dl> <dt>

*plane* 
</dt> <dd>

The clipping plane that is being positioned. Symbolic names of the form GL\_CLIP\_PLANE*i*, where *i* is an integer between 0 and GL\_MAX\_CLIP\_PLANES - 1, are accepted.

</dd> <dt>

*equation* 
</dt> <dd>

The address of an array of four double-precision floating-point values. These values are interpreted as a plane equation.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *plane* was not an accepted value.<br/>                                                                                         |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

Geometry is always clipped against the boundaries of a six-plane frustum in *x*, *y*, and *z*. The **glClipPlane** function allows the specification of additional planes, not necessarily perpendicular to the *x-*axis, *y-*axis, or *z*-axis, against which all geometry is clipped. Up to GL\_MAX\_CLIP\_PLANES planes can be specified, where GL\_MAX\_CLIP\_PLANES is at least six in all implementations. Because the resulting clipping region is the intersection of the defined half-spaces, it is always convex.

The **glClipPlane** function specifies a half-space using a four-component plane equation. When you call **glClipPlane**,*equation* is transformed by the inverse of the modelview matrix and stored in the resulting eye coordinates. Subsequent changes to the modelview matrix have no effect on the stored plane-equation components. If the dot product of the eye coordinates of a vertex with the stored plane equation components is positive or zero, the vertex is in with respect to that clipping plane. Otherwise, it is out.

Use the [**glEnable**](glenable.md) and [**glDisable**](gldisable.md) functions to enable and disable clipping planes. Call clipping planes with the argument GL\_CLIP\_PLANE*i*, where *i* is the plane number.

By default, all clipping planes are defined as (0,0,0,0) in eye coordinates and are disabled.

It is always the case that GL\_CLIP\_PLANE*i* = GL\_CLIP\_PLANE0 + *i*.

The following functions retrieve information related to **glClipPlane**:

[**glGetClipPlane**](glgetclipplane.md)

[**glIsEnabled**](glisenabled.md) with argument GL\_CLIP\_PLANE *i*

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

[**glDisable**](gldisable.md)
</dt> <dt>

[**glEnable**](glenable.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glGetClipPlane**](glgetclipplane.md)
</dt> <dt>

[**glIsEnabled**](glisenabled.md)
</dt> </dl>

 

 





