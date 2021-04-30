---
title: glTexSubImage2D function (Gl.h)
description: The glTexSubImage2D function specifies a portion of an existing one-dimensional texture image. You cannot define a new texture with glTexSubImage2D.
ms.assetid: 2b6cb663-8e1d-4270-b8ba-5a8b43a2ece7
keywords:
- glTexSubImage2D function OpenGL
topic_type:
- apiref
api_name:
- glTexSubImage2D
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glTexSubImage2D function

The **glTexSubImage2D** function specifies a portion of an existing one-dimensional texture image. You cannot define a new texture with **glTexSubImage2D**.

## Syntax


```C++
void WINAPI glTexSubImage2D(
         GLenum  target,
         GLint   level,
         GLint   xoffset,
         GLint   yoffset,
         GLsizei width,
         GLsizei height,
         GLenum  format,
         GLenum  type,
   const GLvoid  *pixels
);
```



## Parameters

<dl> <dt>

*target* 
</dt> <dd>

The target texture. Must be GL\_TEXTURE\_2D.

</dd> <dt>

*level* 
</dt> <dd>

The level-of-detail number. Level 0 is the base image. Level *n* is the *n*th mipmap reduction image.

</dd> <dt>

*xoffset* 
</dt> <dd>

A texel offset in the *x* direction within the texture array.

</dd> <dt>

*yoffset* 
</dt> <dd>

A texel offset in the *y* direction within the texture array.

</dd> <dt>

*width* 
</dt> <dd>

The width of the texture sub-image.

</dd> <dt>

*height* 
</dt> <dd>

The height of the texture sub-image.

</dd> <dt>

*format* 
</dt> <dd>

The format of the pixel data. It can assume one of the following symbolic values.



