---
title: glMapGrid2d function (Gl.h)
description: Defines a one-dimensional mesh. | glMapGrid2d function (Gl.h)
ms.assetid: 5e5887d1-e137-434b-a1f3-b3f10d462823
keywords:
- glMapGrid2d function OpenGL
topic_type:
- apiref
api_name:
- glMapGrid2d
api_location:
- Opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glMapGrid2d function

Defines a one-dimensional mesh.

## Syntax


```C++
void WINAPI glMapGrid2d(
   GLint    un,
   GLdouble u1,
   GLdouble u2,
   GLint    vn,
   GLdouble v1,
   GLdouble v2
);
```



## Parameters

<dl> <dt>

*un* 
</dt> <dd>

The number of partitions in the grid range interval \[u1, u2\]. This value must be positive.

</dd> <dt>

*u1* 
</dt> <dd>

A value used as the mapping for integer grid domain value i = 0.

</dd> <dt>

*u2* 
</dt> <dd>

A value used as the mapping for integer grid domain value i = un.

</dd> <dt>

*vn* 
</dt> <dd>

The number of partitions in the grid range interval \[v1, v2\].

</dd> <dt>

*v1* 
</dt> <dd>

A value used as the mapping for integer grid domain value j = 0.

</dd> <dt>

*v2* 
</dt> <dd>

A value used as the mapping for integer grid domain value j = vn.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | Either *un* or *vn* was not positive.<br/>                                                                                      |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glMapGrid** and [glEvalMesh](glevalmesh-functions.md) functions are used in tandem to efficiently generate and evaluate a series of evenly spaced map domain values. The glEvalMesh function steps through the integer domain of a one- or two-dimensional grid, whose range is the domain of the evaluation maps specified by [**glMap1**](glmap1.md) and [**glMap2**](glmap2.md).

The [**glMapGrid1**](glmapgrid1d.md) and **glMapGrid2** functions specify the linear grid mappings between the i (or i and j) integer grid coordinates, to the u (or u and v) floating-point evaluation map coordinates. See [**glMap1**](glmap1.md) and [**glMap2**](glmap2.md) for details of how u and v coordinates are evaluated.

The [**glMapGrid1**](glmapgrid1d.md) function specifies a single linear mapping such that integer grid coordinate 0 maps exactly to u1, and integer grid coordinate *un* maps exactly to *u2*. All other integer grid coordinates *i* are mapped such that:

*u = i(u2 u1)/un + u1*

The **glMapGrid2** function specifies two such linear mappings. One maps integer grid coordinate *i = 0* exactly to *u1*, and integer grid coordinate *i = un* exactly to *u2*. The other maps integer grid coordinate *j = 0* exactly to *v1*, and integer grid coordinate *j = vn* exactly to *v2*. Other integer grid coordinates i and j are mapped such that

*u = i(u2 u1)/un + u1*

*v = j (v2 v1)/vn + v1*

The mappings specified by [**glMapGrid**](glmapgrid1d.md) are used identically by [glEvalMesh](glevalmesh-functions.md) and [**glEvalPoint**](glevalpoint.md).

The following functions retrieve information related to [**glMapGrid**](glmapgrid1d.md):

<dl>

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_MAP1\_GRID\_DOMAIN  
[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_MAP2\_GRID\_DOMAIN  
[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_MAP1\_GRID\_SEGMENTS  
[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_MAP2\_GRID\_SEGMENTS  
</dl>

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

[**glBegin**](glbegin.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glEvalCoord**](glevalcoord-functions.md)
</dt> <dt>

[glEvalMesh](glevalmesh-functions.md)
</dt> <dt>

[**glEvalPoint**](glevalpoint.md)
</dt> <dt>

[**glMap1**](glmap1.md)
</dt> <dt>

[**glMap2**](glmap2.md)
</dt> </dl>

 

 





