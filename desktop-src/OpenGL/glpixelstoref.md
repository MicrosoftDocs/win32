---
title: glPixelStoref function (Gl.h)
description: Sets pixel storage modes. | glPixelStoref function (Gl.h)
ms.assetid: 8d5055d7-3ea4-40b7-9447-2a005129da58
keywords:
- glPixelStoref function OpenGL
topic_type:
- apiref
api_name:
- glPixelStoref
api_location:
- Opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glPixelStoref function

Sets pixel storage modes.

## Syntax


```C++
void WINAPI glPixelStoref(
   GLenum  pname,
   GLfloat param
);
```



## Parameters

<dl> <dt>

*pname* 
</dt> <dd>

The symbolic name of the parameter to be set. Six of the storage parameters affect how pixel data is returned to client memory, and are therefore significant only for [**glReadPixels**](glreadpixels.md) commands. They are as follows:



| Storage Parameter                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GL\_PACK\_SWAP\_BYTES                                       | If true, byte ordering for multibyte color components, depth components, color indexes, or stencil indexes is reversed. That is, if a four-byte component is made up of bytes *b*0 , *b*1 , *b*2 , *b*3 , it is stored in memory as *b*3 , *b*2 , *b*1 , *b*0 if GL\_PACK\_SWAP\_BYTES is true. GL\_PACK\_SWAP\_BYTES has no effect on the memory order of components within a pixel, only on the order of bytes within components or indexes. For example, the three components of a GL\_RGB format pixel are always stored with red first, green second, and blue third, regardless of the value of GL\_PACK\_SWAP\_BYTES.                                                                                                                                                                                                                                                                                                                                                                                               |
| GL\_PACK\_LSB\_FIRST                                        | If true, bits are ordered within a byte from least significant to most significant; otherwise, the first bit in each byte is the most significant one. This parameter is significant for bitmap data only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| GL\_PACK\_ROW\_LENGTH                                       | If greater than zero, GL\_PACK\_ROW\_LENGTH defines the number of pixels in a row. If the first pixel of a row is placed at location p in memory, then the location of the first pixel of the next row is obtained by skipping ![Equation showing the location of the first pixel of the next row in GL_PACK_ROW_LENGTH.](images/pix01.png)\[newline\] components or indexes, where *n* is the number of components or indexes in a pixel, *l* is the number of pixels in a row (gl\-pack\-row\-length if it is greater than zero, the width argument to the pixel routine otherwise), *a* is the value of gl\-pack\-alignment, and *s* is the size, in bytes, of a single component (if *a* < *s*, then it is as if *a* = *s*). in the case of 1-bit values, the location of the next row is obtained by skipping ![Equation showing the location of the next row in GL_PACK_ROW_LENGTH.](images/pix02.png)<br/> components or indexes. The word *component* in this description refers to the nonindex values red, green, blue, alpha, and depth. Storage format GL\_RGB, for example, has three components per pixel: first red, then green, and finally blue.<br/> |
| GL\_PACK\_SKIP\_PIXELS and <br/> GL\_PACK\_SKIP\_ROWS | These values are provided as a convenience to the programmer; they provide no functionality that cannot be duplicated simply by incrementing the pointer passed to [**glReadPixels**](glreadpixels.md). Setting GL\_PACK\_SKIP\_PIXELS to *i* is equivalent to incrementing the pointer by *i n* components or indexes, where *n* is the number of components or indexes in each pixel. Setting GL\_PACK\_SKIP\_ROWS to *j* is equivalent to incrementing the pointer by *j k* components or indexes, where *k* is the number of components or indexes per row, as computed above in the GL\_PACK\_ROW\_LENGTH section.                                                                                                                                                                                                                                                                                                                                                                                                   |
| GL\_PACK\_ALIGNMENT                                         | Specifies the alignment requirements for the start of each pixel row in memory. The allowable values are 1 (byte-alignment), 2 (rows aligned to even-numbered bytes), 4 (word alignment), and 8 (rows start on double-word boundaries).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |



 

