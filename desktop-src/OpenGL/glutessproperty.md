---
title: gluTessProperty function (Glu.h)
description: The gluTessProperty function sets the property of a tessellation object.
ms.assetid: 1306b9ef-4f1e-4684-99ea-464bae1d0a61
keywords:
- gluTessProperty function OpenGL
topic_type:
- apiref
api_name:
- gluTessProperty
api_location:
- glu32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# gluTessProperty function

The **gluTessProperty** function sets the property of a tessellation object.

## Syntax


```C++
void WINAPI gluTessProperty(
   GLUtesselator *tess,
   GLenum        which,
   GLdouble      value
);
```



## Parameters

<dl> <dt>

*tess* 
</dt> <dd>

The tessellation object (created with [**gluNewTess**](glunewtess.md)).

</dd> <dt>

*which* 
</dt> <dd>

The property value to set. The following values are valid: GLU\_TESS\_WINDING\_RULE, GLU\_TESS\_BOUNDARY\_ONLY, and GLU\_TESS\_TOLERANCE.



| Value                                                                                                                                                                                      | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="GLU_TESS_WINDING_RULE"></span><span id="glu_tess_winding_rule"></span><dl> <dt>**GLU\_TESS\_WINDING\_RULE**</dt> </dl>    | Determines which parts of the polygon are on the interior. The value parameter may be set to one of the following: GLU\_TESS\_WINDING\_ODD, GLU\_TESS\_WINDING\_NONZERO, GLU\_TESS\_WINDING\_POSITIVE, GLU\_TESS\_WINDING\_NEGATIVE, or GLU\_TESS\_WINDING\_ABS\_GEQ\_TWO. <br/> To understand how the winding rule works, first consider that the input contours partition the plane into regions. The winding rule determines which of these regions are inside the polygon.<br/> For a single-contour C, the winding number of a point x is simply the signed number of revolutions we make around x as we travel once around C (where counterclockwise is positive). When there are several contours, the individual winding numbers are summed. This procedure associates a signed integer value with each point x in the plane. Note that the winding number is the same for all points in a single region.<br/> The winding rule classifies a region as "inside" if its winding number belongs to the chosen category (odd, nonzero, positive, negative, or absolute value of at least two). The previous GLU tessellator (prior to GLU 1.2) used the "odd" rule. The "nonzero" rule (GLU\_TESS\_WINDING\_NONZERO) is another common way to define the interior. The other three rules (GLU\_TESS\_WINDING\_POSITIVE, GLU\_TESS\_WINDING\_NEGATIVE, GLU\_TESS\_WINDING\_ABS\_GEQ\_TWO) are useful for polygon CSG operations.<br/> |
| <span id="GLU_TESS_BOUNDARY_ONLY"></span><span id="glu_tess_boundary_only"></span><dl> <dt>**GLU\_TESS\_BOUNDARY\_ONLY**</dt> </dl> | Specifies a Boolean value (set value to GL\_TRUE or GL\_FALSE). When you set value to GL\_TRUE, a set of closed contours separating the polygon interior and exterior is returned instead of a tessellation. Exterior contours are oriented counterclockwise with respect to the normal; interior contours are oriented clockwise. The GLU\_TESS\_BEGIN and GLU\_TESS\_BEGIN\_DATA callbacks use the type GL\_LINE\_LOOP for each contour.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| <span id="GLU_TESS_TOLERANCE"></span><span id="glu_tess_tolerance"></span><dl> <dt>**GLU\_TESS\_TOLERANCE**</dt> </dl>              | Specifies a tolerance for merging features to reduce the size of the output. For example, two vertexes that are very close to each other might be replaced by a single vertex. The tolerance is multiplied by the largest coordinate magnitude of any input vertex; this specifies the maximum distance that any feature can move as the result of a single merge operation. If a single feature takes part in several merge operations, the total distance moved can be larger. <br/> Feature merging is completely optional; the tolerance is only a hint. The implementation is free to merge in some cases and not in others, or to never merge features at all. The default tolerance is zero.<br/> The current implementation merges vertexes only if they are exactly coincident, regardless of the current tolerance. A vertex is spliced into an edge only if the implementation is unable to distinguish which side of the edge the vertex lies on. Two edges are merged only when both endpoints are identical.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                 |



 

</dd> <dt>

*value* 
</dt> <dd>

The value of the indicated property.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The **gluTessProperty** function controls properties stored in a tessellation object. These properties affect the way the polygons are interpreted and rendered.

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

[**gluGetTessProperty**](glugettessproperty.md)
</dt> <dt>

[**gluNewTess**](glunewtess.md)
</dt> </dl>

 

 





