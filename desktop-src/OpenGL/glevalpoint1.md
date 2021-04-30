---
title: glEvalPoint1 function (Gl.h)
description: The glEvalPoint1 and glEvalPoint2 functions generate and evaluate a single point in a mesh. | glEvalPoint1 function (Gl.h)
ms.assetid: 5ef1d2f0-d77b-4bb8-a0d4-45c1a6a91c18
keywords:
- glEvalPoint1 function OpenGL
topic_type:
- apiref
api_name:
- glEvalPoint1
api_location:
- Opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glEvalPoint1 function

The [**glEvalPoint1**](glevalpoint.md) and **glEvalPoint2** functions generate and evaluate a single point in a mesh.

## Syntax


```C++
void glEvalPoint1(
   GLint i
);
```



## Parameters

<dl> <dt>

*i* 
</dt> <dd>

The integer value for grid domain variable *i*.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

The [**glMapGrid**](glmapgrid-functions.md) and [**glEvalMesh**](glevalmesh-functions.md) functions are used in tandem to efficiently generate and evaluate a series of evenly spaced map domain values. You can use **glEvalPoint** to evaluate a single grid point in the same gridspace that is traversed by **glEvalMesh**. Calling [**glEvalPoint1**](glevalpoint.md) is equivalent to calling

**glEvalCoord1** (*i* ?*u* +*u*1 );

where

?*u* = (*u*2 *u*1 )/*n*

and *n*, *u*1 , and *u*2 are the arguments to the most recent **glMapGrid1** function. The one absolute numeric requirement is that if *i* = *n*, then the value computed from (*i* ?*u* + u1 ) is exactly *u*2 .

In the two-dimensional case, **glEvalPoint2**, let

?*u* = (*u*2 *u*1 )/*n*

?*v* = (*v*2 *v*1 )/*m*

where *n*, *u*1 , *u*2 , *m*, *v*1 , and *v*2  are the arguments to the most recent **glMapGrid2** function. Then the **glEvalPoint2** function is equivalent to calling

**glEvalCoord2** (*i* ?*u* + *u*1 , *j* ?*v* + *v*1 );

The only absolute numeric requirements are that if *i*=*n*, then the value computed from (*i* ?*u* + *u*1 ) is exactly u2 , and if *j* = *m*, then the value computed from (*j* ?*v* + *v*1  ) is exactly *v*2 .

The following functions retrieve information relating to [**glEvalPoint1**](glevalpoint.md) and **glEvalPoint2**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_MAP1\_GRID\_DOMAIN

**glGet** with argument GL\_MAP2\_GRID\_DOMAIN

**glGet** with argument GL\_MAP1\_GRID\_SEGMENTS

**glGet** with argument GL\_MAP2\_GRID\_SEGMENTS

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

[**glEvalCoord**](glevalcoord-functions.md)
</dt> <dt>

[**glEvalMesh**](glevalmesh-functions.md)
</dt> <dt>

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md)
</dt> <dt>

[**glMap1**](glmap1.md)
</dt> <dt>

[**glMap2**](glmap2.md)
</dt> <dt>

[**glMapGrid**](glmapgrid-functions.md)
</dt> </dl>

 

 





