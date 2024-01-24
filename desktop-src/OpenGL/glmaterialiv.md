---
title: glMaterialiv function (Gl.h)
description: The glMaterialiv function specifies material parameters for the lighting model.
ms.assetid: 9d045202-e565-4cf7-946a-60299e1bc1b1
keywords:
- glMaterialfv function OpenGL
topic_type:
- apiref
api_name:
- glMaterialfv
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glMaterialiv function

The **glMaterialiv** function specifies material parameters for the lighting model.

## Syntax


```C++
void WINAPI glMaterialfv(
         GLenum face,
         GLenum pname,
   const GLint  *params
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

The material parameter of the face or faces being updated. The parameters that can be specified using [**glMaterialiv**](glmaterialfv.md), and their interpretations by the lighting equation, are as follows.



| Value                                                                                                                                                                                      | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_AMBIENT"></span><span id="gl_ambient"></span><dl> <dt>**GL\_AMBIENT**</dt> </dl>                                       | The params parameter contains four integer values that specify the ambient RGBA reflectance of the material. Integer values are mapped linearly such that the most positive representable value maps to 1.0, and the most negative representable value maps to -1.0. Floating-point values are mapped directly. Neither integer nor floating-point values are clamped. The default ambient reflectance for both front-facing and back-facing materials is (0.2, 0.2, 0.2, 1.0). <br/>    |
| <span id="GL_DIFFUSE"></span><span id="gl_diffuse"></span><dl> <dt>**GL\_DIFFUSE**</dt> </dl>                                       | The params parameter contains four integer values that specify the diffuse RGBA reflectance of the material. Integer values are mapped linearly such that the most positive representable value maps to 1.0, and the most negative representable value maps to -1.0. Floating-point values are mapped directly. Neither integer nor floating-point values are clamped. The default diffuse reflectance for both front-facing and back-facing materials is (0.8, 0.8, 0.8, 1.0). <br/>    |
| <span id="GL_SPECULAR"></span><span id="gl_specular"></span><dl> <dt>**GL\_SPECULAR**</dt> </dl>                                    | The params parameter contains four integer values that specify the specular RGBA reflectance of the material. Integer values are mapped linearly such that the most positive representable value maps to 1.0, and the most negative representable value maps to -1.0. Floating-point values are mapped directly. Neither integer nor floating-point values are clamped. The default specular reflectance for both front-facing and back-facing materials is (0.0, 0.0, 0.0, 1.0). <br/>  |
| <span id="GL_EMISSION"></span><span id="gl_emission"></span><dl> <dt>**GL\_EMISSION**</dt> </dl>                                    | The params parameter contains four integer values that specify the RGBA emitted light intensity of the material. Integer values are mapped linearly such that the most positive representable value maps to 1.0, and the most negative representable value maps to -1.0. Floating-point values are mapped directly. Neither integer nor floating-point values are clamped. The default emission intensity for both front-facing and back-facing materials is (0.0, 0.0, 0.0, 1.0). <br/> |
| <span id="GL_SHININESS"></span><span id="gl_shininess"></span><dl> <dt>**GL\_SHININESS**</dt> </dl>                                 | The *param* parameter is a single integer that specifies the RGBA specular exponent of the material. Integer values are mapped directly. Only values in the range \[0, 128\] are accepted. The default specular exponent for both front-facing and back-facing materials is 0. <br/>                                                                                                                                                                                                     |
| <span id="GL_AMBIENT_AND_DIFFUSE"></span><span id="gl_ambient_and_diffuse"></span><dl> <dt>**GL\_AMBIENT\_AND\_DIFFUSE**</dt> </dl> | Equivalent to calling [**glMaterial**](glmaterial-functions.md) twice with the same parameter values, once with GL\_AMBIENT and once with GL\_DIFFUSE. <br/>                                                                                                                                                                                                                                                                                                                            |
| <span id="GL_COLOR_INDEXES"></span><span id="gl_color_indexes"></span><dl> <dt>**GL\_COLOR\_INDEXES**</dt> </dl>                    | The params parameter contains three integer values specifying the color indexes for ambient, diffuse, and specular lighting. These three values, and GL\_SHININESS, are the only material values used by the color-index mode lighting equation. Refer to [**glLightModel**](gllightmodel-functions.md) for a discussion of color-index lighting.<br/>                                                                                                                                  |



 

</dd> <dt>

*params* 
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

The [**glMaterialiv**](glmaterialf.md) function assigns values to material parameters. There are two matched sets of material parameters. One, the *front-facing* set, is used to shade points, lines, bitmaps, and all polygons (when two-sided lighting is disabled), or just front-facing polygons (when two-sided lighting is enabled). The other set, *back-facing*, is used to shade back-facing polygons only when two-sided lighting is enabled. Refer to [**glLightModel**](gllightmodel-functions.md) for details concerning one-sided and two-sided lighting calculations.

The [**glMaterialiv**](glmaterialf.md) function takes three arguments. The first, *face*, specifies whether the GL\_FRONT materials, the GL\_BACK materials, or both GL\_FRONT\_AND\_BACK materials will be modified. The second, *pname*, specifies which of several parameters in one or both sets will be modified. The third, *param*, specifies what value will be assigned to the specified parameter.

Material parameters are used in the lighting equation that is optionally applied to each vertex. The equation is discussed in [**glLightModel**](gllightmodel-functions.md).

The material parameters can be updated at any time. In particular, [**glMaterialiv**](glmaterialf.md) can be called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md). If only a single material parameter is to be changed per vertex, however, [**glColorMaterial**](glcolormaterial.md) is preferred over **glMaterialiv**.

The following function retrieves information related to [**glMaterialiv**](glmaterialf.md):

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

 

 





