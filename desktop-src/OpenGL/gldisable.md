---
title: glDisable function (Gl.h)
description: The glEnable and glDisable functions enable or disable OpenGL capabilities. | glDisable function (Gl.h)
ms.assetid: 094f730e-5e2b-485e-8d9d-fee2902d3d5f
keywords:
- glDisable function OpenGL
topic_type:
- apiref
api_name:
- glDisable
api_location:
- Opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glDisable function

The [**glEnable**](glenable.md) and **glDisable** functions enable or disable OpenGL capabilities.

## Syntax


```C++
void WINAPI glDisable(
   GLenum cap
);
```



## Parameters

<dl> <dt>

*cap* 
</dt> <dd>

A symbolic constant indicating an OpenGL capability.

For discussion of the values *cap* can take, see the following Remarks section.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *cap* was not one of the values listed in the preceding Remarks section.<br/>                                                   |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The [**glEnable**](glenable.md) and **glDisable** functions enable and disable various OpenGL graphics capabilities. Use [**glIsEnabled**](glisenabled.md) or [**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) to determine the current setting of any capability.

Both [**glEnable**](glenable.md) and **glDisable** take a single argument, *cap*, which can assume one of the following values:



| Value                       | Meaning                                                                                                                                                                                                                                                     |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GL\_ALPHA\_TEST             | If enabled, do alpha testing. See [**glAlphaFunc**](glalphafunc.md).                                                                                                                                                                                       |
| GL\_AUTO\_NORMAL            | If enabled, compute surface normal vectors analytically when either GL\_MAP2\_VERTEX\_3 or GL\_MAP2\_VERTEX\_4 has generated vertices. See [**glMap2**](glmap2.md).                                                                                        |
| GL\_BLEND                   | If enabled, blend the incoming RGBA color values with the values in the color buffers. See [**glBlendFunc**](glblendfunc.md).                                                                                                                              |
| GL\_CLIP\_PLANE*i*          | If enabled, clip geometry against user-defined clipping plane *i*. See [**glClipPlane**](glclipplane.md).                                                                                                                                                  |
| GL\_COLOR\_LOGIC\_OP        | If enabled, apply the current logical operation to the incoming RGBA color and color buffer values. See [**glLogicOp**](gllogicop.md).                                                                                                                     |
| GL\_COLOR\_MATERIAL         | If enabled, have one or more material parameters track the current color. See [**glColorMaterial**](glcolormaterial.md).                                                                                                                                   |
| GL\_CULL\_FACE              | If enabled, cull polygons based on their winding in window coordinates. See [**glCullFace**](glcullface.md).                                                                                                                                               |
| GL\_DEPTH\_TEST             | If enabled, do depth comparisons and update the depth buffer. See [**glDepthFunc**](gldepthfunc.md) and [**glDepthRange**](gldepthrange.md).                                                                                                              |
| GL\_DITHER                  | If enabled, dither color components or indexes before they are written to the color buffer.                                                                                                                                                                 |
| GL\_FOG                     | If enabled, blend a fog color into the post-texturing color. See [**glFog**](glfog.md).                                                                                                                                                                    |
| GL\_INDEX\_LOGIC\_OP        | If enabled, apply the current logical operation to the incoming index and color buffer indices. See [**glLogicOp**](gllogicop.md).                                                                                                                         |
| GL\_LIGHT*i*                | If enabled, include light *i* in the evaluation of the lighting equation. See [**glLightModel**](gllightmodel-functions.md) and [**glLight**](gllight-functions.md).                                                                                      |
| GL\_LIGHTING                | If enabled, use the current lighting parameters to compute the vertex color or index. If disabled, associate the current color or index with each vertex. See [**glMaterial**](glmaterial-functions.md), **glLightModel**, and **glLight**.                |
| GL\_LINE\_SMOOTH            | If enabled, draw lines with correct filtering. If disabled, draw aliased lines. See [**glLineWidth**](gllinewidth.md).                                                                                                                                     |
| GL\_LINE\_STIPPLE           | If enabled, use the current line stipple pattern when drawing lines. See [**glLineStipple**](gllinestipple.md).                                                                                                                                            |
| GL\_LOGIC\_OP               | If enabled, apply the currently selected logical operation to the incoming and color-buffer indexes. See [**glLogicOp**](gllogicop.md).                                                                                                                    |
| GL\_MAP1\_COLOR\_4          | If enabled, calls to [**glEvalCoord1**](glevalcoord-functions.md), [**glEvalMesh1**](glevalmesh-functions.md), and [**glEvalPoint1**](glevalpoint.md) generate RGBA values. See also [**glMap1**](glmap1.md).                                           |
| GL\_MAP1\_INDEX             | If enabled, calls to **glEvalCoord1**, **glEvalMesh1**, and **glEvalPoint1** generate color indexes. See also **glMap1**.                                                                                                                                   |
| GL\_MAP1\_NORMAL            | If enabled, calls to [**glEvalCoord1**](glevalcoord-functions.md), [**glEvalMesh1**](glevalmesh-functions.md), and [**glEvalPoint1**](glevalpoint.md) generate normals. See also [**glMap1**](glmap1.md).                                               |
| GL\_MAP1\_TEXTURE\_COORD\_1 | If enabled, calls to **glEvalCoord1**, **glEvalMesh1**, and **glEvalPoint1** generate *s* texture coordinates. See also **glMap1**.                                                                                                                         |
| GL\_MAP1\_TEXTURE\_COORD\_2 | If enabled, calls to [**glEvalCoord1**](glevalcoord-functions.md), [**glEvalMesh1**](glevalmesh-functions.md), and [**glEvalPoint1**](glevalpoint.md) generate *s* and *t* texture coordinates. See also [**glMap1**](glmap1.md).                       |
| GL\_MAP1\_TEXTURE\_COORD\_3 | If enabled, calls to **glEvalCoord1**, **glEvalMesh1**, and **glEvalPoint1** generate *s*, *t*, and *r* texture coordinates. See also **glMap1**.                                                                                                           |
| GL\_MAP1\_TEXTURE\_COORD\_4 | If enabled, calls to [glEvalCoord1](glevalcoord-functions.md), [glEvalMesh1](glevalmesh-functions.md), and [**glEvalPoint1**](glevalpoint.md) generate *s*, *t*, *r*, and *q* texture coordinates. See also [**glMap1**](glmap1.md).                    |
| GL\_MAP1\_VERTEX\_3         | If enabled, calls to **glEvalCoord1**, **glEvalMesh1**, and **glEvalPoint1** generate *x*, *y*, and *z* vertex coordinates. See also **glMap1**.                                                                                                            |
| GL\_MAP1\_VERTEX\_4         | If enabled, calls to [**glEvalCoord1**](glevalcoord-functions.md), [**glEvalMesh1**](glevalmesh-functions.md), and [**glEvalPoint1**](glevalpoint.md) generate homogeneous *x*, *y*, *z*, and *w* vertex coordinates. See also [**glMap1**](glmap1.md). |
| GL\_MAP2\_COLOR\_4          | If enabled, calls to [**glEvalCoord2**](glevalcoord-functions.md), [**glEvalMesh2**](glevalmesh-functions.md), and [**glEvalPoint2**](glevalpoint.md) generate RGBA values. See also [**glMap2**](glmap2.md).                                           |
| GL\_MAP2\_INDEX             | If enabled, calls to **glEvalCoord2**, **glEvalMesh2**, and **glEvalPoint2** generate color indexes. See also **glMap2**.                                                                                                                                   |
| GL\_MAP2\_NORMAL            | If enabled, calls to [**glEvalCoord2**](glevalcoord-functions.md), [**glEvalMesh2**](glevalmesh-functions.md), and [**glEvalPoint2**](glevalpoint.md) generate normals. See also [**glMap2**](glmap2.md).                                               |
| GL\_MAP2\_TEXTURE\_COORD\_1 | If enabled, calls to **glEvalCoord2**, **glEvalMesh2**, and **glEvalPoint2** generate *s* texture coordinates. See also **glMap2**.                                                                                                                         |
| GL\_MAP2\_TEXTURE\_COORD\_2 | If enabled, calls to [**glEvalCoord2**](glevalcoord-functions.md), [**glEvalMesh2**](glevalmesh-functions.md), and [**glEvalPoint2**](glevalpoint.md) generate *s* and *t* texture coordinates. See also [**glMap2**](glmap2.md).                       |
| GL\_MAP2\_TEXTURE\_COORD\_3 | If enabled, calls to **glEvalCoord2**, **glEvalMesh2**, and **glEvalPoint2** generate *s*, *t*, and *r* texture coordinates. See also **glMap2**.                                                                                                           |
| GL\_MAP2\_TEXTURE\_COORD\_4 | If enabled, calls to [**glEvalCoord2**](glevalcoord-functions.md), [**glEvalMesh2**](glevalmesh-functions.md), and [**glEvalPoint2**](glevalpoint.md) generate *s*, *t*, *r*, and *q* texture coordinates. See also [**glMap2**](glmap2.md).            |
| GL\_MAP2\_VERTEX\_3         | If enabled, calls to **glEvalCoord2**, **glEvalMesh2**, and **glEvalPoint2** generate *x*, *y*, and *z* vertex coordinates. See also **glMap2**.                                                                                                            |
| GL\_MAP2\_VERTEX\_4         | If enabled, calls to [**glEvalCoord2**](glevalcoord-functions.md), [**glEvalMesh2**](glevalmesh-functions.md), and [**glEvalPoint2**](glevalpoint.md) generate homogeneous *x*, *y*, *z*, and *w* vertex coordinates. See also [**glMap2**](glmap2.md). |
| GL\_NORMALIZE               | If enabled, normal vectors specified with **glNormal** are scaled to unit length after transformation. See [**glNormal**](glnormal-functions.md).                                                                                                          |
| GL\_POINT\_SMOOTH           | If enabled, draw points with proper filtering. If disabled, draw aliased points. See [**glPointSize**](glpointsize.md).                                                                                                                                    |
| GL\_POLYGON\_OFFSET\_FILL   | If enabled, and if the polygon is rendered in GL\_FILL mode, an offset is added to depth values of a polygon's fragments before the depth comparison is performed. See [**glPolygonOffset**](glpolygonoffset.md)**.**                                      |
| GL\_POLYGON\_OFFSET\_LINE   | If enabled, and if the polygon is rendered in GL\_LINE mode, an offset is added to depth values of a polygon's fragments before the depth comparison is performed. See **glPolygonOffset**.                                                                 |
| GL\_POLYGON\_OFFSET\_POINT  | If enabled, an offset is added to depth values of a polygon's fragments before the depth comparison is performed, if the polygon is rendered in GL\_POINT mode. See [**glPolygonOffset**](glpolygonoffset.md).                                             |
| GL\_POLYGON\_SMOOTH         | If enabled, draw polygons with proper filtering. If disabled, draw aliased polygons. See [**glPolygonMode**](glpolygonmode.md).                                                                                                                            |
| GL\_POLYGON\_STIPPLE        | If enabled, use the current polygon stipple pattern when rendering polygons. See [**glPolygonStipple**](glpolygonstipple.md).                                                                                                                              |
| GL\_SCISSOR\_TEST           | If enabled, discard fragments that are outside the scissor rectangle. See [**glScissor**](glscissor.md).                                                                                                                                                   |
| GL\_STENCIL\_TEST           | If enabled, do stencil testing and update the stencil buffer. See [**glStencilFunc**](glstencilfunc.md) and [**glStencilOp**](glstencilop.md).                                                                                                            |
| GL\_TEXTURE\_1D             | If enabled, one-dimensional texturing is performed (unless two-dimensional texturing is also enabled). See [**glTexImage1D**](glteximage1d.md).                                                                                                            |
| GL\_TEXTURE\_2D             | If enabled, two-dimensional texturing is performed. See [**glTexImage2D**](glteximage2d.md).                                                                                                                                                               |
| GL\_TEXTURE\_GEN\_Q         | If enabled, the *q* texture coordinate is computed using the texture-generation function defined with [**glTexGen**](gltexgen-functions.md). Otherwise, the current *q* texture coordinate is used.                                                        |
| GL\_TEXTURE\_GEN\_R         | If enabled, the *r* texture coordinate is computed using the texture generation function defined with [**glTexGen**](gltexgen-functions.md). If disabled, the current *r* texture coordinate is used.                                                      |
| GL\_TEXTURE\_GEN\_S         | If enabled, the *s* texture coordinate is computed using the texture generation function defined with **glTexGen**. If disabled, the current *s* texture coordinate is used.                                                                                |
| GL\_TEXTURE\_GEN\_T         | If enabled, the *t* texture coordinate is computed using the texture generation function defined with [**glTexGen**](gltexgen-functions.md). If disabled, the current *t* texture coordinate is used.                                                      |



 

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

