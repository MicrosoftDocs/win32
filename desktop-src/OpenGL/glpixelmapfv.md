---
title: glPixelMapfv function (Gl.h)
description: The glPixelMapfv function sets up pixel transfer maps.
ms.assetid: 13403243-1ec4-4b1d-a9da-9a6693b6f9b8
keywords:
- glPixelMapfv function OpenGL
topic_type:
- apiref
api_name:
- glPixelMapfv
api_location:
- Opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glPixelMapfv function

The **glPixelMapfv** function sets up pixel transfer maps.

## Syntax


```C++
void WINAPI glPixelMapfv(
         GLenum  map,
         GLsizei mapsize,
   const GLfloat *values
);
```



## Parameters

<dl> <dt>

*map* 
</dt> <dd>

A symbolic map name. The ten maps are as follows.



| Value                                                                                                                                                                               | Meaning                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <span id="GL_PIXEL_MAP_I_TO_I"></span><span id="gl_pixel_map_i_to_i"></span><dl> <dt>**GL\_PIXEL\_MAP\_I\_TO\_I**</dt> </dl> | Maps color indexes to color indexes.<br/>       |
| <span id="GL_PIXEL_MAP_S_TO_S"></span><span id="gl_pixel_map_s_to_s"></span><dl> <dt>**GL\_PIXEL\_MAP\_S\_TO\_S**</dt> </dl> | Maps stencil indexes to stencil indexes.<br/>   |
| <span id="GL_PIXEL_MAP_I_TO_R"></span><span id="gl_pixel_map_i_to_r"></span><dl> <dt>**GL\_PIXEL\_MAP\_I\_TO\_R**</dt> </dl> | Maps color indexes to red components.<br/>      |
| <span id="GL_PIXEL_MAP_I_TO_G"></span><span id="gl_pixel_map_i_to_g"></span><dl> <dt>**GL\_PIXEL\_MAP\_I\_TO\_G**</dt> </dl> | Maps color indexes to green components.<br/>    |
| <span id="GL_PIXEL_MAP_I_TO_B"></span><span id="gl_pixel_map_i_to_b"></span><dl> <dt>**GL\_PIXEL\_MAP\_I\_TO\_B**</dt> </dl> | Maps color indexes to blue components.<br/>     |
| <span id="GL_PIXEL_MAP_I_TO_A"></span><span id="gl_pixel_map_i_to_a"></span><dl> <dt>**GL\_PIXEL\_MAP\_I\_TO\_A**</dt> </dl> | Maps color indexes to alpha components.<br/>    |
| <span id="GL_PIXEL_MAP_R_TO_R"></span><span id="gl_pixel_map_r_to_r"></span><dl> <dt>**GL\_PIXEL\_MAP\_R\_TO\_R**</dt> </dl> | Maps red components to red components.<br/>     |
| <span id="GL_PIXEL_MAP_G_TO_G"></span><span id="gl_pixel_map_g_to_g"></span><dl> <dt>**GL\_PIXEL\_MAP\_G\_TO\_G**</dt> </dl> | Maps green components to green components.<br/> |
| <span id="GL_PIXEL_MAP_B_TO_B"></span><span id="gl_pixel_map_b_to_b"></span><dl> <dt>**GL\_PIXEL\_MAP\_B\_TO\_B**</dt> </dl> | Maps blue components to blue components.<br/>   |
| <span id="GL_PIXEL_MAP_A_TO_A"></span><span id="gl_pixel_map_a_to_a"></span><dl> <dt>**GL\_PIXEL\_MAP\_A\_TO\_A**</dt> </dl> | Maps alpha components to alpha components.<br/> |



 

</dd> <dt>

*mapsize* 
</dt> <dd>

The size of the map being defined.

</dd> <dt>

*values* 
</dt> <dd>

An array of *mapsize* values.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *map* was not an accepted value.<br/>                                                                                                                                                                                |
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | *mapsize* was negative or larger than GL\_PIXEL\_MAP\_TABLE. <br/>                                                                                                                                                   |
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | *map* was GL\_PIXEL\_MAP\_I\_TO\_I, GL\_PIXEL\_MAP\_S\_TO\_S, GL\_PIXEL\_MAP\_I\_TO\_R, GL\_PIXEL\_MAP\_I\_TO\_G, GL\_PIXEL\_MAP\_I\_TO\_B, or GL\_PIXEL\_MAP\_I\_TO\_A, and *mapsize* was not a power of two. <br/> |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md). <br/>                                                                                     |



## Remarks

The **glPixelMap** function sets up translation tables, or *maps*, used by [**glCopyPixels**](glcopypixels.md), [**glCopyTexImage1D**](glcopyteximage1d.md), [**glCopyTexImage2D**](glcopyteximage2d.md), [**glCopyTexSubImage1D**](glcopytexsubimage1d.md), [**glCopyTexSubImage2D**](glcopytexsubimage2d.md), [**glDrawPixels**](gldrawpixels.md), [**glReadPixels**](glreadpixels.md), [**glTexImage1D**](glteximage1d.md), [**glTexImage2D**](glteximage2d.md), [**glTexSubImage1D**](gltexsubimage1d.md), and [**glTexSubImage2D**](gltexsubimage2d.md). Use of these maps is described completely in the [**glPixelTransfer**](glpixeltransfer.md) topic, and partly in the topics for the pixel and texture image commands. Only the specification of the maps is described in this topic.

