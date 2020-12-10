---
title: glDeleteTextures function (Gl.h)
description: The glDeleteTextures function deletes named textures.
ms.assetid: 300eb99a-9ee5-4495-9489-7e084db9c6c1
keywords:
- glDeleteTextures function OpenGL
topic_type:
- apiref
api_name:
- glDeleteTextures
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glDeleteTextures function

The **glDeleteTextures** function deletes named textures.

## Syntax


```C++
void WINAPI glDeleteTextures(
         GLsizei n,
   const GLuint  *textures
);
```



## Parameters

<dl> <dt>

*n* 
</dt> <dd>

The number of textures to be deleted.

</dd> <dt>

*textures* 
</dt> <dd>

An array of textures to be deleted.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | *n* was a negative value.<br/>                                                                                                  |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glDeleteTextures** function deletes *n* textures named by the elements of the array *textures*. After a texture is deleted, it has no contents or dimensionality, and its name is free for reuse (for example, by **glGenTextures**). The **glDeleteTextures** function ignores zeros and names that do not correspond to existing textures.

If a texture that is currently bound is deleted, the binding reverts to zero (the default texture).

You cannot include calls to **glDeleteTextures** in display lists.

> [!Note]  
> The **glDeleteTextures** function is only available in OpenGL version 1.1 or later.

 

The following function retrieves information related to **glDeleteTextures**:

-   [**glIsTexture**](glistexture.md)

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

[**glAreTexturesResident**](glaretexturesresident.md)
</dt> <dt>

[**glBegin**](glbegin.md)
</dt> <dt>

[**glBindTexture**](glbindtexture.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glGenTextures**](glgentextures.md)
</dt> <dt>

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**glGetTexParameter**](glgettexparameter.md)
</dt> <dt>

[**glIsTexture**](glistexture.md)
</dt> <dt>

[**glPrioritizeTextures**](glprioritizetextures.md)
</dt> <dt>

[**glTexGen**](gltexgen-functions.md)
</dt> <dt>

[**glTexImage1D**](glteximage1d.md)
</dt> <dt>

[**glTexImage2D**](glteximage2d.md)
</dt> <dt>

[**glTexParameter**](gltexparameter-functions.md)
</dt> </dl>

 

 





