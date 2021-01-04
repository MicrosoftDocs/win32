---
title: glTexEnvi function (Gl.h)
description: The glTexEnvi function sets a texture environment parameter.
ms.assetid: 3f4c10c4-524c-4cce-b42b-bc72fc3b9f31
keywords:
- glTexEnvi function OpenGL
topic_type:
- apiref
api_name:
- glTexEnvi
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glTexEnvi function

The **glTexEnvi** function sets a texture environment parameter.

## Syntax


```C++
void WINAPI glTexEnvi(
   GLenum target,
   GLenum pname,
   GLint  param
);
```



## Parameters

<dl> <dt>

*target* 
</dt> <dd>

A texture environment. Must be GL\_TEXTURE\_ENV.

</dd> <dt>

*pname* 
</dt> <dd>

The symbolic name of a single-valued texture environment parameter. Must be GL\_TEXTURE\_ENV\_MODE.

</dd> <dt>

*param* 
</dt> <dd>

A single symbolic constant, one of GL\_MODULATE, GL\_DECAL, GL\_BLEND, or GL\_REPLACE.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *target* or *pname* was not one of the accepted defined values, or when *params* should have had a defined constant value (based on the value of *pname*) and did not.<br/> |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/>                                             |



## Remarks

A texture environment specifies how texture values are interpreted when a fragment is textured. The *target* parameter must be GL\_TEXTURE\_ENV. The *pname* parameter is GL\_TEXTURE\_ENV\_MODE. Three texture functions are defined: GL\_MODULATE, GL\_DECAL, and GL\_BLEND.

A texture function acts on the fragment to be textured using the texture image value that applies to the fragment (see [**glTexParameter**](gltexparameter-functions.md)) and produces an RGBA color for that fragment. The following table shows how the RGBA color is produced for each of the three texture functions that can be chosen. *C* is a triple of color values (RGB) and *A* is the associated alpha value. RGBA values extracted from a texture image are in the range \[0, 1\]. The subscript *f* refers to the incoming fragment, the subscript *t* to the texture image, the subscript *c* to the texture environment color, and subscript *v* indicates a value produced by the texture function.

A texture image can have up to four components per texture element (see [**glTexImage1D**](glteximage1d.md) and [**glTexImage2D**](glteximage2d.md)). In a one-component image, Lt indicates that single component. A two-component image uses *L?*  and *A?* . A three-component image has only a color value, *C?* . A four-component image has both a color value *C?*  and an alpha value *A?* .



<table>
<thead>
<tr class="header">
<th>Number of components</th>
<th>GL_MODULATE</th>
<th>GL_DECAL</th>
<th>GL_BLEND</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2">1${REMOVE}$<br />
</td>
<td><em>C<sub>v</sub></em> = <em>L?</em> <em>C<sub>f</sub></em></td>
<td rowspan="2">undefined${REMOVE}$<br />
</td>
<td><em>C<sub>v</sub></em> = <em>(1</em> - <em>L?</em> <em>)C<sub>f</sub></em> + <em>L?</em> <em>C<sub>c</sub></em></td>
</tr>
<tr class="even">
<td><em>A<sub>v</sub></em> = <em>A<sub>f</sub></em></td>
<td><em>A<sub>v</sub></em> = <em>A<sub>f</sub></em></td>


</tr>
<tr class="odd">
<td rowspan="2">2${REMOVE}$<br />
</td>
<td><em>C<sub>v</sub></em> = <em>L?</em> <em>C<sub>f</sub></em></td>
<td rowspan="2">undefined${REMOVE}$<br />
</td>
<td><em>C<sub>v</sub></em> = <em>(1</em> - <em>L?</em> <em>)C<sub>f</sub></em> + <em>L?</em> <em>C<sub>c</sub></em></td>
</tr>
<tr class="even">
<td><em>A<sub>v</sub></em> = <em>A<sub>f</sub></em></td>
<td><em>A<sub>v</sub></em> = <em>A<sub>f</sub></em></td>


</tr>
<tr class="odd">
<td rowspan="2">3${REMOVE}$<br />
</td>
<td><em>C<sub>v</sub></em> = <em>C?</em> <em>C<sub>f</sub></em></td>
<td><em>C<sub>v</sub></em> = <em>C?</em></td>
<td rowspan="2">undefined${REMOVE}$<br />
</td>
</tr>
<tr class="even">
<td><em>A<sub>v</sub></em> = <em>A<sub>f</sub></em> </td>
<td><em>A<sub>v</sub></em> = <em>A<sub>f</sub></em></td>


</tr>
<tr class="odd">
<td rowspan="2">4${REMOVE}$<br />
</td>
<td><em>C<sub>v</sub></em> = <em>C?</em> <em>C<sub>f</sub></em></td>
<td><em>C<sub>v</sub></em> = (1 - <em>A?</em> <em>)C<sub>f</sub></em> + <em>A?</em> <em>C?</em></td>
<td rowspan="2">undefined${REMOVE}$<br />
</td>
</tr>
<tr class="even">
<td><em>A<sub>v</sub></em> = <em>A?</em> <em>A<sub>f</sub></em> </td>
<td><em>A<sub>v</sub></em> = <em>A<sub>f</sub></em></td>


</tr>
</tbody>
</table>



 

GL\_TEXTURE\_ENV\_MODE defaults to GL\_MODULATE.

The following function retrieves information related to **glTexEnvi**:

[**glTexGetEnviv**](glgettexenviv.md)

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

[**glTexImage1D**](glteximage1d.md)
</dt> <dt>

[**glTexImage2D**](glteximage2d.md)
</dt> <dt>

[**glTexParameter**](gltexparameter-functions.md)
</dt> </dl>

 

 





