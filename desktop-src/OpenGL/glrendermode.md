---
title: glRenderMode function (Gl.h)
description: The glRenderMode function sets the rasterization mode.
ms.assetid: bcbc3bba-c552-425b-8284-6cadff0c9f56
keywords:
- glRenderMode function OpenGL
topic_type:
- apiref
api_name:
- glRenderMode
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glRenderMode function

The **glRenderMode** function sets the rasterization mode.

## Syntax


```C++
GLint WINAPI glRenderMode(
   GLenum mode
);
```



## Parameters

<dl> <dt>

*mode* 
</dt> <dd>

The rasterization mode. The following three values are accepted. The default value is GL\_RENDER.



| Value                                                                                                                                                   | Meaning                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_RENDER"></span><span id="gl_render"></span><dl> <dt>**GL\_RENDER**</dt> </dl>       | Render mode. Primitives are rasterized, producing pixel fragments, which are written into the framebuffer. This is the normal mode and also the default mode.<br/>                                                                                                                                                                                                      |
| <span id="GL_SELECT"></span><span id="gl_select"></span><dl> <dt>**GL\_SELECT**</dt> </dl>       | Selection mode. No pixel fragments are produced, and no change to the framebuffer contents is made. Instead, a record of the names of primitives that would have been drawn if the render mode was GL\_RENDER is returned in a select buffer, which must be created (see [**glSelectBuffer**](glselectbuffer.md)) before selection mode is entered.<br/>               |
| <span id="GL_FEEDBACK"></span><span id="gl_feedback"></span><dl> <dt>**GL\_FEEDBACK**</dt> </dl> | Feedback mode. No pixel fragments are produced, and no change to the framebuffer contents is made. Instead, the coordinates and attributes of vertices that would have been drawn had the render mode been GL\_RENDER are returned in a feedback buffer, which must be created (see [**glFeedbackBuffer**](glfeedbackbuffer.md)) before feedback mode is entered.<br/> |



 

</dd> </dl>

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *mode* was not one of three accepted values.<br/>                                                                                     |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called with argument GL\_SELECT before [**glSelectBuffer**](glselectbuffer.md) was called at least once.<br/>       |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called with argument GL\_FEEDBACK before [**glBeedbackBuffer**](glfeedbackbuffer.md) was called at least once.<br/> |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/>       |



## Remarks

The **glRenderMode** function takes one argument, *mode*, which can assume one of three predefined values above.

The return value of the **glRenderMode** function is determined by the render mode at the time **glRenderMode** is called, rather than by *mode*. The values returned for the three render modes are as follows.



| Value        | Meaning                                                                 |
|--------------|-------------------------------------------------------------------------|
| GL\_RENDER   | Zero.                                                                   |
| GL\_SELECT   | The number of hit records transferred to the select buffer.             |
| GL\_FEEDBACK | The number of values (not vertices) transferred to the feedback buffer. |



 

Refer to [**glSelectBuffer**](glselectbuffer.md) and [**glFeedbackBuffer**](glfeedbackbuffer.md) for more details concerning selection and feedback operation.

If an error is generated, **glRenderMode** returns zero regardless of the current render mode.

The following function retrieves information related to **glRenderMode**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_RENDER\_MODE

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

[**glFeedbackBuffer**](glfeedbackbuffer.md)
</dt> <dt>

[**glInitNames**](glinitnames.md)
</dt> <dt>

[**glLoadName**](glloadname.md)
</dt> <dt>

[**glPassThrough**](glpassthrough.md)
</dt> <dt>

[**glPushName**](glpushname.md)
</dt> <dt>

[**glSelectBuffer**](glselectbuffer.md)
</dt> </dl>

 

 





