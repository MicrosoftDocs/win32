---
title: glPushAttrib function (Gl.h)
description: Pushes the attribute stack.
ms.assetid: 3c7b93cc-2112-4771-b422-a244821447e5
keywords:
- glPushAttrib function OpenGL
topic_type:
- apiref
api_name:
- glPushAttrib
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glPushAttrib function

Pushes the attribute stack.

## Syntax


```C++
void WINAPI glPushAttrib(
   GLbitfield mask
);
```



## Parameters

<dl> <dt>

*mask* 
</dt> <dd>

A mask that indicates which attributes to save. The symbolic mask constants and their associated OpenGL state are as follows (the indented paragraphs list which attributes are saved):

<dl> <dt>

<span id="GL_ACCUM_BUFFER_BIT_"></span><span id="gl_accum_buffer_bit_"></span>GL\_ACCUM\_BUFFER\_BIT 
</dt> <dd>

Accumulation buffer clear value

</dd> <dt>

<span id="GL_COLOR_BUFFER_BIT"></span><span id="gl_color_buffer_bit"></span>GL\_COLOR\_BUFFER\_BIT
</dt> <dd>

GL\_ALPHA\_TEST enable bit

Alpha test function and reference value

GL\_BLEND enable bit

Blending source and destination functions

GL\_DITHER enable bit

GL\_DRAW\_BUFFER setting

GL\_LOGIC\_OP enable bit

Logic op function

Color-mode and index-mode clear values

Color-mode and index-mode writemasks

</dd> <dt>

<span id="GL_CURRENT_BIT"></span><span id="gl_current_bit"></span>GL\_CURRENT\_BIT
</dt> <dd>

Current RGBA color

Current color index

Current normal vector

Current texture coordinates

Current raster position GL\_CURRENT\_RASTER\_POSITION\_VALID flag

RGBA color associated with current raster position

Color index associated with current raster position

Texture coordinates associated with current raster position

GL\_EDGE\_FLAG flag

</dd> <dt>

<span id="GL_DEPTH_BUFFER_BIT"></span><span id="gl_depth_buffer_bit"></span>GL\_DEPTH\_BUFFER\_BIT
</dt> <dd>

GL\_DEPTH\_TEST enable bit

Depth buffer test function

Depth buffer clear value

GL\_DEPTH\_WRITEMASK enable bit

</dd> <dt>

<span id="GL_ENABLE_BIT"></span><span id="gl_enable_bit"></span>GL\_ENABLE\_BIT
</dt> <dd>

GL\_ALPHA\_TEST flag

GL\_AUTO\_NORMAL flag

GL\_BLEND flag

Enable bits for the user-definable clipping planes

GL\_COLOR\_MATERIAL

GL\_CULL\_FACE flag

GL\_DEPTH\_TEST flag

GL\_DITHER flag

GL\_FOG flag

GL\_LIGHT*i* where 0 <= *i* < GL\_MAX\_LIGHTS

GL\_LIGHTING flag

GL\_LINE\_SMOOTH flag

GL\_LINE\_STIPPLE flag

GL\_COLOR\_LOGIC\_OP flag

GL\_INDEX\_LOGIC\_OP flag

GL\_MAP1\_x where x is a map type

GL\_MAP2\_x where x is a map type

GL\_NORMALIZE flag

GL\_POINT\_SMOOTH flag

GL\_POLYGON\_OFFSET\_LINE flag

GL\_POLYGON\_OFFSET\_FILL flag

GL\_POLYGON\_OFFSET\_POINT flag

GL\_POLYGON\_SMOOTH flag

GL\_POLYGON\_STIPPLE flag

GL\_SCISSOR\_TEST flag

GL\_STENCIL\_TEST flag

GL\_TEXTURE\_1D flag

GL\_TEXTURE\_2D flag

Flags GL\_TEXTURE\_GEN\_x where x is S, T, R, or Q

</dd> <dt>

<span id="GL_EVAL_BIT"></span><span id="gl_eval_bit"></span>GL\_EVAL\_BIT
</dt> <dd>

GL\_MAP1\_x enable bits, where x is a map type

GL\_MAP2\_x enable bits, where x is a map type

1-D grid endpoints and divisions

2-D grid endpoints and divisions

