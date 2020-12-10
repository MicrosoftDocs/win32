---
title: glPolygonMode function (Gl.h)
description: The glPolygonMode function selects a polygon rasterization mode.
ms.assetid: d8781bae-e78c-40fb-9f33-c742c70ebda1
keywords:
- glPolygonMode function OpenGL
topic_type:
- apiref
api_name:
- glPolygonMode
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glPolygonMode function

The **glPolygonMode** function selects a polygon rasterization mode.

## Syntax


```C++
void WINAPI glPolygonMode(
   GLenum face,
   GLenum mode
);
```



## Parameters

<dl> <dt>

*face* 
</dt> <dd>

The polygons that *mode* applies to. Must be GL\_FRONT for front-facing polygons, GL\_BACK for back-facing polygons, or GL\_FRONT\_AND\_BACK for front- and back-facing polygons.

</dd> <dt>

*mode* 
</dt> <dd>

The way polygons will be rasterized. The following modes are defined and can be specified in *mode*. The default is GL\_FILL for both front- and back-facing polygons.



| Value                                                                                                                                          | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_POINT"></span><span id="gl_point"></span><dl> <dt>**GL\_POINT**</dt> </dl> | Polygon vertices that are marked as the start of a boundary edge are drawn as points. Point attributes such as GL\_POINT\_SIZE and GL\_POINT\_SMOOTH control the rasterization of the points. Polygon rasterization attributes other than GL\_POLYGON\_MODE have no effect.<br/>                                                                                                                                                    |
| <span id="GL_LINE"></span><span id="gl_line"></span><dl> <dt>**GL\_LINE**</dt> </dl>    | Boundary edges of the polygon are drawn as line segments. They are treated as connected line segments for line stippling; the line stipple counter and pattern are not reset between segments (see [**glLineStipple**](gllinestipple.md)). Line attributes such as GL\_LINE\_WIDTH and GL\_LINE\_SMOOTH control the rasterization of the lines. Polygon rasterization attributes other than GL\_POLYGON\_MODE have no effect.<br/> |
| <span id="GL_FILL"></span><span id="gl_fill"></span><dl> <dt>**GL\_FILL**</dt> </dl>    | The interior of the polygon is filled. Polygon attributes such as GL\_POLYGON\_STIPPLE and GL\_POLYGON\_SMOOTH control the rasterization of the polygon.<br/>                                                                                                                                                                                                                                                                       |



 

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | Either *face* or *mode* was not an accepted value.<br/>                                                                         |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glPolygonMode** function controls the interpretation of polygons for rasterization. The *face* parameter describes which polygons *mode* applies to: front-facing polygons (GL\_FRONT), back-facing polygons (GL\_BACK), or both (GL\_FRONT\_AND\_BACK). The polygon mode affects only the final rasterization of polygons. In particular, a polygon's vertices are lit and the polygon is clipped and possibly culled before these modes are applied.

To draw a surface with filled back-facing polygons and outlined front-facing polygons, call

**glPolygonMode**(GL\_FRONT, GL\_LINE);

Vertices are marked as boundary or nonboundary with an edge flag. Edge flags are generated internally by OpenGL when it decomposes polygons, and they can be set explicitly using [**glEdgeFlag**](gledgeflag-functions.md).

The following function retrieves information related to **glPolygonMode**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_POLYGON\_MODE

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

[**glEdgeFlag**](gledgeflag-functions.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glLineStipple**](gllinestipple.md)
</dt> <dt>

[**glLineWidth**](gllinewidth.md)
</dt> <dt>

[**glPointSize**](glpointsize.md)
</dt> <dt>

[**glPolygonStipple**](glpolygonstipple.md)
</dt> </dl>

 

 





