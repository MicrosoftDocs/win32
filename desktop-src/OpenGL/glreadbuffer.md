---
title: glReadBuffer function (Gl.h)
description: The glReadBuffer function selects a color buffer source for pixels.
ms.assetid: 734153fa-e809-4b70-867e-55e46ab95712
keywords:
- glReadBuffer function OpenGL
topic_type:
- apiref
api_name:
- glReadBuffer
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glReadBuffer function

The **glReadBuffer** function selects a color buffer source for pixels.

## Syntax


```C++
void WINAPI glReadBuffer(
   GLenum mode
);
```



## Parameters

<dl> <dt>

*mode* 
</dt> <dd>

A color buffer. Accepted values are GL\_FRONT\_LEFT, GL\_FRONT\_RIGHT, GL\_BACK\_LEFT, GL\_BACK\_RIGHT, GL\_FRONT, GL\_BACK, GL\_LEFT, GL\_RIGHT, and GL\_AUX *i*, where *i* is between 0 and GL\_AUX\_BUFFERS 1.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *mode* was not an one of the twelve (or more) accepted values.<br/>                                                             |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | *mode* specified a buffer that does not exist.<br/>                                                                             |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glReadBuffer** function specifies a color buffer as the source for subsequent [**glReadPixels**](glreadpixels.md) and [**glCopyPixels**](glcopypixels.md) commands. The *mode* parameter accepts one of twelve or more predefined values. (GL\_AUX0 through GL\_AUX3 are always defined.) In a fully configured system, GL\_FRONT, GL\_LEFT, and GL\_FRONT\_LEFT all name the front-left buffer, GL\_FRONT\_RIGHT and GL\_RIGHT name the front-right buffer, and GL\_BACK\_LEFT and GL\_BACK name the back-left buffer.

Nonstereo double-buffered configurations have only a front-left and a back-left buffer. Single-buffered configurations have a front-left and a front-right buffer if stereo, and only a front-left buffer if nonstereo. It is an error to specify a nonexistent buffer to **glReadBuffer**.

By default, *mode* is GL\_FRONT in single-buffered configurations, and GL\_BACK in double-buffered configurations.

The following function retrieves information related to **glReadBuffer**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_READ\_BUFFER

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

[**glDrawBuffer**](gldrawbuffer.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glReadPixels**](glreadpixels.md)
</dt> </dl>

 

 





