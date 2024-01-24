---
title: gluQuadricDrawStyle function (Glu.h)
description: The gluQuadricDrawStyle function specifies the draw style desired for quadrics.
ms.assetid: 30f6da40-9306-46bb-a815-f51722e57e18
keywords:
- gluQuadricDrawStyle function OpenGL
topic_type:
- apiref
api_name:
- gluQuadricDrawStyle
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluQuadricDrawStyle function

The **gluQuadricDrawStyle** function specifies the draw style desired for quadrics.

## Syntax


```C++
void WINAPI gluQuadricDrawStyle(
   GLUquadric *quadObject,
   GLenum     drawStyle
);
```



## Parameters

<dl> <dt>

*quadObject* 
</dt> <dd>

The quadric object (created with [**gluNewQuadric**](glunewquadric.md)).

</dd> <dt>

*drawStyle* 
</dt> <dd>

The desired draw style. The following values are valid.



| Value                                                                                                                                                            | Meaning                                                                                                                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GLU_FILL"></span><span id="glu_fill"></span><dl> <dt>**GLU\_FILL**</dt> </dl>                   | Quadrics are rendered with polygon primitives. The polygons are drawn in a counterclockwise fashion with respect to their normals (as defined with [**gluQuadricOrientation**](gluquadricorientation.md)).<br/> |
| <span id="GLU_LINE"></span><span id="glu_line"></span><dl> <dt>**GLU\_LINE**</dt> </dl>                   | Quadrics are rendered as a set of lines.<br/>                                                                                                                                                                    |
| <span id="GLU_SILHOUETTE"></span><span id="glu_silhouette"></span><dl> <dt>**GLU\_SILHOUETTE**</dt> </dl> | Quadrics are rendered as a set of lines, except that edges separating coplanar faces will not be drawn.<br/>                                                                                                     |
| <span id="GLU_POINT"></span><span id="glu_point"></span><dl> <dt>**GLU\_POINT**</dt> </dl>                | Quadrics are rendered as a set of points.<br/>                                                                                                                                                                   |



 

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The **gluQuadricDrawStyle** function specifies the draw style for quadrics rendered with **quadObject**.

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

[**gluNewQuadric**](glunewquadric.md)
</dt> <dt>

[**gluQuadricNormals**](gluquadricnormals.md)
</dt> <dt>

[**gluQuadricOrientation**](gluquadricorientation.md)
</dt> <dt>

[**gluQuadricTexture**](gluquadrictexture.md)
</dt> </dl>

 

 