GL\_AUTO\_NORMAL enable bit

</dd> <dt>

<span id="GL_FOG_BIT"></span><span id="gl_fog_bit"></span>GL\_FOG\_BIT
</dt> <dd>

GL\_FOG enable flag

Fog color

Fog density

Linear fog start

Linear fog end

Fog index

GL\_FOG\_MODE value

</dd> <dt>

<span id="GL_HINT_BIT"></span><span id="gl_hint_bit"></span>GL\_HINT\_BIT
</dt> <dd>

GL\_PERSPECTIVE\_CORRECTION\_HINT setting

GL\_POINT\_SMOOTH\_HINT setting

GL\_LINE\_SMOOTH\_HINT setting

GL\_POLYGON\_SMOOTH\_HINT setting

GL\_FOG\_HINT setting

</dd> <dt>

<span id="GL_LIGHTING_BIT"></span><span id="gl_lighting_bit"></span>GL\_LIGHTING\_BIT
</dt> <dd>

GL\_COLOR\_MATERIAL enable bit

GL\_COLOR\_MATERIAL\_FACE value

Color material parameters that are tracking the current color

Ambient scene color

GL\_LIGHT\_MODEL\_LOCAL\_VIEWER value

GL\_LIGHT\_MODEL\_TWO\_SIDE setting

GL\_LIGHTING enable bit

Enable bit for each light

Ambient, diffuse, and specular intensity for each light

Direction, position, exponent, and cutoff angle for each light

Constant, linear, and quadratic attenuation factors for each light

Ambient, diffuse, specular, and emissive color for each material

Ambient, diffuse, and specular color indexes for each material

Specular exponent for each material GL\_SHADE\_MODEL setting

</dd> <dt>

<span id="GL_LINE_BIT_"></span><span id="gl_line_bit_"></span>GL\_LINE\_BIT 
</dt> <dd>

GL\_LINE\_SMOOTH flag

GL\_LINE\_STIPPLE enable bit

Line stipple pattern and repeat counter

Line width

</dd> <dt>

<span id="GL_LIST_BIT"></span><span id="gl_list_bit"></span>GL\_LIST\_BIT
</dt> <dd>

GL\_LIST\_BASE setting

</dd> <dt>

<span id="GL_PIXEL_MODE_BIT"></span><span id="gl_pixel_mode_bit"></span>GL\_PIXEL\_MODE\_BIT
</dt> <dd>

GL\_RED\_BIAS and GL\_RED\_SCALE settings

GL\_GREEN\_BIAS and GL\_GREEN\_SCALE values

GL\_BLUE\_BIAS and GL\_BLUE\_SCALE

GL\_ALPHA\_BIAS and GL\_ALPHA\_SCALE

GL\_DEPTH\_BIAS and GL\_DEPTH\_SCALE

GL\_INDEX\_OFFSET and GL\_INDEX\_SHIFT values

GL\_MAP\_COLOR and GL\_MAP\_STENCIL flags

GL\_ZOOM\_X and GL\_ZOOM\_Y factors

GL\_READ\_BUFFER setting

</dd> <dt>

<span id="GL_POINT_BIT"></span><span id="gl_point_bit"></span>GL\_POINT\_BIT
</dt> <dd>

GL\_POINT\_SMOOTH flag

Point size

</dd> <dt>

<span id="GL_POLYGON_BIT"></span><span id="gl_polygon_bit"></span>GL\_POLYGON\_BIT
</dt> <dd>

GL\_CULL\_FACE enable bit

GL\_CULL\_FACE\_MODE value

GL\_FRONT\_FACE indicator

GL\_POLYGON\_MODE setting

GL\_POLYGON\_SMOOTH flag

GL\_POLYGON\_STIPPLE enable bit

GL\_POLYGON\_OFFSET\_FILL flag

GL\_POLYGON\_OFFSET\_LINE flag

GL\_POLYGON\_OFFSET\_POINT flag

GL\_POLYGON\_OFFSET\_FACTOR

GL\_POLYGON\_OFFSET\_UNITS

</dd> <dt>

<span id="GL_POLYGON_STIPPLE_BIT"></span><span id="gl_polygon_stipple_bit"></span>GL\_POLYGON\_STIPPLE\_BIT
</dt> <dd>

