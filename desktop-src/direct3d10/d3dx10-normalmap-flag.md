---
description: These flags are used to control how D3DX10ComputeNormalMap generates normal maps. Any number of these flags may be OR'd together in any combination.
ms.assetid: 307936c1-3137-41fe-8bea-7a82e6db0867
title: D3DX10_NORMALMAP_FLAG enumeration (D3DX10Tex.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DX10_NORMALMAP_FLAG
api_type: 
- HeaderDef
api_location: 
- D3DX10Tex.h
---

# D3DX10\_NORMALMAP\_FLAG enumeration

These flags are used to control how [**D3DX10ComputeNormalMap**](d3dx10computenormalmap.md) generates normal maps. Any number of these flags may be OR'd together in any combination.

## Syntax


```C++
typedef enum D3DX10_NORMALMAP_FLAG { 
  D3DX10_NORMALMAP_MIRROR_U           = (1 << 16),
  D3DX10_NORMALMAP_MIRROR_V           = (2 << 16),
  D3DX10_NORMALMAP_MIRROR             = (3 << 16),
  D3DX10_NORMALMAP_INVERTSIGN         = (8 << 16),
  D3DX10_NORMALMAP_COMPUTE_OCCLUSION  = (16 << 16)
} D3DX10_NORMALMAP_FLAG, *LPD3DX10_NORMALMAP_FLAG;
```



## Constants

<dl> <dt>

<span id="D3DX10_NORMALMAP_MIRROR_U"></span><span id="d3dx10_normalmap_mirror_u"></span>**D3DX10\_NORMALMAP\_MIRROR\_U**
</dt> <dd>

Indicates that pixels off the edge of the texture on the U-axis should be mirrored, not wraped.

</dd> <dt>

<span id="D3DX10_NORMALMAP_MIRROR_V"></span><span id="d3dx10_normalmap_mirror_v"></span>**D3DX10\_NORMALMAP\_MIRROR\_V**
</dt> <dd>

Indicates that pixels off the edge of the texture on the V-axis should be mirrored, not wraped.

</dd> <dt>

<span id="D3DX10_NORMALMAP_MIRROR"></span><span id="d3dx10_normalmap_mirror"></span>**D3DX10\_NORMALMAP\_MIRROR**
</dt> <dd>

Same as D3DX10\_NORMALMAP\_MIRROR\_U \| D3DX10\_NORMALMAP\_MIRROR\_V.

</dd> <dt>

<span id="D3DX10_NORMALMAP_INVERTSIGN"></span><span id="d3dx10_normalmap_invertsign"></span>**D3DX10\_NORMALMAP\_INVERTSIGN**
</dt> <dd>

Inverts the direction of each normal.

</dd> <dt>

<span id="D3DX10_NORMALMAP_COMPUTE_OCCLUSION"></span><span id="d3dx10_normalmap_compute_occlusion"></span>**D3DX10\_NORMALMAP\_COMPUTE\_OCCLUSION**
</dt> <dd>

Computes the per pixel occlusion term and encodes it into the alpha. An Alpha of 1 means that the pixel is not obscured in any way, and an alpha of 0 would mean that the pixel is completely obscured.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Tex.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](d3d10-graphics-reference-d3dx10-enums.md)
</dt> </dl>

 

 




