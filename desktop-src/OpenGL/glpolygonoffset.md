---
title: glPolygonOffset function (Gl.h)
description: The glPolygonOffset function sets the scale and units OpenGL uses to calculate depth values.
ms.assetid: 06bc1aba-1692-40f0-8535-2cb65b487490
keywords:
- glPolygonOffset function OpenGL
topic_type:
- apiref
api_name:
- glPolygonOffset
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glPolygonOffset function

The **glPolygonOffset** function sets the scale and units OpenGL uses to calculate depth values.

## Syntax


```C++
void WINAPI glPolygonOffset(
   GLfloat factor,
   GLfloat units
);
```



## Parameters

<dl> <dt>

*factor* 
</dt> <dd>

Specifies a scale factor that is used to create a variable depth offset for each polygon. The initial value is zero.

</dd> <dt>

*units* 
</dt> <dd>

Specifies a value that is multiplied by an implementation-specific value to create a constant depth offset. The initial value is 0.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error code can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

When GL\_POLYGON\_OFFSET is enabled, each fragment's depth value will be offset after it is interpolated from the depth values of the appropriate vertices. The value of the offset is *factor* \* ?z + r \**units*, where ?z is a measurement of the change in depth relative to the screen area of the polygon, and r is the smallest value that is guaranteed to produce a resolvable offset for a given implementation. The offset is added before the depth test is performed and before the value is written into the depth buffer.

The **glPolygonOffset** function is useful for rendering hidden-line images, for applying decals to surfaces, and for rendering solids with highlighted edges.

The **glPolygonOffset** function has no effect on depth coordinates placed in the feedback buffer. It also has no effect on selection.

The following functions retrieve information related to **glPolygonOffset**:

-   [**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_POLYGON\_OFFSET\_FACTOR
-   [**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_POLYGON\_OFFSET\_UNITS
-   [**glIsEnabled**](glisenabled.md) with argument GL\_POLYGON\_OFFSET\_FILL
-   [**glIsEnabled**](glisenabled.md) with argument GL\_POLYGON\_OFFSET\_LINE
-   [**glIsEnabled**](glisenabled.md) with argument GL\_POLYGON\_OFFSET\_POINT

> [!Note]  
> The **glPolygonOffset** function is only available in OpenGl version 1.1 or greater.

 

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

[**glDepthFunc**](gldepthfunc.md)
</dt> <dt>

[**glDisable**](gldisable.md)
</dt> <dt>

[**glEnable**](glenable.md)
</dt> <dt>

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**glIsEnabled**](glisenabled.md)
</dt> <dt>

[**glLineWidth**](gllinewidth.md)
</dt> <dt>

[**glStencilOp**](glstencilop.md)
</dt> <dt>

[**glTexEnv**](gltexenv-functions.md)
</dt> </dl>

 

 





