---
title: glScissor function (Gl.h)
description: The glScissor function defines the scissor box.
ms.assetid: c06a1d20-bf7b-4283-b0fe-8bd80bece4ce
keywords:
- glScissor function OpenGL
topic_type:
- apiref
api_name:
- glScissor
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glScissor function

The **glScissor** function defines the scissor box.

## Syntax


```C++
void WINAPI glScissor(
   GLint   x,
   GLint   y,
   GLsizei width,
   GLsizei height
);
```



## Parameters

<dl> <dt>

*x* 
</dt> <dd>

The x (vertical axis) coordinate for the lower-left corner of the scissor box.

</dd> <dt>

*y* 
</dt> <dd>

The y (horizontal axis) coordinate for the lower-left corner of the scissor box. Together, x and y specify the lower-left corner of the scissor box. Initially (0,0).

</dd> <dt>

*width* 
</dt> <dd>

The width of the scissor box.

</dd> <dt>

*height* 
</dt> <dd>

The height of the scissor box. When an OpenGL context is *first* attached to a window, *width* and *height* are set to the dimensions of that window.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error code can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | Either *width* or *height* was negative.<br/>                                                                                   |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glScissor** function defines a rectangle, called the scissor box, in window coordinates. The first two parameters, *x* and *y*, specify the lower-left corner of the box. The *width* and *height* parameters specify the width and height of the box.

The scissor test is enabled and disabled using [**glEnable**](glenable.md) and **glDisable** with argument GL\_SCISSOR\_TEST. While the scissor test is enabled, only pixels that lie within the scissor box can be modified by drawing commands. Window coordinates have integer values at the shared corners of framebuffer pixels, so **glScissor**(0,0,1,1) allows only the lower-left pixel in the window to be modified, and **glScissor**(0,0,0,0) disallows modification to all pixels in the window.

When the scissor test is disabled, it is as though the scissor box includes the entire window.

The following functions retrieve information related to **glScissor**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_SCISSOR\_BOX

[**glIsEnabled**](glisenabled.md) with argument GL\_SCISSOR\_TEST

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

[**glEnable**](glenable.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glIsEnabled**](glisenabled.md)
</dt> <dt>

[**glViewport**](glviewport.md)
</dt> </dl>

 

 





