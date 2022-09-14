---
title: glDrawBuffer function (Gl.h)
description: The glDrawBuffer function specifies which color buffers are to be drawn into.
ms.assetid: ea625699-303b-4e60-b9aa-771949a8d52d
keywords:
- glDrawBuffer function OpenGL
topic_type:
- apiref
api_name:
- glDrawBuffer
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glDrawBuffer function

The **glDrawBuffer** function specifies which color buffers are to be drawn into.

## Syntax


```C++
void WINAPI glDrawBuffer(
   GLenum mode
);
```



## Parameters

<dl> <dt>

*mode* 
</dt> <dd>

Specifies up to four color buffers to be drawn into with the following acceptable symbolic constants.



| Value                                                                                                                                                                       | Meaning                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_NONE"></span><span id="gl_none"></span><dl> <dt>**GL\_NONE**</dt> </dl>                                 | No color buffers are written.<br/>                                                                                                                                                                                                                                                                                                                                                                     |
| <span id="GL_FRONT_LEFT"></span><span id="gl_front_left"></span><dl> <dt>**GL\_FRONT\_LEFT**</dt> </dl>              | Only the front-left color buffer is written.<br/>                                                                                                                                                                                                                                                                                                                                                      |
| <span id="GL_FRONT_RIGHT"></span><span id="gl_front_right"></span><dl> <dt>**GL\_FRONT\_RIGHT**</dt> </dl>           | Only the front-right color buffer is written.<br/>                                                                                                                                                                                                                                                                                                                                                     |
| <span id="GL_BACK_LEFT"></span><span id="gl_back_left"></span><dl> <dt>**GL\_BACK\_LEFT**</dt> </dl>                 | Only the back-left color buffer is written.<br/>                                                                                                                                                                                                                                                                                                                                                       |
| <span id="GL_BACK_RIGHT"></span><span id="gl_back_right"></span><dl> <dt>**GL\_BACK\_RIGHT**</dt> </dl>              | Only the back-right color buffer is written.<br/>                                                                                                                                                                                                                                                                                                                                                      |
| <span id="GL_FRONT"></span><span id="gl_front"></span><dl> <dt>**GL\_FRONT**</dt> </dl>                              | Only the front-left and front-right color buffers are written. If there is no front-right color buffer, only the front left-color buffer is written.<br/>                                                                                                                                                                                                                                              |
| <span id="GL_BACK"></span><span id="gl_back"></span><dl> <dt>**GL\_BACK**</dt> </dl>                                 | Only the back-left and back-right color buffers are written. If there is no back-right color buffer, only the back-left color buffer is written.<br/>                                                                                                                                                                                                                                                  |
| <span id="GL_LEFT"></span><span id="gl_left"></span><dl> <dt>**GL\_LEFT**</dt> </dl>                                 | Only the front-left and back-left color buffers are written. If there is no back-left color buffer, only the front-left color buffer is written.<br/>                                                                                                                                                                                                                                                  |
| <span id="GL_RIGHT"></span><span id="gl_right"></span><dl> <dt>**GL\_RIGHT**</dt> </dl>                              | Only the front-right and back-right color buffers are written. If there is no back-right color buffer, only the front-right color buffer is written.<br/>                                                                                                                                                                                                                                              |
| <span id="GL_FRONT_AND_BACK"></span><span id="gl_front_and_back"></span><dl> <dt>**GL\_FRONT\_AND\_BACK**</dt> </dl> | All the front and back color buffers (front-left, front-right, back-left, back-right) are written. If there are no back color buffers, only the front-left and front-right color buffers are written. If there are no right color buffers, only the front-left and back-left color buffers are written. If there are no right or back color buffers, only the front-left color buffer is written.<br/> |
| <span id="GL_AUXi"></span><span id="gl_auxi"></span><span id="GL_AUXI"></span><dl> <dt>**GL\_AUXi**</dt> </dl>       | Only the auxiliary color buffer *i* is written; *i* is between 0 and GL\_AUX\_BUFFERS - 1. (GL\_AUX\_BUFFERS is not the upper limit; use [**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) to query the number of available auxiliary buffers.)<br/>                                                                                                                            |



 

The default value is GL\_FRONT for single-buffered contexts, and GL\_BACK for double-buffered contexts.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *mode* was not an accepted value.<br/>                                                                                          |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | None of the buffers indicated by *mode* existed.<br/>                                                                           |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |


## Remarks

When colors are written to the framebuffer, they are written into the color buffers specified by **glDrawBuffer**.

If more than one color buffer is selected for drawing, then blending or logical operations are computed and applied independently for each color buffer and can produce different results in each buffer.

Monoscopic contexts include only left buffers, and stereoscopic contexts include both left and right buffers. Likewise, single-buffered contexts include only front buffers, and double-buffered contexts include both front and back buffers. The context is selected at OpenGL initialization.

It is always the case that GL\_AUX *i* = GL\_AUX0 + *i*.

The following functions retrieve information related to the **glDrawBuffer** function:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_DRAW\_BUFFER

**glGet** with argument GL\_AUX\_BUFFERS

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

[**glBlendFunc**](glblendfunc.md)
</dt> <dt>

[**glColorMask**](glcolormask.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**glIndexMask**](glindexmask.md)
</dt> <dt>

[**glLogicOp**](gllogicop.md)
</dt> <dt>

[**glReadBuffer**](glreadbuffer.md)
</dt> </dl>

 

 





