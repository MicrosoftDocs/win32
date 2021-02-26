---
title: glPixelTransferi function (Gl.h)
description: The glPixelTransferf and glPixelTransferi functions set pixel transfer modes. | glPixelTransferi function (Gl.h)
ms.assetid: 351a872d-2cce-4fb1-b736-72201baf4157
keywords:
- glPixelTransferi function OpenGL
topic_type:
- apiref
api_name:
- glPixelTransferi
api_location:
- Opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glPixelTransferi function

The [**glPixelTransferf**](glpixeltransferf.md) and **glPixelTransferi** functions set pixel transfer modes.

## Syntax


```C++
void WINAPI glPixelTransferi(
   GLenum pname,
   GLint  param
);
```



## Parameters

<dl> <dt>

*pname* 
</dt> <dd>

The symbolic name of the pixel transfer parameter to be set. The following table gives the type, initial value, and range of valid values for each of the pixel transfer parameters that are set with **glPixelTransfer**.



| Pname             | Type    | Initial Value  | Valid Range  |
|-------------------|---------|----------------|--------------|
| GL\_MAP\_COLOR    | Boolean | false          | true/false   |
| GL\_MAP\_STENCIL  | Boolean | false          | true/false   |
| GL\_INDEX\_SHIFT  | integer | 0              | (8,8)        |
| GL\_INDEX\_OFFSET | integer | 0              | (8,8)        |
| GL\_RED\_SCALE    | integer | 1.0            | (8,8)        |
| GL\_GREEN\_SCALE  | float   | 1.0            | (8,8)        |
| GL\_BLUE\_SCALE   | float   | 1.0            | (8,8)        |
| GL\_ALPHA\_SCALE  | float   | 1.0            | (8,8)        |
| GL\_DEPTH\_SCALE  | float   | 1.0            | (8,8)        |
| GL\_RED\_BIAS     | float   | 0.0            | (8,8)        |
| GL\_GREEN\_BIAS   | float   | 0.0            | (8,8)        |
| GL\_BLUE\_BIAS    | float   | 0.0            | (8,8)        |
| GL\_ALPHA\_BIAS   | float   | 0.0            | (8,8)        |
| GL\_DEPTH\_BIAS   | float   | 0.0            | (8,8)        |



 

</dd> <dt>

*param* 
</dt> <dd>

The value that *pname* is set to.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The **glPixelTransfer** function sets pixel transfer modes that affect the operation of subsequent [**glCopyPixels**](glcopypixels.md), [**glCopyTexImage1D**](glcopyteximage1d.md), [**glCopyTexImage2D**](glcopyteximage2d.md), [**glCopyTexSubImage1D**](glcopytexsubimage1d.md), [**glCopyTexSubImage2D**](glcopytexsubimage2d.md), [**glDrawPixels**](gldrawpixels.md), [**glReadPixels**](glreadpixels.md), [**glTexImage1D**](glteximage1d.md), [**glTexImage2D**](glteximage2d.md), [**glTexSubImage1D**](gltexsubimage1d.md), and [**glTexSubImage2D**](gltexsubimage2d.md) commands. The algorithms that are specified by pixel transfer modes operate on pixels after they are read from the framebuffer (**glReadPixels** and **glCopyPixels**) or unpacked from client memory (**glDrawPixels**, **glTexImage1D**, and **glTexImage2D**). Pixel transfer operations happen in the same order, and in the same manner, regardless of the command that resulted in the pixel operation. Pixel storage modes ([**glPixelStore**](glpixelstore-functions.md)) control the unpacking of pixels being read from client memory, and the packing of pixels being written back into client memory.

Pixel transfer operations handle four fundamental pixel types: *color*, *color index*, *depth*, and *stencil*.Color pixels are made up of four floating-point values with unspecified mantissa and exponent sizes, scaled such that 0.0 represents zero intensity and 1.0 represents full intensity. Color indexes comprise a single fixed-point value, with unspecified precision to the right of the binary point. Depth pixels comprise a single floating-point value, with unspecified mantissa and exponent sizes, scaled such that 0.0 represents the minimum depth buffer value, and 1.0 represents the maximum depth buffer value. Finally, stencil pixels comprise a single fixed-point value, with unspecified precision to the right of the binary point.

The pixel transfer operations performed on the four basic pixel types are as follows:



