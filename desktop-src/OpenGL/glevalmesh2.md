---
title: glEvalMesh2 function (Gl.h)
description: Computes a two-dimensional grid of points or lines.
ms.assetid: 21e94388-903e-4b9d-8e54-9c914d0ce372
keywords:
- glEvalMesh2 function OpenGL
topic_type:
- apiref
api_name:
- glEvalMesh2
api_location:
- Opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glEvalMesh2 function

Computes a two-dimensional grid of points or lines.

## Syntax


```C++
void WINAPI glEvalMesh2(
   GLenum mode,
   GLint  i1,
   GLint  i2,
   GLint  j1,
   GLint  j2
);
```



## Parameters

<dl> <dt>

*mode* 
</dt> <dd>

A value that specifies whether to compute a two-dimensional mesh of points, lines, or polygons. The following symbolic constants are accepted: GL\_POINT, GL\_LINE, and GL\_FILL.

</dd> <dt>

*i1* 
</dt> <dd>

The first integer value for grid domain variable i.

</dd> <dt>

*i2* 
</dt> <dd>

The last integer value for grid domain variable i.

</dd> <dt>

*j1* 
</dt> <dd>

The first integer value for grid domain variable j.

</dd> <dt>

*j2* 
</dt> <dd>

The last integer value for grid domain variable j.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                                |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_ENUM**</dt> </dl>      | Indicates that *mode* is not an accepted value. <br/>                                                                            |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md). <br/> |



## Remarks

Use [**glMapGrid**](glmapgrid-functions.md) and [**glEvalMesh**](glevalmesh-functions.md) in tandem to efficiently generate and evaluate a series of evenly spaced map domain values. The **glEvalMesh** function steps through the integer domain of a one- or two-dimensional grid, whose range is the domain of the evaluation maps specified by [**glMap1**](glmap1.md) and [**glMap2**](glmap2.md). The mode parameter determines whether the resulting vertices are connected as points, lines, or filled polygons.

In the two-dimensional case, **glEvalMesh2**, let

? u = (u2 u1)/n

? v = (v2 v1)/m,

where n, u1, u2, m, v1, and v2 are the arguments to the most recent [**glMapGrid2**](glmapgrid-functions.md) function. Then, if *mode* is GL\_FILL, **glEvalMesh2** is equivalent to:

for (j = j1; j < j2; j += 1)

{

[**glBegin**](glbegin.md)(GL\_QUAD\_STRIP);

for (i = i1; i <= i2; i += 1)

{

[**glEvalCoord2**](glevalcoord2d.md)(i? u + u1 ( ) , j ? v + v1);

[**glEvalCoord2**](glevalcoord2d.md)(i? u + u1 ( ) , (j+1) ? v + v1);

}

[**glEnd**](glend.md)( ); }

If *mode* is GL\_LINE, then a call to **glEvalMesh2** is equivalent to:

for (j = j1; j <= j2; j += 1)

{

[**glBegin**](glbegin.md)(GL\_LINE\_STRIP);

for (i = i1; i <= i2; i += 1)

{

[**glEvalCoord2**](glevalcoord2d.md)(i? u + u1, j? v + v1);

}

[**glEnd**](glend.md)( );

}

for (i = i1; i <= i2; i += 1)

{

[**glBegin**](glbegin.md)(GL\_LINE\_STRIP);

for (j = j1; j <= j1; j += 1)

{

[**glEvalCoord2**](glevalcoord2d.md)(i? u + u1, j? v + v1);

}

glEnd( );

}

And finally, if *mode* is GL\_POINT, then a call to **glEvalMesh2** is equivalent to:

[**glBegin**](glbegin.md)(GL\_POINTS);

for (j = j1; j <= j2; j += 1)

{

for (i = i1; i <= i2; i += 1)

{

[**glEvalCoord2**](glevalcoord2d.md)(i? u + u1, j? v + v1);

}

}

[**glEnd**](glend.md)( );

In all three cases, the only absolute numeric requirements are that if i = n, then the value computed from i? u + u1 is exactly u2, and if j = m, then the value computed from j? v + v1 is exactly v2. The following functions retrieve information relating to **glEvalMesh**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_MAP1\_GRID\_DOMAIN

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_MAP2\_GRID\_DOMAIN

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_MAP1\_GRID\_SEGMENTS

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_MAP2\_GRID\_SEGMENTS

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Gl.h</dt> </dl>         |
| Library<br/>                  | <dl> <dt>Opengl32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Opengl32.dll</dt> </dl> |



 

 





