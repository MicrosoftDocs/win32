---
title: glTexImage1D function (Gl.h)
description: The glTexImage1D function specifies a one-dimensional texture image.
ms.assetid: 4f537b89-2ea2-4e2e-8c57-c372bf53f12c
keywords:
- glTexImage1D function OpenGL
topic_type:
- apiref
api_name:
- glTexImage1D
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glTexImage1D function

The **glTexImage1D** function specifies a one-dimensional texture image.

## Syntax


```C++
void WINAPI glTexImage1D(
         GLenum  target,
         GLint   level,
         GLint   internalformat,
         GLsizei width,
         GLint   border,
         GLint   format,
         GLenum  type,
   const GLvoid  *pixels
);
```



## Parameters

<dl> <dt>

*target* 
</dt> <dd>

The target texture. Must be GL\_TEXTURE\_1D.

</dd> <dt>

*level* 
</dt> <dd>

The level-of-detail number. Level 0 is the base image level. Level *n* is the *n*Th mipmap reduction image.

</dd> <dt>

*internalformat* 
</dt> <dd>

Specifies the number of color components in the texture. Must be 1, 2, 3, or 4, or one of the following symbolic constants: GL\_ALPHA, GL\_ALPHA4, GL\_ALPHA8, GL\_ALPHA12, GL\_ALPHA16, GL\_LUMINANCE, GL\_LUMINANCE4, GL\_LUMINANCE8, GL\_LUMINANCE12, GL\_LUMINANCE16, GL\_LUMINANCE\_ALPHA, GL\_LUMINANCE4\_ALPHA4, GL\_LUMINANCE6\_ALPHA2, GL\_LUMINANCE8\_ALPHA8, GL\_LUMINANCE12\_ALPHA4, GL\_LUMINANCE12\_ALPHA12, GL\_LUMINANCE16\_ALPHA16, GL\_INTENSITY, GL\_INTENSITY4, GL\_INTENSITY8, GL\_INTENSITY12, GL\_INTENSITY16, GL\_RGB, GL\_R3\_G3\_B2, GL\_RGB4, GL\_RGB5, GL\_RGB8, GL\_RGB10, GL\_RGB12, GL\_RGB16, GL\_RGBA, GL\_RGBA2, GL\_RGBA4, GL\_RGB5\_A1, GL\_RGBA8, GL\_RGB10\_A2, GL\_RGBA12, or GL\_RGBA16.

</dd> <dt>

*width* 
</dt> <dd>

The width of the texture image. Must be 2*n* + 2( *border* ) for some integer *n*. The height of the texture image is 1.

</dd> <dt>

*border* 
</dt> <dd>

The width of the border. Must be either 0 or 1.

</dd> <dt>

*format* 
</dt> <dd>

The format of the pixel data. It can assume one of nine symbolic values.