| Value                                                                                                                                                                         | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_COLOR_INDEX"></span><span id="gl_color_index"></span><dl> <dt>**GL\_COLOR\_INDEX**</dt> </dl>             | Each element is a single value, a color index. It is converted to fixed point format (with an unspecified number of 0 bits to the right of the binary point), shifted left or right, depending on the value and sign of GL\_INDEX\_SHIFT, and added to GL\_INDEX\_OFFSET (see [**glPixelTransfer**](glpixeltransfer.md)). The resulting index is converted to a set of color components using the GL\_PIXEL\_MAP\_I\_TO\_R, GL\_PIXEL\_MAP\_I\_TO\_G, GL\_PIXEL\_MAP\_I\_TO\_B, and GL\_PIXEL\_MAP\_I\_TO\_A tables, and clamped to the range \[0,1\].<br/> |
| <span id="GL_RED"></span><span id="gl_red"></span><dl> <dt>**GL\_RED**</dt> </dl>                                      | Each element is a single red component. It is converted to floating point format and assembled into an RGBA element by attaching 0.0 for green and blue, and 1.0 for alpha. Each component is then multiplied by the signed scale factor GL\_c\_SCALE, added to the signed bias GL\_c\_BIAS, and clamped to the range \[0,1\] (see **glPixelTransfer**).<br/>                                                                                                                                                                                                |
| <span id="GL_GREEN"></span><span id="gl_green"></span><dl> <dt>**GL\_GREEN**</dt> </dl>                                | Each element is a single green component. It is converted to floating point format and assembled into an RGBA element by attaching 0.0 for red and blue, and 1.0 for alpha. Each component is then multiplied by the signed scale factor GL\_c\_SCALE, added to the signed bias GL\_c\_BIAS, and clamped to the range \[0,1\] (see [**glPixelTransfer**](glpixeltransfer.md)).<br/>                                                                                                                                                                         |
| <span id="GL_BLUE"></span><span id="gl_blue"></span><dl> <dt>**GL\_BLUE**</dt> </dl>                                   | Each element is a single blue component. It is converted to floating point format and assembled into an RGBA element by attaching 0.0 for red and green, and 1.0 for alpha. Each component is then multiplied by the signed scale factor GL\_c\_SCALE, added to the signed bias GL\_c\_BIAS, and clamped to the range \[0,1\] (see **glPixelTransfer**).<br/>                                                                                                                                                                                                |
| <span id="GL_ALPHA"></span><span id="gl_alpha"></span><dl> <dt>**GL\_ALPHA**</dt> </dl>                                | Each element is a single alpha component. It is converted to floating point format and assembled into an RGBA element by attaching 0.0 for red, green, and blue. Each component is then multiplied by the signed scale factor GL\_c\_SCALE, added to the signed bias GL\_c\_BIAS, and clamped to the range \[0,1\] (see [**glPixelTransfer**](glpixeltransfer.md)).<br/>                                                                                                                                                                                    |
| <span id="GL_RGB"></span><span id="gl_rgb"></span><dl> <dt>**GL\_RGB**</dt> </dl>                                      | Each element is an RGB triple. It is converted to floating point format and assembled into an RGBA element by attaching 1.0 for alpha. Each component is then multiplied by the signed scale factor GL\_c\_SCALE, added to the signed bias GL\_c\_BIAS, and clamped to the range \[0,1\] (see **glPixelTransfer**).<br/>                                                                                                                                                                                                                                     |
| <span id="GL_RGBA"></span><span id="gl_rgba"></span><dl> <dt>**GL\_RGBA**</dt> </dl>                                   | Each element is a complete RGBA element. It is converted to floating point. Each component is then multiplied by the signed scale factor GL\_c\_SCALE, added to the signed bias GL\_c\_BIAS, and clamped to the range \[0,1\] (see **glPixelTransfer**).<br/>                                                                                                                                                                                                                                                                                                |
| <span id="GL_LUMINANCE"></span><span id="gl_luminance"></span><dl> <dt>**GL\_LUMINANCE**</dt> </dl>                    | Each element is a single luminance value. It is converted to floating point format, and then assembled into an RGBA element by replicating the luminance value three times for red, green, and blue, and attaching 1.0 for alpha. Each component is then multiplied by the signed scale factor GL\_c\_SCALE, added to the signed bias GL\_c\_BIAS, and clamped to the range \[0,1\] (see [**glPixelTransfer**](glpixeltransfer.md)).<br/>                                                                                                                   |
| <span id="GL_LUMINANCE_ALPHA"></span><span id="gl_luminance_alpha"></span><dl> <dt>**GL\_LUMINANCE\_ALPHA**</dt> </dl> | Each element is a luminance/alpha pair. It is converted to floating point format, and then assembled into an RGBA element by replicating the luminance value three times for red, green, and blue. Each component is then multiplied by the signed scale factor GL\_c\_SCALE, added to the signed bias GL\_c\_BIAS, and clamped to the range \[0,1\] (see **glPixelTransfer**).<br/>                                                                                                                                                                         |



 

</dd> <dt>

*type* 
</dt> <dd>

The data type of the pixel data. The following symbolic values are accepted: GL\_UNSIGNED\_BYTE, GL\_BYTE, GL\_BITMAP, GL\_UNSIGNED\_SHORT, GL\_SHORT, GL\_UNSIGNED\_INT, GL\_INT, and GL\_FLOAT.

</dd> <dt>

*pixels* 
</dt> <dd>

