---
description: Defines the basis type of a high-order patch surface.
ms.assetid: 18c31c77-7ba3-449c-af4a-717b8c1dced1
title: D3DBASISTYPE enumeration (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DBASISTYPE
api_type: 
- HeaderDef
api_location: 
- D3D9Types.h
---

# D3DBASISTYPE enumeration

Defines the basis type of a high-order patch surface.

## Syntax


```C++
typedef enum D3DBASISTYPE { 
  D3DBASIS_BEZIER       = 0,
  D3DBASIS_BSPLINE      = 1,
  D3DBASIS_CATMULL_ROM  = 2,
  D3DBASIS_FORCE_DWORD  = 0x7fffffff
} D3DBASISTYPE, *LPD3DBASISTYPE;
```



## Constants

<dl> <dt>

<span id="D3DBASIS_BEZIER"></span><span id="d3dbasis_bezier"></span>**D3DBASIS\_BEZIER**
</dt> <dd>

Input vertices are treated as a series of Bézier patches. The number of vertices specified must be divisible by 4. Portions of the mesh beyond this criterion will not be rendered. Full continuity is assumed between sub-patches in the interior of the surface rendered by each call. Only the vertices at the corners of each sub-patch are guaranteed to lie on the resulting surface.

</dd> <dt>

<span id="D3DBASIS_BSPLINE"></span><span id="d3dbasis_bspline"></span>**D3DBASIS\_BSPLINE**
</dt> <dd>

Input vertices are treated as control points of a B-spline surface. The number of apertures rendered is two fewer than the number of apertures in that direction. In general, the generated surface does not contain the control vertices specified.

</dd> <dt>

<span id="D3DBASIS_CATMULL_ROM"></span><span id="d3dbasis_catmull_rom"></span>**D3DBASIS\_CATMULL\_ROM**
</dt> <dd>

An interpolating basis defines the surface so that the surface goes through all the input vertices specified. In DirectX 8, this was D3DBASIS\_INTERPOLATE.

</dd> <dt>

<span id="D3DBASIS_FORCE_DWORD"></span><span id="d3dbasis_force_dword"></span>**D3DBASIS\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Remarks

The members of **D3DBASISTYPE** specify the formulation to be used in evaluating the high-order patch surface primitive during tessellation.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Enumerations](dx9-graphics-reference-d3d-enums.md)
</dt> <dt>

[**D3DRECTPATCH\_INFO**](d3drectpatch-info.md)
</dt> <dt>

[**D3DTRIPATCH\_INFO**](d3dtripatch-info.md)
</dt> </dl>

 

 




