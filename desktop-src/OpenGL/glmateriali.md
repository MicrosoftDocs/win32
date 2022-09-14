---
title: glMateriali function (Gl.h)
description: TheglMateriali function specifies material parameters for the lighting model.
ms.assetid: e3722dfd-3bdd-4460-8226-e50580ca1d79
keywords:
- glMateriali function OpenGL
topic_type:
- apiref
api_name:
- glMateriali
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glMateriali function

The**glMateriali** function specifies material parameters for the lighting model.

## Syntax


```C++
void WINAPI glMateriali(
   GLenum face,
   GLenum pname,
   GLint  param
);
```



## Parameters

<dl> <dt>

*face* 
</dt> <dd>

The face or faces that are being updated. Must be one of the following: GL\_FRONT, GL\_BACK, or GL\_FRONT and GL\_BACK.

</dd> <dt>

*pname* 
</dt> <dd>

The single-valued material parameter of the face or faces being updated. Must be GL\_SHININESS.



| Value                                                                                                                                                      | Meaning                                                                                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_SHININESS"></span><span id="gl_shininess"></span><dl> <dt>**GL\_SHININESS**</dt> </dl> | The *param* parameter is a single integer that specifies the RGBA specular exponent of the material. Integer values are mapped directly. Only values in the range \[0, 128\] are accepted. The default specular exponent for both front-facing and back-facing materials is 0. <br/> |



 

</dd> <dt>

*param* 
</dt> <dd>

The value to which parameter GL\_SHININESS will be set.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                              | Meaning                                                                       |
|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>  | Either *face* or *pname* was not an accepted value.<br/>                |
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl> | A specular exponent outside the range of \[0, 128\] was specified.<br/> |



## Remarks

The **glMateriali** function assigns values to material parameters. There are two matched sets of material parameters. One, the *front-facing* set, is used to shade points, lines, bitmaps, and all polygons (when two-sided lighting is disabled), or just front-facing polygons (when two-sided lighting is enabled). The other set, *back-facing*, is used to shade back-facing polygons only when two-sided lighting is enabled. Refer to [**glLightModel**](gllightmodel-functions.md) for details concerning one-sided and two-sided lighting calculations.

The **glMateriali** function takes three arguments. The first, *face*, specifies whether the GL\_FRONT materials, the GL\_BACK materials, or both GL\_FRONT\_AND\_BACK materials will be modified. The second, *pname*, specifies which of several parameters in one or both sets will be modified. The third, *param*, specifies what value will be assigned to the specified parameter.

Material parameters are used in the lighting equation that is optionally applied to each vertex. The equation is discussed in [**glLightModel**](gllightmodel-functions.md).

The material parameters can be updated at any time. In particular, **glMateriali** can be called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md). If only a single material parameter is to be changed per vertex, however, [**glColorMaterial**](glcolormaterial.md) is preferred over **glMateriali**.

The following function retrieves information related to **glMateriali**:

[**glGetMaterial**](glgetmaterial.md)

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

[**glColorMaterial**](glcolormaterial.md)
</dt> <dt>

[**glLight**](gllight-functions.md)
</dt> <dt>

[**glLightModel**](gllightmodel-functions.md)
</dt> </dl>

 

 





