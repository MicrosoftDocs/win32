---
title: glReadPixels function (Gl.h)
description: The glReadPixels function reads a block of pixels from the framebuffer.
ms.assetid: 41fbad5c-b8ca-456d-bbfc-b48c176e15b0
keywords:
- glReadPixels function OpenGL
topic_type:
- apiref
api_name:
- glReadPixels
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glReadPixels function

The **glReadPixels** function reads a block of pixels from the framebuffer.

## Syntax


```C++
void WINAPI glReadPixels(
   GLint   x,
   GLint   y,
   GLsizei width,
   GLsizei height,
   GLenum  format,
   GLenum  type,
   GLvoid  *pixels
);
```



## Parameters

<dl> <dt>

*x* 
</dt> <dd>

The window *x* coordinate of the first pixel that is read from the framebuffer. Together with the *y* coordinate, specifies the location of the lower-left corner of a rectangular block of pixels.

</dd> <dt>

*y* 
</dt> <dd>

The window *y* coordinates of the first pixel that is read from the framebuffer. Together with the *x* coordinate, specifies the location of the lower-left corner of a rectangular block of pixels.

</dd> <dt>

*width* 
</dt> <dd>

The width of the pixel rectangle.

</dd> <dt>

*height* 
</dt> <dd>

The height of the pixel rectangle. *Width* and *height* parameters of value "1" correspond to a single pixel.

</dd> <dt>

*format* 
</dt> <dd>

The format of the pixel data. The following symbolic values are accepted:



| Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_COLOR_INDEX"></span><span id="gl_color_index"></span><dl> <dt>**GL\_COLOR\_INDEX**</dt> </dl>                                                                                                                                                                                                                                                                                                               | Color indexes are read from the color buffer selected by [**glReadBuffer**](glreadbuffer.md). Each index is converted to fixed point, shifted left or right, depending on the value and sign of GL\_INDEX\_SHIFT, and added to GL\_INDEX\_OFFSET. If GL\_MAP\_COLOR is GL\_TRUE, indexes are replaced by their mappings in the table GL\_PIXEL\_MAP\_I\_TO\_I.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <span id="GL_STENCIL_INDEX"></span><span id="gl_stencil_index"></span><dl> <dt>**GL\_STENCIL\_INDEX**</dt> </dl>                                                                                                                                                                                                                                                                                                         | Stencil values are read from the stencil buffer. Each index is converted to fixed point, shifted left or right, depending on the value and sign of GL\_INDEX\_SHIFT, and added to GL\_INDEX\_OFFSET. If GL\_MAP\_STENCIL is GL\_TRUE, indexes are replaced by their mappings in the table GL\_PIXEL\_MAP\_S\_TO\_S.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <span id="GL_DEPTH_COMPONENT"></span><span id="gl_depth_component"></span><dl> <dt>**GL\_DEPTH\_COMPONENT**</dt> </dl>                                                                                                                                                                                                                                                                                                   | Depth values are read from the depth buffer. Each component is converted to floating point such that the minimum depth value maps to 0.0 and the maximum value maps to 1.0. Each component is then multiplied by GL\_DEPTH\_SCALE, added to GL\_DEPTH\_BIAS, and finally clamped to the range \[0,1\].<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| <span id="GL_RED__GL_GREEN__GL_BLUE__GL_ALPHA__GL_RGB__GL_RGBA__GL_BGR_EXT__GL_BGRA_EXT__GL_LUMINANCE__GL_LUMINANCE_ALPHA"></span><span id="gl_red__gl_green__gl_blue__gl_alpha__gl_rgb__gl_rgba__gl_bgr_ext__gl_bgra_ext__gl_luminance__gl_luminance_alpha"></span><dl> <dt>**GL\_RED, GL\_GREEN, GL\_BLUE, GL\_ALPHA, GL\_RGB, GL\_RGBA, GL\_BGR\_EXT, GL\_BGRA\_EXT, GL\_LUMINANCE, GL\_LUMINANCE\_ALPHA**</dt> </dl> | Processing differs depending on whether color buffers store color indexes or RGBA color components. If color indexes are stored, they are read from the color buffer selected by [**glReadBuffer**](glreadbuffer.md). Each index is converted to fixed point, shifted left or right, depending on the value and sign of GL\_INDEX\_SHIFT, and added to GL\_INDEX\_OFFSET. Indexes are then replaced by the red, green, blue, and alpha values obtained by indexing the GL\_PIXEL\_MAP\_I\_TO\_R, GL\_PIXEL\_MAP\_I\_TO\_G, GL\_PIXEL\_MAP\_I\_TO\_B, and GL\_PIXEL\_MAP\_I\_TO\_A tables. If RGBA color components are stored in the color buffers, they are read from the color buffer selected by **glReadBuffer**. Each color component is converted to floating point such that zero intensity maps to 0.0 and full intensity maps to 1.0. Each component is then multiplied by GL\_c\_SCALE and added to GL\_c\_BIAS, where c is GL\_RED, GL\_GREEN, GL\_BLUE, and GL\_ALPHA. Each component is clamped to the range \[0,1\]. Finally, if GL\_MAP\_COLOR is GL\_TRUE, each color component c is replaced by its mapping in the table GL\_PIXEL\_MAP\_c\_TO\_c, where c again is GL\_RED, GL\_GREEN, GL\_BLUE, and GL\_ALPHA. Each component is scaled to the size of its corresponding table before the lookup is performed. Finally, unneeded data is discarded. For example, GL\_RED discards the green, blue, and alpha components, while GL\_RGB discards only the alpha component. GL\_LUMINANCE computes a single component value as the sum of the red, green, and blue components, and GL\_LUMINANCE\_ALPHA does the same, while keeping alpha as a second value.<br/> |



 

