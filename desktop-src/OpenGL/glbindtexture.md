---
title: glBindTexture function (Gl.h)
description: The glBindTexture function enables the creation of a named texture that is bound to a texture target.
ms.assetid: 800f2360-b40e-4911-9a45-6f310aeeefeb
keywords:
- glBindTexture function OpenGL
topic_type:
- apiref
api_name:
- glBindTexture
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glBindTexture function

The **glBindTexture** function enables the creation of a named texture that is bound to a texture target.

## Syntax


```C++
void WINAPI glBindTexture(
   GLenum target,
   GLuint texture
);
```



## Parameters

<dl> <dt>

*target* 
</dt> <dd>

The target to which the texture is bound. Must have the value GL\_TEXTURE\_1D or GL\_TEXTURE\_2D.

</dd> <dt>

*texture* 
</dt> <dd>

The name of a texture; the texture name cannot currently be in use.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | The parameter *target* was not an accepted value.<br/>                                                                                                                                                       |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The parameter *texture* did not have the same dimensionality as *target*, or the function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glBindTexture** function enables you to create a named texture. Calling **glBindTexture** with *target* set to GL\_TEXTURE\_1D or GL\_TEXTURE\_2D, and *texture* set to the name of the new texture you have created binds the texture name to the appropriate texture target. When a texture is bound to a target, the previous binding for that target is no longer in effect.

Texture names are unsigned integers with the value zero reserved to represent the default texture for each texture target. Texture names and the corresponding texture contents are local to the shared display-list space of the current OpenGL rendering context; two rendering contexts share texture names only if they also share display lists. You can generate a set of new texture names using [**glGenTextures**](glgentextures.md).

When a texture is first bound, it assumes the dimensionality of its texture target; a texture bound to GL\_TEXTURE\_1D becomes one-dimensional and a texture bound to GL\_TEXTURE\_2D becomes two-dimensional. Operations you perform on a texture target also affect a texture bound to the target. When you query a texture target, the return value is the state of the texture bound to it. Texture targets become aliases for textures currently bound to them.

When you bind a texture with **glBindTexture**, the binding remains active until a different texture is bound to the same target or you delete the bound texture with the [**glDeleteTextures**](gldeletetextures.md) function. Once you create a named texture you can bind it to a texture target that has the same dimensionality as often as needed.

It is usually much faster to use **glBindTexture** to bind an existing named texture to one of the texture targets than it is to reload the texture image using [**glTexImage1D**](glteximage1d.md) or [**glTexImage2D**](glteximage2d.md). For additional control of texturing performance, use [**glPrioritizeTextures**](glprioritizetextures.md).

You can include calls to **glBindTexture** in display lists.

> [!Note]  
> The **glBindTexture** function is only available in OpenGL version 1.1 or later.

 

The following functions retrieve information related to **glBindTexture**:

-   [**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_TEXTURE\_1D\_BINDING

**glGet** with argument GL\_TEXTURE\_2D\_BINDING

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

[**glDeleteTextures**](gldeletetextures.md)
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

[**glTexImage1D**](glteximage1d.md)
</dt> <dt>

[**glTexImage2D**](glteximage2d.md)
</dt> <dt>

[**glTexParameter**](gltexparameter-functions.md)
</dt> </dl>

 

 





