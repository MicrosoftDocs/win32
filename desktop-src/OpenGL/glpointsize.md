---
title: glPointSize function (Gl.h)
description: The glPointSize function specifies the diameter of rasterized points.
ms.assetid: efa35fa8-721a-48e5-bf59-d33b9bbe7f73
keywords:
- glPointSize function OpenGL
topic_type:
- apiref
api_name:
- glPointSize
api_location:
- opengl32.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# glPointSize function

The **glPointSize** function specifies the diameter of rasterized points.

## Syntax


```C++
void WINAPI glPointSize(
   GLfloat size
);
```



## Parameters

<dl> <dt>

*size* 
</dt> <dd>

The diameter of rasterized points. The default is 1.0.

</dd> </dl>

## Return value

This function does not return a value.

## Error codes

The following error codes can be retrieved by the [**glGetError**](glgeterror.md) function.



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**GL\_INVALID\_VALUE**</dt> </dl>     | *size* was less than or equal to zero.<br/>                                                                                     |
| <dl> <dt>**GL\_INVALID\_OPERATION**</dt> </dl> | The function was called between a call to [**glBegin**](glbegin.md) and the corresponding call to [**glEnd**](glend.md).<br/> |



## Remarks

The **glPointSize** function specifies the rasterized diameter of both aliased and antialiased points. Using a point size other than 1.0 has different effects, depending on whether point antialiasing is enabled. Point antialiasing is controlled by calling [**glEnable**](glenable.md) and **glDisable** with argument GL\_POINT\_SMOOTH.

If point antialiasing is disabled, the actual size is determined by rounding the supplied size to the nearest integer. (If the rounding results in the value 0, it is as if the point size were 1.) If the rounded size is odd, then the center point (*x*,*y*) of the pixel fragment that represents the point is computed as

(*x*<sub>w</sub> + .5, *y*<sub>w</sub> + .5)

where *w* subscripts indicate window coordinates. All pixels that lie within the square grid of the rounded size centered at (*x*,*y*) make up the fragment. If the size is even, the center point is

(*x*<sub>w</sub> + .5, *y*<sub>w</sub> + .5)

and the rasterized fragment's centers are the half-integer window coordinates within the square of the rounded size centered at (*x*,*y*). All pixel fragments produced in rasterizing a nonantialiased point are assigned the same associated data; that of the vertex corresponding to the point.

If antialiasing is enabled, then point rasterization produces a fragment for each pixel square that intersects the region lying within the circle having diameter equal to the current point size and centered at the points (*x*<sub>w</sub> ,*y*<sub>w</sub> ). The coverage value for each fragment is the window coordinate area of the intersection of the circular region with the corresponding pixel square. This value is saved and used in the final rasterization step. The data associated with each fragment is the data associated with the point being rasterized.

Not all sizes are supported when point antialiasing is enabled. If an unsupported size is requested, the nearest supported size is used. Only size 1.0 is guaranteed to be supported; others depend on the implementation. The range of supported sizes and the size difference between supported sizes within the range can be queried by calling [**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with arguments GL\_POINT\_SIZE\_RANGE and GL\_POINT\_SIZE\_GRANULARITY.

The point size specified by **glPointSize** is always returned when GL\_POINT\_SIZE is queried. Clamping and rounding for aliased and antialiased points have no effect on the specified value.

Non-antialiased point size may be clamped to an implementation-dependent maximum. Although this maximum cannot be queried, it must be no less than the maximum value for antialiased points, rounded to the nearest integer value.

The following functions retrieve information related to **glPointSize**:

[**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) with argument GL\_POINT\_SIZE

**glGet** with argument GL\_POINT\_SIZE\_RANGE

**glGet** with argument GL\_POINT\_SIZE\_GRANULARITY

[**glIsEnabled**](glisenabled.md) with argument GL\_POINT\_SMOOTH

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

[**glEnable**](glenable.md)
</dt> <dt>

[**glEnd**](glend.md)
</dt> <dt>

[**glIsEnabled**](glisenabled.md)
</dt> </dl>

 

 





