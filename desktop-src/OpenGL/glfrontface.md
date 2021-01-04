---
title: glFrontFace function (Gl.h)
description: The glFrontFace function defines front-facing and back-facing polygons.
ms.assetid: 4087107c-99cd-4c26-92e3-8dc43633d51f
keywords:
- glFrontFace function OpenGL
topic_type:
- apiref
api_name:
- glFrontFace
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glFrontFace function

The **glFrontFace** function defines front-facing and back-facing polygons.

## Syntax


```C++
void WINAPI glFrontFace(
   GLenum mode
);
```



## Parameters

<dl> <dt>

*mode* 
</dt> <dd>

The orientation of front-facing polygons. GL\_CW and GL\_CCW are accepted. The default value is GL\_CCW.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *mode* was not an accepted value.<br/>                                                                                          |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

In a scene composed entirely of opaque closed surfaces, back-facing polygons are never visible. Eliminating these invisible polygons has the obvious benefit of speeding up the rendering of the image. You enable and disable elimination of back-facing polygons with [**glEnable**](glenable.md) and [**glDisable**](gldisable.md) using argument GL\_CULL\_FACE.

The projection of a polygon to window coordinates is said to have clockwise winding if an imaginary object following the path from its first vertex, its second vertex, and so on, to its last vertex, and finally back to its first vertex, moves in a clockwise direction about the interior of the polygon. The polygon's winding is said to be counterclockwise if the imaginary object following the same path moves in a counterclockwise direction about the interior of the polygon. The **glFrontFace** function specifies whether polygons with clockwise winding in window coordinates, or counterclockwise winding in window coordinates, are taken to be front-facing. Passing GL\_CCW to *mode* selects counterclockwise polygons as front-facing; GL\_CW selects clockwise polygons as front-facing. By default, counterclockwise polygons are taken to be front-facing.

The following function retrieves information about **glFrontface**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_FRONT\_FACE

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

[**glCullFace**](glcullface.md)
</dt> <dt>

[**glDisable**](gldisable.md)
</dt> <dt>

[**glEnable**](glenable.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**glLightModel**](gllightmodel-functions.md)
</dt> </dl>

 

 