The other six storage parameters affect how pixel data is read from client memory. These values are significant for [**glDrawPixels**](gldrawpixels.md), [**glTexImage1D**](glteximage1d.md), [**glTexImage2D**](glteximage2d.md), [**glBitmap**](glbitmap.md), and [**glPolygonStipple**](glpolygonstipple.md). They are as follows:



| Storage Parameter                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GL\_UNPACK\_SWAP\_BYTES                                         | If true, byte ordering for multibyte color components, depth components, color indexes, or stencil indexes is reversed. That is, if a four-byte component is made up of bytes *b*0 , *b*1 , *b*2 , *b*3 , it is stored in memory as *b*3 , *b*2 , *b*1 , *b*0 if GL\_UNPACK\_SWAP\_BYTES is true. GL\_UNPACK\_SWAP\_BYTES has no effect on the memory order of components within a pixel, only on the order of bytes within components or indexes. For example, the three components of a GL\_RGB format pixel are always stored with red first, green second, and blue third, regardless of the value of GL\_UNPACK\_SWAP\_BYTES.                                                                                                                                                                                                                                                                                                                                                                                           |
| GL\_UNPACK\_LSB\_FIRST                                          | If true, bits are ordered within a byte from least significant to most significant; otherwise, the first bit in each byte is the most significant one. This is significant for bitmap data only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| GL\_UNPACK\_ROW\_LENGTH                                         | If greater than zero, GL\_UNPACK\_ROW\_LENGTH defines the number of pixels in a row. If the first pixel of a row is placed at location p in memory, then the location of the first pixel of the next row is obtained by skipping ![Equation showing the location of the first pixel of the next row in GL_UNPACK_ROW_LENGTH.](images/pix01.png)\[newline\] components or indexes, where *n* is the number of components or indexes in a pixel, *l* is the number of pixels in a row (gl\-pack\-row\-length if it is greater than zero, the width argument to the pixel routine otherwise), *a* is the value of gl\-pack\-alignment, and *s* is the size, in bytes, of a single component (if *a* < *s*, then it is as if *a* = *s*). in the case of 1-bit values, the location of the next row is obtained by skipping ![Equation showing the location of the next row in GL_UNPACK_ROW_LENGTH.](images/pix02.png)<br/> components or indexes. The word *component* in this description refers to the nonindex values red, green, blue, alpha, and depth. Storage format GL\_RGB, for example, has three components per pixel: first red, then green, and finally blue.<br/> |
| GL\_UNPACK\_SKIP\_PIXELS and <br/> GL\_UNPACK\_SKIP\_ROWS | These values are provided as a convenience to the programmer; they provide no functionality that cannot be duplicated simply by incrementing the pointer passed to [**glDrawPixels**](gldrawpixels.md), [**glTexImage1D**](glteximage1d.md), [**glTexImage2D**](glteximage2d.md), [**glBitmap**](glbitmap.md), or [**glPolygonStipple**](glpolygonstipple.md). Setting GL\_UNPACK\_SKIP\_PIXELS to *i* is equivalent to incrementing the pointer by *i n* components or indexes, where *n* is the number of components or indexes in each pixel. Setting GL\_UNPACK\_SKIP\_ROWS to *j* is equivalent to incrementing the pointer by *j k* components or indexes, where *k* is the number of components or indexes per row, as computed above in the GL\_UNPACK\_ROW\_LENGTH section.                                                                                                                                                                                                                                    |
| GL\_UNPACK\_ALIGNMENT                                           | Specifies the alignment requirements for the start of each pixel row in memory. The allowable values are 1 (byte-alignment), 2 (rows aligned to even-numbered bytes), 4 (word alignment), and 8 (rows start on double-word boundaries).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |



 

</dd> <dt>

*param* 
</dt> <dd>

The value that *pname* is set to.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The **glPixelStore** function sets pixel storage modes that affect the operation of subsequent [**glDrawPixels**](gldrawpixels.md) and [**glReadPixels**](glreadpixels.md) as well as the unpacking of polygon stipple patterns (see [**glPolygonStipple**](glpolygonstipple.md)), bitmaps (see [**glBitmap**](glbitmap.md)), and texture patterns (see [**glTexImage1D**](glteximage1d.md), [**glTexImage2D**](glteximage2d.md), [**glTexSubImage1D**](gltexsubimage1d.md), and [**glTexSubImage2D**](gltexsubimage2d.md)).

