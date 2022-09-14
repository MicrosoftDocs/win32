---
title: glEdgeFlagv function (Gl.h)
description: Flags edges as either boundary or nonboundary. | glEdgeFlagv function (Gl.h)
ms.assetid: 69b5ddbd-7c0c-47f0-a358-d8bf81755c88
keywords:
- glEdgeFlagv function OpenGL
topic_type:
- apiref
api_name:
- glEdgeFlagv
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glEdgeFlagv function

Flags edges as either boundary or nonboundary.

## Syntax


```C++
void WINAPI glEdgeFlagv(
   const GLboolean *flag
);
```



## Parameters

<dl> <dt>

*flag* 
</dt> <dd>

Specifies a pointer to an array that contains a single Boolean element, which replaces the current edge flag value.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

Each vertex of a polygon, separate triangle, or separate quadrilateral specified between a [**glBegin**](/windows/desktop/OpenGL/glbegin)/[**glEnd**](/windows/desktop/OpenGL/glend) pair is marked as the start of either a boundary or nonboundary edge. If the current edge flag is **TRUE** when the vertex is specified, the vertex is marked as the start of a boundary edge. If the current edge flag is **FALSE**, the vertex is marked as the start of a nonboundary edge. The **glEdgeFlagv** function sets the edge flag to **TRUE** if flag is nonzero, **FALSE** otherwise.

The vertices of connected triangles and connected quadrilaterals are always marked as boundary, regardless of the value of the edge flag.

Boundary and nonboundary edge flags on vertices are significant only if GL\_POLYGON\_MODE is set to GL\_POINT or GL\_LINE. See [**glPolygonMode**](/windows/desktop/OpenGL/glpolygonmode).

Initially, the edge flag bit is **TRUE**.

The current edge flag can be updated at any time. In particular, **glEdgeFlagv** can be called between a call to [**glBegin**](/windows/desktop/OpenGL/glbegin) and the corresponding call to [**glEnd**](/windows/desktop/OpenGL/glend).

The following functions retrieve information related to **glEdgeFlagv**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_EDGE\_FLAG

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Gl.h</dt> </dl>         |
| Library<br/>                  | <dl> <dt>Opengl32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Opengl32.dll</dt> </dl> |



 

