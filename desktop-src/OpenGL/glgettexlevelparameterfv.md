---
title: glGetTexLevelParameterfv function (Gl.h)
description: The glGetTexLevelParameterfv and glGetTexLevelParameteriv functions return texture parameter values for a specific level of detail. | glGetTexLevelParameterfv function (Gl.h)
ms.assetid: 5ea91f2e-c0cd-41ee-be95-df096f1c78ef
keywords:
- glGetTexLevelParameterfv function OpenGL
topic_type:
- apiref
api_name:
- glGetTexLevelParameterfv
api_location:
- Opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glGetTexLevelParameterfv function

The **glGetTexLevelParameterfv** and [**glGetTexLevelParameteriv**](glgettexlevelparameteriv.md) functions return texture parameter values for a specific level of detail.

## Syntax


```C++
void WINAPI glGetTexLevelParameterfv(
   GLenum  target,
   GLint   level,
   GLenum  pname,
   GLfloat *params
);
```



## Parameters

<dl> <dt>

*target* 
</dt> <dd>

The symbolic name of the target texture: either GL\_TEXTURE\_1D, GL\_TEXTURE\_2D, GL\_PROXY\_TEXTURE\_1D, or GL\_PROXY\_TEXTURE\_2D.

</dd> <dt>

*level* 
</dt> <dd>

The level-of-detail number of the desired image. Level 0 is the base image level. Level *n* is the *n*th mipmap reduction image.

</dd> <dt>

*pname* 
</dt> <dd>

The symbolic name of a texture parameter. The following parameter names are accepted.



| Value                                                                                                                                                                                                  | Meaning                                                                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_TEXTURE_WIDTH"></span><span id="gl_texture_width"></span><dl> <dt>**GL\_TEXTURE\_WIDTH**</dt> </dl>                                | The *params* parameter returns a single value containing the width of the texture image. This value includes the border of the texture image.<br/>                                                                                                                                          |
| <span id="GL_TEXTURE_HEIGHT"></span><span id="gl_texture_height"></span><dl> <dt>**GL\_TEXTURE\_HEIGHT**</dt> </dl>                             | The *params* parameter returns a single value containing the height of the texture image. This value includes the border of the texture image.<br/>                                                                                                                                         |
| <span id="GL_TEXTURE_INTERNAL_FORMAT"></span><span id="gl_texture_internal_format"></span><dl> <dt>**GL\_TEXTURE\_INTERNAL\_FORMAT**</dt> </dl> | The *params* parameter returns a single value which describes the texel format of the texture.<br/>                                                                                                                                                                                         |
| <span id="GL_TEXTURE_BORDER"></span><span id="gl_texture_border"></span><dl> <dt>**GL\_TEXTURE\_BORDER**</dt> </dl>                             | The *params* parameter returns a single value: the width in pixels of the border of the texture image.<br/>                                                                                                                                                                                 |
| <span id="GL_TEXTURE_RED_SIZE"></span><span id="gl_texture_red_size"></span><dl> <dt>**GL\_TEXTURE\_RED\_SIZE**</dt> </dl>                      | The internal storage resolution of the red component of a texel. The resolution chosen by the OpenGL will be a close match for the resolution requested by the user with the component argument of [**glTexImage1D**](glteximage1d.md) or [**glTexImage2D**](glteximage2d.md).<br/>       |
| <span id="GL_TEXTURE_GREEN_SIZE"></span><span id="gl_texture_green_size"></span><dl> <dt>**GL\_TEXTURE\_GREEN\_SIZE**</dt> </dl>                | The internal storage resolution of the green component of a texel. The resolution chosen by the OpenGL will be a close match for the resolution requested by the user with the component argument of [**glTexImage1D**](glteximage1d.md) or [**glTexImage2D**](glteximage2d.md).<br/>     |
| <span id="GL_TEXTURE_BLUE_SIZE"></span><span id="gl_texture_blue_size"></span><dl> <dt>**GL\_TEXTURE\_BLUE\_SIZE**</dt> </dl>                   | The internal storage resolution of the blue component of a texel. The resolution chosen by the OpenGL will be a close match for the resolution requested by the user with the component argument of [**glTexImage1D**](glteximage1d.md) or [**glTexImage2D**](glteximage2d.md).<br/>      |
| <span id="GL_TEXTURE_ALPHA_SIZE"></span><span id="gl_texture_alpha_size"></span><dl> <dt>**GL\_TEXTURE\_ALPHA\_SIZE**</dt> </dl>                | The internal storage resolution of the alpha component of a texel. The resolution chosen by the OpenGL will be a close match for the resolution requested by the user with the component argument of [**glTexImage1D**](glteximage1d.md) or [**glTexImage2D**](glteximage2d.md).<br/>     |
| <span id="GL_TEXTURE_LUMINANCE_SIZE"></span><span id="gl_texture_luminance_size"></span><dl> <dt>**GL\_TEXTURE\_LUMINANCE\_SIZE**</dt> </dl>    | The internal storage resolution of the luminance component of a texel. The resolution chosen by the OpenGL will be a close match for the resolution requested by the user with the component argument of [**glTexImage1D**](glteximage1d.md) or [**glTexImage2D**](glteximage2d.md).<br/> |
| <span id="GL_TEXTURE_INTENSITY_SIZE"></span><span id="gl_texture_intensity_size"></span><dl> <dt>**GL\_TEXTURE\_INTENSITY\_SIZE**</dt> </dl>    | The internal storage resolution of the intensity component of a texel. The resolution chosen by the OpenGL will be a close match for the resolution requested by the user with the component argument of [**glTexImage1D**](glteximage1d.md) or [**glTexImage2D**](glteximage2d.md).<br/> |
| <span id="GL_TEXTURE_COMPONENTS"></span><span id="gl_texture_components"></span><dl> <dt>**GL\_TEXTURE\_COMPONENTS**</dt> </dl>                 | The *params* parameter returns a single value: the number of components in the texture image.<br/>                                                                                                                                                                                          |



 

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
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | *level* is less than zero or greater than *log*2*(max)*, where *max* is the returned value of GL\_MAX\_TEXTURE\_SIZE.<br/>      |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glGetTexLevelParameter** function returns in *params* texture parameter values for a specific level-of-detail value, specified as *level*. The *target* parameter defines the target texture, either GL\_TEXTURE\_1D, GL\_TEXTURE\_2D, GL\_PROXY\_TEXTURE\_1D, or GL\_PROXY\_TEXTURE\_2D to specify one-dimensional or two-dimensional texturing. The *pname* parameter specifies the texture parameter whose value or values will be returned.

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

[**glGetTexParameter**](glgettexparameter.md)
</dt> <dt>

[**glTexImage1D**](glteximage1d.md)
</dt> <dt>

[**glTexImage2D**](glteximage2d.md)
</dt> <dt>

[**glTexParameter**](gltexparameter-functions.md)
</dt> </dl>

 

 





