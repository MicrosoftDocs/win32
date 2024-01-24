---
title: glClearStencil function (Gl.h)
description: The glClearStencil function specifies the clear value for the stencil buffer.
ms.assetid: bbde8fa8-78f3-45bd-bac3-5d03839acc52
keywords:
- glClearStencil function OpenGL
topic_type:
- apiref
api_name:
- glClearStencil
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glClearStencil function

The **glClearStencil** function specifies the clear value for the stencil buffer.

## Syntax


```C++
void WINAPI glClearStencil(
   GLint s
);
```



## Parameters

<dl> <dt>

*s* 
</dt> <dd>

The index used when the stencil buffer is cleared. The default value is zero.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error code can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glClearStencil** function specifies the index used by [**glClear**](glclear.md) to clear the stencil buffer. The *s* parameter is masked with 2<sup>m</sup>  - 1, where *m* is the number of bits in the stencil buffer.

The following functions retrieve information related to the **glClearStencil** function:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_STENCIL\_CLEAR\_VALUE

**glGet** with argument GL\_STENCIL\_BITS

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

 

 





