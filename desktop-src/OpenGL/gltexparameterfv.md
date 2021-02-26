---
title: glTexParameterfv function (Gl.h)
description: Sets texture parameters. | glTexParameterfv function (Gl.h)
ms.assetid: 29aa2823-5c73-48f1-891f-018dd7a93323
keywords:
- glTexParameterfv function OpenGL
topic_type:
- apiref
api_name:
- glTexParameterfv
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glTexParameterfv function

Sets texture parameters.

## Syntax


```C++
void WINAPI glTexParameterfv(
         GLenum  target,
         GLenum  pname,
   const GLfloat *params
);
```



## Parameters

<dl> <dt>

*target* 
</dt> <dd>

The target texture, which must be either GL\_TEXTURE\_1D or GL\_TEXTURE\_2D.

</dd> <dt>

*pname* 
</dt> <dd>

The symbolic name of a single valued texture parameter. The following symbols are accepted in *pname*.



| Value                                                                                                                                                                                         | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_TEXTURE_MIN_FILTER"></span><span id="gl_texture_min_filter"></span><dl> <dt>**GL\_TEXTURE\_MIN\_FILTER**</dt> </dl>       | The texture minifying function is used whenever the pixel being textured maps to an area greater than one texture element. There are six defined minifying functions. Two of them use the nearest one or nearest four texture elements to compute the texture value. The other four use mipmaps. <br/> A mipmap is an ordered set of arrays representing the same image at progressively lower resolutions. If the texture has dimensions 2nx2<sup>m</sup> there are max(n, m) + 1 mipmaps. The first mipmap is the original texture, with dimensions 2nx2<sup>m</sup>. Each subsequent mipmap has dimensions 2<sup>k</sup>1x2<sup>l</sup>1 where 2<sup>k</sup>x2<sup>l</sup> are the dimensions of the previous mipmap, until either k = 0 or l = 0. At that point, subsequent mipmaps have dimension 1x2<sup>l</sup>1 or 2<sup>k</sup>1x1 until the final mipmap, which has dimension 1x1. Mipmaps are defined using [**glTexImage1D**](glteximage1d.md) or [**glTexImage2D**](glteximage2d.md) with the level-of-detail argument indicating the order of the mipmaps. Level 0 is the original texture; level bold max(n, m) is the final 1x1 mipmap.<br/> |
| <span id="GL_TEXTURE_MAG_FILTER"></span><span id="gl_texture_mag_filter"></span><dl> <dt>**GL\_TEXTURE\_MAG\_FILTER**</dt> </dl>       | The texture magnification function is used when the pixel being textured maps to an area less than or equal to one texture element. It sets the texture magnification function to either GL\_NEAREST or GL\_LINEAR.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <span id="GL_TEXTURE_WRAP_S"></span><span id="gl_texture_wrap_s"></span><dl> <dt>**GL\_TEXTURE\_WRAP\_S**</dt> </dl>                   | Sets the wrap parameter for texture coordinate s to either GL\_CLAMP or GL\_REPEAT. GL\_CLAMP causes s coordinates to be clamped to the range \[0,1\] and is useful for preventing wrapping artifacts when mapping a single image onto an object. GL\_REPEAT causes the integer part of the s coordinate to be ignored; OpenGL uses only the fractional part, thereby creating a repeating pattern. Border texture elements are accessed only if wrapping is set to GL\_CLAMP. Initially, GL\_TEXTURE\_WRAP\_S is set to GL\_REPEAT.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <span id="GL_TEXTURE_WRAP_T"></span><span id="gl_texture_wrap_t"></span><dl> <dt>**GL\_TEXTURE\_WRAP\_T**</dt> </dl>                   | Sets the wrap parameter for texture coordinate t to either GL\_CLAMP or GL\_REPEAT. See the discussion under GL\_TEXTURE\_WRAP\_S. Initially, GL\_TEXTURE\_WRAP\_T is set to GL\_REPEAT.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <span id="GL_TEXTURE_BORDER_COLOR"></span><span id="gl_texture_border_color"></span><dl> <dt>**GL\_TEXTURE\_BORDER\_COLOR**</dt> </dl> | Sets a border color. The *params* parameter contains four values that comprise the RGBA color of the texture border. Integer color components are interpreted linearly such that the most positive integer maps to 1.0, and the most negative integer maps to 1.0. The values are clamped to the range \[0,1\] when they are specified. Initially, the border color is (0, 0, 0, 0).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <span id="GL_TEXTURE_PRIORITY"></span><span id="gl_texture_priority"></span><dl> <dt>**GL\_TEXTURE\_PRIORITY**</dt> </dl>              | Specifies the texture residence priority of the currently bound texture. Permissible values are in the range \[0, 1\]. See [**glPrioritizeTextures**](glprioritizetextures.md) and [**glBindTexture**](glbindtexture.md) for more information.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |



 