| Pixel type  | Pixel transfer operation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Color       | Each of the four color components is multiplied by a scale factor, and then added to a bias factor. That is, the red component is multiplied by GL\_RED\_SCALE, and then added to GL\_RED\_BIAS; the green component is multiplied by GL\_GREEN\_SCALE, and then added to GL\_GREEN\_BIAS; the blue component is multiplied by GL\_BLUE\_SCALE, and then added to GL\_BLUE\_BIAS; and the alpha component is multiplied by GL\_ALPHA\_SCALE, and then added to GL\_ALPHA\_BIAS. After all four color components are scaled and biased, each is clamped to the range \[0,1\]. All color scale and bias values are specified with **glPixelTransfer**. <br/> If GL\_MAP\_COLOR is true, each color component is scaled by the size of the corresponding color-to-color map, and then replaced by the contents of that map indexed by the scaled component. That is, the red component is scaled by GL\_PIXEL\_MAP\_R\_TO\_R\_SIZE, and then replaced by the contents of GL\_PIXEL\_MAP\_R\_TO\_R indexed by itself. The green component is scaled by GL\_PIXEL\_MAP\_G\_TO\_G\_SIZE, and then replaced by the contents of GL\_PIXEL\_MAP\_G\_TO\_G indexed by itself. The blue component is scaled by GL\_PIXEL\_MAP\_B\_TO\_B\_SIZE, and then replaced by the contents of GL\_PIXEL\_MAP\_B\_TO\_B indexed by itself. The alpha component is scaled by GL\_PIXEL\_MAP\_A\_TO\_A\_SIZE, and then replaced by the contents of GL\_PIXEL\_MAP\_A\_TO\_A indexed by itself. All components taken from the maps are then clamped to the range \[0,1\]. GL\_MAP\_COLOR is specified with **glPixelTransfer**. The contents of the various maps are specified with **glPixelMap**.<br/>                                                                                                                        |
| Color index | Each color index is shifted left by GL\_INDEX\_SHIFT bits, filling with zeros any bits beyond the number of fraction bits carried by the fixed-point index. If GL\_INDEX\_SHIFT is negative, the shift is to the right, again zero filled. GL\_INDEX\_OFFSET is then added to the index. GL\_INDEX\_SHIFT and GL\_INDEX\_OFFSET are specified with **glPixelTransfer**.<br/> From this point, operation diverges depending on the required format of the resulting pixels. If the resulting pixels are to be written to a color-index buffer, or if they are being read back to client memory in GL\_COLOR\_INDEX format, the pixels continue to be treated as indexes. If GL\_MAP\_COLOR is true, then each index is masked by 2 ^ *n* 1, where *n* is GL\_PIXEL\_MAP\_I\_TO\_I\_SIZE, and then replaced by the contents of GL\_PIXEL\_MAP\_I\_TO\_I indexed by the masked value. GL\_MAP\_COLOR is specified with **glPixelTransfer**. The contents of the index map are specified with **glPixelMap**.<br/> If the resulting pixels are to be written to an RGBA color buffer, or if they are being read back to client memory in a format other than GL\_COLOR\_INDEX, the pixels are converted from indexes to colors by referencing the four maps GL\_PIXEL\_MAP\_I\_TO\_R, GL\_PIXEL\_MAP\_I\_TO\_G, GL\_PIXEL\_MAP\_I\_TO\_B, and GL\_PIXEL\_MAP\_I\_TO\_A. Before being dereferenced, the index is masked by 2 n 1, where n is GL\_PIXEL\_MAP\_I\_TO\_R\_SIZE for the red map, GL\_PIXEL\_MAP\_I\_TO\_G\_SIZE for the green map, GL\_PIXEL\_MAP\_I\_TO\_B\_SIZE for the blue map, and GL\_PIXEL\_MAP\_I\_TO\_A\_SIZE for the alpha map. All components taken from the maps are then clamped to the range \[0,1\]. The contents of the four maps are specified with **glPixelMap**.<br/> |
| Depth       | Each depth value is multiplied by GL\_DEPTH\_SCALE, added to GL\_DEPTH\_BIAS, and then clamped to the range \[0,1\].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Stencil     | Each index is shifted GL\_INDEX\_SHIFT bits just as a color index is, and then added to GL\_INDEX\_OFFSET. If GL\_MAP\_STENCIL is true, each index is masked by 2n 1, where *n* is GL\_PIXEL\_MAP\_S\_TO\_S\_SIZE, then replaced by the contents of GL\_PIXEL\_MAP\_S\_TO\_S indexed by the masked value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |



 

The [**glPixelTransferf**](glpixeltransfer.md) function can be used to set any pixel transfer parameter. If the parameter type is Boolean, 0.0 implies false and any other value implies true. If *pname* is an integer parameter, *param* is rounded to the nearest integer.

Likewise, **glPixelTransferi** can also be used to set any of the pixel transfer parameters. Boolean parameters are set to false if *param* is 0 and true otherwise. The *param* parameter is converted to floating point before being assigned to real-valued parameters.

If a [**glDrawPixels**](gldrawpixels.md), [**glReadPixels**](glreadpixels.md), [**glCopyPixels**](glcopypixels.md), [**glTexImage1D**](glteximage1d.md), or [**glTexImage2D**](glteximage2d.md) command is placed in a display list (see [**glNewList**](glnewlist.md) and [**glCallList**](glcalllist.md)), the pixel transfer mode settings in effect when the display list is *executed* are the ones that are used. They may be different from the settings when the command was compiled into the display list.

The following functions retrieve information related to **glPixelTransfer**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_MAP\_COLOR

**glGet** with argument GL\_MAP\_STENCIL

**glGet** with argument GL\_INDEX\_SHIFT

**glGet** with argument GL\_INDEX\_OFFSET

**glGet** with argument GL\_RED\_SCALE

**glGet** with argument GL\_RED\_BIAS

**glGet** with argument GL\_GREEN\_SCALE

**glGet** with argument GL\_GREEN\_BIAS

**glGet** with argument GL\_BLUE\_SCALE

**glGet** with argument GL\_BLUE\_BIAS

**glGet** with argument GL\_ALPHA\_SCALE

**glGet** with argument GL\_ALPHA\_BIAS

**glGet** with argument GL\_DEPTH\_SCALE

**glGet** with argument GL\_DEPTH\_BIAS

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

[**glCallList**](glcalllist.md)
</dt> <dt>

[**glCopyPixels**](glcopypixels.md)
</dt> <dt>

[**glDrawPixels**](gldrawpixels.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glNewList**](glnewlist.md)
</dt> <dt>

[**glPixelMap**](glpixelmap.md)
</dt> <dt>

[**glPixelStore**](glpixelstore-functions.md)
</dt> <dt>

[**glPixelZoom**](glpixelzoom.md)
</dt> <dt>

[**glReadPixels**](glreadpixels.md)
</dt> <dt>

[**glTexImage1D**](glteximage1d.md)
</dt> <dt>

[**glTexImage2D**](glteximage2d.md)
</dt> </dl>

 

 