The *map* parameter is a symbolic map name, indicating one of ten maps to set. The *mapsize* parameter specifies the number of entries in the map, and *values* is a pointer to an array of *mapsize* map values.

The entries in a map can be specified as single-precision floating-point numbers, unsigned short integers, or unsigned long integers. Maps that store color component values (all but GL\_PIXEL\_MAP\_I\_TO\_I and GL\_PIXEL\_MAP\_S\_TO\_S) retain their values in floating-point format, with unspecified mantissa and exponent sizes. Floating-point values specified by [**glPixelMapfv**](glpixelmap.md) are converted directly to the internal floating-point format of these maps, and then clamped to the range \[0,1\]. Unsigned integer values specified by **glPixelMapusv** and **glPixelMapuiv** are converted linearly such that the largest representable integer maps to 1.0, and zero maps to 0.0.

Maps that store indexes, GL\_PIXEL\_MAP\_I\_TO\_I and GL\_PIXEL\_MAP\_S\_TO\_S, retain their values in fixed-point format, with an unspecified number of bits to the right of the binary point. Floating-point values specified by [**glPixelMapfv**](glpixelmap.md) are converted directly to the internal fixed-point format of these maps. Unsigned integer values specified by **glPixelMapusv** and **glPixelMapuiv** specify integer values, with all zeros to the right of the binary point.

The following table shows the initial sizes and values for each of the maps. Maps that are indexed by either color or stencil indexes must have *mapsize* = 2 ^ *n* for some *n* or results are undefined. The maximum allowable size for each map depends on the implementation and can be determined by calling **glGet** with argument GL\_MAX\_PIXEL\_MAP\_TABLE. The single maximum applies to all maps, and it is at least 32.



| Map                      | Lookup Index  | Lookup Value  | Initial Size | Initial Value |
|--------------------------|---------------|---------------|--------------|---------------|
| GL\_PIXEL\_MAP\_I\_TO\_I | color index   | color index   | 1            | 0.0           |
| GL\_PIXEL\_MAP\_S\_TO\_S | stencil index | stencil index | 1            | 0.0           |
| GL\_PIXEL\_MAP\_I\_TO\_R | color index   | R             | 1            | 0.0           |
| GL\_PIXEL\_MAP\_I\_TO\_G | color index   | G             | 1            | 0.0           |
| GL\_PIXEL\_MAP\_I\_TO\_B | color index   | B             | 1            | 0.0           |
| GL\_PIXEL\_MAP\_I\_TO\_A | color index   | A             | 1            | 0.0           |
| GL\_PIXEL\_MAP\_R\_TO\_R | R             | R             | 1            | 0.0           |
| GL\_PIXEL\_MAP\_G\_TO\_G | G             | G             | 1            | 0.0           |
| GL\_PIXEL\_MAP\_B\_TO\_B | B             | B             | 1            | 0.0           |
| GL\_PIXEL\_MAP\_A\_TO\_A | A             | A             | 1            | 0.0           |



 

The following functions retrieve information related to **glPixelMap**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_PIXEL\_MAP\_I\_TO\_I\_SIZE

**glGet** with argument GL\_PIXEL\_MAP\_S\_TO\_S\_SIZE

**glGet** with argument GL\_PIXEL\_MAP\_I\_TO\_R\_SIZE

**glGet** with argument GL\_PIXEL\_MAP\_I\_TO\_G\_SIZE

**glGet** with argument GL\_PIXEL\_MAP\_I\_TO\_B\_SIZE

**glGet** with argument GL\_PIXEL\_MAP\_I\_TO\_A\_SIZE

**glGet** with argument GL\_PIXEL\_MAP\_R\_TO\_R\_SIZE

**glGet** with argument GL\_PIXEL\_MAP\_G\_TO\_G\_SIZE

**glGet** with argument GL\_PIXEL\_MAP\_B\_TO\_B\_SIZE

**glGet** with argument GL\_PIXEL\_MAP\_A\_TO\_A\_SIZE

**glGet** with argument GL\_MAX\_PIXEL\_MAP\_TABLE

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

[**glCopyPixels**](glcopypixels.md)
</dt> <dt>

[**glDrawPixels**](gldrawpixels.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glPixelStore**](glpixelstore-functions.md)
</dt> <dt>

[**glPixelTransfer**](glpixeltransfer.md)
</dt> <dt>

[**glReadPixels**](glreadpixels.md)
</dt> <dt>

[**glTexImage1D**](glteximage1d.md)
</dt> <dt>

[**glTexImage2D**](glteximage2d.md)
</dt> </dl>

 

 





