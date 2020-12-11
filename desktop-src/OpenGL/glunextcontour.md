---
title: gluNextContour function (Glu.h)
description: The gluNextContour function marks the beginning of another contour.
ms.assetid: 622cd631-3426-4206-9e23-af2a74343da5
keywords:
- gluNextContour function OpenGL
topic_type:
- apiref
api_name:
- gluNextContour
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluNextContour function

\[The **gluNextContour** function is obsolete and is provided for backward compatibility only. The **gluNextContour** function is mapped to [**gluTessEndContour**](glutessendcontour.md) followed by [**gluTessBeginContour**](glutessbegincontour.md).\]

The **gluNextContour** function marks the beginning of another contour.

## Syntax


```C++
void WINAPI gluNextContour(
   GLUtesselator *tess,
   GLenum        type
);
```



## Parameters

<dl> <dt>

*tess* 
</dt> <dd>

The tessellation object (created with [**gluNewTess**](glunewtess.md)).

</dd> <dt>

*type* 
</dt> <dd>

The type of the contour being defined. The following values are valid.



| Value                                                                                                                                                                | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GLU_EXTERIOR"></span><span id="glu_exterior"></span><dl> <dt>**GLU\_EXTERIOR**</dt> </dl>           | An exterior contour defines an exterior boundary of the polygon.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| <span id="GLU_INTERIOR"></span><span id="glu_interior"></span><dl> <dt>**GLU\_INTERIOR**</dt> </dl>           | An interior contour defines an interior boundary of the polygon (such as a hole).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <span id="GLU_UNKNOWN"></span><span id="glu_unknown"></span><dl> <dt>**GLU\_UNKNOWN**</dt> </dl>              | An unknown contour is analyzed by the library to determine whether it is interior or exterior.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| <span id="GLU_CCW__GLU_CW"></span><span id="glu_ccw__glu_cw"></span><dl> <dt>**GLU\_CCW, GLU\_CW**</dt> </dl> | The first GLU\_CCW or GLU\_CW contour defined is considered to be exterior. All other contours are considered to be exterior if they are oriented in the same direction (clockwise or counterclockwise) as the first contour, and interior if they are not.<br/> If one contour is of type GLU\_CCW or GLU\_CW, then all contours must be of the same type (if they are not, then all GLU\_CCW and GLU\_CW contours will be changed to GLU\_UNKNOWN). Note that there is no real difference between the GLU\_CCW and GLU\_CW contour types.<br/> |



 

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

Use the **gluNextContour** function to describe polygons with multiple contours. After you describe the first contour through a series of [**gluTessVertex**](glutessvertex.md) calls, a **gluNextContour** call indicates that the previous contour is complete and that the next contour is about to begin. Perform another series of **gluTessVertex** calls to describe the new contour. Repeat this process until all contours have been described.

The *type* parameter defines what type of contour follows.

To define the type of the first contour, you can call **gluNextContour** before describing the first contour. If you do not call **gluNextContour** before the first contour, the first contour is marked GLU\_EXTERIOR.

## Examples

You can describe a quadrilateral with a triangular hole in it as follows:

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

[**gluTessBeginContour**](glutessbegincontour.md)
</dt> <dt>

[**gluTessBeginPolygon**](glubeginpolygon.md)
</dt> <dt>

[*gluTessCallback*](glutess.md)
</dt> <dt>

[**gluTessEndContour**](glutessendcontour.md)
</dt> <dt>

[**gluTessVertex**](glutessvertex.md)
</dt> </dl>

 

 





