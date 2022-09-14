---
title: glGetPixelMapuiv function (Gl.h)
description: The glGetPixelMapfv, glGetPixelMapuiv, and glGetPixelMapusv functions return the specified pixel map. | glGetPixelMapuiv function (Gl.h)
ms.assetid: a49f5fd2-c350-4acc-8f61-ecb92b0164cc
keywords:
- glGetPixelMapuiv function OpenGL
topic_type:
- apiref
api_name:
- glGetPixelMapuiv
api_location:
- Opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glGetPixelMapuiv function

The [**glGetPixelMapfv**](glgetpixelmapfv.md), **glGetPixelMapuiv**, and [**glGetPixelMapusv**](glgetpixelmapusv.md) functions return the specified pixel map.

## Syntax


```C++
void WINAPI glGetPixelMapuiv(
   GLenum map,
   GLuint *values
);
```



## Parameters

<dl> <dt>

*map* 
</dt> <dd>

The name of the pixel map to return. Accepted values are GL\_PIXEL\_MAP\_I\_TO\_I, GL\_PIXEL\_MAP\_S\_TO\_S, GL\_PIXEL\_MAP\_I\_TO\_R, GL\_PIXEL\_MAP\_I\_TO\_G, GL\_PIXEL\_MAP\_I\_TO\_B, GL\_PIXEL\_MAP\_I\_TO\_A, GL\_PIXEL\_MAP\_R\_TO\_R, GL\_PIXEL\_MAP\_G\_TO\_G, GL\_PIXEL\_MAP\_B\_TO\_B, and GL\_PIXEL\_MAP\_A\_TO\_A.

</dd> <dt>

*values* 
</dt> <dd>

Returns the pixel map contents.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *map* was not an accepted value.<br/>                                                                                           |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

See [**glPixelMap**](glpixelmap.md) for a description of the acceptable values for the *map* parameter. The **glGetPixelMap** function returns in *values* the contents of the pixel map specified in *map*. Use pixel maps during the execution of [**glReadPixels**](glreadpixels.md), [**glDrawPixels**](gldrawpixels.md), [**glCopyPixels**](glcopypixels.md), [**glTexImage1D**](glteximage1d.md), and [**glTexImage2D**](glteximage2d.md) to map color indexes, stencil indexes, color components, and depth components to other values.

Unsigned integer values, if requested, are linearly mapped from the internal fixed or floating-point representation such that 1.0 maps to the largest representable integer value, and 0.0 maps to zero. Return unsigned integer values are undefined if the map value was not in the range \[0,1\].

To determine the required size of *map*, call [**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with the appropriate symbolic constant.

If an error is generated, no change is made to the contents of *values*.

The following functions retrieve information related to **glGetPixelMap**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_PIXEL\_MAP\_I\_TO\_I\_SIZE

**glGet** with argument GL\_PIXEL\_MAP\_S\_TO\_S\_SIZE

**glGet** with argument GL\_PIXEL\_MAP\_I\_TO\_R\_SIZE

**glGet** with argument GL\_PIXEL\_MAP\_I\_TO\_G\_SIZE

**glGet** with argument GL\_PIXEL\_MAP\_I\_TO\_B\_SIZE

**glGet** with argument GL\_PIXEL\_MAP\_I\_TO\_A\_SIZE

**glGet** with argument GL\_PIXEL\_MAP\_R\_TO\_R\_SIZE

**glGet** with argument GL\_PIXEL\_MAP\_G\_TO\_G\_SIZE

**glGet** with argument GL\_PIXEL\_MAP\_B\_TO\_B\_SIZE

**glGet** with argument GL\_PIXEL\_MAP\_A\_TO\_A\_SIZE

**glGet** with argument GL\_MAX\_PIXEL\_MAP\_TABLE

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

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**glPixelMap**](glpixelmap.md)
</dt> <dt>

[**glPixelTransfer**](glpixeltransfer.md)
</dt> <dt>

[**glReadPixels**](glreadpixels.md)
</dt> <dt>

[**glTexImage1D**](glteximage1d.md)
</dt> <dt>

[**glTexImage2D**](glteximage2d.md)
</dt> </dl>

 

 





