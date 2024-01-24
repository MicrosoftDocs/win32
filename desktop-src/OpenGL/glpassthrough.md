---
title: glPassThrough function (Gl.h)
description: The glPassThrough function places a marker in the feedback buffer.
ms.assetid: 14664ac6-eb25-46ae-86d8-7ece31df103f
keywords:
- glPassThrough function OpenGL
topic_type:
- apiref
api_name:
- glPassThrough
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glPassThrough function

The **glPassThrough** function places a marker in the feedback buffer.

## Syntax


```C++
void WINAPI glPassThrough(
   GLfloat token
);
```



## Parameters

<dl> <dt>

*token* 
</dt> <dd>

A marker value to be placed in the feedback buffer. It is indicated with the following unique identifying value.



| Value                                                                                                                                                                                   | Meaning                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_PASS_THROUGH_TOKEN"></span><span id="gl_pass_through_token"></span><dl> <dt>**GL\_PASS\_THROUGH\_TOKEN**</dt> </dl> | The order of **glPassThrough** commands with respect to the specification of graphics primitives is maintained.<br/> |



 

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error code can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

Feedback is an OpenGL render mode selected by calling [**glRenderMode**](glrendermode.md) with GL\_FEEDBACK. When OpenGL is in feedback mode, no pixels are produced by rasterization. Instead, information about primitives that would have been rasterized is fed back to the application by OpenGL. See [**glFeedbackBuffer**](glfeedbackbuffer.md) for a description of the feedback buffer and the values in it.

The **glPassThrough** function inserts a user-defined marker in the feedback buffer when it is executed in feedback mode. The *token* parameter is returned as if it were a primitive.

The **glPassThrough** function is ignored if OpenGL is not in feedback mode.

The following function retrieves information related to **glPassThrough**:

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

[**glRenderMode**](glrendermode.md)
</dt> </dl>

 

 





