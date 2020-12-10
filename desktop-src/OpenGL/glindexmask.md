---
title: glIndexMask function (Gl.h)
description: The glIndexMask function controls the writing of individual bits in the color-index buffers.
ms.assetid: f4b5df36-390f-4254-95fb-98589750a11b
keywords:
- glIndexMask function OpenGL
topic_type:
- apiref
api_name:
- glIndexMask
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glIndexMask function

The **glIndexMask** function controls the writing of individual bits in the color-index buffers.

## Syntax


```C++
void WINAPI glIndexMask(
   GLuint mask
);
```



## Parameters

<dl> <dt>

*mask* 
</dt> <dd>

A bit mask to enable and disable the writing of individual bits in the color-index buffers. Initially, the mask is all ones.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error code can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glIndexMask** function controls the writing of individual bits in the color-index buffers. The least significant *n* bits of *mask*, where *1* is the number of bits in a color-index buffer, specify a mask. Wherever a one appears in the mask, the corresponding bit in the color-index buffer (or buffers) is made writable. Where a zero appears, the bit is write-protected.

This mask is used only in color-index mode, and it affects only the buffers currently selected for writing (see [**glDrawBuffer**](gldrawbuffer.md)). Initially, all bits are enabled for writing.

The following function retrieves information related to **glIndexMask**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_INDEX\_WRITEMASK

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

[**glDepthMask**](gldepthmask.md)
</dt> <dt>

[**glDrawBuffer**](gldrawbuffer.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glIndex**](glindex-functions.md)
</dt> <dt>

[**glStencilMask**](glstencilmask.md)
</dt> </dl>

 

 





