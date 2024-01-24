---
title: glIsEnabled function (Gl.h)
description: The gllsEnabled function tests whether a capability is enabled.
ms.assetid: 18df5a6f-dc21-434d-a2e8-2c58597df037
keywords:
- glIsEnabled function OpenGL
topic_type:
- apiref
api_name:
- glIsEnabled
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glIsEnabled function

The **gllsEnabled** function tests whether a capability is enabled.

## Syntax


```C++
GLboolean WINAPI glIsEnabled(
   GLenum cap
);
```



## Parameters

<dl> <dt>

*cap* 
</dt> <dd>

A symbolic constant indicating an OpenGL capability. The following capabilities are accepted.



| Value                                                                                                                                                                                                    | Meaning                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_ALPHA_TEST"></span><span id="gl_alpha_test"></span><dl> <dt>**GL\_ALPHA\_TEST**</dt> </dl>                                           | See [**glAlphaFunc**](glalphafunc.md)<br/>                                                                                                   |
| <span id="GL_AUTO_NORMAL"></span><span id="gl_auto_normal"></span><dl> <dt>**GL\_AUTO\_NORMAL**</dt> </dl>                                        | See [**glEvalCoord**](glevalcoord-functions.md)<br/>                                                                                         |
| <span id="GL_BLEND"></span><span id="gl_blend"></span><dl> <dt>**GL\_BLEND**</dt> </dl>                                                           | See [**glBlendFunc**](glblendfunc.md)<br/>                                                                                                   |
| <span id="GL_CLIP_PLANE_i"></span><span id="gl_clip_plane_i"></span><span id="GL_CLIP_PLANE_I"></span><dl> <dt>**GL\_CLIP\_PLANE *i***</dt> </dl> | See [**glClipPlane**](glclipplane.md)<br/>                                                                                                   |
| <span id="GL_COLOR_ARRAY"></span><span id="gl_color_array"></span><dl> <dt>**GL\_COLOR\_ARRAY**</dt> </dl>                                        | See [**glColorPointer**](glcolorpointer.md)<br/>                                                                                             |
| <span id="GL_COLOR_LOGIC_OP"></span><span id="gl_color_logic_op"></span><dl> <dt>**GL\_COLOR\_LOGIC\_OP**</dt> </dl>                              | See [**glLogicOp**](gllogicop.md)<br/>                                                                                                       |
| <span id="GL_COLOR_MATERIAL"></span><span id="gl_color_material"></span><dl> <dt>**GL\_COLOR\_MATERIAL**</dt> </dl>                               | See [**glColorMaterial**](glcolormaterial.md)<br/>                                                                                           |
| <span id="GL_CULL_FACE"></span><span id="gl_cull_face"></span><dl> <dt>**GL\_CULL\_FACE**</dt> </dl>                                              | See [**glCullFace**](glcullface.md)<br/>                                                                                                     |
| <span id="GL_DEPTH_TEST"></span><span id="gl_depth_test"></span><dl> <dt>**GL\_DEPTH\_TEST**</dt> </dl>                                           | See [**glDepthFunc**](gldepthfunc.md) and [**glDepthRange**](gldepthrange.md)<br/>                                                          |
| <span id="GL_DITHER"></span><span id="gl_dither"></span><dl> <dt>**GL\_DITHER**</dt> </dl>                                                        | See [**glEnable**](glenable.md)<br/>                                                                                                         |
| <span id="GL_FOG"></span><span id="gl_fog"></span><dl> <dt>**GL\_FOG**</dt> </dl>                                                                 | See [**glFog**](glfog.md)<br/>                                                                                                               |
| <span id="GL_INDEX_ARRAY"></span><span id="gl_index_array"></span><dl> <dt>**GL\_INDEX\_ARRAY**</dt> </dl>                                        | See [**glIndexPointer**](glindexpointer.md)<br/>                                                                                             |
| <span id="GL_INDEX_LOGIC_OP"></span><span id="gl_index_logic_op"></span><dl> <dt>**GL\_INDEX\_LOGIC\_OP**</dt> </dl>                              | See [**glLogicOp**](gllogicop.md)<br/>                                                                                                       |
| <span id="GL_LIGHT_i"></span><span id="gl_light_i"></span><span id="GL_LIGHT_I"></span><dl> <dt>**GL\_LIGHT *i***</dt> </dl>                      | See [**glLightModel**](gllightmodel-functions.md) and [**glLight**](gllight-functions.md)<br/>                                              |
| <span id="GL_LIGHTING"></span><span id="gl_lighting"></span><dl> <dt>**GL\_LIGHTING**</dt> </dl>                                                  | See [**glMaterial**](glmaterial-functions.md), [**glLightModel**](gllightmodel-functions.md), and [**glLight**](gllight-functions.md)<br/> |
| <span id="GL_LINE_SMOOTH"></span><span id="gl_line_smooth"></span><dl> <dt>**GL\_LINE\_SMOOTH**</dt> </dl>                                        | See [**glLineWidth**](gllinewidth.md)<br/>                                                                                                   |
| <span id="GL_LINE_STIPPLE"></span><span id="gl_line_stipple"></span><dl> <dt>**GL\_LINE\_STIPPLE**</dt> </dl>                                     | See [**glLineStipple**](gllinestipple.md)<br/>                                                                                               |
| <span id="GL_MAP1_COLOR_4"></span><span id="gl_map1_color_4"></span><dl> <dt>**GL\_MAP1\_COLOR\_4**</dt> </dl>                                    | See [**glMap1**](glmap1.md)<br/>                                                                                                             |
| <span id="GL_MAP1_INDEX"></span><span id="gl_map1_index"></span><dl> <dt>**GL\_MAP1\_INDEX**</dt> </dl>                                           | See [**glMap1**](glmap1.md)<br/>                                                                                                             |
| <span id="GL_MAP1_NORMAL"></span><span id="gl_map1_normal"></span><dl> <dt>**GL\_MAP1\_NORMAL**</dt> </dl>                                        | See [**glMap1**](glmap1.md)<br/>                                                                                                             |
| <span id="GL_MAP1_TEXTURE_COORD_1"></span><span id="gl_map1_texture_coord_1"></span><dl> <dt>**GL\_MAP1\_TEXTURE\_COORD\_1**</dt> </dl>           | See [**glMap1**](glmap1.md)<br/>                                                                                                             |
| <span id="GL_MAP1_TEXTURE_COORD_2"></span><span id="gl_map1_texture_coord_2"></span><dl> <dt>**GL\_MAP1\_TEXTURE\_COORD\_2**</dt> </dl>           | See [**glMap1**](glmap1.md)<br/>                                                                                                             |
| <span id="GL_MAP1_TEXTURE_COORD_3"></span><span id="gl_map1_texture_coord_3"></span><dl> <dt>**GL\_MAP1\_TEXTURE\_COORD\_3**</dt> </dl>           | See [**glMap1**](glmap1.md)<br/>                                                                                                             |
| <span id="GL_MAP1_TEXTURE_COORD_4"></span><span id="gl_map1_texture_coord_4"></span><dl> <dt>**GL\_MAP1\_TEXTURE\_COORD\_4**</dt> </dl>           | See [**glMap1**](glmap1.md)<br/>                                                                                                             |
| <span id="GL_MAP1_VERTEX_3"></span><span id="gl_map1_vertex_3"></span><dl> <dt>**GL\_MAP1\_VERTEX\_3**</dt> </dl>                                 | See [**glMap1**](glmap1.md)<br/>                                                                                                             |
| <span id="GL_MAP1_VERTEX_4"></span><span id="gl_map1_vertex_4"></span><dl> <dt>**GL\_MAP1\_VERTEX\_4**</dt> </dl>                                 | See [**glMap1**](glmap1.md)<br/>                                                                                                             |
| <span id="GL_MAP2_COLOR_4"></span><span id="gl_map2_color_4"></span><dl> <dt>**GL\_MAP2\_COLOR\_4**</dt> </dl>                                    | See [**glMap2**](glmap2.md)<br/>                                                                                                             |
| <span id="GL_MAP2_INDEX"></span><span id="gl_map2_index"></span><dl> <dt>**GL\_MAP2\_INDEX**</dt> </dl>                                           | See [**glMap2**](glmap2.md)<br/>                                                                                                             |
| <span id="GL_MAP2_NORMAL"></span><span id="gl_map2_normal"></span><dl> <dt>**GL\_MAP2\_NORMAL**</dt> </dl>                                        | See [**glMap2**](glmap2.md)<br/>                                                                                                             |
| <span id="GL_MAP2_TEXTURE_COORD_1"></span><span id="gl_map2_texture_coord_1"></span><dl> <dt>**GL\_MAP2\_TEXTURE\_COORD\_1**</dt> </dl>           | See [**glMap2**](glmap2.md)<br/>                                                                                                             |
| <span id="GL_MAP2_TEXTURE_COORD_2"></span><span id="gl_map2_texture_coord_2"></span><dl> <dt>**GL\_MAP2\_TEXTURE\_COORD\_2**</dt> </dl>           | See [**glMap2**](glmap2.md)<br/>                                                                                                             |
| <span id="GL_MAP2_TEXTURE_COORD_3"></span><span id="gl_map2_texture_coord_3"></span><dl> <dt>**GL\_MAP2\_TEXTURE\_COORD\_3**</dt> </dl>           | See [**glMap2**](glmap2.md)<br/>                                                                                                             |
| <span id="GL_MAP2_TEXTURE_COORD_4"></span><span id="gl_map2_texture_coord_4"></span><dl> <dt>**GL\_MAP2\_TEXTURE\_COORD\_4**</dt> </dl>           | See [**glMap2**](glmap2.md)<br/>                                                                                                             |
| <span id="GL_MAP2_VERTEX_3"></span><span id="gl_map2_vertex_3"></span><dl> <dt>**GL\_MAP2\_VERTEX\_3**</dt> </dl>                                 | See [**glMap2**](glmap2.md)<br/>                                                                                                             |
| <span id="GL_MAP2_VERTEX_4"></span><span id="gl_map2_vertex_4"></span><dl> <dt>**GL\_MAP2\_VERTEX\_4**</dt> </dl>                                 | See [**glMap2**](glmap2.md)<br/>                                                                                                             |
| <span id="GL_NORMAL_ARRAY"></span><span id="gl_normal_array"></span><dl> <dt>**GL\_NORMAL\_ARRAY**</dt> </dl>                                     | See [**glNormalPointer**](glnormalpointer.md)<br/>                                                                                           |
| <span id="GL_NORMALIZE"></span><span id="gl_normalize"></span><dl> <dt>**GL\_NORMALIZE**</dt> </dl>                                               | See [**glNormal**](glnormal-functions.md)<br/>                                                                                               |
| <span id="GL_POINT_SMOOTH"></span><span id="gl_point_smooth"></span><dl> <dt>**GL\_POINT\_SMOOTH**</dt> </dl>                                     | See [**glPointSize**](glpointsize.md)<br/>                                                                                                   |
| <span id="GL_POLYGON_OFFSET_FILL"></span><span id="gl_polygon_offset_fill"></span><dl> <dt>**GL\_POLYGON\_OFFSET\_FILL**</dt> </dl>               | See [**glPolygonOffset**](glpolygonoffset.md)<br/>                                                                                           |
| <span id="GL_POLYGON_OFFSET_LINE"></span><span id="gl_polygon_offset_line"></span><dl> <dt>**GL\_POLYGON\_OFFSET\_LINE**</dt> </dl>               | See [**glPolygonOffset**](glpolygonoffset.md)<br/>                                                                                           |
| <span id="GL_POLYGON_OFFSET_POINT"></span><span id="gl_polygon_offset_point"></span><dl> <dt>**GL\_POLYGON\_OFFSET\_POINT**</dt> </dl>            | See [**glPolygonOffset**](glpolygonoffset.md)<br/>                                                                                           |
| <span id="GL_POLYGON_SMOOTH"></span><span id="gl_polygon_smooth"></span><dl> <dt>**GL\_POLYGON\_SMOOTH**</dt> </dl>                               | See [**glPolygonMode**](glpolygonmode.md)<br/>                                                                                               |
| <span id="GL_POLYGON_STIPPLE"></span><span id="gl_polygon_stipple"></span><dl> <dt>**GL\_POLYGON\_STIPPLE**</dt> </dl>                            | See [**glPolygonStipple**](glpolygonstipple.md)<br/>                                                                                         |
| <span id="GL_SCISSOR_TEST"></span><span id="gl_scissor_test"></span><dl> <dt>**GL\_SCISSOR\_TEST**</dt> </dl>                                     | See [**glScissor**](glscissor.md)<br/>                                                                                                       |
| <span id="GL_STENCIL_TEST"></span><span id="gl_stencil_test"></span><dl> <dt>**GL\_STENCIL\_TEST**</dt> </dl>                                     | See [**glStencilFunc**](glstencilfunc.md) and [**glStencilOp**](glstencilop.md)<br/>                                                        |
| <span id="GL_TEXTURE_1D"></span><span id="gl_texture_1d"></span><dl> <dt>**GL\_TEXTURE\_1D**</dt> </dl>                                           | See [**glTexImage1D**](glteximage1d.md)<br/>                                                                                                 |
| <span id="GL_TEXTURE_2D"></span><span id="gl_texture_2d"></span><dl> <dt>**GL\_TEXTURE\_2D**</dt> </dl>                                           | See [**glTexImage2D**](glteximage2d.md)<br/>                                                                                                 |
| <span id="GL_TEXTURE_COORD_ARRAY"></span><span id="gl_texture_coord_array"></span><dl> <dt>**GL\_TEXTURE\_COORD\_ARRAY**</dt> </dl>               | See [**glTexCoordPointer**](gltexcoordpointer.md)<br/>                                                                                       |
| <span id="GL_TEXTURE_GEN_Q"></span><span id="gl_texture_gen_q"></span><dl> <dt>**GL\_TEXTURE\_GEN\_Q**</dt> </dl>                                 | See [**glTexGen**](gltexgen-functions.md)<br/>                                                                                               |
| <span id="GL_TEXTURE_GEN_R"></span><span id="gl_texture_gen_r"></span><dl> <dt>**GL\_TEXTURE\_GEN\_R**</dt> </dl>                                 | See [**glTexGen**](gltexgen-functions.md)<br/>                                                                                               |
| <span id="GL_TEXTURE_GEN_S"></span><span id="gl_texture_gen_s"></span><dl> <dt>**GL\_TEXTURE\_GEN\_S**</dt> </dl>                                 | See [**glTexGen**](gltexgen-functions.md)<br/>                                                                                               |
| <span id="GL_TEXTURE_GEN_T"></span><span id="gl_texture_gen_t"></span><dl> <dt>**GL\_TEXTURE\_GEN\_T**</dt> </dl>                                 | See [**glTexGen**](gltexgen-functions.md)<br/>                                                                                               |
| <span id="GL_VERTEX_ARRAY"></span><span id="gl_vertex_array"></span><dl> <dt>**GL\_VERTEX\_ARRAY**</dt> </dl>                                     | See [**glVertexPointer**](glvertexpointer.md)<br/>                                                                                           |



 

</dd> </dl>

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *cap* was not an accepted value.<br/>                                                                                           |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **gllsEnabled** function returns GL\_TRUE if *cap* is an enabled capability and returns GL\_FALSE otherwise.

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

[**glEnable**](glenable.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> </dl>

 

 





