---
title: glLogicOp function (Gl.h)
description: The glLogicOp function specifies a logical pixel operation for color index rendering.
ms.assetid: 29edf9bd-f3b8-4de7-9afb-07714f4efd92
keywords:
- glLogicOp function OpenGL
topic_type:
- apiref
api_name:
- glLogicOp
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glLogicOp function

The **glLogicOp** function specifies a logical pixel operation for color index rendering.

## Syntax


```C++
void WINAPI glLogicOp(
   GLenum opcode
);
```



## Parameters

<dl> <dt>

*opcode* 
</dt> <dd>

A symbolic constant that selects a logical operation. The following symbols are accepted where s equals the value of the source bit and d is the value of the destination bit.



| Value                                                                                                                                                                   | Meaning              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| <span id="GL_CLEAR"></span><span id="gl_clear"></span><dl> <dt>**GL\_CLEAR**</dt> </dl>                          | 0<br/>         |
| <span id="GL_SET"></span><span id="gl_set"></span><dl> <dt>**GL\_SET**</dt> </dl>                                | 1<br/>         |
| <span id="GL_COPY"></span><span id="gl_copy"></span><dl> <dt>**GL\_COPY**</dt> </dl>                             | s<br/>         |
| <span id="GL_COPY_INVERTED"></span><span id="gl_copy_inverted"></span><dl> <dt>**GL\_COPY\_INVERTED**</dt> </dl> | !s<br/>        |
| <span id="GL_NOOP"></span><span id="gl_noop"></span><dl> <dt>**GL\_NOOP**</dt> </dl>                             | d<br/>         |
| <span id="GL_INVERT"></span><span id="gl_invert"></span><dl> <dt>**GL\_INVERT**</dt> </dl>                       | !d<br/>        |
| <span id="GL_AND"></span><span id="gl_and"></span><dl> <dt>**GL\_AND**</dt> </dl>                                | s & d<br/>     |
| <span id="GL_NAND"></span><span id="gl_nand"></span><dl> <dt>**GL\_NAND**</dt> </dl>                             | !(s & d)<br/>  |
| <span id="GL_OR"></span><span id="gl_or"></span><dl> <dt>**GL\_OR**</dt> </dl>                                   | s \| d<br/>    |
| <span id="GL_NOR"></span><span id="gl_nor"></span><dl> <dt>**GL\_NOR**</dt> </dl>                                | !(s \| d)<br/> |
| <span id="GL_XOR"></span><span id="gl_xor"></span><dl> <dt>**GL\_XOR**</dt> </dl>                                | s ^ d<br/>     |
| <span id="GL_EQUIV"></span><span id="gl_equiv"></span><dl> <dt>**GL\_EQUIV**</dt> </dl>                          | !(s ^ d)<br/>  |
| <span id="GL_AND_REVERSE"></span><span id="gl_and_reverse"></span><dl> <dt>**GL\_AND\_REVERSE**</dt> </dl>       | s & !d<br/>    |
| <span id="GL_AND_INVERTED"></span><span id="gl_and_inverted"></span><dl> <dt>**GL\_AND\_INVERTED**</dt> </dl>    | !s & d<br/>    |
| <span id="GL_OR_REVERSE"></span><span id="gl_or_reverse"></span><dl> <dt>**GL\_OR\_REVERSE**</dt> </dl>          | s \| !d<br/>   |
| <span id="GL_OR_INVERTED"></span><span id="gl_or_inverted"></span><dl> <dt>**GL\_OR\_INVERTED**</dt> </dl>       | !s \| d<br/>   |



 

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *opcode* was not an accepted value.<br/>                                                                                        |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glLogicOp** function specifies a logical operation that, when enabled, is applied between the incoming color index and the color index at the corresponding location in the framebuffer. The logical operation is enabled or disabled with [**glEnable**](glenable.md) and **glDisable** using the symbolic constant GL\_LOGIC\_OP.

The *opcode* parameter is a symbolic constant chosen from the list below. In the explanation of the logical operations, *s* represents the incoming color index and *d* represents the index in the framebuffer. Standard C-language operators are used. As these bitwise operators suggest, the logical operation is applied independently to each bit pair of the source and destination indexes.

Logical pixel operations are not applied to RGBA color buffers.

When more than one color-index buffer is enabled for drawing, logical operations are done separately for each enabled buffer, using the contents of that buffer for the destination index (see [**glDrawBuffer**](gldrawbuffer.md)).

The *opcode* parameter must be one of the 16 accepted values. Other values result in an error.

The following functions retrieve information related to **glLogicOp**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_LOGIC\_OP\_MODE

[**glIsEnabled**](glisenabled.md) with argument GL\_LOGIC\_OP

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

[**glAlphaFunc**](glalphafunc.md)
</dt> <dt>

[**glBegin**](glbegin.md)
</dt> <dt>

[**glBlendFunc**](glblendfunc.md)
</dt> <dt>

[**glDrawBuffer**](gldrawbuffer.md)
</dt> <dt>

[**glEnable**](glenable.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glIsEnabled**](glisenabled.md)
</dt> <dt>

[**glStencilOp**](glstencilop.md)
</dt> </dl>

 

 





