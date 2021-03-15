---
description: Describes the resolution of the shadow z-buffer that will be used in Precomputed Radiance Transfer (PRT) direct lighting simulation on the GPU.
ms.assetid: 05354328-9b6f-45f5-a913-47ede170b03f
title: D3DXSHGPUSIMOPT enumeration (D3dx9mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXSHGPUSIMOPT
api_type: 
- HeaderDef
api_location: 
- d3dx9mesh.h
---

# D3DXSHGPUSIMOPT enumeration

Describes the resolution of the shadow z-buffer that will be used in Precomputed Radiance Transfer (PRT) direct lighting simulation on the GPU. A higher quality z-buffer can also be specified to reduce noise in the results of the direct lighting simulation, although the simulation will be slower.

## Syntax


```C++
typedef enum D3DXSHGPUSIMOPT { 
  D3DXSHGPUSIMOPT_SHADOWRES256   = 1,
  D3DXSHGPUSIMOPT_SHADOWRES512   = 0,
  D3DXSHGPUSIMOPT_SHADOWRES1024  = 2,
  D3DXSHGPUSIMOPT_SHADOWRES2048  = 3,
  D3DXSHGPUSIMOPT_HIGHQUALITY    = 4,
  D3DXSHGPUSIMOPT_FORCE_DWORD    = 0x7fffffff
} D3DXSHGPUSIMOPT, *LPD3DXSHGPUSIMOPT;
```



## Constants

<dl> <dt>

<span id="D3DXSHGPUSIMOPT_SHADOWRES256"></span><span id="d3dxshgpusimopt_shadowres256"></span>**D3DXSHGPUSIMOPT\_SHADOWRES256**
</dt> <dd>

Low resolution simulation. A 256 x 256 pixel texture is used in the simulation to encode the shadow z-buffer.

</dd> <dt>

<span id="D3DXSHGPUSIMOPT_SHADOWRES512"></span><span id="d3dxshgpusimopt_shadowres512"></span>**D3DXSHGPUSIMOPT\_SHADOWRES512**
</dt> <dd>

Medium resolution simulation. A 512 x 512 pixel texture is used in the simulation to encode the shadow z-buffer. This is the default value.

</dd> <dt>

<span id="D3DXSHGPUSIMOPT_SHADOWRES1024"></span><span id="d3dxshgpusimopt_shadowres1024"></span>**D3DXSHGPUSIMOPT\_SHADOWRES1024**
</dt> <dd>

High resolution simulation. A 1024 x 1024 pixel texture is used in the simulation to encode the shadow z-buffer.

</dd> <dt>

<span id="D3DXSHGPUSIMOPT_SHADOWRES2048"></span><span id="d3dxshgpusimopt_shadowres2048"></span>**D3DXSHGPUSIMOPT\_SHADOWRES2048**
</dt> <dd>

Highest resolution simulation. A 2048 x 2048 pixel texture is used in the simulation to encode the shadow z-buffer.

</dd> <dt>

<span id="D3DXSHGPUSIMOPT_HIGHQUALITY"></span><span id="d3dxshgpusimopt_highquality"></span>**D3DXSHGPUSIMOPT\_HIGHQUALITY**
</dt> <dd>

The simulation is of high precision, regardless of the selected resolution. Setting this value will reduce noise in the results of the direct lighting simulation, although the simulation will be slower. May be combined with one of the resolution values.

</dd> <dt>

<span id="D3DXSHGPUSIMOPT_FORCE_DWORD"></span><span id="d3dxshgpusimopt_force_dword"></span>**D3DXSHGPUSIMOPT\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Remarks

Only one of the resolution values may be specified, and may be combined with the high-quality value.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9mesh.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](dx9-graphics-reference-d3dx-enums.md)
</dt> </dl>

 

 




