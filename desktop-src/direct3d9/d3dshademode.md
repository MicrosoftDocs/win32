---
description: Defines constants that describe the supported shading modes.
ms.assetid: ba4e0c62-b496-427b-a324-2fb560d153ba
title: D3DSHADEMODE enumeration (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DSHADEMODE
api_type: 
- HeaderDef
api_location: 
- d3d9types.h
---

# D3DSHADEMODE enumeration

Defines constants that describe the supported shading modes.

## Syntax


```C++
typedef enum D3DSHADEMODE { 
  D3DSHADE_FLAT         = 1,
  D3DSHADE_GOURAUD      = 2,
  D3DSHADE_PHONG        = 3,
  D3DSHADE_FORCE_DWORD  = 0x7fffffff
} D3DSHADEMODE, *LPD3DSHADEMODE;
```



## Constants

<dl> <dt>

<span id="D3DSHADE_FLAT"></span><span id="d3dshade_flat"></span>**D3DSHADE\_FLAT**
</dt> <dd>

Flat shading mode. The color and specular component of the first vertex in the triangle are used to determine the color and specular component of the face. These colors remain constant across the triangle; that is, they are not interpolated. The specular alpha is interpolated. See Remarks.

</dd> <dt>

<span id="D3DSHADE_GOURAUD"></span><span id="d3dshade_gouraud"></span>**D3DSHADE\_GOURAUD**
</dt> <dd>

Gouraud shading mode. The color and specular components of the face are determined by a linear interpolation between all three of the triangle's vertices.

</dd> <dt>

<span id="D3DSHADE_PHONG"></span><span id="d3dshade_phong"></span>**D3DSHADE\_PHONG**
</dt> <dd>

Not supported.

</dd> <dt>

<span id="D3DSHADE_FORCE_DWORD"></span><span id="d3dshade_force_dword"></span>**D3DSHADE\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Remarks

The first vertex of a triangle for flat shading mode is defined in the following manner.

-   For a triangle list, the first vertex of the triangle i is i \* 3.
-   For a triangle strip, the first vertex of the triangle i is vertex i.
-   For a triangle fan, the first vertex of the triangle i is vertex i + 1.

The members of this enumerated type define the vales for the D3DRS\_SHADEMODE render state.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Enumerations](dx9-graphics-reference-d3d-enums.md)
</dt> <dt>

[**D3DRENDERSTATETYPE**](./d3drenderstatetype.md)
</dt> </dl>

 

 