</dd> <dt>

*params* 
</dt> <dd>

A pointer to an array where the value or values of pname are stored. The params parameter supplies a function for minifying the texture as one of the following.



| Value                                                                                                                                                                                               | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_NEAREST_"></span><span id="gl_nearest_"></span><dl> <dt>**GL\_NEAREST** </dt> </dl>                                             | Returns the value of the texture element that is nearest (in Manhattan distance) to the center of the pixel being textured. <br/>                                                                                                                                                                                                                                                                                                                                                                            |
| <span id="GL_LINEAR"></span><span id="gl_linear"></span><dl> <dt>**GL\_LINEAR**</dt> </dl>                                                   | Returns the weighted average of the four texture elements that are closest to the center of the pixel being textured. These can include border texture elements, depending on the values of GL\_TEXTURE\_WRAP\_S, GL\_TEXTURE\_WRAP\_T, and on the exact mapping. GL\_NEAREST is generally faster than GL\_LINEAR, but it can produce textured images with sharper edges because the transition between texture elements is not as smooth. The default value of GL\_TEXTURE\_MAG\_FILTER is GL\_LINEAR.<br/> |
| <span id="GL_NEAREST_MIPMAP_NEAREST"></span><span id="gl_nearest_mipmap_nearest"></span><dl> <dt>**GL\_NEAREST\_MIPMAP\_NEAREST**</dt> </dl> | Chooses the mipmap that most closely matches the size of the pixel being textured and uses the GL\_NEAREST criterion (the texture element nearest to the center of the pixel) to produce a texture value. <br/>                                                                                                                                                                                                                                                                                              |
| <span id="GL_LINEAR_MIPMAP_NEAREST"></span><span id="gl_linear_mipmap_nearest"></span><dl> <dt>**GL\_LINEAR\_MIPMAP\_NEAREST**</dt> </dl>    | Chooses the mipmap that most closely matches the size of the pixel being textured and uses the GL\_LINEAR criterion (a weighted average of the four texture elements that are closest to the center of the pixel) to produce a texture value. <br/>                                                                                                                                                                                                                                                          |
| <span id="GL_NEAREST_MIPMAP_LINEAR"></span><span id="gl_nearest_mipmap_linear"></span><dl> <dt>**GL\_NEAREST\_MIPMAP\_LINEAR**</dt> </dl>    | Chooses the two mipmaps that most closely match the size of the pixel being textured and uses the GL\_NEAREST criterion (the texture element nearest to the center of the pixel) to produce a texture value from each mipmap. The final texture value is a weighted average of those two values. <br/>                                                                                                                                                                                                       |
| <span id="GL_LINEAR_MIPMAP_LINEAR"></span><span id="gl_linear_mipmap_linear"></span><dl> <dt>**GL\_LINEAR\_MIPMAP\_LINEAR**</dt> </dl>       | Chooses the two mipmaps that most closely match the size of the pixel being textured and uses the GL\_LINEAR criterion (a weighted average of the four texture elements that are closest to the center of the pixel) to produce a texture value from each mipmap. The final texture value is a weighted average of those two values.<br/>                                                                                                                                                                    |



 

The *params* parameter supplies a function for magnifying the texture as one of the following.



