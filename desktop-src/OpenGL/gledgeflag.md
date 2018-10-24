---
title: glEdgeFlag function
description: Flags edges as either boundary or nonboundary.
ms.assetid: cebaa4af-a3bc-4396-9ee0-8cc10bcaf256
keywords:
- glEdgeFlag function OpenGL
topic_type:
- apiref
api_name:
- glEdgeFlag
api_location:
- opengl32.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# glEdgeFlag function

Flags edges as either boundary or nonboundary.

## Syntax


```C++
void WINAPI glEdgeFlag(
   GLboolean flag
);
```



## Parameters

<dl> <dt>

*flag* 
</dt> <dd>

Specifies the current edge flag value, either **TRUE** or **FALSE**.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

Each vertex of a polygon, separate triangle, or separate quadrilateral specified between a [**glBegin**](https://msdn.microsoft.com/library/windows/desktop/dd318361)/[**glEnd**](https://msdn.microsoft.com/library/windows/desktop/dd318849) pair is marked as the start of either a boundary or nonboundary edge. If the current edge flag is **TRUE** when the vertex is specified, the vertex is marked as the start of a boundary edge. If the current edge flag is **FALSE**, the vertex is marked as the start of a nonboundary edge. The **glEdgeFlag** function sets the edge flag to **TRUE** if flag is nonzero, **FALSE** otherwise.

The vertices of connected triangles and connected quadrilaterals are always marked as boundary, regardless of the value of the edge flag.

Boundary and nonboundary edge flags on vertices are significant only if GL\_POLYGON\_MODE is set to GL\_POINT or GL\_LINE. See [**glPolygonMode**](https://msdn.microsoft.com/library/windows/desktop/dd373972).

Initially, the edge flag bit is **TRUE**.

The current edge flag can be updated at any time. In particular, **glEdgeFlag** can be called between a call to [**glBegin**](https://msdn.microsoft.com/library/windows/desktop/dd318361) and the corresponding call to [**glEnd**](https://msdn.microsoft.com/library/windows/desktop/dd318849).

The following functions retrieve information related to **glEdgeFlag**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_EDGE\_FLAG

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Gl.h</dt> </dl>         |
| Library<br/>                  | <dl> <dt>Opengl32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Opengl32.dll</dt> </dl> |



 

 





