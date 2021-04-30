---
title: glAlphaFunc function (Gl.h)
description: The glAlphaFunc function enables your application to set the alpha test function.
ms.assetid: 6c0c06b5-1bad-4590-a262-f134f63f0936
keywords:
- glAlphaFunc function OpenGL
topic_type:
- apiref
api_name:
- glAlphaFunc
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glAlphaFunc function

The **glAlphaFunc** function enables your application to set the alpha test function.

## Syntax


```C++
void WINAPI glAlphaFunc(
   GLenum   func,
   GLclampf ref
);
```



## Parameters

<dl> <dt>

*func* 
</dt> <dd>

The alpha comparison function. The following are the accepted symbolic constants and their meanings.



| Value                                                                                                                                                   | Meaning                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| <span id="GL_NEVER"></span><span id="gl_never"></span><dl> <dt>**GL\_NEVER**</dt> </dl>          | Never passes.<br/>                                                                       |
| <span id="GL_LESS"></span><span id="gl_less"></span><dl> <dt>**GL\_LESS**</dt> </dl>             | Passes if the incoming alpha value is less than the reference value.<br/>                |
| <span id="GL_EQUAL"></span><span id="gl_equal"></span><dl> <dt>**GL\_EQUAL**</dt> </dl>          | Passes if the incoming alpha value is equal to the reference value.<br/>                 |
| <span id="GL_LEQUAL"></span><span id="gl_lequal"></span><dl> <dt>**GL\_LEQUAL**</dt> </dl>       | Passes if the incoming alpha value is less than or equal to the reference value.<br/>    |
| <span id="GL_GREATER"></span><span id="gl_greater"></span><dl> <dt>**GL\_GREATER**</dt> </dl>    | Passes if the incoming alpha value is greater than the reference value.<br/>             |
| <span id="GL_NOTEQUAL"></span><span id="gl_notequal"></span><dl> <dt>**GL\_NOTEQUAL**</dt> </dl> | Passes if the incoming alpha value is not equal to the reference value.<br/>             |
| <span id="GL_GEQUAL"></span><span id="gl_gequal"></span><dl> <dt>**GL\_GEQUAL**</dt> </dl>       | Passes if the incoming alpha value is greater than or equal to the reference value.<br/> |
| <span id="GL_ALWAYS"></span><span id="gl_always"></span><dl> <dt>**GL\_ALWAYS**</dt> </dl>       | Always passes. This is the default.<br/>                                                 |



 

</dd> <dt>

*ref* 
</dt> <dd>

The reference value to which incoming alpha values are compared. This value is clamped to the range 0 through 1, where 0 represents the lowest possible alpha value and 1 the highest possible value. The default reference is 0.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *func* was not an accepted value.<br/>                                                                                          |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The alpha test discards fragments depending on the outcome of a comparison between the incoming fragments' alpha values and a constant reference value. The **glAlphaFunc** function specifies the reference and comparison function. The comparison is performed only if alpha testing is enabled. (For more information on GL\_ALPHA\_TEST, see [**glEnable**](glenable.md).)

The *func* and *ref* parameters specify the conditions under which the pixel is drawn. The incoming alpha value is compared to *ref* using the function specified by *func*. If the comparison passes, the incoming fragment is drawn, conditional on subsequent stencil and depth-buffer tests. If the comparison fails, no change is made to the framebuffer at that pixel location.

The **glAlphaFunc** function operates on all pixel writes, including those resulting from the scan conversion of points, lines, polygons, and bitmaps, and from pixel draw and copy operations. The **glAlphaFunc** function does not affect screen clear operations.

Alpha testing is done only in RGBA mode.

The following functions retrieve information related to the **glAlphaFunc** function:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_ALPHA\_TEST\_FUNC

**glGet** with argument GL\_ALPHA\_TEST\_REF

[**glIsEnabled**](glisenabled.md) with argument GL\_ALPHA\_TEST

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

[**glDepthFunc**](gldepthfunc.md)
</dt> <dt>

[**glEnable**](glenable.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**glIsEnabled**](glisenabled.md)
</dt> <dt>

[**glStencilFunc**](glstencilfunc.md)
</dt> </dl>

 

 





