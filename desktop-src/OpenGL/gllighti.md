---
title: glLighti function (Gl.h)
description: The glLighti function returns light source parameter values.
ms.assetid: 4fa5e604-d45d-412e-a08c-c38e0836596f
keywords:
- glLighti function OpenGL
topic_type:
- apiref
api_name:
- glLighti
api_location:
- Opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glLighti function

The **glLighti** function returns light source parameter values.

## Syntax


```C++
void WINAPI glLighti(
   GLenum light,
   GLenum pname,
   GLint  param
);
```



## Parameters

<dl> <dt>

*light* 
</dt> <dd>

The identifier of a light. The number of possible lights depends on the implementation, but at least eight lights are supported. They are identified by symbolic names of the form GL\_LIGHT*i* where *i* is a value: 0 to GL\_MAX\_LIGHTS - 1.

</dd> <dt>

*pname* 
</dt> <dd>

A single-valued light source parameter for *light*. The following symbolic names are accepted.



| Value                                                                                                                                                                                                                                                                                                                                               | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_SPOT_EXPONENT"></span><span id="gl_spot_exponent"></span><dl> <dt>**GL\_SPOT\_EXPONENT**</dt> </dl>                                                                                                                                                                             | The *param* parameter is a single integer value that specifies the intensity distribution of the light. Integer and floating-point values are mapped directly. Only values in the range \[0, 128\] are accepted. <br/> Effective light intensity is attenuated by the cosine of the angle between the direction of the light and the direction from the light to the vertex being lighted, raised to the power of the spot exponent. Thus, higher spot exponents result in a more focused light source, regardless of the spot cutoff angle. The default spot exponent is 0, resulting in uniform light distribution.<br/> |
| <span id="GL_SPOT_CUTOFF"></span><span id="gl_spot_cutoff"></span><dl> <dt>**GL\_SPOT\_CUTOFF**</dt> </dl>                                                                                                                                                                                   | The *param* parameter is a single integer value that specifies the maximum spread angle of a light source. Integer and floating-point values are mapped directly. Only values in the range \[0, 90\], and the special value 180, are accepted. <br/> If the angle between the direction of the light and the direction from the light to the vertex being lighted is greater than the spot cutoff angle, then the light is completely masked. Otherwise, its intensity is controlled by the spot exponent and the attenuation factors. The default spot cutoff is 180, resulting in uniform light distribution.<br/>       |
| <span id="GL_CONSTANT_ATTENUATION__GL_LINEAR_ATTENUATION__GL_QUADRATIC_ATTENUATION"></span><span id="gl_constant_attenuation__gl_linear_attenuation__gl_quadratic_attenuation"></span><dl> <dt>**GL\_CONSTANT\_ATTENUATION, GL\_LINEAR\_ATTENUATION, GL\_QUADRATIC\_ATTENUATION**</dt> </dl> | The *param* parameter is a single integer value that specifies one of the three light attenuation factors. Integer and floating-point values are mapped directly. Only nonnegative values are accepted. <br/> If the light is positional, rather than directional, its intensity is attenuated by the reciprocal of the sum of: the constant factor, the linear factor multiplied by the distance between the light and the vertex being lighted, and the quadratic factor multiplied by the square of the same distance. The default attenuation factors are (1,0,0), resulting in no attenuation.<br/>                   |



 

</dd> <dt>

*param* 
</dt> <dd>

Specifies the value that parameter *pname* of light source *light* will be set to.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *light* or *pname* was not an accepted value.<br/>                                                                                                                                                                  |
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | A spot exponent value was specified outside the range \[0, 128\], or spot cutoff was specified outside the range \[0, 90\] (except for the special value 180), or a negative attenuation factor was specified.<br/> |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/>                                                                                     |



## Remarks

The **glLighti** function sets the value or values of individual light source parameters. The *light* parameter names the light and is a symbolic name of the form GL\_LIGHT*i*, where 0 = *i* < GL\_MAX\_LIGHTS.

The *pname* parameter specifies one of the light source parameters, again by symbolic name. The *param* parameter is either a single value or a pointer to an array that contains the new values.

Lighting calculation is enabled and disabled using [**glEnable**](glenable.md) and [**glDisable**](gldisable.md) with argument GL\_LIGHTING. When lighting is enabled, light sources that are enabled contribute to the lighting calculation. Light source *i* is enabled and disabled using **glEnable** and **glDisable** with argument GL\_LIGHT*i*.

It is always the case that GL\_LIGHT*i* = GL\_LIGHT0 + *i*.

The following functions retrieve information related to the **glLighti** function:

[**glGetLight**](glgetlight.md)

[**glIsEnabled**](glisenabled.md) with argument GL\_LIGHTING

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

[**glColorMaterial**](glcolormaterial.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glLightModel**](gllightmodel-functions.md)
</dt> <dt>

[**glMaterial**](glmaterial-functions.md)
</dt> </dl>

 

 





