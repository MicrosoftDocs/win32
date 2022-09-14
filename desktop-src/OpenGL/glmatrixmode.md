---
title: glMatrixMode function (Gl.h)
description: The glMatrixMode function specifies which matrix is the current matrix.
ms.assetid: f1006ea3-322a-42a9-b33c-6c7181985ef9
keywords:
- glMatrixMode function OpenGL
topic_type:
- apiref
api_name:
- glMatrixMode
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glMatrixMode function

The **glMatrixMode** function specifies which matrix is the current matrix.

## Syntax


```C++
void WINAPI glMatrixMode(
   GLenum mode
);
```



## Parameters

<dl> <dt>

*mode* 
</dt> <dd>

The matrix stack that is the target for subsequent matrix operations. The *mode* parameter can assume one of three values.



| Value                                                                                                                                                         | Meaning                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| <span id="GL_MODELVIEW"></span><span id="gl_modelview"></span><dl> <dt>**GL\_MODELVIEW**</dt> </dl>    | Applies subsequent matrix operations to the modelview matrix stack.<br/>  |
| <span id="GL_PROJECTION"></span><span id="gl_projection"></span><dl> <dt>**GL\_PROJECTION**</dt> </dl> | Applies subsequent matrix operations to the projection matrix stack.<br/> |
| <span id="GL_TEXTURE"></span><span id="gl_texture"></span><dl> <dt>**GL\_TEXTURE**</dt> </dl>          | Applies subsequent matrix operations to the texture matrix stack.<br/>    |



 

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *mode* was not an accepted value.<br/>                                                                                          |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glMatrixMode** function sets the current matrix mode.

The following function retrieves information related to **glMatrixMode**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_MATRIX\_MODE

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

[**glEnd**](glend.md)
</dt> <dt>

[**glLoadMatrix**](glloadmatrix.md)
</dt> <dt>

[**glPushMatrix**](glpushmatrix.md)
</dt> </dl>

 

 





