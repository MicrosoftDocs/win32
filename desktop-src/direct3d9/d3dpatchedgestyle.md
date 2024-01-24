---
description: Defines whether the current tessellation mode is discrete or continuous.
ms.assetid: d8055a25-6a8e-4018-a993-762f6f0e0cd3
title: D3DPATCHEDGESTYLE enumeration (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DPATCHEDGESTYLE
api_type: 
- HeaderDef
api_location: 
- D3D9Types.h
---

# D3DPATCHEDGESTYLE enumeration

Defines whether the current tessellation mode is discrete or continuous.

## Syntax


```C++
typedef enum D3DPATCHEDGESTYLE { 
  D3DPATCHEDGE_DISCRETE     = 0,
  D3DPATCHEDGE_CONTINUOUS   = 1,
  D3DPATCHEDGE_FORCE_DWORD  = 0x7fffffff
} D3DPATCHEDGESTYLE, *LPD3DPATCHEDGESTYLE;
```



## Constants

<dl> <dt>

<span id="D3DPATCHEDGE_DISCRETE"></span><span id="d3dpatchedge_discrete"></span>**D3DPATCHEDGE\_DISCRETE**
</dt> <dd>

Discrete edge style. In discrete mode, you can specify float tessellation but it will be truncated to integers.

</dd> <dt>

<span id="D3DPATCHEDGE_CONTINUOUS"></span><span id="d3dpatchedge_continuous"></span>**D3DPATCHEDGE\_CONTINUOUS**
</dt> <dd>

Continuous edge style. In continuous mode, tessellation is specified as float values that can be smoothly varied to reduce "popping" artifacts.

</dd> <dt>

<span id="D3DPATCHEDGE_FORCE_DWORD"></span><span id="d3dpatchedge_force_dword"></span>**D3DPATCHEDGE\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Remarks

Note that continuous tessellation produces a completely different tessellation pattern from the discrete one for the same tessellation values (this is more apparent in wireframe mode). Thus, 4.0 continuous is not the same as 4 discrete.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Enumerations](dx9-graphics-reference-d3d-enums.md)
</dt> </dl>

 

 




