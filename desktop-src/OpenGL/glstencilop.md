---
title: glStencilOp function (Gl.h)
description: The glStencilOp function sets the stencil test actions.
ms.assetid: 16809735-5624-49cf-bfa5-9908d008b234
keywords:
- glStencilOp function OpenGL
topic_type:
- apiref
api_name:
- glStencilOp
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glStencilOp function

The **glStencilOp** function sets the stencil test actions.

## Syntax


```C++
void WINAPI glStencilOp(
   GLenum fail,
   GLenum zfail,
   GLenum zpass
);
```



## Parameters

<dl> <dt>

*fail* 
</dt> <dd>

The action to take when the stencil test fails. The following six symbolic constants are accepted.



| Value                                                                                                                                                | Meaning                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| <span id="GL_KEEP"></span><span id="gl_keep"></span><dl> <dt>**GL\_KEEP**</dt> </dl>          | Keeps the current value.<br/>                                                                         |
| <span id="GL_ZERO"></span><span id="gl_zero"></span><dl> <dt>**GL\_ZERO**</dt> </dl>          | Sets the stencil buffer value to zero.<br/>                                                           |
| <span id="GL_REPLACE"></span><span id="gl_replace"></span><dl> <dt>**GL\_REPLACE**</dt> </dl> | Sets the stencil buffer value to *ref*, as specified by **glStencilFunc**.<br/>                       |
| <span id="GL_INCR"></span><span id="gl_incr"></span><dl> <dt>**GL\_INCR**</dt> </dl>          | Increments the current stencil buffer value. Clamps to the maximum representable unsigned value.<br/> |
| <span id="GL_DECR"></span><span id="gl_decr"></span><dl> <dt>**GL\_DECR**</dt> </dl>          | Decrements the current stencil buffer value. Clamps to zero.<br/>                                     |
| <span id="GL_INVERT"></span><span id="gl_invert"></span><dl> <dt>**GL\_INVERT**</dt> </dl>    | Bitwise inverts the current stencil buffer value.<br/>                                                |



 

</dd> <dt>

*zfail* 
</dt> <dd>

Stencil action when the stencil test passes, but the depth test fails. Accepts the same symbolic constants as *fail.*

</dd> <dt>

*zpass* 
</dt> <dd>

Stencil action when both the stencil test and the depth test pass, or when the stencil test passes and either there is no depth buffer or depth testing is not enabled. Accepts the same symbolic constants as *fail*.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *fail*, *zfail*, or *zpass* was any value other than the six defined constant values.<br/>                                      |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

Stenciling, like *z*-buffering, enables and disables drawing on a per-pixel basis. You draw into the stencil planes using OpenGL drawing primitives, then render geometry and images, using the stencil planes to mask out portions of the screen. Stenciling is typically used in multipass rendering algorithms to achieve special effects, such as decals, outlining, and constructive solid geometry rendering.

The stencil test conditionally eliminates a pixel based on the outcome of a comparison between the value in the stencil buffer and a reference value. The test is enabled with [**glEnable**](glenable.md) and [**glDisable**](gldisable.md) calls with argument GL\_STENCIL\_TEST, and controlled with [**glStencilFunc**](glstencilfunc.md).

The **glStencilOp** function takes three arguments that indicate what happens to the stored stencil value while stenciling is enabled. If the stencil test fails, no change is made to the pixel's color or depth buffers, and *fail* specifies what happens to the stencil buffer contents.

Stencil buffer values are treated as unsigned integers. When incremented and decremented, values are clamped to 0 and 2*n* 1, where *n* is the value returned by querying GL\_STENCIL\_BITS.

The other two arguments to **glStencilOp** specify stencil buffer actions should subsequent depth buffer tests succeed (*zpass*) or fail (*zfail*). (See [**glDepthFunc**](gldepthfunc.md).) They are specified using the same six symbolic constants as *fail*. Note that *zfail* is ignored when there is no depth buffer, or when the depth buffer is not enabled. In these cases, *fail* and *zpass* specify stencil action when the stencil test fails and passes, respectively.

Initially the stencil test is disabled. If there is no stencil buffer, no stencil modification can occur and it is as if the stencil tests always pass, regardless of any call to **glStencilOp**.

The following functions retrieve information related to **glStencilOp**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_STENCIL\_FAIL

**glGet** with argument GL\_STENCIL\_PASS\_DEPTH\_PASS

**glGet** with argument GL\_STENCIL\_PASS\_DEPTH\_FAIL

**glGet** with argument GL\_STENCIL\_BITS

[**glIsEnabled**](glisenabled.md) with argument GL\_STENCIL\_TEST

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

[**glDepthFunc**](gldepthfunc.md)
</dt> <dt>

[**glEnable**](glenable.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glIsEnabled**](glisenabled.md)
</dt> <dt>

[**glLogicOp**](gllogicop.md)
</dt> <dt>

[**glStencilFunc**](glstencilfunc.md)
</dt> </dl>

 

 





