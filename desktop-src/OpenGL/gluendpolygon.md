---
title: gluEndPolygon function (Glu.h)
description: The gluBeginPolygon and gluEndPolygon functions delimit a polygon description. | gluEndPolygon function (Glu.h)
ms.assetid: fdb8cc73-c6c3-4377-aa5b-36a79791e7a9
keywords:
- gluEndPolygon function OpenGL
topic_type:
- apiref
api_name:
- gluEndPolygon
api_location:
- Glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluEndPolygon function

\[The **gluEndPolygon** function is obsolete and is provided for backward compatibility only. The **gluEndPolygon** function is mapped to **gluTessEndPolygon** followed by **gluTessEndContour**.\]

The [**gluBeginPolygon**](glubeginpolygon.md) and **gluEndPolygon** functions delimit a polygon description.

## Syntax


```C++
void gluEndPolygon(
   GLUtesselator *tess
);
```



## Parameters

<dl> <dt>

*tess* 
</dt> <dd>

The tessellation object (created with [**gluNewTess**](glunewtess.md)).

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

Use [**gluBeginPolygon**](glubeginpolygon.md) and **gluEndPolygon** to delimit the definition of a nonconvex polygon.

1.  Call **gluBeginPolygon**.
2.  Define the contours of the polygon by calling [**gluTessVertex**](glutessvertex.md) for each vertex and [**gluNextContour**](glunextcontour.md) to start each new contour.
3.  Call **gluEndPolygon** to signal the end of the definition.

    Once **gluEndPolygon** is called, the polygon is tessellated, and the resulting triangles are described through callbacks. For descriptions of the callback functions, see [*gluTessCallback*](glutess.md).

## Examples

The following example describes a quadrilateral with a triangular hole:

``` syntax
gluBeginPolygon(tess); 
    gluTessVertex(tess, v1, v1); 
    gluTessVertex(tess, v2, v2); 
    gluTessVertex(tess, v3, v3); 
    gluTessVertex(tess, v4, v4); 
gluNextContour(tess, GLU_INTERIOR); 
    gluTessVertex(tess, v5, v5); 
    gluTessVertex(tess, v6, v6); 
    gluTessVertex(tess, v7, v7); 
gluEndPolygon(tess);
```

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

[**gluNewTess**](glunewtess.md)
</dt> <dt>

[**gluNextContour**](glunextcontour.md)
</dt> <dt>

[**gluTessBeginContour**](glutessbegincontour.md)
</dt> <dt>

[**gluTessBeginPolygon**](glutessbeginpolygon.md)
</dt> <dt>

[*gluTessCallback*](glutess.md)
</dt> <dt>

[**gluTessVertex**](glutessvertex.md)
</dt> </dl>

 

 





