---
title: gluLoadSamplingMatrices function (Glu.h)
description: The gluLoadSamplingMatrices function loads Non-Uniform Rational B-Spline (NURBS) sampling and culling matrices.
ms.assetid: 7fdbc4e2-a037-4f07-bb03-e51feea42775
keywords:
- gluLoadSamplingMatrices function OpenGL
topic_type:
- apiref
api_name:
- gluLoadSamplingMatrices
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluLoadSamplingMatrices function

The **gluLoadSamplingMatrices** function loads Non-Uniform Rational B-Spline ([NURBS](using-nurbs-curves-and-surfaces.md)) sampling and culling matrices.

## Syntax


```C++
void WINAPI gluLoadSamplingMatrices(
         GLUnurbs *nobj,
   const GLfloat  modelMatrix[16],
   const GLfloat  projMatrix[16],
   const GLint    viewport[4]
);
```



## Parameters

<dl> <dt>

*nobj* 
</dt> <dd>

The NURBS object (created with [**gluNewNurbsRenderer**](glunewnurbsrenderer.md)).

</dd> <dt>

*modelMatrix* 
</dt> <dd>

A modelview matrix (as from a [**glGetFloatv**](glgetfloatv.md) call).

</dd> <dt>

*projMatrix* 
</dt> <dd>

A projection matrix (as from a **glGetFloatv** call).

</dd> <dt>

*viewport* 
</dt> <dd>

A viewport (as from a [**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) call).

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The **gluLoadSamplingMatrices** function uses *modelMatrix*, *projMatrix*, and *viewport* to recompute the sampling and culling matrices stored in *nobj*. The sampling matrix determines how finely a NURBS curve or surface must be tessellated to satisfy the sampling tolerance (as determined by the GLU\_SAMPLING\_TOLERANCE property). The culling matrix is used in deciding if a NURBS curve or surface should be culled before rendering (when the GLU\_CULLING property is turned on).

The **gluLoadSamplingMatrices** function is necessary only if the GLU\_AUTO\_LOAD\_MATRIX property is turned off (see [**gluNurbsProperty**](glunurbsproperty.md)). Although it can be convenient to leave the GLU\_AUTO\_LOAD\_MATRIX property turned on, doing so necessitates a round trip to the OpenGL server to get the current values of the modelview matrix, projection matrix, and viewport.)

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Glu.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Glu32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Glu32.dll</dt> </dl> |



## See also

<dl> <dt>

[**glGetFloatv**](glgetfloatv.md)
</dt> <dt>

[**glGetIntegerv**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**gluGetNurbsProperty**](glugetnurbsproperty.md)
</dt> <dt>

[**gluNewNurbsRenderer**](glunewnurbsrenderer.md)
</dt> </dl>

 

 