[**glAlphaFunc**](glalphafunc.md)
</dt> <dt>

[**glArrayElement**](glarrayelement.md)
</dt> <dt>

[**glBegin**](glbegin.md)
</dt> <dt>

[**glBlendFunc**](glblendfunc.md)
</dt> <dt>

[**glClipPlane**](glclipplane.md)
</dt> <dt>

[**glColorMaterial**](glcolormaterial.md)
</dt> <dt>

[**glColorPointer**](glcolorpointer.md)
</dt> <dt>

[**glCullFace**](glcullface.md)
</dt> <dt>

[**glDepthFunc**](gldepthfunc.md)
</dt> <dt>

[**glDepthRange**](gldepthrange.md)
</dt> <dt>

[**glDrawArrays**](gldrawarrays.md)
</dt> <dt>

[**glEdgeFlagPointer**](gledgeflagpointer.md)
</dt> <dt>

[**glEnable**](glenable.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glEvalCoord1**](glevalcoord-functions.md)
</dt> <dt>

[**glEvalMesh1**](glevalmesh-functions.md)
</dt> <dt>

[**glEvalPoint1**](glevalpoint.md)
</dt> <dt>

[**glFog**](glfog.md)
</dt> <dt>

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**glIndexPointer**](glindexpointer.md)
</dt> <dt>

