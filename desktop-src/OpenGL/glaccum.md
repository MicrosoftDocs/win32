---
title: glAccum function (Gl.h)
description: The glAccum function operates on the accumulation buffer.
ms.assetid: 3ddd69fe-74fc-4ac0-be8d-bcaa71ac0292
keywords:
- glAccum function OpenGL
topic_type:
- apiref
api_name:
- glAccum
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glAccum function

The **glAccum** function operates on the accumulation buffer.

## Syntax


```C++
void WINAPI glAccum(
   GLenum  op,
   GLfloat value
);
```



## Parameters

<dl> <dt>

*op* 
</dt> <dd>

The accumulation buffer operation. The accepted symbolic constants are as follows.



| Value                                                                                                                                             | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_ACCUM"></span><span id="gl_accum"></span><dl> <dt>**GL\_ACCUM**</dt> </dl>    | Obtains R, G, B, and A values from the buffer currently selected for reading (see [**glReadBuffer**](glreadbuffer.md)). Each component value is divided by 2*n*  1, where *n* is the number of bits allocated to each color component in the currently selected buffer. The result is a floating-point value in the range \[0,1\], which is multiplied by *value* and added to the corresponding pixel component in the accumulation buffer, thereby updating the accumulation buffer.<br/> |
| <span id="GL_LOAD"></span><span id="gl_load"></span><dl> <dt>**GL\_LOAD**</dt> </dl>       | Similar to GL\_ACCUM, except that the current value in the accumulation buffer is not used in the calculation of the new value. That is, the R, G, B, and A values from the currently selected buffer are divided by 2*n*  1, multiplied by *value*, and then stored in the corresponding accumulation buffer cell, overwriting the current value.<br/>                                                                                                                                      |
| <span id="GL_ADD"></span><span id="gl_add"></span><dl> <dt>**GL\_ADD**</dt> </dl>          | Adds *value* to each R, G, B, and A in the accumulation buffer.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <span id="GL_MULT"></span><span id="gl_mult"></span><dl> <dt>**GL\_MULT**</dt> </dl>       | Multiplies each R, G, B, and A in the accumulation buffer by *value* and returns the scaled component to its corresponding accumulation buffer location.<br/>                                                                                                                                                                                                                                                                                                                                |
| <span id="GL_RETURN"></span><span id="gl_return"></span><dl> <dt>**GL\_RETURN**</dt> </dl> | Transfers accumulation buffer values to the color buffer or buffers currently selected for writing. Each R, G, B, and A component is multiplied by *value*, then multiplied by 2*n*  1, clamped to the range \[0, 2*n*  1 \], and stored in the corresponding display buffer cell. The only fragment operations that are applied to this transfer are pixel ownership, scissor, dithering, and color writemasks.<br/>                                                                        |



 

</dd> <dt>

*value* 
</dt> <dd>

A floating-point value used in the accumulation buffer operation. The *op* parameter determines how *value* is used.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *op* was not an accepted value.<br/>                                                                                                                                            |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | There was no accumulation buffer or the function **glAccum** was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The accumulation buffer is an extended-range color buffer. Images are not rendered into it. Rather, images rendered into one of the color buffers are added to the contents of the accumulation buffer after rendering. You can create effects such as antialiasing (of points, lines, and polygons), motion blur, and depth of field by accumulating images generated with different transformation matrices.

Each pixel in the accumulation buffer consists of red, green, blue, and alpha values. The number of bits per component in the accumulation buffer depends on the implementation. You can examine this number by calling [**glGetIntegerv**](glgetintegerv.md) four times, with the arguments GL\_ACCUM\_RED\_BITS, GL\_ACCUM\_GREEN\_BITS, GL\_ACCUM\_BLUE\_BITS, and GL\_ACCUM\_ALPHA\_BITS, respectively. Regardless of the number of bits per component, however, the range of values stored by each component is \[ 1,?1\]. The accumulation buffer pixels are mapped one-to-one with framebuffer pixels.

The **glAccum** function operates on the accumulation buffer. The first argument, *op*, is a symbolic constant that selects an accumulation buffer operation. The second argument, *value*, is a floating-point value to be used in that operation. Five operations are specified: GL\_ACCUM, GL\_LOAD, GL\_ADD, GL\_MULT, and GL\_RETURN.

All accumulation buffer operations are limited to the area of the current scissor box and are applied identically to the red, green, blue, and alpha components of each pixel. The contents of an accumulation buffer pixel component are undefined if the **glAccum** operation results in a value outside the range \[ 1,1\].

To clear the accumulation buffer, use the [**glClearAccum**](glclearaccum.md) function to specify R, G, B, and A values to set it to, and issue a [**glClear**](glclear.md) function with the accumulation buffer enabled.

Only those pixels within the current scissor box are updated by any **glAccum** operation.

The following functions retrieve information related to the **glAccum** function:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_ACCUM\_RED\_BITS

**glGet** with argument GL\_ACCUM\_GREEN\_BITS

**glGet** with argument GL\_ACCUM\_BLUE\_BITS

**glGet** with argument GL\_ACCUM\_ALPHA\_BITS

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

[**glBlendFunc**](glblendfunc.md)
</dt> <dt>

[**glClear**](glclear.md)
</dt> <dt>

[**glClearAccum**](glclearaccum.md)
</dt> <dt>

[**glCopyPixels**](glcopypixels.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**glLogicOp**](gllogicop.md)
</dt> <dt>

[**glPixelStore**](glpixelstore-functions.md)
</dt> <dt>

[**glPixelTransfer**](glpixeltransfer.md)
</dt> <dt>

[**glReadBuffer**](glreadbuffer.md)
</dt> <dt>

[**glReadPixels**](glreadpixels.md)
</dt> <dt>

[**glScissor**](glscissor.md)
</dt> <dt>

[**glStencilOp**](glstencilop.md)
</dt> </dl>

 

 





