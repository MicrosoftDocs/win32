---
title: glHint function (Gl.h)
description: The glHint function specifies implementation-specific hints.
ms.assetid: 6d03e107-321a-45ee-9ce7-25fa9cab32d9
keywords:
- glHint function OpenGL
topic_type:
- apiref
api_name:
- glHint
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glHint function

The **glHint** function specifies implementation-specific hints.

## Syntax


```C++
void WINAPI glHint(
   GLenum target,
   GLenum mode
);
```



## Parameters

<dl> <dt>

*target* 
</dt> <dd>

A symbolic constant indicating the behavior to be controlled. The following symbolic constants, along with suggested semantics, are accepted.



| Value                                                                                                                                                                                                              | Meaning                                                                                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GL_FOG_HINT"></span><span id="gl_fog_hint"></span><dl> <dt>**GL\_FOG\_HINT**</dt> </dl>                                                           | Indicates the accuracy of fog calculation. If per-pixel fog calculation is not efficiently supported by the OpenGL implementation, hinting GL\_DONT\_CARE or GL\_FASTEST can result in per-vertex calculation of fog effects.<br/>                                                                          |
| <span id="GL_LINE_SMOOTH_HINT"></span><span id="gl_line_smooth_hint"></span><dl> <dt>**GL\_LINE\_SMOOTH\_HINT**</dt> </dl>                                  | Indicates the sampling quality of antialiased lines. Hinting GL\_NICEST can result in more pixel fragments being generated during rasterization, if a larger filter function is applied.<br/>                                                                                                               |
| <span id="GL_PERSPECTIVE_CORRECTION_HINT"></span><span id="gl_perspective_correction_hint"></span><dl> <dt>**GL\_PERSPECTIVE\_CORRECTION\_HINT**</dt> </dl> | Indicates the quality of color and texture coordinate interpolation. If perspective-corrected parameter interpolation is not efficiently supported by the OpenGL implementation, hinting GL\_DONT\_CARE or GL\_FASTEST can result in simple linear interpolation of colors and/or texture coordinates.<br/> |
| <span id="GL_POINT_SMOOTH_HINT"></span><span id="gl_point_smooth_hint"></span><dl> <dt>**GL\_POINT\_SMOOTH\_HINT**</dt> </dl>                               | Indicates the sampling quality of antialiased points. Hinting GL\_NICEST can result in more pixel fragments being generated during rasterization, if a larger filter function is applied.<br/>                                                                                                              |
| <span id="GL_POLYGON_SMOOTH_HINT"></span><span id="gl_polygon_smooth_hint"></span><dl> <dt>**GL\_POLYGON\_SMOOTH\_HINT**</dt> </dl>                         | Indicates the sampling quality of antialiased polygons. Hinting GL\_NICEST can result in more pixel fragments being generated during rasterization, if a larger filter function is applied.<br/>                                                                                                            |



 

</dd> <dt>

*mode* 
</dt> <dd>

A symbolic constant indicating the desired behavior. The following symbolic constants are accepted.



| Value                                                                                                                                                       | Meaning                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <span id="GL_FASTEST"></span><span id="gl_fastest"></span><dl> <dt>**GL\_FASTEST**</dt> </dl>        | The most efficient option should be chosen.<br/>                    |
| <span id="GL_NICEST"></span><span id="gl_nicest"></span><dl> <dt>**GL\_NICEST**</dt> </dl>           | The most correct, or highest quality, option should be chosen.<br/> |
| <span id="GL_DONT_CARE"></span><span id="gl_dont_care"></span><dl> <dt>**GL\_DONT\_CARE**</dt> </dl> | The client doesn't have a preference.<br/>                          |



 

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | *target* or *mode* was not an accepted value.<br/>                                                                              |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

When there is room for interpretation, you can control certain aspects of OpenGL behavior with hints. You specify a hint with two arguments. The *target* parameter is a symbolic constant indicating the behavior to be controlled, and *mode* is another symbolic constant indicating the desired behavior.

Though the implementation aspects that can be hinted are well defined, the interpretation of the hints depends on the implementation.

The **glHint** function can be ignored.

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
</dt> </dl>

 

 