Polygon stipple image

</dd> <dt>

<span id="GL_SCISSOR_BIT"></span><span id="gl_scissor_bit"></span>GL\_SCISSOR\_BIT
</dt> <dd>

GL\_SCISSOR\_TEST flag

Scissor box

</dd> <dt>

<span id="GL_STENCIL_BUFFER_BIT"></span><span id="gl_stencil_buffer_bit"></span>GL\_STENCIL\_BUFFER\_BIT
</dt> <dd>

GL\_STENCIL\_TEST enable bit

Stencil function and reference value

Stencil value mask

Stencil fail, pass, and depth buffer pass actions

Stencil buffer clear value

Stencil buffer writemask

</dd> <dt>

<span id="GL_TEXTURE_BIT"></span><span id="gl_texture_bit"></span>GL\_TEXTURE\_BIT
</dt> <dd>

Enable bits for the four texture coordinates

Border color for each texture image

Minification function for each texture image

Magnification function for each texture image

Texture coordinates and wrap mode for each texture image

Color and mode for each texture environment

Enable bits GL\_TEXTURE\_GEN\_*x*; *x* is S, T, R, and Q

GL\_TEXTURE\_GEN\_MODE setting for S, T, R, and Q

glTexGen plane equations for S, T, R, and Q

</dd> <dt>

<span id="GL_TRANSFORM_BIT"></span><span id="gl_transform_bit"></span>GL\_TRANSFORM\_BIT
</dt> <dd>

Coefficients of the six clipping planes

Enable bits for the user-definable clipping planes

GL\_MATRIX\_MODE value

GL\_NORMALIZE flag

</dd> <dt>

<span id="GL_VIEWPORT_BIT"></span><span id="gl_viewport_bit"></span>GL\_VIEWPORT\_BIT
</dt> <dd>

Depth range (near and far)

Viewport origin and extent

</dd> </dl> </dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_STACK\_OVERFLOW**</dt> </dl>    | The function was called while the attribute stack was full.<br/>                                                                |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glPushAttrib** function takes one argument, a mask that indicates which groups of state variables to save on the attribute stack. Symbolic constants are used to set bits in the mask. The mask parameter is typically constructed by applying the logical **OR** operation to several of these constants. You can use the special mask GL\_ALL\_ATTRIB\_BITS to save all stackable states.

The [**glPopAttrib**](glpopattrib.md) function restores the values of the state variables saved with the last **glPushAttrib** command. Those not saved are left unchanged.

It is an error to push attributes onto a full stack, or to pop attributes off an empty stack. In either case, the error flag is set and no other change is made to the OpenGL state.

Initially, the attribute stack is empty.

Not all values for the OpenGL state can be saved on the attribute stack. For example, you cannot save pixel pack and unpack state, render mode state, and select and feedback state.

The depth of the attribute stack depends on the implementation, but it must be at least 16.

The following functions retrieve information related to **glPushAttrib** and [**glPopAttrib**](glpopattrib.md):

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_ATTRIB\_STACK\_DEPTH

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_MAX\_ATTRIB\_STACK\_DEPTH

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

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**glGetClipPlane**](glgetclipplane.md)
</dt> <dt>

[**glGetError**](glgeterror.md)
</dt> <dt>

[**glGetLight**](glgetlight.md)
</dt> <dt>

[**glGetMap**](glgetmap.md)
</dt> <dt>

[**glGetMaterial**](glgetmaterial.md)
</dt> <dt>

[**glGetPixelMap**](glgetpixelmap.md)
</dt> <dt>

[**glGetPolygonStipple**](glgetpolygonstipple.md)
</dt> <dt>

[**glGetString**](glgetstring.md)
</dt> <dt>

[**glGetTexEnv**](glgettexenv.md)
</dt> <dt>

[**glGetTexGen**](glgettexgen.md)
</dt> <dt>

[**glGetTexImage**](glgetteximage.md)
</dt> <dt>

[**glGetTexLevelParameter**](glgettexlevelparameter.md)
</dt> <dt>

[**glGetTexParameter**](glgettexparameter.md)
</dt> <dt>

[**glIsEnabled**](glisenabled.md)
</dt> </dl>

 

 





