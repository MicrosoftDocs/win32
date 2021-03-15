---
title: glGetTexEnviv function (Gl.h)
description: The glGetTexEnvfv and glGetTexEnviv functions return texture environment parameters. | glGetTexEnviv function (Gl.h)
ms.assetid: c1429cb9-4392-41ef-a978-a51db66445f2
keywords:
- glGetTexEnviv function OpenGL
topic_type:
- apiref
api_name:
- glGetTexEnviv
api_location:
- Opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glGetTexEnviv function

The [**glGetTexEnvfv**](glgettexenvfv.md) and **glGetTexEnviv** functions return texture environment parameters.

## Syntax


```C++
void WINAPI glGetTexEnviv(
   GLenum target,
   GLenum pname,
   GLint  *params
);
```



## Parameters

<dl> <dt>

*target* 
</dt> <dd>

A texture environment. Must be GL\_TEXTURE\_ENV.

</dd> <dt>

*pname* 
</dt> <dd>

The symbolic name of a texture environment parameter. The following values are accepted.



| Value                                                                                                                                                                                | Meaning                                                                                                                                                                                                                                                                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_TEXTURE_ENV_MODE"></span><span id="gl_texture_env_mode"></span><dl> <dt>**GL\_TEXTURE\_ENV\_MODE**</dt> </dl>    | The *params* parameter returns the single-valued texture environment mode, a symbolic constant.<br/>                                                                                                                                                                                                                                           |
| <span id="GL_TEXTURE_ENV_COLOR"></span><span id="gl_texture_env_color"></span><dl> <dt>**GL\_TEXTURE\_ENV\_COLOR**</dt> </dl> | The *params* parameter returns four integer or floating-point values that are the texture environment color. Integer values, when requested, are linearly mapped from the internal floating-point representation such that 1.0 maps to the most positive representable integer, and -1.0 maps to the most negative representable integer.<br/> |



 

</dd> <dt>

*params* 
</dt> <dd>

Returns the requested data.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *target* or *pname* was not an accepted value.<br/>                                                                             |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glGetTexEnv** function returns in *params* selected values of a texture environment that was specified with [**glTexEnv**](gltexenv-functions.md). The *target* parameter specifies a texture environment. Currently, only one texture environment is defined and supported: GL\_TEXTURE\_ENV.

The *pname* parameter names a specific texture environment parameter.

If an error is generated, no change is made to the contents of *params*.

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

[**glTexEnv**](gltexenv-functions.md)
</dt> </dl>

 

 





