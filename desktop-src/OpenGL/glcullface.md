---
title: glCullFace function (Gl.h)
description: The glCullFace function specifies whether front-facing or back-facing facets can be culled.
ms.assetid: 53bf05b5-a68b-4d96-b4e7-2878a0a86a13
keywords:
- glCullFace function OpenGL
topic_type:
- apiref
api_name:
- glCullFace
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glCullFace function

The **glCullFace** function specifies whether front-facing or back-facing facets can be culled.

## Syntax


```C++
void WINAPI glCullFace(
   GLenum mode
);
```



## Parameters

<dl> <dt>

*mode* 
</dt> <dd>

Specifies whether front-facing or back-facing facets are candidates for culling. The symbolic constants GL\_FRONT, GL\_BACK, and GL\_FRONT\_AND\_BACK are accepted. The default value is GL\_BACK.

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

The **glCullFace** function specifies whether front-facing or back-facing facets are culled (as specified by *mode*) when facet culling is enabled. You enable and disable facet culling using [**glEnable**](glenable.md) and [**glDisable**](gldisable.md) with the argument GL\_CULL\_FACE. Facets include triangles, quadrilaterals, polygons, and rectangles.

The [**glFrontFace**](glfrontface.md) function specifies which of the clockwise and counterclockwise facets are front-facing and back-facing.

If *mode* is GL\_FRONT\_AND\_BACK, no facets are drawn, but other primitives, such as points and lines, are drawn.

The following functions retrieve information related to **glCullFace**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_CULL\_FACE\_MODE

[**glIsEnabled**](glisenabled.md) with argument GL\_CULL\_FACE

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

[**glDisable**](gldisable.md)
</dt> <dt>

[**glEnable**](glenable.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glFrontFace**](glfrontface.md)
</dt> <dt>

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**glIsEnabled**](glisenabled.md)
</dt> </dl>

 

 





