---
title: glDepthFunc function (Gl.h)
description: The glDepthFunc function specifies the value used for depth-buffer comparisons.
ms.assetid: 6ab8774a-8887-4c1e-b567-4492c0a60cf2
keywords:
- glDepthFunc function OpenGL
topic_type:
- apiref
api_name:
- glDepthFunc
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glDepthFunc function

The **glDepthFunc** function specifies the value used for depth-buffer comparisons.

## Syntax


```C++
void WINAPI glDepthFunc(
   GLenum func
);
```



## Parameters

<dl> <dt>

*func* 
</dt> <dd>

Specifies the depth-comparison function. The following symbolic constants are accepted.



| Value                                                                                                                                                   | Meaning                                                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| <span id="GL_NEVER"></span><span id="gl_never"></span><dl> <dt>**GL\_NEVER**</dt> </dl>          | Never passes.<br/>                                                                                  |
| <span id="GL_LESS"></span><span id="gl_less"></span><dl> <dt>**GL\_LESS**</dt> </dl>             | Passes if the incoming *z* value is less than the stored *z* value. This is the default value.<br/> |
| <span id="GL_LEQUAL"></span><span id="gl_lequal"></span><dl> <dt>**GL\_LEQUAL**</dt> </dl>       | Passes if the incoming z value is less than or equal to the stored z value.<br/>                    |
| <span id="GL_EQUAL"></span><span id="gl_equal"></span><dl> <dt>**GL\_EQUAL**</dt> </dl>          | Passes if the incoming z value is equal to the stored z value.<br/>                                 |
| <span id="GL_GREATER"></span><span id="gl_greater"></span><dl> <dt>**GL\_GREATER**</dt> </dl>    | Passes if the incoming z value is greater than the stored z value.<br/>                             |
| <span id="GL_NOTEQUAL"></span><span id="gl_notequal"></span><dl> <dt>**GL\_NOTEQUAL**</dt> </dl> | Passes if the incoming z value is not equal to the stored z value.<br/>                             |
| <span id="GL_GEQUAL"></span><span id="gl_gequal"></span><dl> <dt>**GL\_GEQUAL**</dt> </dl>       | Passes if the incoming z value is greater than or equal to the stored z value.<br/>                 |
| <span id="GL_ALWAYS"></span><span id="gl_always"></span><dl> <dt>**GL\_ALWAYS**</dt> </dl>       | Always passes.<br/>                                                                                 |



 

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error code can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glDepthFunc** function specifies the function used to compare each incoming pixel *z* value with the *z* value present in the depth buffer. The comparison is performed only if depth testing is enabled. (See [**glEnable**](glenable.md) with the argument GL\_DEPTH\_TEST.)

Initially, depth testing is disabled.

The following functions retrieve information related to **glDepthFunc**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_DEPTH\_FUNC

[**glIsEnabled**](glisenabled.md) with argument GL\_DEPTH\_TEST

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

[**glDepthRange**](gldepthrange.md)
</dt> <dt>

[**glEnable**](glenable.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**glIsEnabled**](glisenabled.md)
</dt> </dl>

 

 