The following table gives the type, initial value, and range of valid values for each of the storage parameters that can be set with **glPixelStore**.



| Pname                    | Type    | Initial Value | Valid Range   |
|--------------------------|---------|---------------|---------------|
| GL\_PACK\_SWAP\_BYTES    | Boolean | false         | true or false |
| GL\_PACK\_SWAP\_BYTES    | Boolean | false         | true or false |
| GL\_PACK\_ROW\_LENGTH    | integer | 0             | \[0,?)        |
| GL\_PACK\_SKIP\_ROWS     | integer | 0             | \[0,?)        |
| GL\_PACK\_SKIP\_PIXELS   | integer | 0             | \[0,?)        |
| GL\_PACK\_ALIGNMENT      | integer | 4             | 1, 2, 4, or 8 |
| GL\_UNPACK\_SWAP\_BYTES  | Boolean | false         | true or false |
| GL\_UNPACK\_LSB\_FIRST   | Boolean | false         | true or false |
| GL\_UNPACK\_ROW\_LENGTH  | integer | 0             | \[0,?)        |
| GL\_UNPACK\_SKIP\_ROWS   | integer | 0             | \[0,?)        |
| GL\_UNPACK\_SKIP\_PIXELS | integer | 0             | \[0,?)        |
| GL\_UNPACK\_ALIGNMENT    | integer | 4             | 1, 2, 4, or 8 |



 

The **glPixelStoref** function can be used to set any pixel store parameter. If the parameter type is Boolean, and if *param* is 0.0, then the parameter is false; otherwise it is set to true. If *pname* is an integer type parameter, then *param* is rounded to the nearest integer.

Likewise, the **glPixelStorei** function can also be used to set any of the pixel store parameters. Boolean parameters are set to false if *param* is 0 and true otherwise. The *param* parameter is converted to floating point before being assigned to real-valued parameters.

The pixel storage modes in effect when [**glDrawPixels**](gldrawpixels.md), [**glReadPixels**](glreadpixels.md), [**glTexImage1D**](glteximage1d.md), [**glTexImage2D**](glteximage2d.md), [**glBitmap**](glbitmap.md), or [**glPolygonStipple**](glpolygonstipple.md) is placed in a display list control the interpretation of memory data. The pixel storage modes in effect when a display list is executed are not significant.

The following functions retrieve information related to **glPixelStore**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_PACK\_SWAP\_BYTES

**glGet** with argument GL\_PACK\_LSB\_FIRST

**glGet** with argument GL\_PACK\_ROW\_LENGTH

**glGet** with argument GL\_PACK\_SKIP\_ROWS

**glGet** with argument GL\_PACK\_SKIP\_PIXELS

**glGet** with argument GL\_PACK\_ALIGNMENT

**glGet** with argument GL\_UNPACK\_SWAP\_BYTES

**glGet** with argument GL\_UNPACK\_LSB\_FIRST

**glGet** with argument GL\_UNPACK\_ROW\_LENGTH

**glGet** with argument GL\_UNPACK\_SKIP\_ROWS

**glGet** with argument GL\_UNPACK\_SKIP\_PIXELS

**glGet** with argument GL\_UNPACK\_ALIGNMENT

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

[**glBitmap**](glbitmap.md)
</dt> <dt>

[**glDrawPixels**](gldrawpixels.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glPixelMap**](glpixelmap.md)
</dt> <dt>

[**glPixelTransfer**](glpixeltransfer.md)
</dt> <dt>

[**glPixelZoom**](glpixelzoom.md)
</dt> <dt>

[**glPolygonStipple**](glpolygonstipple.md)
</dt> <dt>

[**glReadPixels**](glreadpixels.md)
</dt> <dt>

[**glTexImage1D**](glteximage1d.md)
</dt> <dt>

[**glTexImage2D**](glteximage2d.md)
</dt> </dl>

 

 