| Value                                                                                                                                                                         | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_COLOR_INDEX"></span><span id="gl_color_index"></span><dl> <dt>**GL\_COLOR\_INDEX**</dt> </dl>             | Each element is a single value, a color index. It is converted to fixed point (with an unspecified number of 0 bits to the right of the binary point), shifted left or right, depending on the value and sign of GL\_INDEX\_SHIFT, and added to GL\_INDEX\_OFFSET (see [**glPixelTransfer**](glpixeltransfer.md)). The resulting index is converted to a set of color components using the GL\_PIXEL\_MAP\_I\_TO\_R, GL\_PIXEL\_MAP\_I\_TO\_G, GL\_PIXEL\_MAP\_I\_TO\_B, and GL\_PIXEL\_MAP\_I\_TO\_A tables, and clamped to the range \[0,1\].<br/> |
| <span id="GL_RED"></span><span id="gl_red"></span><dl> <dt>**GL\_RED**</dt> </dl>                                      | Each element is a single red component. It is converted to floating point and assembled into an RGBA element by attaching 0.0 for green and blue, and 1.0 for alpha. Each component is then multiplied by the signed scale factor GL\_c\_SCALE, added to the signed bias GL\_c\_BIAS, and clamped to the range \[0,1\] (see **glPixelTransfer**).<br/>                                                                                                                                                                                                |
| <span id="GL_GREEN"></span><span id="gl_green"></span><dl> <dt>**GL\_GREEN**</dt> </dl>                                | Each element is a single green component. It is converted to floating point and assembled into an RGBA element by attaching 0.0 for red and blue, and 1.0 for alpha. Each component is then multiplied by the signed scale factor GL\_c\_SCALE, added to the signed bias GL\_c\_BIAS, and clamped to the range \[0,1\] (see [**glPixelTransfer**](glpixeltransfer.md)).<br/>                                                                                                                                                                         |
| <span id="GL_BLUE"></span><span id="gl_blue"></span><dl> <dt>**GL\_BLUE**</dt> </dl>                                   | Each element is a single blue component. It is converted to floating point and assembled into an RGBA element by attaching 0.0 for red and green, and 1.0 for alpha. Each component is then multiplied by the signed scale factor GL\_c\_SCALE, added to the signed bias GL\_c\_BIAS, and clamped to the range \[0,1\] (see **glPixelTransfer**).<br/>                                                                                                                                                                                                |
| <span id="GL_ALPHA"></span><span id="gl_alpha"></span><dl> <dt>**GL\_ALPHA**</dt> </dl>                                | Each element is a single red component. It is converted to floating point and assembled into an RGBA element by attaching 0.0 for red, green, and blue. Each component is then multiplied by the signed scale factor GL\_c\_SCALE, added to the signed bias GL\_c\_BIAS, and clamped to the range \[0,1\] (see [**glPixelTransfer**](glpixeltransfer.md)).<br/>                                                                                                                                                                                      |
| <span id="GL_RGB"></span><span id="gl_rgb"></span><dl> <dt>**GL\_RGB**</dt> </dl>                                      | Each element is an RGB triple. It is converted to floating point and assembled into an RGBA element by attaching 1.0 for alpha. Each component is then multiplied by the signed scale factor GL\_c\_SCALE, added to the signed bias GL\_c\_BIAS, and clamped to the range \[0,1\] (see **glPixelTransfer**).<br/>                                                                                                                                                                                                                                     |
| <span id="GL_RGBA"></span><span id="gl_rgba"></span><dl> <dt>**GL\_RGBA**</dt> </dl>                                   | Each element is a complete RGBA element. It is converted to floating point. Each component is then multiplied by the signed scale factor GL\_c\_SCALE, added to the signed bias GL\_c\_BIAS, and clamped to the range \[0,1\] (see **glPixelTransfer**).<br/>                                                                                                                                                                                                                                                                                         |
| <span id="GL_BGR_EXT"></span><span id="gl_bgr_ext"></span><dl> <dt>**GL\_BGR\_EXT**</dt> </dl>                         | Each pixel is a group of three components in this order: blue, green, red.<br/> GL\_BGR\_EXT provides a format that matches the memory layout of Windows device-independent bitmaps (DIBs). Thus your applications can use the same data with Windows function calls and OpenGL pixel function calls.<br/>                                                                                                                                                                                                                                      |
| <span id="GL_BGRA_EXT"></span><span id="gl_bgra_ext"></span><dl> <dt>**GL\_BGRA\_EXT**</dt> </dl>                      | Each pixel is a group of four components in this order: blue, green, red, alpha.<br/> GL\_BGRA\_EXT provides a format that matches the memory layout of Windows device-independent bitmaps (DIBs). Thus your applications can use the same data with Windows function calls and OpenGL pixel function calls.<br/>                                                                                                                                                                                                                               |
| <span id="GL_LUMINANCE"></span><span id="gl_luminance"></span><dl> <dt>**GL\_LUMINANCE**</dt> </dl>                    | Each element is a single luminance value. It is converted to floating point, and then assembled into an RGBA element by replicating the luminance value three times for red, green, and blue, and attaching 1.0 for alpha. Each component is then multiplied by the signed scale factor GL\_c\_SCALE, added to the signed bias GL\_c\_BIAS, and clamped to the range \[0,1\] (see [**glPixelTransfer**](glpixeltransfer.md)).<br/>                                                                                                                   |
| <span id="GL_LUMINANCE_ALPHA"></span><span id="gl_luminance_alpha"></span><dl> <dt>**GL\_LUMINANCE\_ALPHA**</dt> </dl> | Each element is a luminance/alpha pair. It is converted to floating point, and then assembled into an RGBA element by replicating the luminance value three times for red, green, and blue. Each component is then multiplied by the signed scale factor GL\_c\_SCALE, added to the signed bias GL\_c\_BIAS, and clamped to the range \[0,1\] (see **glPixelTransfer**).<br/>                                                                                                                                                                         |



 

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



