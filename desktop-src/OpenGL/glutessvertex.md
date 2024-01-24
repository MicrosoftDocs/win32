---
title: gluTessVertex function (Glu.h)
description: The gluTessVertex function specifies a vertex on a polygon.
ms.assetid: 9c555b32-5257-4eeb-9323-ccad59591097
keywords:
- gluTessVertex function OpenGL
topic_type:
- apiref
api_name:
- gluTessVertex
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluTessVertex function

The **gluTessVertex** function specifies a vertex on a polygon.

## Syntax


```C++
void WINAPI gluTessVertex(
   GLUtesselator *tess,
   GLdouble      coords[3],
   void          *data
);
```



## Parameters

<dl> <dt>

*tess* 
</dt> <dd>

The tessellation object (created with [**gluNewTess**](glunewtess.md)).

</dd> <dt>

*coords* 
</dt> <dd>

The location of the vertex.

</dd> <dt>

*data* 
</dt> <dd>

An pointer passed back to the program with the vertex callback (as specified by [*gluTessCallback*](glutess.md)).

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The **gluTessVertex** function describes a vertex on a polygon that the user is defining. Successive **gluTessVertex** calls describe a closed contour. For example, to describe a quadrilateral, call **gluTessVertex** four times. You can only call **gluTessVertex** between [**gluTessBeginContour**](glutessbegincontour.md) and [**gluTessEndContour**](glutessendcontour.md).

The *data* parameter normally points to a structure containing the vertex location, as well as other per-vertex attributes such as color and normal. This pointer is passed back to the program through the GLU\_VERTEX callback after tessellation (see [*gluTessCallback*](glutess.md)).

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

[**gluTessBeginPolygon**](glubeginpolygon.md)
</dt> <dt>

[*gluTessCallback*](glutess.md)
</dt> <dt>

[**gluTessEndContour**](glutessendcontour.md)
</dt> <dt>

[**gluTessNormal**](glutessnormal.md)
</dt> <dt>

[**gluTessProperty**](glutessproperty.md)
</dt> </dl>

 

 





