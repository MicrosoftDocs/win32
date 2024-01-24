---
title: glStencilFunc function (Gl.h)
description: The glStencilFunc function sets the function and reference value for stencil testing.
ms.assetid: 6c84415b-4d22-494b-90f2-6243d1406725
keywords:
- glStencilFunc function OpenGL
topic_type:
- apiref
api_name:
- glStencilFunc
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glStencilFunc function

The **glStencilFunc** function sets the function and reference value for stencil testing.

## Syntax


```C++
void WINAPI glStencilFunc(
   GLenum func,
   GLint  ref,
   GLuint mask
);
```



## Parameters

<dl> <dt>

*func* 
</dt> <dd>

The test function. The following eight tokens are valid.



| Value                                                                                                                                                   | Meaning                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <span id="GL_NEVER"></span><span id="gl_never"></span><dl> <dt>**GL\_NEVER**</dt> </dl>          | Always fails.<br/>                                         |
| <span id="GL_LESS"></span><span id="gl_less"></span><dl> <dt>**GL\_LESS**</dt> </dl>             | Passes if (*ref* & *mask*) < (*stencil* & *mask*).<br/> |
| <span id="GL_LEQUAL"></span><span id="gl_lequal"></span><dl> <dt>**GL\_LEQUAL**</dt> </dl>       | Passes if (*ref* & *mask*) = (*stencil* & *mask*).<br/>    |
| <span id="GL_GREATER"></span><span id="gl_greater"></span><dl> <dt>**GL\_GREATER**</dt> </dl>    | Passes if (*ref* & *mask*) > (*stencil* & *mask*).<br/> |
| <span id="GL_GEQUAL"></span><span id="gl_gequal"></span><dl> <dt>**GL\_GEQUAL**</dt> </dl>       | Passes if (*ref* & *mask*) = (*stencil* & *mask*).<br/>    |
| <span id="GL_EQUAL"></span><span id="gl_equal"></span><dl> <dt>**GL\_EQUAL**</dt> </dl>          | Passes if (*ref* & *mask*) = (*stencil* & *mask*).<br/>    |
| <span id="GL_NOTEQUAL"></span><span id="gl_notequal"></span><dl> <dt>**GL\_NOTEQUAL**</dt> </dl> | Passes if (*ref* & *mask*) ? (*stencil* & *mask*).<br/>    |
| <span id="GL_ALWAYS"></span><span id="gl_always"></span><dl> <dt>**GL\_ALWAYS**</dt> </dl>       | Always passes.<br/>                                        |



 

</dd> <dt>

*ref* 
</dt> <dd>

The reference value for the stencil test. The *ref* parameter is clamped to the range \[0, 2*n* 1\], where *n* is the number of bitplanes in the stencil buffer.

</dd> <dt>

*mask* 
</dt> <dd>

A mask that is **AND**ed with both the reference value and the stored stencil value when the test is done.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *func* was not one of the eight accepted values.<br/>                                                                           |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

Stenciling, like *z*-buffering, enables and disables drawing on a per-pixel basis. You draw into the stencil planes using OpenGL drawing primitives, then render geometry and images, using the stencil planes to mask out portions of the screen. Stenciling is typically used in multipass rendering algorithms to achieve special effects, such as decals, outlining, and constructive solid geometry rendering.

The stencil test conditionally eliminates a pixel based on the outcome of a comparison between the reference value and the value in the stencil buffer. The test is enabled by [**glEnable**](glenable.md) and [**glDisable**](gldisable.md) with argument GL\_STENCIL\_TEST. Actions taken based on the outcome of the stencil test are specified with [**glStencilOp**](glstencilop.md).

The *func* parameter is a symbolic constant that determines the stencil comparison function. It accepts one of the eight values shown above. The *ref* parameter is an integer reference value that is used in the stencil comparison. It is clamped to the range \[0, 2*n* 1\], where *n* is the number of bitplanes in the stencil buffer. The *mask* parameter is bitwise **AND**ed with both the reference value and the stored stencil value, with the **AND**ed values participating in the comparison.

If *stencil* represents the value stored in the corresponding stencil buffer location, the preceding list shows the effect of each comparison function that can be specified by *func*. Only if the comparison succeeds is the pixel passed through to the next stage in the rasterization process (see [**glStencilOp**](glstencilop.md)). All tests treat *stencil* values as unsigned integers in the range \[0, 2*n* 1\], where *n* is the number of bitplanes in the stencil buffer.

Initially, the stencil test is disabled. If there is no stencil buffer, no stencil modification can occur and it is as if the stencil test always passes.

The following functions retrieve information related to **glStencilFunc**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_STENCIL\_FUNC

**glGet** with argument GL\_STENCIL\_VALUE\_MASK

**glGet** with argument GL\_STENCIL\_REF

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

[**glStencilOp**](glstencilop.md)
</dt> </dl>

 

 





