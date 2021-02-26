---
title: glGetLightiv function (Gl.h)
description: The glGetLightfv and glGetLightiv functions return light source parameter values. | glGetLightiv function (Gl.h)
ms.assetid: be4316ca-dc49-4bfa-929a-fa25f5057fde
keywords:
- glGetLightiv function OpenGL
topic_type:
- apiref
api_name:
- glGetLightiv
api_location:
- Opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glGetLightiv function

The [**glGetLightfv**](glgetlightfv.md) and **glGetLightiv** functions return light source parameter values.

## Syntax


```C++
void WINAPI glGetLightiv(
   GLenum light,
   GLenum pname,
   GLint  *params
);
```



## Parameters

<dl> <dt>

*light* 
</dt> <dd>

A light source. The number of possible lights depends on the implementation, but at least eight lights are supported. They are identified by symbolic names of the form GL\_LIGHT *i* where 0 = *i* < GL\_MAX\_LIGHTS.

</dd> <dt>

*pname* 
</dt> <dd>

A light source parameter for *light*. The following symbolic names are accepted.



| Value                                                                                                                                                                                           | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_AMBIENT"></span><span id="gl_ambient"></span><dl> <dt>**GL\_AMBIENT**</dt> </dl>                                            | The *params* parameter returns four integer or floating-point values representing the ambient intensity of the light source. Integer values, when requested, are linearly mapped from the internal floating-point representation such that 1.0 maps to the most positive representable integer value, and -1.0 maps to the most negative representable integer value. If the internal value is outside the range \[-1,1\], the corresponding integer return value is undefined.<br/>                                                                                                                                                                  |
| <span id="GL_DIFFUSE"></span><span id="gl_diffuse"></span><dl> <dt>**GL\_DIFFUSE**</dt> </dl>                                            | The *params* parameter returns four integer or floating-point values representing the diffuse intensity of the light source. Integer values, when requested, are linearly mapped from the internal floating-point representation such that 1.0 maps to the most positive representable integer value, and -1.0 maps to the most negative representable integer value. If the internal value is outside the range \[-1,1\], the corresponding integer return value is undefined.<br/>                                                                                                                                                                  |
| <span id="GL_SPECULAR"></span><span id="gl_specular"></span><dl> <dt>**GL\_SPECULAR**</dt> </dl>                                         | The *params* parameter returns four integer or floating-point values representing the specular intensity of the light source. Integer values, when requested, are linearly mapped from the internal floating-point representation such that 1.0 maps to the most positive representable integer value, and -1.0 maps to the most negative representable integer value. If the internal value is outside the range \[-1,1\], the corresponding integer return value is undefined.<br/>                                                                                                                                                                 |
| <span id="GL_POSITION"></span><span id="gl_position"></span><dl> <dt>**GL\_POSITION**</dt> </dl>                                         | The *params* parameter returns four integer or floating-point values representing the position of the light source. Integer values, when requested, are computed by rounding the internal floating-point values to the nearest integer value. The returned values are those maintained in eye coordinates. They will not be equal to the values specified using [**glLight**](gllight-functions.md), unless the modelview matrix was identified at the time **glLight** was called.<br/>                                                                                                                                                             |
| <span id="GL_SPOT_DIRECTION"></span><span id="gl_spot_direction"></span><dl> <dt>**GL\_SPOT\_DIRECTION**</dt> </dl>                      | The *params* parameter returns three integer or floating-point values representing the direction of the light source. Integer values, when requested, are computed by rounding the internal floating-point values to the nearest integer value. The returned values are those maintained in eye coordinates. They will not be equal to the values specified using **glLight**, unless the modelview matrix was identified at the time **glLight** was called. Although spot direction is normalized before being used in the lighting equation, the returned values are the transformed versions of the specified values prior to normalization.<br/> |
| <span id="GL_SPOT_EXPONENT"></span><span id="gl_spot_exponent"></span><dl> <dt>**GL\_SPOT\_EXPONENT**</dt> </dl>                         | The *params* parameter returns a single integer or floating-point value representing the spot exponent of the light. An integer value, when requested, is computed by rounding the internal floating-point representation to the nearest integer.<br/>                                                                                                                                                                                                                                                                                                                                                                                                |
| <span id="GL_SPOT_CUTOFF"></span><span id="gl_spot_cutoff"></span><dl> <dt>**GL\_SPOT\_CUTOFF**</dt> </dl>                               | The *params* parameter returns a single integer or floating-point value representing the spot cutoff angle of the light. An integer value, when requested, is computed by rounding the internal floating-point representation to the nearest integer.<br/>                                                                                                                                                                                                                                                                                                                                                                                            |
| <span id="GL_CONSTANT_ATTENUATION"></span><span id="gl_constant_attenuation"></span><dl> <dt>**GL\_CONSTANT\_ATTENUATION**</dt> </dl>    | The *params* parameter returns a single integer or floating-point value representing the constant (not distance-related) attenuation of the light. An integer value, when requested, is computed by rounding the internal floating-point representation to the nearest integer.<br/>                                                                                                                                                                                                                                                                                                                                                                  |
| <span id="GL_LINEAR_ATTENUATION"></span><span id="gl_linear_attenuation"></span><dl> <dt>**GL\_LINEAR\_ATTENUATION**</dt> </dl>          | The *params* parameter returns a single integer or floating-point value representing the linear attenuation of the light. An integer value, when requested, is computed by rounding the internal floating-point representation to the nearest integer.<br/>                                                                                                                                                                                                                                                                                                                                                                                           |
| <span id="GL_QUADRATIC_ATTENUATION"></span><span id="gl_quadratic_attenuation"></span><dl> <dt>**GL\_QUADRATIC\_ATTENUATION**</dt> </dl> | The *params* parameter returns a single integer or floating-point value representing the quadratic attenuation of the light. An integer value, when requested, is computed by rounding the internal floating-point representation to the nearest integer.<br/>                                                                                                                                                                                                                                                                                                                                                                                        |



 

</dd> <dt>

*params* 
</dt> <dd>

Returns the requested data.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The **glGetLight** function returns in *params* the value or values of a light source parameter. The *light* parameter names the light and is a symbolic name of the form GL\_LIGHT*i* for 0 = *i* < GL\_MAX\_LIGHTS, where GL\_MAX\_LIGHTS is an implementation-dependent constant that is greater than or equal to eight. The *pname* parameter specifies one of ten light source parameters, again by symbolic name.

It is always the case that GL\_LIGHT*i* = GL\_LIGHT0 + *i*.

If an error is generated, no change is made to the contents of *params*.

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

[**glLight**](gllight-functions.md)
</dt> </dl>

 

 





