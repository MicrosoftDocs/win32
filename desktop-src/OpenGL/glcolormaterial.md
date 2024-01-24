---
title: glColorMaterial function (Gl.h)
description: The glColorMaterial function causes a material color to track the current color.
ms.assetid: 6dbef2c2-f902-4f25-8a87-9e3d710dd807
keywords:
- glColorMaterial function OpenGL
topic_type:
- apiref
api_name:
- glColorMaterial
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glColorMaterial function

The **glColorMaterial** function causes a material color to track the current color.

## Syntax


```C++
void WINAPI glColorMaterial(
   GLenum face,
   GLenum mode
);
```



## Parameters

<dl> <dt>

*face* 
</dt> <dd>

Specifies whether front, back, or both front and back material parameters should track the current color. Accepted values are GL\_FRONT, GL\_BACK, and GL\_FRONT\_AND\_BACK. The default value is GL\_FRONT\_AND\_BACK.

</dd> <dt>

*mode* 
</dt> <dd>

Specifies which of several material parameters track the current color. Accepted values are GL\_EMISSION, GL\_AMBIENT, GL\_DIFFUSE, GL\_SPECULAR, and GL\_AMBIENT\_AND\_DIFFUSE. The default value is GL\_AMBIENT\_AND\_DIFFUSE.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *face* or *mode* was not an accepted value.<br/>                                                                                |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glColorMaterial** function specifies which material parameters track the current color. When you enable GL\_COLOR\_MATERIAL, for each of the material or materials specified by *face*, the material parameter or parameters specified by *mode* track the current color at all times. Enable and disable GL\_COLOR\_MATERIAL with the functions [**glEnable**](glenable.md) and [**glDisable**](gldisable.md), which you call with GL\_COLOR\_MATERIAL as their argument. By default, GL\_COLOR\_MATERIAL is disabled.

With **glColorMaterial**, you can change a subset of material parameters for each vertex using only the [**glColor**](glcolor-functions.md) function, without calling [**glMaterial**](glmaterial-functions.md). If you are going to specify only such a subset of parameters for each vertex, it is better to do so with **glColorMaterial** than with **glMaterial**.

The following functions retrieve information related to **glColorMaterial**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_COLOR\_MATERIAL\_PARAMETER

**glGet** with argument GL\_COLOR\_MATERIAL\_FACE

[**glIsEnabled**](glisenabled.md) with argument GL\_COLOR\_MATERIAL

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

[**glColor**](glcolor-functions.md)
</dt> <dt>

[**glDisable**](gldisable.md)
</dt> <dt>

[**glEnable**](glenable.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**glIsEnabled**](glisenabled.md)
</dt> <dt>

[**glLight**](gllight-functions.md)
</dt> <dt>

[**glLightModel**](gllightmodel-functions.md)
</dt> <dt>

[**glMaterial**](glmaterial-functions.md)
</dt> </dl>

 

 





