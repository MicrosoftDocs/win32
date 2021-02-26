---
title: gluTessBeginContour function (Glu.h)
description: The gluTessBeginContour and gluTessEndContour functions delimit a contour description. | gluTessBeginContour function (Glu.h)
ms.assetid: 4008ce9c-86e7-4b24-9bda-5915f469596a
keywords:
- gluTessBeginContour function OpenGL
topic_type:
- apiref
api_name:
- gluTessBeginContour
api_location:
- Glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluTessBeginContour function

The **gluTessBeginContour** and [**gluTessEndContour**](glutessendcontour.md) functions delimit a contour description.

## Syntax


```C++
void WINAPI gluTessBeginContour(
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

The **gluTessBeginContour** and [**gluTessEndPolygon**](glutessendpolygon.md) functions delimit the definition of a polygon contour. Within each **gluTessBeginContour**/**gluTessEndPolygon** pair, there can be zero or more calls to [**gluTessVertex**](glutessvertex.md). The vertexes specify a closed contour (the last vertex of each contour is automatically linked to the first). You can call **gluTessBeginContour** only between [**gluTessBeginPolygon**](glutessbeginpolygon.md) and **gluTessEndPolygon**.

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

[**gluTessBeginPolygon**](glutessbeginpolygon.md)
</dt> <dt>

[*gluTessCallback*](glutess.md)
</dt> <dt>

[**gluTessEndPolygon**](glutessendpolygon.md)
</dt> <dt>

[**gluTessNormal**](glutessnormal.md)
</dt> <dt>

[**gluTessProperty**](glutessproperty.md)
</dt> <dt>

[**gluTessVertex**](glutessvertex.md)
</dt> </dl>

 

 