</dd> <dt>

*type* 
</dt> <dd>

The data type of the pixel data. Must be one of the following values.



| Type                | Index mask | Component conversion |
|---------------------|------------|----------------------|
| GL\_UNSIGNED\_BYTE  | 281        | (281)*c*             |
| GL\_BYTE            | 271        | \[(271)*c*-1\]/2     |
| GL\_BITMAP          | 1          | 1                    |
| GL\_UNSIGNED\_SHORT | 2 61       | (2 61)*c*            |
| GL\_SHORT           | 2 51       | \[(2 51)*c*1\]/2     |
| GL\_UNSIGNED\_INT\_ | 2  1       | (2  1)*c*            |
| GL\_INT             | 2   1      | \[(2  1)*c*1\]/2     |
| GL\_FLOAT           | none       | *c*                  |



 

</dd> <dt>

*pixels* 
</dt> <dd>

Returns the pixel data.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *format* or *type* was not an accepted value.<br/>                                                                              |
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | Either *width* or *height* was negative.<br/>                                                                                   |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | *format* was GL\_COLOR\_INDEX, and the color buffers stored RGBA or BGRA color components.<br/>                                 |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | *format* was GL\_STENCIL\_INDEX, and there was no stencil buffer.<br/>                                                          |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | *format* was GL\_DEPTH\_COMPONENT, and there was no depth buffer.<br/>                                                          |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |

## Remarks

The **glReadPixels** function returns pixel data from the framebuffer, starting with the pixel whose lower-left corner is at location (*x*, *y*), into client memory starting at location *pixels*. Several parameters control the processing of the pixel data before it is placed into client memory. These parameters are set with three commands: [**glPixelStore**](glpixelstore-functions.md), [**glPixelTransfer**](glpixeltransfer.md), and [**glPixelMap**](glpixelmap.md). This topic describes the effects on **glReadPixels** of most, but not all of the parameters specified by these three commands.

The **glReadPixels** function returns values from each pixel with lower-left corner at (*x* + i, *y* + j) for 0 = i < *width* and 0 = j < *height*. This pixel is said to be the *i*th pixel in the *j*th row. Pixels are returned in row order from the lowest to the highest row, left to right in each row.

The shift, scale, bias, and lookup factors described above are all specified by [**glPixelTransfer**](glpixeltransfer.md). The lookup table contents are specified by [**glPixelMap**](glpixelmap.md).

The final step involves converting the indexes or components to the proper format, as specified by *type*. If *format* is GL\_COLOR\_INDEX or GL\_STENCIL\_INDEX and *type* is not GL\_FLOAT, each index is masked with the mask value given in the following table. If *type* is GL\_FLOAT, then each integer index is converted to single-precision floating-point format.

If *format* is GL\_RED, GL\_GREEN, GL\_BLUE, GL\_ALPHA, GL\_RGB, GL\_RGBA, GL\_BGR\_EXT, GL\_BGRA\_EXT, GL\_LUMINANCE, or GL\_LUMINANCE\_ALPHA and *type* is not GL\_FLOAT, each component is multiplied by the multiplier shown in the preceding table. If type is GL\_FLOAT, then each component is passed as is (or converted to the client's single-precision floating-point format if it is different from the one used by OpenGL).

Return values are placed in memory as follows. If *format* is GL\_COLOR\_INDEX, GL\_STENCIL\_INDEX, GL\_DEPTH\_COMPONENT, GL\_RED, GL\_GREEN, GL\_BLUE, GL\_ALPHA, or GL\_LUMINANCE, a single value is returned and the data for the *i*th pixel in the *j*th row is placed in location (*j* )*width* + *i*. GL\_RGB and GL\_BGR\_EXT return three values, GL\_RGBA and GL\_BGRA\_EXT return four values, and GL\_LUMINANCE\_ALPHA returns two values for each pixel, with all values corresponding to a single pixel occupying contiguous space in *pixels*. Storage parameters set by [**glPixelStore**](glpixelstore-functions.md), such as GL\_PACK\_SWAP\_BYTES and GL\_PACK\_LSB\_FIRST, affect the way that data is written into memory. See [**glPixelStore**](glpixelstore-functions.md) for a description.

Values for pixels that lie outside the window connected to the current OpenGL context are undefined.

If an error is generated, no change is made to the contents of *pixels*.

The following function retrieves information related to **glReadPixels**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_INDEX\_MODE

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

[**glDrawPixels**](gldrawpixels.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glPixelMap**](glpixelmap.md)
</dt> <dt>

[**glPixelStore**](glpixelstore-functions.md)
</dt> <dt>

[**glPixelTransfer**](glpixeltransfer.md)
</dt> <dt>

[**glReadBuffer**](glreadbuffer.md)
</dt> </dl>

 

 





