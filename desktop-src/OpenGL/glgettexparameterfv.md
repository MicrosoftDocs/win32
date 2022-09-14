---
title: glGetTexParameterfv function (Gl.h)
description: The glGetTexParameterfv and glGetTexParameteriv functions return texture parameter values. | glGetTexParameterfv function (Gl.h)
ms.assetid: 616292ea-222c-4efe-bb69-3058d9c99910
keywords:
- glGetTexParameterfv function OpenGL
topic_type:
- apiref
api_name:
- glGetTexParameterfv
api_location:
- Opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glGetTexParameterfv function

The **glGetTexParameterfv** and [**glGetTexParameteriv**](glgettexparameteriv.md) functions return texture parameter values.

## Syntax


```C++
void WINAPI glGetTexParameterfv(
   GLenum  target,
   GLenum  pname,
   GLfloat *params
);
```



## Parameters

<dl> <dt>

*target* 
</dt> <dd>

The symbolic name of the target texture. GL\_TEXTURE\_1D and GL\_TEXTURE\_2D are accepted.

</dd> <dt>

*pname* 
</dt> <dd>

The symbolic name of a texture parameter. The following values are accepted.



| Value                                                                                                                                                                                         | Meaning                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_TEXTURE_MAG_FILTER"></span><span id="gl_texture_mag_filter"></span><dl> <dt>**GL\_TEXTURE\_MAG\_FILTER**</dt> </dl>       | Returns the single-valued texture magnification filter, a symbolic constant.<br/>                                                                                                                                                                                                                                                                                                      |
| <span id="GL_TEXTURE_MIN_FILTER"></span><span id="gl_texture_min_filter"></span><dl> <dt>**GL\_TEXTURE\_MIN\_FILTER**</dt> </dl>       | Returns the single-valued texture minification filter, a symbolic constant.<br/>                                                                                                                                                                                                                                                                                                       |
| <span id="GL_TEXTURE_WRAP_S"></span><span id="gl_texture_wrap_s"></span><dl> <dt>**GL\_TEXTURE\_WRAP\_S**</dt> </dl>                   | Returns the single-valued wrapping function for texture coordinate *s*, a symbolic constant.<br/>                                                                                                                                                                                                                                                                                      |
| <span id="GL_TEXTURE_WRAP_T"></span><span id="gl_texture_wrap_t"></span><dl> <dt>**GL\_TEXTURE\_WRAP\_T**</dt> </dl>                   | Returns the single-valued wrapping function for texture coordinate *t*, a symbolic constant.<br/>                                                                                                                                                                                                                                                                                      |
| <span id="GL_TEXTURE_BORDER_COLOR"></span><span id="gl_texture_border_color"></span><dl> <dt>**GL\_TEXTURE\_BORDER\_COLOR**</dt> </dl> | Returns four integer or floating-point numbers that comprise the RGBA color of the texture border. Floating-point values are returned in the range \[0,1\]. Integer values are returned as a linear mapping of the internal floating-point representation such that 1.0 maps to the most positive representable integer and -1.0 maps to the most negative representable integer.<br/> |
| <span id="GL_TEXTURE_PRIORITY"></span><span id="gl_texture_priority"></span><dl> <dt>**GL\_TEXTURE\_PRIORITY**</dt> </dl>              | Returns the residence priority of the target texture (or the named texture bound to it). The initial value is 1. See [**glPrioritizeTextures**](glprioritizetextures.md).<br/>                                                                                                                                                                                                        |
| <span id="GL_TEXTURE_RESIDENT"></span><span id="gl_texture_resident"></span><dl> <dt>**GL\_TEXTURE\_RESIDENT**</dt> </dl>              | Returns the residence status of the target texture. If the value returned in params is GL\_TRUE, the texture is resident in texture memory. See [**glAreTexturesResident**](glaretexturesresident.md).<br/>                                                                                                                                                                           |



 

</dd> <dt>

*params* 
</dt> <dd>

Returns the texture parameters.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *target* or *name* was not an accepted value.<br/>                                                                              |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glGetTexParameter** function returns in *params* the value or values of the texture parameter specified as *pname*. The *target* parameter defines the target texture, either GL\_TEXTURE\_1D or GL\_TEXTURE\_2D, to specify one-dimensional or two-dimensional texturing. The *pname* parameter accepts the same symbols as [**glTexParameter**](gltexparameter-functions.md), with the same interpretations.

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

[**glTexParameter**](gltexparameter-functions.md)
</dt> </dl>

 

 





