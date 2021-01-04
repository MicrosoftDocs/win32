---
title: glClear function (Gl.h)
description: The glClear function clears buffers to preset values.
ms.assetid: 9818f969-3145-45ea-aa9c-2abed953a8e0
keywords:
- glClear function OpenGL
topic_type:
- apiref
api_name:
- glClear
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glClear function

The **glClear** function clears buffers to preset values.

## Syntax


```C++
void WINAPI glClear(
   GLbitfield mask
);
```



## Parameters

<dl> <dt>

*mask* 
</dt> <dd>

Bitwise OR operators of masks that indicate the buffers to be cleared. The four masks are as follows.



| Value                                                                                                                                                                                   | Meaning                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <span id="GL_COLOR_BUFFER_BIT"></span><span id="gl_color_buffer_bit"></span><dl> <dt>**GL\_COLOR\_BUFFER\_BIT**</dt> </dl>       | The buffers currently enabled for color writing.<br/> |
| <span id="GL_DEPTH_BUFFER_BIT"></span><span id="gl_depth_buffer_bit"></span><dl> <dt>**GL\_DEPTH\_BUFFER\_BIT**</dt> </dl>       | The depth buffer.<br/>                                |
| <span id="GL_ACCUM_BUFFER_BIT"></span><span id="gl_accum_buffer_bit"></span><dl> <dt>**GL\_ACCUM\_BUFFER\_BIT**</dt> </dl>       | The accumulation buffer.<br/>                         |
| <span id="GL_STENCIL_BUFFER_BIT"></span><span id="gl_stencil_buffer_bit"></span><dl> <dt>**GL\_STENCIL\_BUFFER\_BIT**</dt> </dl> | The stencil buffer.<br/>                              |



 

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | Any bit other than the four defined bits was set in *mask*.<br/>                                                                |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glClear** function sets the bitplane area of the window to values previously selected by [**glClearColor**](glclearcolor.md), [**glClearIndex**](glclearindex.md), [**glClearDepth**](glcleardepth.md), [**glClearStencil**](glclearstencil.md), and [**glClearAccum**](glclearaccum.md). You can clear multiple color buffers simultaneously by selecting more than one buffer at a time using [**glDrawBuffer**](gldrawbuffer.md).

The pixel-ownership test, the scissor test, dithering, and the buffer writemasks affect the operation of **glClear**. The scissor box bounds the cleared region. The **glClear** function ignores the alpha function, blend function, logical operation, stenciling, texture mapping, and *z*-buffering.

The **glClear** function takes a single argument (*mask*) that is the bitwise OR of several values indicating which buffer is to be cleared.

The value to which each buffer is cleared depends on the setting of the clear value for that buffer.

If a buffer is not present, a **glClear** call directed at that buffer has no effect.

The following functions retrieve information related to **glClear**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_ACCUM\_CLEAR\_VALUE

**glGet** with argument GL\_DEPTH\_CLEAR\_VALUE

**glGet** with argument GL\_INDEX\_CLEAR\_VALUE

**glGet** with argument GL\_COLOR\_CLEAR\_VALUE

**glGet** with argument GL\_STENCIL\_CLEAR\_VALUE

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

[**glClearAccum**](glclearaccum.md)
</dt> <dt>

[**glClearColor**](glclearcolor.md)
</dt> <dt>

[**glClearDepth**](glcleardepth.md)
</dt> <dt>

[**glClearIndex**](glclearindex.md)
</dt> <dt>

[**glClearStencil**](glclearstencil.md)
</dt> <dt>

[**glDrawBuffer**](gldrawbuffer.md)
</dt> <dt>

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**glScissor**](glscissor.md)
</dt> </dl>

 

 





