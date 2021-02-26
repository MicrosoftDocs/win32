---
title: gluTessBeginPolygon function (Glu.h)
description: The gluTessBeginPolygon and gluTessEndPolygon functions delimit a polygon description. | gluTessBeginPolygon function (Glu.h)
ms.assetid: 3a04363a-c492-4fa5-b312-f2fa2a805782
keywords:
- gluTessBeginPolygon function OpenGL
topic_type:
- apiref
api_name:
- gluTessBeginPolygon
api_location:
- Glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluTessBeginPolygon function

The **gluTessBeginPolygon** and [**gluTessEndPolygon**](glutessendpolygon.md) functions delimit a polygon description.

## Syntax


```C++
void WINAPI gluTessBeginPolygon(
   GLUtesselator *tess,
   void          *polygon_data
);
```



## Parameters

<dl> <dt>

*tess* 
</dt> <dd>

The tessellation object (created with [**gluNewTess**](glunewtess.md)).

</dd> <dt>

*polygon\_data* 
</dt> <dd>

A pointer to a programmer-defined polygon data structure.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The **gluTessBeginPolygon** and [**gluTessEndPolygon**](glutessendpolygon.md) functions delimit the definition of a nonconvex polygon. Within each **gluTessBeginPolygon** / **gluTessEndPolygon** pair, include one or more calls to [**gluTessBeginContour**](glutessbegincontour.md). Within each contour, there are zero or more calls to [**gluTessVertex**](glutessvertex.md). The vertexes specify a closed contour (the last vertex of each contour is automatically linked to the first).

The *polygon\_data* parameter is a pointer to a programmer-defined data structure. If the appropriate callbacks are specified (see [*gluTessCallback*](glutess.md)), this pointer is returned to the callback function or functions, making it a convenient way to store per-polygon information.

When you call [**gluTessEndPolygon**](glutessendpolygon.md), the polygon is tessellated, and the resulting triangles are described through callbacks. For descriptions of the callback functions, see [*gluTessCallback*](glutess.md).

## Examples

The following describes a quadrilateral with a triangular hole:

``` syntax
gluTessBeginPolygon(tobj, NULL); 
  gluTessBeginContour(tobj); 
    gluTessVertex(tobj, v1, v1); 
    gluTessVertex(tobj, v2, v2); 
    gluTessVertex(tobj, v3, v3); 
    gluTessVertex(tobj, v4, v4); 
  gluTessEndContour(tobj); 
  gluTessBeginContour(tobj); 
    gluTessVertex(tobj, v5, v5); 
    gluTessVertex(tobj, v6, v6); 
    gluTessVertex(tobj, v7, v7); 
  gluTessEndContour(tobj); 
gluTessEndPolygon(tobj);
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

[**gluTessBeginContour**](glutessbegincontour.md)
</dt> <dt>

[*gluTessCallback*](glutess.md)
</dt> <dt>

[**gluTessEndContour**](glutessendcontour.md)
</dt> <dt>

[**gluTessNormal**](glutessnormal.md)
</dt> <dt>

[**gluTessProperty**](glutessproperty.md)
</dt> <dt>

[**gluTessVertex**](glutessvertex.md)
</dt> </dl>

 

 