| Value                                                                                                                                                   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_NEAREST_"></span><span id="gl_nearest_"></span><dl> <dt>**GL\_NEAREST** </dt> </dl> | Returns the value of the texture element that is nearest (in Manhattan distance) to the center of the pixel being textured. <br/>                                                                                                                                                                                                                                                                                                                                                                            |
| <span id="GL_LINEAR"></span><span id="gl_linear"></span><dl> <dt>**GL\_LINEAR**</dt> </dl>       | Returns the weighted average of the four texture elements that are closest to the center of the pixel being textured. These can include border texture elements, depending on the values of GL\_TEXTURE\_WRAP\_S, GL\_TEXTURE\_WRAP\_T, and on the exact mapping. GL\_NEAREST is generally faster than GL\_LINEAR, but it can produce textured images with sharper edges because the transition between texture elements is not as smooth. The default value of GL\_TEXTURE\_MAG\_FILTER is GL\_LINEAR.<br/> |



 

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM** </dt> </dl>     | *target* or *pname* was not one of the accepted defined values, or when *param* should have had a defined constant value (based on the value of *pname*) and did not.<br/> |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/>                                            |



## Remarks

Texture mapping is a technique that applies an image onto an object's surface as if the image were a decal or cellophane shrink-wrap. The image is created in texture space, with an (*s*, *t*) coordinate system. A texture is a one- or two-dimensional image and a set of parameters that determine how samples are derived from the image.

The **glTexParameter** function assigns the value or values in params to the texture parameter specified as pname. The target parameter defines the target texture, either GL\_TEXTURE\_1D or GL\_TEXTURE\_2D.

As more texture elements are sampled in the minification process, fewer aliasing artifacts will be apparent. While the GL\_NEAREST and GL\_LINEAR minification functions can be faster than the other four, they sample only one or four texture elements to determine the texture value of the pixel being rendered and can produce moire patterns or ragged transitions. The default value of GL\_TEXTURE\_MIN\_FILTER is GL\_NEAREST\_MIPMAP\_LINEAR.

Suppose that texturing is enabled (by calling [**glEnable**](glenable.md) with argument GL\_TEXTURE\_1D or GL\_TEXTURE\_2D) and GL\_TEXTURE\_MIN\_FILTER is set to one of the functions that requires a mipmap. If either the dimensions of the texture images currently defined (with previous calls to [**glTexImage1D**](glteximage1d.md) or [**glTexImage2D**](glteximage2d.md)) do not follow the proper sequence for mipmaps, or there are fewer texture images defined than are needed, or the set of texture images have differing numbers of texture components, then it is as if texture mapping were disabled. Linear filtering accesses the four nearest texture elements only in 2-D textures. In 1-D textures, linear filtering accesses the two nearest texture elements. The following function retrieves information related to **glTexParameterf**, **glTexParameteri**, **glTexParameterfv**, and **glTexParameteriv**:

[**glGetTexParameter**](glgettexparameter.md)

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

[**glBindTexture**](glbindtexture.md)
</dt> <dt>

[**glCopyPixels**](glcopypixels.md)
</dt> <dt>

[**glCopyTexImage1D**](glcopyteximage1d.md)
</dt> <dt>

[**glCopyTexImage2D**](glcopyteximage2d.md)
</dt> <dt>

[**glCopyTexSubImage2D**](glcopytexsubimage2d.md)
</dt> <dt>

[**glDrawPixels**](gldrawpixels.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glGetTexParameter**](glgettexparameter.md)
</dt> <dt>

[**glPixelStore**](glpixelstore-functions.md)
</dt> <dt>

[**glPixelTransfer**](glpixeltransfer.md)
</dt> <dt>

[**glPrioritizeTextures**](glprioritizetextures.md)
</dt> <dt>

[glTexEnv](gltexenv-functions.md)
</dt> <dt>

[glTexGen](gltexgen-functions.md)
</dt> <dt>

[**glTexImage1D**](glteximage1d.md)
</dt> <dt>

[**glTexImage2D**](glteximage2d.md)
</dt> <dt>

[**glTexSubImage1D**](gltexsubimage1d.md)
</dt> <dt>

[**glTexSubImage2D**](gltexsubimage2d.md)
</dt> </dl>

 

 