[**glIsEnabled**](glisenabled.md)
</dt> <dt>

[**glLight**](gllight-functions.md)
</dt> <dt>

[**glLightModel**](gllightmodel-functions.md)
</dt> <dt>

[**glLineWidth**](gllinewidth.md)
</dt> <dt>

[**glLineStipple**](gllinestipple.md)
</dt> <dt>

[**glLogicOp**](gllogicop.md)
</dt> <dt>

[**glMap1**](glmap1.md)
</dt> <dt>

[**glMap2**](glmap2.md)
</dt> <dt>

[**glMaterial**](glmaterial-functions.md)
</dt> <dt>

[**glNormal**](glnormal-functions.md)
</dt> <dt>

[**glNormalPointer**](glnormalpointer.md)
</dt> <dt>

[**glPointSize**](glpointsize.md)
</dt> <dt>

[**glPolygonMode**](glpolygonmode.md)
</dt> <dt>

[**glPolygonStipple**](glpolygonstipple.md)
</dt> <dt>

[**glScissor**](glscissor.md)
</dt> <dt>

[**glStencilFunc**](glstencilfunc.md)
</dt> <dt>

[**glStencilOp**](glstencilop.md)
</dt> <dt>

[**glTexCoordPointer**](gltexcoordpointer.md)
</dt> <dt>

[**glTexGen**](gltexgen-functions.md)
</dt> <dt>

[**glTexImage1D**](glteximage1d.md)
</dt> <dt>

[**glTexImage2D**](glteximage2d.md)
</dt> </dl>

 

 





