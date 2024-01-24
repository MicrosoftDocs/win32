---
title: glClearIndex function (Gl.h)
description: The glClearIndex function specifies the clear value for the color-index buffers.
ms.assetid: 87983d93-c5a1-445f-8621-1c2952d93a0f
keywords:
- glClearIndex function OpenGL
topic_type:
- apiref
api_name:
- glClearIndex
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glClearIndex function

The **glClearIndex** function specifies the clear value for the color-index buffers.

## Syntax


```C++
void WINAPI glClearIndex(
   GLfloat c
);
```



## Parameters

<dl> <dt>

*c* 
</dt> <dd>

The index used when the color-index buffers are cleared. The default value is zero.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glClearIndex** function specifies the index used by [**glClear**](glclear.md) to clear the color-index buffers. The *c* parameter is not clamped. Rather, *c* is converted to a fixed-point value with unspecified precision to the right of the binary point. The integer part of this value is then masked with 2<sup>m</sup>  - 1, where *m* is the number of bits in a color index stored in the framebuffer.

The following functions retrieve information related to **glClearIndex**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_INDEX\_CLEAR\_VALUE

**glGet** with argument GL\_INDEX\_BITS

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

[**glClear**](glclear.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> </dl>

 

 





