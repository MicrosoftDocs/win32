---
title: glPrioritizeTextures function (Gl.h)
description: The glPrioritizeTextures function sets the residence priority of textures.
ms.assetid: 09018c86-c667-4e43-a95a-51a8077aed33
keywords:
- glPrioritizeTextures function OpenGL
topic_type:
- apiref
api_name:
- glPrioritizeTextures
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glPrioritizeTextures function

The **glPrioritizeTextures** function sets the residence priority of textures.

## Syntax


```C++
void WINAPI glPrioritizeTextures(
         GLsizei  n,
   const GLuint   *textures,
   const GLclampf *priorities
);
```



## Parameters

<dl> <dt>

*n* 
</dt> <dd>

The number of textures to be prioritized.

</dd> <dt>

*textures* 
</dt> <dd>

A pointer to the first element of an array containing the names of the textures to be prioritized.

</dd> <dt>

*priorities* 
</dt> <dd>

A pointer to the first element of an array containing the texture priorities. A priority given in an element of the *priorities* parameter applies to the texture named by the corresponding element of the *textures* parameter.

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

The **glPrioritizeTextures** function assigns the *n* texture priorities specified in the *priorities* parameter to the *n* textures named in the *textures* parameter. On computers with a limited amount of texture memory, OpenGL establishes a "working set" of textures that are resident in texture memory. These textures can be bound to a texture target much more efficiently than textures that are not resident.

By specifying a priority for each texture, the **glPrioritizeTextures** function enables you to determine which textures should be resident.

The texture priorities elements in *priorities* are clamped to the range \[0.0, 1.0\] before being assigned. Zero indicates the lowest priority; thus textures with priority zero are least likely to be resident. The value 1.0 indicates the highest priority; thus textures with priority 1.0 are most likely to be resident. However, textures are not guaranteed to be resident until they are bound.

The **glPrioritizeTextures** function ignores attempts to prioritize texture 0, or any texture name that does not correspond to an existing texture. None of the functions named by the *textures* parameter need to be bound to a texture target.

If a texture is currently bound, you can also use the [**glTexParameter**](gltexparameter-functions.md) function to set its priority. This is the only way to set the priority of a default texture.

You can include **glPrioritizeTextures** in display lists.

The following function retrieves the priority of a currently-bound texture related to **glPrioritizeTextures**:

-   [**glGetTexParameter**](glgettexparameter.md) with parameter name GL\_TEXTURE\_PRIORITY

> [!Note]  
> The **glPrioritizeTextures** function is only available in OpenGL version 1.1 or later.

 

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

[**glEnd**](glend.md)
</dt> <dt>

[**glGetTexParameter**](glgettexparameter.md)
</dt> <dt>

[**glTexImage1D**](glteximage1d.md)
</dt> <dt>

[**glTexImage2D**](glteximage2d.md)
</dt> <dt>

[**glTexParameter**](gltexparameter-functions.md)
</dt> </dl>

 

 





