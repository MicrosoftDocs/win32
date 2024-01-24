---
title: glEvalMesh1 function (Gl.h)
description: Computes a one-dimensional grid of points or lines.
ms.assetid: 176a4b81-f1a7-42fc-8ecd-bba77a0ec5b3
keywords:
- glEvalMesh1 function OpenGL
topic_type:
- apiref
api_name:
- glEvalMesh1
api_location:
- Opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glEvalMesh1 function

Computes a one-dimensional grid of points or lines.

## Syntax


```C++
void WINAPI glEvalMesh1(
   GLenum mode,
   GLint  i1,
   GLint  i2
);
```



## Parameters

<dl> <dt>

*mode* 
</dt> <dd>

A value that specifies whether to compute a one-dimensional mesh of points or lines. The following symbolic constants are accepted: GL\_POINT and GL\_LINE.

</dd> <dt>

*i1* 
</dt> <dd>

The first integer value for grid domain variable i.

</dd> <dt>

*i2* 
</dt> <dd>

The last integer value for grid domain variable i.

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

Use [**glMapGrid**](glmapgrid-functions.md) and [**glEvalMesh**](glevalmesh-functions.md) together to efficiently generate and evaluate a series of evenly spaced map domain values. The **glEvalMesh** function steps through the integer domain of a one- or two-dimensional grid, whose range is the domain of the evaluation maps specified by [**glMap1**](glmap1.md) and [**glMap2**](glmap2.md). The mode parameter determines whether the resulting vertices are connected as points, lines, or filled polygons.

In the one-dimensional case, **glEvalMesh1**, the mesh is generated as if the following code fragment were executed:

[**glBegin**](glbegin.md)(*type*);

for (i = i1; i <= i2; i += 1)

{

[**glEvalCoord1**](glevalcoord1d.md)(i?u + u1)

}

[**glEnd**](glend.md)( );

where

?u = (u2 u1) / n

and n, u1, and u2 are the arguments to the most recent [**glMapGrid1**](glmapgrid1d.md) function. The *type* parameter is GL\_POINTS if mode is GL\_POINT, or GL\_LINES if mode is GL\_LINE. The one absolute numeric requirement is that if i = n, then the value computed from i?u + u1 is exactly u2.

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
</dt> </dl>

 

 





