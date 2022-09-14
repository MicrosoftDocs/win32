---
title: glCopyTexImage2D function (Gl.h)
description: The glCopyTexImage2D function copies pixels from the framebuffer into a two-dimensional texture image.
ms.assetid: 4b9d7be6-054d-4590-b3f0-a2a670786c4b
keywords:
- glCopyTexImage2D function OpenGL
topic_type:
- apiref
api_name:
- glCopyTexImage2D
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glCopyTexImage2D function

The **glCopyTexImage2D** function copies pixels from the framebuffer into a two-dimensional texture image.

## Syntax


```C++
void WINAPI glCopyTexImage2D(
   GLenum  target,
   GLint   level,
   GLenum  internalFormat,
   GLint   x,
   GLint   y,
   GLsizei width,
   GLsizei height,
   GLint   border
);
```



## Parameters

<dl> <dt>

*target* 
</dt> <dd>

The target to which the image data will be changed. Must have the value GL\_TEXTURE\_2D.

</dd> <dt>

*level* 
</dt> <dd>

The level-of-detail number. Level 0 is the base image. Level *n* is the *n*th mipmap reduction image.

</dd> <dt>

*internalFormat* 
</dt> <dd>

The internal format and resolution of the texture data. The values 1, 2, 3, and 4 are not accepted for *internalFormat*. The parameter can assume one of the following symbolic values.



| Constant                 | R Bits | G Bits | B Bits | A Bits | L Bits | I Bits |
|--------------------------|--------|--------|--------|--------|--------|--------|
| GL\_ALPHA                |        |        |        |        |        |        |
| GL\_ALPHA4               |        |        |        | 4      |        |        |
| GL\_ALPHA8               |        |        |        | 8      |        |        |
| GL\_ALPHA12              |        |        |        | 12     |        |        |
| GL\_ALPHA16              |        |        |        | 16     |        |        |
| GL\_LUMINANCE            |        |        |        |        |        |        |
| GL\_LUMINANCE4           |        |        |        |        | 4      |        |
| GL\_LUMINANCE8           |        |        |        |        | 8      |        |
| GL\_LUMINANCE12          |        |        |        |        | 12     |        |
| GL\_LUMINANCE16          |        |        |        |        | 16     |        |
| GL\_LUMINANCE\_ALPHA     |        |        |        |        |        |        |
| GL\_LUMINANCE4\_ALPHA4   |        |        |        | 4      | 4      |        |
| GL\_LUMINANCE6\_ALPHA2   |        |        |        | 2      | 6      |        |
| GL\_LUMINANCE8\_ALPHA8   |        |        |        | 8      | 8      |        |
| GL\_LUMINANCE12\_ALPHA4  |        |        |        | 4      | 12     |        |
| GL\_LUMINANCE12\_ALPHA12 |        |        |        | 12     | 12     |        |
| GL\_LUMINANCE16\_ALPHA16 |        |        |        | 16     | 16     |        |
| GL\_INTENSITY            |        |        |        |        |        |        |
| GL\_INTENSITY4           |        |        |        |        |        | 4      |
| GL\_INTENSITY8           |        |        |        |        |        | 8      |
| GL\_INTENSITY12          |        |        |        |        |        | 12     |
| GL\_INTENSITY16          |        |        |        |        |        | 16     |
| GL\_RGB                  |        |        |        |        |        |        |
| GL\_R3\_G3\_B2           | 3      | 3      | 2      |        |        |        |
| GL\_RGB4                 | 4      | 4      | 4      |        |        |        |
| GL\_RGB5                 | 5      | 5      | 5      |        |        |        |
| GL\_RGB8                 | 8      | 8      | 8      |        |        |        |
| GL\_RGB10                | 10     | 10     | 10     |        |        |        |
| GL\_RGB12                | 12     | 12     | 12     |        |        |        |
| GL\_RGB16                | 16     | 16     | 16     |        |        |        |
| GL\_RGBA                 |        |        |        |        |        |        |
| GL\_RGBA2                | 2      | 2      | 2      | 2      |        |        |
| GL\_RGBA4                | 4      | 4      | 4      | 4      |        |        |
| GL\_RGB5\_A1             | 5      | 5      | 5      | 1      |        |        |
| GL\_RGBA8                | 8      | 8      | 8      | 8      |        |        |
| GL\_RGB10\_A2            | 10     | 10     | 10     | 2      |        |        |
| GL\_RGBA12               | 12     | 12     | 12     | 12     |        |        |
| GL\_RGBA16               | 16     | 16     | 16     | 16     |        |        |



 

</dd> <dt>

*x* 
</dt> <dd>

The window x-plane coordinate of the lower-left corner of the rectangular region of pixels to be copied.

</dd> <dt>

*y* 
</dt> <dd>

The window y-plane coordinate of the lower-left corner of the rectangular region of pixels to be copied.

</dd> <dt>

*width* 
</dt> <dd>

The width of the texture image. Must be 2n + 2 \* *border* for some integer *n*.

</dd> <dt>

*height* 
</dt> <dd>

The height of the texture image. Must be 2n + 2 \* *border* for some integer *n*.

</dd> <dt>

*border* 
</dt> <dd>

The width of the border. Must be either zero or 1.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *target* was not an accepted value.<br/>                                                                                                               |
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | *level* was less than zero or greater than log2 *max*, where *max* is the returned value of GL\_MAX\_TEXTURE\_SIZE.<br/>                               |
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | *border* was not zero or 1.<br/>                                                                                                                       |
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | *width* was less than zero, greater than 2 + GL\_MAX\_TEXTURE\_SIZE, or *width* cannot be represented as 2n + 2 \* *border* for some integer *n*.<br/> |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/>                        |



## Remarks

The **glCopyTexImage2D** function defines a two-dimensional texture image using pixels from the current framebuffer, rather than from main memory as is the case for [**glTexImage2D**](glteximage2d.md).

Using the mipmap level specified with *level*, texture arrays are defined as a rectangle of pixels with the lower-left corner located at the coordinates *x* and *y*, width equal to *width* + (2 \* *border*), and a height equal to *height* + (2 \* *border*). The internal format of the texture array is specified with the *internalFormat* parameter.

The **glCopyTexImage2D** function processes the pixels in a row in the same way as [**glCopyPixels**](glcopypixels.md) except that before the final conversion of the pixels, all pixel component values are clamped to the range \[0,1\] and converted to the texture's internal format for storage in the texture array. Pixel ordering is determined with lower *x* and *y* coordinates corresponding to lower *s* and *t* texture coordinates. If any of the pixels within a specified row of the current framebuffer are outside the window associated with the current rendering context, then their values are undefined.

You cannot include calls to **glCopyTexImage2D** in display lists.

> [!Note]  
> The **glCopyTexImage2D** function is only available in OpenGL version 1.1 or later.

 

Texturing has no effect in color-index mode. The [**glPixelStore**](glpixelstore-functions.md) and [**glPixelTransfer**](glpixeltransfer.md) functions affect texture images in exactly the way they affect [**glDrawPixels**](gldrawpixels.md).

The following function retrieves information related to **glCopyTexImage2D**:

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

[**glBegin**](glbegin.md)
</dt> <dt>

[**glCopyTexImage1D**](glcopyteximage1d.md)
</dt> <dt>

[**glDrawPixels**](gldrawpixels.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glFog**](glfog.md)
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

[**glTexParameter**](gltexparameter-functions.md)
</dt> </dl>

 

 





