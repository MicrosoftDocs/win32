---
description: Defines options for performing geodesic distance calculations, when fitting a texture to a curved surface. Use this flag to choose between high quality versus fast calculations when computing a texture atlas.
ms.assetid: 76649c57-e5ae-4e0d-a7ab-f56385a327c2
title: D3DXUVATLAS enumeration (D3dx9mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXUVATLAS
api_type: 
- HeaderDef
api_location: 
- d3dx9mesh.h
---

# D3DXUVATLAS enumeration

Defines options for performing geodesic distance calculations, when fitting a texture to a curved surface. Use this flag to choose between high quality versus fast calculations when computing a texture atlas.

## Syntax


```C++
typedef enum _D3DXUVATLAS { 
  D3DXUVATLAS_DEFAULT           = 1,
  D3DXUVATLAS_GEODESIC_FAST     = 2,
  D3DXUVATLAS_GEODESIC_QUALITY  = 3
} D3DXUVATLAS;
```



## Constants

<dl> <dt>

<span id="D3DXUVATLAS_DEFAULT"></span><span id="d3dxuvatlas_default"></span>**D3DXUVATLAS\_DEFAULT**
</dt> <dd>

Meshes with more than 25k faces will have the fast geodasic distance method applied to them while meshes with fewer than 25k faces will have the higher quality geodesic distance method applied to them instead.

</dd> <dt>

<span id="D3DXUVATLAS_GEODESIC_FAST"></span><span id="d3dxuvatlas_geodesic_fast"></span>**D3DXUVATLAS\_GEODESIC\_FAST**
</dt> <dd>

Uses approximations to improve charting speed at the cost of added stretch or more charts being output for the mesh.

</dd> <dt>

<span id="D3DXUVATLAS_GEODESIC_QUALITY"></span><span id="d3dxuvatlas_geodesic_quality"></span>**D3DXUVATLAS\_GEODESIC\_QUALITY**
</dt> <dd>

Provides better quality charts, but requires more time and memory than fast.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9mesh.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](dx9-graphics-reference-d3dx-enums.md)
</dt> </dl>

 

 