| Name                                                                                                  | Meaning                                                                                                                                                                                                                        |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *target* was not an GL\_TEXTURE.<br/>                                                                                                                                                                                    |
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *format* was not an accepted *format* constant. Only format constants other than GL\_STENCIL\_INDEX and GL\_DEPTH\_COMPONENT are accepted. See the parameter description of *format* for a list of possible values.<br/> |
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *type* was not a *type* constant.<br/>                                                                                                                                                                                   |
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *type* was GL\_BITMAP and *format* was not GL\_COLOR\_INDEX.<br/>                                                                                                                                                        |
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | *level* was less than zero or greater than log2*max*, where *max* was the returned value of GL\_MAX\_TEXTURE\_SIZE.<br/>                                                                                                 |
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | *internalformat* was was not 1, 2, 3, or 4.<br/>                                                                                                                                                                         |
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | *width* was less than zero or greater than 2 + GL\_MAX\_TEXTURE\_SIZE, or it could not be represented as 2*n* + 2(border) for some integer value of *n*.<br/>                                                            |
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | *border* was not 0 or 1.<br/>                                                                                                                                                                                            |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/>                                                                                          |



## Remarks

The **glTexImage1D** function specifies a one-dimensional texture image. Texturing maps a portion of a specified *texture image* onto each graphical primitive for which texturing is enabled. One-dimensional texturing is enabled and disabled using [**glEnable**](glenable.md) and **glDisable** with argument GL\_TEXTURE\_1D.

Texture images are defined with **glTexImage1D**. The arguments describe the parameters of the texture image, such as width, width of the border, level-of-detail number (see [**glTexParameter**](gltexparameter-functions.md)), and number of color components provided. The last three arguments describe the way the image is represented in memory. These arguments are identical to the pixel formats used for [**glDrawPixels**](gldrawpixels.md).

Data is read from *pixels* as a sequence of signed or unsigned bytes, shorts or longs, or single-precision floating-point values, depending on *type*. These values are grouped into sets of one, two, three, or four values, depending on *format*, to form elements. If *type* is GL\_BITMAP, the data is considered as a string of unsigned bytes (and *format* must be GL\_COLOR\_INDEX). Each data byte is treated as eight 1-bit elements, with bit ordering determined by GL\_UNPACK\_LSB\_FIRST (see [**glPixelStore**](glpixelstore-functions.md)).

A texture image can have up to four components per texture element, depending on *components*. A one-component texture image uses only the red component of the RGBA color extracted from *pixels*. A two-component image uses the R and A values. A three-component image uses the R, G, and B values. A four-component image uses all of the RGBA components.

Texturing has no effect in color-index mode.

The texture image can be represented by the same data formats as the pixels in a [**glDrawPixels**](gldrawpixels.md) command, except that GL\_STENCIL\_INDEX and GL\_DEPTH\_COMPONENT cannot be used. The [**glPixelStore**](glpixelstore-functions.md) and [**glPixelTransfer**](glpixeltransfer.md) modes affect texture images in exactly the way they affect **glDrawPixels**.

A texture image with zero width indicates the null texture. If the null texture is specified for level-of-detail 0, it is as if texturing were disabled.

The following functions retrieve information related to **glTexImageID**:

[**glGetTexImage**](glgetteximage.md)

[**glIsEnabled**](glisenabled.md) with argument GL\_TEXTURE\_1D

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

[**glCopyPixels**](glcopypixels.md)
</dt> <dt>

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

[**glEnd**](glend.md)
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

[**glTexImage2D**](glteximage2d.md)
</dt> <dt>

[**glTexSubImage1D**](gltexsubimage1d.md)
</dt> <dt>

[**glTexSubImage2D**](gltexsubimage2d.md)
</dt> <dt>

[**glTexParameter**](gltexparameter-functions.md)
</dt> </dl>

 

 