A pointer to the image data in memory.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *target* was not GL\_TEXTURE\_2D.<br/>                                                                                                                                                                                                                                                                                                                                                                 |
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *format* was not an accepted constant.<br/>                                                                                                                                                                                                                                                                                                                                                            |
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *type* was not an accepted constant.<br/>                                                                                                                                                                                                                                                                                                                                                              |
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *type* was GL\_BITMAP and *format* was not GL\_COLOR\_INDEX.<br/>                                                                                                                                                                                                                                                                                                                                      |
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | *level* was less than zero or greater than log2 *max*, where *max* was the returned value of GL\_MAX\_TEXTURE\_SIZE.<br/>                                                                                                                                                                                                                                                                              |
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | *xoffset* was less than -*b*; or *xoffset* + *width* was greater than *w* - *b*; or *yoffset* was less than -*b*; or *yoffset* + *height* was greater than *h* - *b*, where *w* is the GL\_TEXTURE\_WIDTH, *h* is the GL\_TEXTURE\_HEIGHT, and *b* is the width of the GL\_TEXTURE\_BORDER of the texture image being modified. <br/> Note that *w* and *h* include twice the border width.<br/> |
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | *width* was was less than *b*, where *b* is the border width of the texture array.<br/>                                                                                                                                                                                                                                                                                                                |
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | *border* was not zero or 1.<br/>                                                                                                                                                                                                                                                                                                                                                                       |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The texture array was not defined by a previous **glTexImage2D** operation.<br/>                                                                                                                                                                                                                                                                                                                       |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/>                                                                                                                                                                                                                                                                        |



## Remarks

Two-dimensional texturing for a primitive is enabled using [**glEnable**](glenable.md) and **glDisable** with the argument GL\_TEXTURE\_2D. During texturing, part of a specified texture image is mapped into each enabled primitive. You use the **glTexSubImage2D** function to specify a contiguous sub-image of an existing two-dimensional texture image for texturing.

The texels referenced by *pixels* replace a region of the existing texture array with *x* indexes of *xoffset* and *xoffset* + (*width* 1) inclusive and *y* indexes of *yoffset* and *yoffset* + (*height* 1) inclusive. This region cannot include any texels outside the range of the originally specified texture array.

Specifying a sub-image with a *width* of zero has no effect and does not generate an error.

Texturing has no effect in color-index mode.

In general, texture images can be represented by the same data formats as the pixels in a [**glDrawPixels**](gldrawpixels.md) command, except that GL\_STENCIL\_INDEX and GL\_DEPTH\_COMPONENT cannot be used. The [**glPixelStore**](glpixelstore-functions.md) and [**glPixelTransfer**](glpixeltransfer.md) modes affect texture images in exactly the way they affect **glDrawPixels**.

The following functions retrieve information related to **glTexSubImage2D**:

[**glGetTexImage**](glgetteximage.md)

[**glIsEnabled**](glisenabled.md) with argument GL\_TEXTURE\_2D

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

[**glCopyTexImage1D**](glcopyteximage1d.md)
</dt> <dt>

[**glCopyTexImage2D**](glcopyteximage2d.md)
</dt> <dt>

[**glCopyTexSubImage1D**](glcopytexsubimage1d.md)
</dt> <dt>

[**glCopyTexSubImage2D**](glcopytexsubimage2d.md)
</dt> <dt>

[**glDrawPixels**](gldrawpixels.md)
</dt> <dt>

[**glEnable**](glenable.md)
</dt> <dt>

[**glFog**](glfog.md)
</dt> <dt>

[**glGetTexImage**](glgetteximage.md)
</dt> <dt>

[**glIsEnabled**](glisenabled.md)
</dt> <dt>

[**glPixelStore**](glpixelstore-functions.md)
</dt> <dt>

[**glPixelTransfer**](glpixeltransfer.md)
</dt> <dt>

[**glTexEnv**](gltexenv-functions.md)
</dt> <dt>

[**glTexGen**](gltexgen-functions.md)
</dt> <dt>

[**glTexImage1D**](glteximage1d.md)
</dt> <dt>

[**glTexImage2D**](glteximage2d.md)
</dt> <dt>

[**glTexSubImage1D**](gltexsubimage1d.md)
</dt> <dt>

[**glTexImage2D**](glteximage2d.md)
</dt> <dt>

[**glTexParameter**](gltexparameter-functions.md)
</dt> </dl>

 

 





